import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.inputs_page import InputsPage

pytestmark = [pytest.mark.basic, pytest.mark.smoke, pytest.mark.regression]


@pytest.mark.parametrize("number", [-3, 0, 7])
def test_number_can_be_entered_and_changed_with_arrows(browser: WebDriver, number: int) -> None:
    page = InputsPage(browser)
    page.open()

    page.type_text(str(number))
    assert page.value() == str(number)

    page.press_up()
    assert page.value() == str(number + 1)

    page.press_down()
    assert page.value() == str(number)


@pytest.mark.parametrize("text", ["abc", "@#$"])
def test_number_input_rejects_non_numeric_text(browser: WebDriver, text: str) -> None:
    page = InputsPage(browser)
    page.open()

    page.type_text(text)
    assert page.value() == ""
