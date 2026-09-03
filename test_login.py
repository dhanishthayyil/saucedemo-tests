from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(2)

page_title = driver.find_element(By.CLASS_NAME, "title").text
assert page_title == "Products", f"Expected 'Products' but got '{page_title}'"

print("✅ Login test passed!")

driver.quit()