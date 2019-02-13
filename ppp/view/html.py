"""
Module to represent links as html.
"""

__all__ = [
    "render",
]


TMPL = """<html>
<head>
<title>
Links
</title>
</head>
<body>
<h3>Total: %s</h3>
%s
<body>
</html>"""


def render(links, enum=False):
    """Render links in HTML format.

    Args:
        links (list): Links sequence.
        enum (bool): Flag to enumerate each link.

    Returns:
        string: HTML with list of links.
    """
    chunks = []
    for i, l in enumerate(links):
        if enum:
            chunk = "<div>{0}. <a href='{1}'>{1}</a></div>".format(i + 1, l)
        else:
            chunk = "<div><a href='{0}'>{0}</a></div>".format(l)
        chunks.append(chunk)
    return TMPL % (len(chunks), "\n".join(chunks))
