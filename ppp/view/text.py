"""
Module to represent links as text.
"""


__all__ = [
    "render",
]


def render(links, enum=False):
    if not enum:
        return "\n".join(links)
    return "\n".join("%s. %s" % ((i + 1), l) for i, l in enumerate(links))
