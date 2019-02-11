"""
Package to parse inet content.
"""

from . import loader
from . import parser
from . import view


__all__ = [
    "links_as_html",
    "links_as_json",
    "links_as_text",
    "links_as_yaml",
]


def _get_links(uri):
    content = loader.web(uri)
    return parser.get_web_links(content)


def links_as_html(uri):
    return view.as_html(_get_links(uri))


def links_as_json(uri):
    return view.as_json(_get_links(uri))


def links_as_text(uri):
    return view.as_text(_get_links(uri))


def links_as_yaml(uri):
    return view.as_yaml(_get_links(uri))
