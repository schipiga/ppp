"""
Module to represent links as json.
"""

import json


__all__ = [
    "render",
]


def render(links):
    """Render links in JSON format.

    Args:
        links (list): Links sequence.

    Returns:
        string: JSON with list of links and total value.
    """
    return json.dumps({"links": list(links), "total": len(links)})
