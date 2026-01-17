from time import sleep

import pytest

from Pages.TransactionPage import TransactionPage
from Pages.WelcomePage import WelcomePage
from Utils.Common_tests import logintest, depositMoneyTest



#@pytest.mark.dev
def test_case3(driver):
    logintest(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.selectAccount("1004")
    originalAmount = welcome_page.getOriginalBalanceAmount()
    depositMoneyTest(driver, "31459")
    welcome_page.clickTransactionsButton()
    transcation_page = TransactionPage(driver)
    amount = transcation_page.getTransactionAmount()
    assert amount == "31459", "wrong deposit amount"
    transcation_page.clickBackButton()
    welcome_page.clickWithdrawlButton()
    welcome_page.enterAmount("31459")
    welcome_page.clickToWithdrawButton()
    sleep(5)
    afterWithdrawalAmount = welcome_page.getBalanceAmountafterWithdral()
    # debug prints for values
    print(f"originalAmount={originalAmount!r}")
    print(f"afterWithdrawalAmount={afterWithdrawalAmount!r}")

    # existing check
    if afterWithdrawalAmount == originalAmount:
        assert True
    else:
       assert False, "amounts not the same after withdrawal"

    welcome_page.clickTransactionsButton()
    withdrawAmount = transcation_page.getTransactionAmountByRow(2)
    assert withdrawAmount == "31459", "wrong withdrawal amount"
    welcome_page.clickLogOutButton()
