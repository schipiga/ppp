"""
Module to represent links as yaml.
"""

import yaml


__all__ = [
    "render",
]


def render(links):
    """Render links in YAML format.

    Args:
        links (list): Links sequence.

    Returns:
        string: YAML with list of links and total value.
    """
    return yaml.dump({"links": list(links), "total": len(links)},
                     default_flow_style=False)
