from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Set up the browser driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Open the SauceDemo site
driver.get("https://www.saucedemo.com")

# 3. Pause so you can actually see it before it closes
time.sleep(5)

# 4. Close the browser
driver.quit()