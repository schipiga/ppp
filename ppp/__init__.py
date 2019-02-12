"""
-------------------------------
Package to parse inet resources
-------------------------------
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


def links_as_html(uri, enum=False):
    """Grab links from URI page and represent them as HTML.

    Args:
        uri (str): URI to grab.
        enum (bool): Flag to enumerate each link.

    Returns:
        string: HTML with list of links.
    """
    return view.as_html(_get_links(uri), enum)


def links_as_json(uri):
    """Grab links from URI page and represent them as JSON.

    Args:
        uri (str): URI to grab.

    Returns:
        string: JSON with list of links and total value.
    """
    return view.as_json(_get_links(uri))


def links_as_text(uri, enum=False):
    """Grab links from URI page and represent them as plan text.

    Args:
        uri (str): URI to grab.
        enum (bool): Flag to enumerate each link.

    Returns:
        string: Plain text with list of links.
    """
    return view.as_text(_get_links(uri), enum)


def links_as_yaml(uri):
    """Grab links from URI page and represent them as YAML.

    Args:
        uri (str): URI to grab.

    Returns:
        string: YAML with list of links and total value.
    """
    return view.as_yaml(_get_links(uri))
