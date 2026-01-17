from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.WelcomePage import WelcomePage



def logintest(driver):
    home_page = HomePage(driver)
    home_page.clickCustomerLoginButton()
    login_page = LoginPage(driver)
    login_page.selectUsername()
    login_page.clickLoginButton()

def depositMoneyTest(driver, amount):
    welcome_page = WelcomePage(driver)
    welcome_page.clickSelectDepositButton()
    welcome_page.enterAmount(amount)
    welcome_page.clickDepositMoneyButton()
    message = welcome_page.getSuccessMessage()
    assert message == "Deposit Successful", "deposit failed"


