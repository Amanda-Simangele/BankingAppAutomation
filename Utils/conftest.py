import pytest
from selenium import webdriver
from Utils.Read_properties import Read_Configs

@pytest.fixture
def setup():
    browser = Read_Configs.get_browser()
    match browser.lower():
        case "firefox":
            driver = webdriver.Firefox()
        case "chrome":
            driver = webdriver.Chrome()
        case "edge":
            driver = webdriver.Edge()
        case _:
            raise ValueError(f"Unsupported browser: {browser}")

    driver.get(Read_Configs.get_application_url())
    driver.maximize_window()
    driver.implicitly_wait(int(Read_Configs.get_implicit_wait()))

    yield driver

    driver.quit()
