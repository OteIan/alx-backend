#!/usr/bin/env python3
"""
Helper module
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Helper function
    """
    return (page_size * (page - 1), page_size * page)
