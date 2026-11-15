from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage


class InputsPage(BasePage):
    path = "/inputs"
    NUMBER_INPUT = (By.TAG_NAME, "input")

    def type_text(self, text: str) -> None:
        self.driver.find_element(*self.NUMBER_INPUT).send_keys(text)

    def press_up(self) -> None:
        self.driver.find_element(*self.NUMBER_INPUT).send_keys(Keys.ARROW_UP)

    def press_down(self) -> None:
        self.driver.find_element(*self.NUMBER_INPUT).send_keys(Keys.ARROW_DOWN)

    def value(self) -> str:
        number_input = self.driver.find_element(*self.NUMBER_INPUT)
        return number_input.get_property("value")
