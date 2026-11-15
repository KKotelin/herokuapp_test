from selenium.webdriver.common.by import By

from .base_page import BasePage


class AddRemoveElementsPage(BasePage):
    path = "/add_remove_elements/"
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")

    def add_element(self) -> None:
        self.driver.find_element(*self.ADD_BUTTON).click()

    def delete_element(self) -> None:
        self.driver.find_element(*self.DELETE_BUTTON).click()

    def delete_button_count(self) -> int:
        return len(self.driver.find_elements(*self.DELETE_BUTTON))
