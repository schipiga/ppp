"""
Package to view links.
"""

from .html import render as as_html
from .json import render as as_json
from .text import render as as_text
from .yaml import render as as_yaml


__all__ = [
    "as_html",
    "as_json",
    "as_text",
    "as_yaml",
]
