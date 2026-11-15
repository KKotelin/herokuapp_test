from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from .base_page import BasePage


class HoversPage(BasePage):
    path = "/hovers"
    PROFILE = (By.CSS_SELECTOR, ".figure")
    AVATAR = (By.TAG_NAME, "img")
    PROFILE_NAME = (By.CSS_SELECTOR, ".figcaption h5")
    PROFILE_LINK = (By.LINK_TEXT, "View profile")

    def hover_over_profile(self, index: int) -> None:
        profile = self.driver.find_elements(*self.PROFILE)[index]
        avatar = profile.find_element(*self.AVATAR)
        ActionChains(self.driver).move_to_element(avatar).perform()

    def profile_name(self, index: int) -> str:
        profile = self.driver.find_elements(*self.PROFILE)[index]
        return profile.find_element(*self.PROFILE_NAME).text

    def open_profile(self, index: int) -> None:
        profile = self.driver.find_elements(*self.PROFILE)[index]
        profile.find_element(*self.PROFILE_LINK).click()

    def profile_response_status(self) -> int:
        return self.driver.execute_script(
            "return performance.getEntriesByType('navigation')[0]"
            ".responseStatus;"
        )
