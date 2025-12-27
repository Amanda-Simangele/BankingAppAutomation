
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import re


class TransactionPage:

    # XPath to the second cell of the first transaction row
    first_amount_cell_xpath = '(//table[@class="table table-bordered table-striped"]/tbody/tr/td[2])[1]'
    rows_xpath = '//table[@class="table table-bordered table-striped"]/tbody/tr'
    backButton_xpath = '//button[@class="btn" and @ng-click="back()"]'

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # python
    def _clean_numeric(self, text: str) -> str:
        # Return the first run of digits (allow commas and dots).
        # Examples: "€31,459.00" -> "31459.00", "No data" -> ""
        if not text:
            return ""
        m = re.search(r'[\d\.,]+', text)
        if not m:
            return ""
        # Remove thousands separators and extra spaces
        return m.group(0).replace(',', '').strip()

    def getTransactionAmount(self) -> str:
        # Try the primary table cell first
        try:
            cell = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.first_amount_cell_xpath))
            )
            amount = self._clean_numeric(cell.text)
            if amount:
                return amount
        except TimeoutException:
            raise AssertionError(f"Timed out waiting for transaction cell: {self.first_amount_cell_xpath}")

        # Fallback: check up to 10 recent rows and return the first numeric value found
        rows = self.driver.find_elements(By.XPATH, self.rows_xpath)[:10]
        for row in rows:
            for td in row.find_elements(By.TAG_NAME, "td"):
                cleaned = self._clean_numeric(td.text)
                if cleaned:
                    return cleaned

        # Nothing found
        raise AssertionError("Could not find a transaction amount in recent rows.")

    def clickBackButton(self):
        back_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.backButton_xpath))
        )
        back_button.click()

    def getTransactionAmountByRow(self, row_index: int) -> str:
        """
        Returns the numeric amount from a specific transaction row.
        row_index is 1-based (1 = first row, 2 = second row)
        """
        rows = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.rows_xpath))
        )

        if row_index > len(rows):
            raise AssertionError(
                f"Requested row {row_index}, but only {len(rows)} rows are available"
            )

        row = rows[row_index - 1]  # convert to 0-based index
        cells = row.find_elements(By.TAG_NAME, "td")

        amount_text = cells[1].text  # 2nd <td> = amount
        return self._clean_numeric(amount_text)
