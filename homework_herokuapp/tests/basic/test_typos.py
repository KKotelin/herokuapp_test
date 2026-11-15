import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.typos_page import TyposPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_typos_displays_a_known_text_variant(browser: WebDriver) -> None:
    page = TyposPage(browser)
    page.open()

    assert page.sample_text() in (
        "Sometimes you'll see a typo, other times you won't.",
        "Sometimes you'll see a typo, other times you won,t.",
    )
