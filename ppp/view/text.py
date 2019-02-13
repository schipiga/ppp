"""
Module to represent links as text.
"""


__all__ = [
    "render",
]


def render(links, enum=False):
    """Render links as plain text.

    Args:
        links (list): Links sequence.
        enum (bool): Flag to enumerate each link.

    Returns:
        string: Plain text with list of links.
    """
    if not enum:
        return "\n".join(links)
    return "\n".join("%s. %s" % ((i + 1), l) for i, l in enumerate(links))
