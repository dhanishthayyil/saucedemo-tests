from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def fill_info(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def get_confirmation_text(self):
        return self.get_text(self.CONFIRMATION_HEADER)

    def get_error_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_subtotal(self):
        text = self.get_text(self.SUMMARY_SUBTOTAL)
        return float(text.replace("Item total: $", ""))

    def get_tax(self):
        text = self.get_text(self.SUMMARY_TAX)
        return float(text.replace("Tax: $", ""))

    def get_total(self):
        text = self.get_text(self.SUMMARY_TOTAL)
        return float(text.replace("Total: $", ""))

    def get_item_prices(self):
        elements = self.driver.find_elements(*self.CART_ITEM_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]