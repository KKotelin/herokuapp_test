import sys

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.sortable_data_tables_page import SortableDataTablesPage


@pytest.fixture(scope="class")
def tables_page(class_browser: WebDriver) -> SortableDataTablesPage:
    page = SortableDataTablesPage(class_browser)
    page.open()
    return page


@pytest.mark.advanced
@pytest.mark.regression
@pytest.mark.skipif(
    sys.platform != "win32", reason="The bundled ChromeDriver requires Windows"
)
class TestSortableDataTables:
    @pytest.mark.parametrize(
        "table, row, column, expected_text",
        [
            (1, 1, 1, "Smith"),
            (1, 2, 2, "Frank"),
            (1, 3, 3, "jdoe@hotmail.com"),
            (1, 4, 4, "$50.00"),
            (2, 1, 2, "John"),
        ],
    )
    def test_cell_contains_expected_text(self, tables_page: SortableDataTablesPage, table: int, row: int, column: int, expected_text: str) -> None:
        assert tables_page.cell_text(row, column, table) == expected_text
