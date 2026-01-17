import pytest
import allure
from selenium import webdriver
from Utils.Read_properties import Read_Configs


@pytest.fixture(scope="function")
def driver(request):
    browser = Read_Configs.get_browser()

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.node.driver = driver

    driver.get(Read_Configs.get_application_url())
    driver.maximize_window()
    driver.implicitly_wait(int(Read_Configs.get_implicit_wait()))

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
