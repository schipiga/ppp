"""
Module to represent links as json.
"""

import json


__all__ = [
    "render",
]


def render(links):
    return json.dumps({"links": list(links), "total": len(links)})
