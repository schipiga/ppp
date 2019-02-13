"""
Module to parse html page.
"""

from bs4 import BeautifulSoup


__all__ = [
    "get_links",
]


def get_links(html):
    """Retrieve links from HTML.

    Args:
        html (str): Raw HTML.

    Returns:
        list: Links sequence.
    """
    soup = BeautifulSoup(html, 'html.parser')
    return {a['href'] for a in soup.find_all('a', href=True, text=True)}
