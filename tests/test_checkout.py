import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import CONFIG
@pytest.mark.regression
def test_checkout_requires_last_name(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["standard_user"]
    login_page.login(creds["username"], creds["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Dany", "", "12345")
    assert "last name is required" in checkout_page.get_error_text().lower()

@pytest.mark.regression
def test_checkout_requires_postal_code(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["standard_user"]
    login_page.login(creds["username"], creds["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Dany", "Test", "")
    assert "postal code is required" in checkout_page.get_error_text().lower()

@pytest.mark.regression
def test_checkout_all_fields_empty(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["standard_user"]
    login_page.login(creds["username"], creds["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("", "", "")
    assert "first name is required" in checkout_page.get_error_text().lower()