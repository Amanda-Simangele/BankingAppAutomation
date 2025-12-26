from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    dropdown_username_ID = "userSelect"
    loginbutton_xpath = '//button[@class="btn btn-default"]'

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def selectUsername(self, name="Harry Potter"):
        # wait until the <select> is visible, then use Select to choose the option
        select_el = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.dropdown_username_ID))
        )
        Select(select_el).select_by_visible_text(name)

    def clickLoginButton(self):
        # wait until the button is clickable, then click
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.loginbutton_xpath))
        )
        login_button.click()