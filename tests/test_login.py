import pytest
from pages import login_page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import CONFIG

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["standard_user"]
    login_page.login(creds["username"], creds["password"])



    inventory_page = InventoryPage(driver)
    assert inventory_page.get_title() == "Products"

@pytest.mark.smoke
def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["users"]["locked_out_user"]
    login_page.login(creds["username"], creds["password"])

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