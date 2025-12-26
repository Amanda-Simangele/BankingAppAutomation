from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    customerLoginButton_xpath = "//button[contains(@class,'btn-primary') and text()='Customer Login']"


    def __init__(self, driver):
        self.driver = driver


    def clickCustomerLoginButton(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.customerLoginButton_xpath ))
        ).click()
