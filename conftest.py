import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield drv
    drv.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_name = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)
            print(f"\nScreenshot saved: {screenshot_name}")