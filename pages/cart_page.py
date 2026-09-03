from selenium.webdriver.common.by import By

class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()