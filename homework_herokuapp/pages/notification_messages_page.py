from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage


class NotificationMessagesPage(BasePage):
    path = "/notification_message_rendered"
    LOAD_MESSAGE_LINK = (By.LINK_TEXT, "Click here")
    NOTIFICATION = (By.ID, "flash")

    def load_message(self) -> None:
        self.driver.find_element(*self.LOAD_MESSAGE_LINK).click()

    def message_text(self) -> str:
        notification = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.NOTIFICATION
            )
        )
        return notification.text.removesuffix("×").strip()
