from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_page import BasePage


class DropdownPage(BasePage):
    path = "/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def _select(self) -> Select:
        return Select(self.driver.find_element(*self.DROPDOWN))

    def option_texts(self) -> list[str]:
        return [option.text for option in self._select().options]

    def select_option(self, text: str) -> None:
        self._select().select_by_visible_text(text)

    def selected_option_text(self) -> str:
        return self._select().first_selected_option.text
