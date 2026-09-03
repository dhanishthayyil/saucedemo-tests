from selenium.webdriver.common.by import By

class InventoryPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*self.PAGE_TITLE).text