import pytest
from selenium import webdriver

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.WelcomePage import WelcomePage
from Utils.conftest import setup


def test_case1(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.clickCustomerLoginButton()
    login_page = LoginPage(driver)
    login_page.selectUsername()
    login_page.clickLoginButton()
    welcome_page = WelcomePage(driver)
    welcome_page.clickSelectDepositButton()
    welcome_page.enterAmount("1000")
    welcome_page.clickDepositMoneyButton()
    message = welcome_page.getSuccessMessage()
    assert message == "Deposit Successful", "depossit failed"
    welcome_page.clickLogOutButton()


def test_case2(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.clickCustomerLoginButton()
    login_page = LoginPage(driver)
    login_page.selectUsername()
    login_page.clickLoginButton()
    welcome_page = WelcomePage(driver)
    welcome_page.selectAccount("1004")
    welcome_page.clickSelectDepositButton()
    welcome_page.enterAmount("500")
    welcome_page.clickDepositMoneyButton()
    message = welcome_page.getSuccessMessage()
    assert message == "Deposit Successful", "depossit failed"
    welcome_page.selectAccount("1005")
    welcome_page.clickSelectDepositButton()
    welcome_page.enterAmount("500")
    welcome_page.clickDepositMoneyButton()
    message = welcome_page.getSuccessMessage()
    assert message == "Deposit Successful", "depossit failed"
    welcome_page.selectAccount("1006")
    welcome_page.clickSelectDepositButton()
    welcome_page.enterAmount("500")
    welcome_page.clickDepositMoneyButton()
    message = welcome_page.getSuccessMessage()
    assert message == "Deposit Successful", "depossit failed"
    welcome_page.clickLogOutButton()


def test_case3(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.clickCustomerLoginButton()
    login_page = LoginPage(driver)
    login_page.selectUsername()
    login_page.clickLoginButton()
    welcome_page = WelcomePage(driver)
    welcome_page.selectAccount("1004")
    welcome_page.clickSelectDepositButton()
    welcome_page.enterAmount("31459")
    welcome_page.clickDepositMoneyButton()
    message = welcome_page.getSuccessMessage()
    assert message == "Deposit Successful", "deposit failed"
    welcome_page.clickTransactionsButton()
