from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    BASE_URL = "https://the-internet.herokuapp.com"
    path: str

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(f"{self.BASE_URL}{self.path}")
