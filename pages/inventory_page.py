from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_to_cart(self, product_slug):
        locator = (By.ID, f"add-to-cart-{product_slug}")
        self.click(locator)

    def get_cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except:
            return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)