from hamcrest import assert_that, only_contains

from ppp import parser


def test_get_web_links():
    html = """
    <html>
    <head>
    <title>My page</title>
    </head>
    <body>
    <a href="http://example.local">my link</a>
    </body>
    </html>
    """
    result = parser.get_web_links(html)
    assert_that(result, only_contains("http://example.local"))
