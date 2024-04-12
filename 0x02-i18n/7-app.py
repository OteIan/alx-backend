#!/usr/bin/env python3
"""
Basic flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz import UnknownTimeZoneError


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """
    Fetches the user
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return


@app.before_request
def before_request():
    """
    Excecuted before all other functions
    """
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale() -> str:
    """
    Determine best supported languages
    """
    locale = request.args.get("locale")
    if locale:
        return locale

    user = request.args.get("login_as")
    if user:
        lang = users.get(int(user)).get("locale")
        if lang in app.config["LANGUAGES"]:
            return lang

    headers = request.headers.get("locale")
    if headers:
        return headers

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """
    Determines the timezone
    """
    try:
        timezone = request.args.get("timezone")
        if timezone:
            return pytz.timezone(timezone)

        user = request.args.get("login_as")
        if user:
            timezone = users.get(int(user)).get("timezone")
            if timezone:
                return pytz.timezone(timezone)

        timezone = request.headers.get(timezone)
        if timezone:
            return pytz.timezone(timezone)

    except UnknownTimeZoneError:
        return app.config.get("BABEL_DEFAULT_TIMEZONE")
    return app.config.get("BABEL_DEFAULT_TIMEZONE")


@app.route('/')
def basic_route() -> str:
    """
    Basic route
    """
    return render_template("5-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
