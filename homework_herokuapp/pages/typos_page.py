from selenium.webdriver.common.by import By

from .base_page import BasePage


class TyposPage(BasePage):
    path = "/typos"
    PARAGRAPH = (By.TAG_NAME, "p")

    def sample_text(self) -> str:
        return self.driver.find_elements(*self.PARAGRAPH)[1].text
