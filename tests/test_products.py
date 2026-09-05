import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import CONFIG
from utils.test_data import EXPECTED_PRODUCTS
from utils.helpers import is_sorted_ascending, is_sorted_descending

@pytest.fixture
def inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["standard_user"]
    login_page.login(creds["username"], creds["password"])
    return InventoryPage(driver)

@pytest.mark.smoke
def test_products_page_displayed(inventory_page):
    assert inventory_page.get_title() == "Products"
    assert inventory_page.get_product_count() == 6

@pytest.mark.regression
def test_product_names_present(inventory_page):
    names = inventory_page.get_product_names()
    assert sorted(names) == sorted(EXPECTED_PRODUCTS)

@pytest.mark.regression
def test_product_prices_are_valid(inventory_page):
    prices = inventory_page.get_product_prices()
    assert all(p > 0 for p in prices)

@pytest.mark.smoke
def test_add_single_product_to_cart(inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == 1

@pytest.mark.regression
def test_add_multiple_products_to_cart(inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")
    assert inventory_page.get_cart_count() == 3

@pytest.mark.regression
def test_remove_product_from_inventory_page(inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == 1
    inventory_page.remove_from_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == 0

@pytest.mark.regression
def test_sort_az(inventory_page):
    inventory_page.sort_by("az")
    assert is_sorted_ascending(inventory_page.get_product_names())

@pytest.mark.regression
def test_sort_za(inventory_page):
    inventory_page.sort_by("za")
    assert is_sorted_descending(inventory_page.get_product_names())

@pytest.mark.regression
def test_sort_price_low_high(inventory_page):
    inventory_page.sort_by("lohi")
    assert is_sorted_ascending(inventory_page.get_product_prices())

@pytest.mark.regression
def test_sort_price_high_low(inventory_page):
    inventory_page.sort_by("hilo")
    assert is_sorted_descending(inventory_page.get_product_prices())

@pytest.mark.smoke
def test_logout(inventory_page):
    inventory_page.logout()
    assert "saucedemo.com" in inventory_page.driver.current_url