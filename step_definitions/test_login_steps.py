import pytest
import os
from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage
from playwright.sync_api import Page

FEATURE_FILE = os.path.join(os.path.dirname(__file__), "../features/login.feature")

@scenario(FEATURE_FILE, 'Successful login with valid credentials')
def test_login_flow():
    pass

@given('the user is on the Magente homepage')
def go_home(page: Page):
    login_pg = LoginPage(page)
    login_pg.navigate("https://magento.softwaretestingboard.com/")

@when('the user navigates to the login page')
def go_to_login(page: Page):
    page.get_by_role("link", name="Sign In").click()

@when('logs in with "pao_tester@example.com" and "Password123!"')
def perfom_login(page: Page):
    login_pg = LoginPage(page)
    login_pg.login("pao_tester@example.com", "Password123!")

@then('the user should see their personalized welcome message')
def verify_welcome(page: Page):
    login_pg = LoginPage(page)
    login_pg.verify_success()