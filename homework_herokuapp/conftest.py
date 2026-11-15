from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


DRIVER_PATH = Path(__file__).resolve().parent / "drivers" / "chromedriver.exe"


@contextmanager
def _chrome_session() -> Iterator[webdriver.Chrome]:
    service = Service(executable_path=str(DRIVER_PATH))
    driver = webdriver.Chrome(service=service)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def browser() -> Iterator[webdriver.Chrome]:
    with _chrome_session() as driver:
        yield driver


@pytest.fixture(scope="class")
def class_browser() -> Iterator[webdriver.Chrome]:
    with _chrome_session() as driver:
        yield driver
