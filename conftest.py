import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield drv
    drv.quit()