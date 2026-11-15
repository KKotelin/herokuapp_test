from urllib.parse import urlsplit

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.hovers_page import HoversPage


class ProfileNotFoundError(AssertionError):
    """The expected profile URL returned HTTP 404."""


@pytest.mark.advanced
@pytest.mark.regression
@pytest.mark.xfail(
    reason="The demo site's profile links currently return HTTP 404",
    raises=ProfileNotFoundError,
    strict=True,
)
@pytest.mark.parametrize("profile_number", [1, 2, 3])
def test_profile_can_be_opened_after_hovering(browser: WebDriver, profile_number: int) -> None:
    page = HoversPage(browser)
    page.open()

    index = profile_number - 1
    page.hover_over_profile(index)
    assert page.profile_name(index) == f"name: user{profile_number}"

    page.open_profile(index)
    assert urlsplit(browser.current_url).path == f"/users/{profile_number}"

    status = page.profile_response_status()
    if status == 404:
        raise ProfileNotFoundError(f"{browser.current_url} returned HTTP 404")
    assert 200 <= status < 300
