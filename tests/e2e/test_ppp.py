from hamcrest import assert_that, equal_to
import ppp


def test_links_as_html(web_url):
    result = ppp.links_as_html(web_url)
    assert_that(result, equal_to("""<html>
<head>
<title>
Links
</title>
</head>
<body>
<h3>Total: 1</h3>
<div><a href='http://example.local'>http://example.local</a></div>
<body>
</html>"""))


def test_links_as_json(web_url):
    result = ppp.links_as_json(web_url)
    assert_that(
        result,
        equal_to('{"links": ["http://example.local"], "total": 1}'))


def test_links_as_text(web_url):
    result = ppp.links_as_text(web_url)
    assert_that(result, equal_to("http://example.local"))


def test_links_as_yaml(web_url):
    result = ppp.links_as_yaml(web_url)
    assert_that(result, equal_to("links:\n- http://example.local\ntotal: 1\n"))
