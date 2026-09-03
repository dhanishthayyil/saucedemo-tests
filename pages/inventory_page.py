from selenium.webdriver.common.by import By

class InventoryPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*self.PAGE_TITLE).text

    def add_to_cart(self, product_slug):
        # e.g. product_slug = "sauce-labs-backpack"
        locator = (By.ID, f"add-to-cart-{product_slug}")
        self.driver.find_element(*locator).click()

    def get_cart_count(self):
        try:
            return int(self.driver.find_element(*self.CART_BADGE).text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()