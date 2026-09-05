from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_to_cart(self, product_slug):
        self.click((By.ID, f"add-to-cart-{product_slug}"))

    def remove_from_cart(self, product_slug):
        self.click((By.ID, f"remove-{product_slug}"))

    def get_cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except:
            return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def get_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]

    def sort_by(self, value):
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.SORT_DROPDOWN)).select_by_value(value)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)