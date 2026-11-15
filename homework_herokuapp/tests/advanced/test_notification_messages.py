import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.notification_messages_page import NotificationMessagesPage


@pytest.mark.advanced
@pytest.mark.regression
def test_notification_displays_a_known_message(browser: WebDriver) -> None:
    page = NotificationMessagesPage(browser)
    page.open()

    page.load_message()

    assert page.message_text() in (
        "Action successful",
        "Action unsuccesful, please try again",
    )
