"""
Module to download web page.
"""

import requests


__all__ = [
    "download",
]


def download(uri):
    """Download content from URI.

    Args:
        uri (str): `URI <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`_.

    Returns:
        str: URI content.
    """  # noqa
    r = requests.get(uri)
    return r.text
