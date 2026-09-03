import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_title() == "Products"

@pytest.mark.smoke
def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_text().lower()

@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected_error", [
    ("", "secret_sauce", "username is required"),
    ("standard_user", "", "password is required"),
])
def test_invalid_login_combos(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    assert expected_error in login_page.get_error_text().lower()