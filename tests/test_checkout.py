import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import CONFIG

@pytest.mark.smoke
def test_complete_purchase_flow(driver):
    # Log in
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["standard_user"]
    login_page.login(creds["username"], creds["password"])

    # Add items to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    assert inventory_page.get_cart_count() == 2

    # Go to cart
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 2

    # Checkout
    cart_page.checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Dany", "Test", "12345")
    checkout_page.finish_order()

    # Confirm order
    assert checkout_page.get_confirmation_text() == "Thank you for your order!"


@pytest.mark.regression
def test_checkout_requires_first_name(driver):
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
    checkout_page.fill_info("", "Test", "12345")  # missing first name

    assert "first name is required" in checkout_page.get_error_text().lower()