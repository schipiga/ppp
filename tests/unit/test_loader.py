from unittest import mock

import attrdict
from hamcrest import assert_that, equal_to
import pytest
import requests

from ppp import loader


@pytest.fixture
def mock_request_get(reset_mock):

    def mock_get(result):
        reset_mock(
            requests, "get",
            mock.Mock(return_value=attrdict.AttrDict({"text": result})))

    return mock_get


def test_download(mock_request_get):
    mock_request_get("mocked content")
    result = loader.web("https://example.local")
    assert_that(result, equal_to("mocked content"))
    assert_that(
        requests.get.call_args[0][0],
        equal_to("https://example.local"))
