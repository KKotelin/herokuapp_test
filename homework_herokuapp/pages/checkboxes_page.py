from selenium.webdriver.common.by import By

from .base_page import BasePage


class CheckboxesPage(BasePage):
    path = "/checkboxes"
    CHECKBOX = (By.CSS_SELECTOR, "[type='checkbox']")

    def click_checkbox(self, index: int) -> None:
        self.driver.find_elements(*self.CHECKBOX)[index].click()

    def is_checked(self, index: int) -> bool:
        return self.driver.find_elements(*self.CHECKBOX)[index].is_selected()
