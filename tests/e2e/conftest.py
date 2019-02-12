import pytest


WEB_PAGE = """
<html>
<head>
<title>My page</title>
</head>
<body>
<a href="http://example.local">my link</a>
</body>
</html>
"""


@pytest.fixture
def web_url(httpserver):
    httpserver.serve_content(WEB_PAGE)
    return httpserver.url
