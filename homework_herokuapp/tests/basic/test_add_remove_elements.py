import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.add_remove_elements_page import AddRemoveElementsPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_add_two_elements_and_remove_one(browser: WebDriver) -> None:
    page = AddRemoveElementsPage(browser)
    page.open()

    page.add_element()
    page.add_element()
    assert page.delete_button_count() == 2

    page.delete_element()
    assert page.delete_button_count() == 1
