import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.dropdown_page import DropdownPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("option", ["Option 1", "Option 2"])
def test_dropdown_option_can_be_selected(browser: WebDriver, option: str) -> None:
    page = DropdownPage(browser)
    page.open()

    assert page.option_texts() == [
        "Please select an option",
        "Option 1",
        "Option 2",
    ]

    page.select_option(option)
    assert page.selected_option_text() == option
