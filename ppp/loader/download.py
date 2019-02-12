"""
Module to download web page.
"""

import requests


__all__ = [
    "download",
]


def download(uri):
    """Download URI.
    """
    r = requests.get(uri)
    return r.text
