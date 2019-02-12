from hamcrest import assert_that, equal_to

from ppp import view


def test_as_html():
    result = view.as_html(["http://example.local"])
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


def test_as_html_enum():
    result = view.as_html(["http://example.local"], enum=True)
    assert_that(result, equal_to("""<html>
<head>
<title>
Links
</title>
</head>
<body>
<h3>Total: 1</h3>
<div>1. <a href='http://example.local'>http://example.local</a></div>
<body>
</html>"""))


def test_as_json():
    result = view.as_json(["http://example.local"])
    assert_that(
        result,
        equal_to('{"links": ["http://example.local"], "total": 1}'))


def test_as_text():
    result = view.as_text(["http://example.local"])
    assert_that(result, equal_to("http://example.local"))


def test_as_text_enum():
    result = view.as_text(["http://example.local"], enum=True)
    assert_that(result, equal_to("1. http://example.local"))


def test_as_yaml():
    result = view.as_yaml(["http://example.local"])
    assert_that(
        result,
        equal_to('links:\n- http://example.local\ntotal: 1\n'))
