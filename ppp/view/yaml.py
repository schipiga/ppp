"""
Module to represent links as yaml.
"""

import yaml


__all__ = [
    "render",
]


def render(links):
    return yaml.dump({"links": list(links), "total": len(links)},
                     default_flow_style=False)
