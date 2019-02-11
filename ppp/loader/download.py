"""
Module to download web page.
"""

import requests


__all__ = [
    "download",
]


def download(uri):
    r = requests.get(uri)
    return r.text
