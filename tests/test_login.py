import time
import pytest
import json
import requests

# from constants import POSITIVE_LOGIN_CREDS, POSITIVE_SIGNUP_CREDS, NEGATIVE_LOGIN_CREDS
from ui_project.pages.auth_page import AuthPage


class TestAuthClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = AuthPage(browser, url)
        self.main_page.open_page()

    def test_login_ui(self):
        self.main_page.login_ui('ekaterin.lisitsyna@gmail.com', "xkZZ7D$tM@9$B3$")
        self.main_page.check_login_successfully_complete()

