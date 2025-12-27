from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class WelcomePage:

    selectDepositButton_xpath = '//button[@ng-click="deposit()"]'
    amountInput_xpath = '//input[@type="number"]'
    depositMoneyButton_xpath = '//button[@type="submit"]'
    successMessage_xpath = '//span[@class="error ng-binding" and @ng-show="message" ]'
    logOutButton_xpath = '//button[@ng-show="logout" and @ng-click="byebye()"]'
    accountSelect_ID = "accountSelect"
    transactionsButton_xpath = '//button[@ng-class="btnClass1" and @ng-click="transactions()" ]'
    withdrawlButton_xpath = '//button[@ng-class="btnClass3" and @ng-click="withdrawl()"]'
    balanceAmount_xpath = '(//strong[@class="ng-binding"])[2]'
    toWithdrawButton_xpath = '//button[@type="submit" and @class="btn btn-default"]'

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

#for option in select.options:
   # select.select_by_visible_text(option.text)
    def selectAccount(self, account_number):
        account_select = self.wait.until(
            EC.element_to_be_clickable((By.ID, self.accountSelect_ID))
        )
        Select(account_select).select_by_visible_text(account_number)

    def getOriginalBalanceAmount(self):
        balance_amount = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.balanceAmount_xpath))
        )
        return balance_amount.text

    def clickSelectDepositButton(self):
        deposit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.selectDepositButton_xpath))
        )
        deposit_button.click()

    def enterAmount(self, amount):
        amount_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.amountInput_xpath))
        )
        amount_input.clear()
        amount_input.send_keys(str(amount))



    def clickDepositMoneyButton(self):
        deposit_money_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.depositMoneyButton_xpath))
        )
        deposit_money_button.click()



    def getSuccessMessage(self):
        success_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.successMessage_xpath))
        )
        return success_message.text

    def clickLogOutButton(self):
        log_out_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.logOutButton_xpath))
        )
        log_out_button.click()

    def clickTransactionsButton(self):
        transactionsButton = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.transactionsButton_xpath))
        )
        transactionsButton.click()


    def clickWithdrawlButton(self):
        withdrawlButton = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.withdrawlButton_xpath))
        )
        withdrawlButton.click()

    def clickToWithdrawButton(self):
        toWithdrawButton = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.toWithdrawButton_xpath))
        )
        toWithdrawButton.click()

    def getBalanceAmountafterWithdral(self):
        balance_amount = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.balanceAmount_xpath))
        )
        return balance_amount.text