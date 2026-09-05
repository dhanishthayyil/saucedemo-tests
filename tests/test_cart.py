import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config_reader import CONFIG

@pytest.fixture
def inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["standard_user"]
    login_page.login(creds["username"], creds["password"])
    return InventoryPage(driver)

@pytest.mark.smoke
def test_open_cart(inventory_page, driver):
    inventory_page.go_to_cart()
    assert "cart.html" in driver.current_url

@pytest.mark.regression
def test_cart_shows_added_product(inventory_page, driver):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1

@pytest.mark.regression
def test_cart_shows_multiple_products(inventory_page, driver):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 3

@pytest.mark.regression
def test_remove_product_from_cart_page(inventory_page, driver):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 2
    cart_page.remove_item("sauce-labs-backpack")
    assert cart_page.get_item_count() == 1

@pytest.mark.regression
def test_continue_shopping_returns_to_products(inventory_page, driver):
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.continue_shopping()
    assert inventory_page.get_title() == "Products"