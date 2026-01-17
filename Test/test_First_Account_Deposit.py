
import pytest
from Pages.WelcomePage import WelcomePage
from Utils.Common_tests import logintest, depositMoneyTest


#@pytest.mark.dev
def test_case1(driver):
    logintest(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.clickSelectDepositButton()
    welcome_page.enterAmount("1000")
    welcome_page.clickDepositMoneyButton()
    message = welcome_page.getSuccessMessage()
    #allure.attach(driver.get_screenshot_as_png(), name="deposit sucessful",
     #             attachment_type=allure.attachment_type.PNG)
    assert message == "Deposit Successful", "depossit failed"
    welcome_page.clickLogOutButton()

'''
@pytest.mark.dev
def test_case2(setup):
    driver = setup
    logintest(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.selectAccount("1004")
    depositMoneyTest(driver, "1500")
    welcome_page.selectAccount("1005")
    depositMoneyTest(driver, "1500")
    welcome_page.selectAccount("1006")
    depositMoneyTest(driver, "1500")
    welcome_page.clickLogOutButton()

@pytest.mark.dev
def test_case3(setup):
    driver = setup
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
'''





