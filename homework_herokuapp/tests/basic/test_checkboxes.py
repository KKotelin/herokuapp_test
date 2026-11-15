import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.checkboxes_page import CheckboxesPage


pytestmark = [pytest.mark.basic, pytest.mark.smoke, pytest.mark.regression]


def test_first_checkbox_can_be_checked(browser: WebDriver) -> None:
    page = CheckboxesPage(browser)
    page.open()

    assert not page.is_checked(0)
    page.click_checkbox(0)
    assert page.is_checked(0)


def test_second_checkbox_can_be_unchecked(browser: WebDriver) -> None:
    page = CheckboxesPage(browser)
    page.open()

    assert page.is_checked(1)
    page.click_checkbox(1)
    assert not page.is_checked(1)
