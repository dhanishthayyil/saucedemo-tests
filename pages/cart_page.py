from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def remove_item(self, product_slug):
        self.click((By.ID, f"remove-{product_slug}"))

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)