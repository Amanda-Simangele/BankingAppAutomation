import pytest

from Pages.WelcomePage import WelcomePage
from Utils.Common_tests import logintest, depositMoneyTest

#@pytest.mark.dev
def test_case2(driver):
    logintest(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.selectAccount("1004")
    depositMoneyTest(driver, "1500")
    welcome_page.selectAccount("1005")
    depositMoneyTest(driver, "1500")
    welcome_page.selectAccount("1006")
    depositMoneyTest(driver, "1500")
    welcome_page.clickLogOutButton()