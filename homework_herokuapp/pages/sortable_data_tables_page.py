from selenium.webdriver.common.by import By

from .base_page import BasePage


class SortableDataTablesPage(BasePage):
    path = "/tables"
    CELL_XPATH = "//table[{table}]//tbody/tr[{row}]/td[{column}]"

    def cell_text(self, row: int, column: int, table: int = 1) -> str:
        """Read a cell using one-based table, row, and column numbers."""
        xpath = self.CELL_XPATH.format(table=table, row=row, column=column)
        return self.driver.find_element(By.XPATH, xpath).text
