from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TransactionPage:

    row_xpath = "//tr[contains(@id,'anchor')][td[2]='1']"

    def __init__(self, driver):
        self.driver = driver

    def getFirstTransactionRow(self):
        row_amountLable = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.row_xpath))
        )
        return row_amountLable.text





