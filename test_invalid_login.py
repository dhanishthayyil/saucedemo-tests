from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
error_text = error_element.text

assert "locked out" in error_text.lower(), f"Expected a locked-out error, got: '{error_text}'"

print("✅ Invalid login test passed!")

driver.quit()