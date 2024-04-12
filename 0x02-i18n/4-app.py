#!/usr/bin/env python3
"""
Basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale() -> str:
    """
    Determine best supported languages
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def basic_route() -> str:
    """
    Basic route
    """
    return render_template("4-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
