from selenium.webdriver.common.by import By
import pytest
from ui_project.pages.blueprints_page import BlueprintsPage


class TestBlueprintClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = BlueprintsPage(browser, url)
        self.main_page.open_page()

    def test_adding_blueprint_from_scratch(self):
        self.main_page.create_blueprint_from_scratch()
        self.main_page.adding_blueprint_name()
        self.main_page.adding_blueprint_description()
        self.main_page.adding_blueprint_confirmation()
        self.main_page.is_blueprint_present()

    def test_adding_blueprint_level_1(self):
        self.main_page.create_blueprint_from_template_level_1()
        self.main_page.adding_blueprint_name()
        self.main_page.adding_blueprint_description()
        self.main_page.adding_blueprint_confirmation()
        self.main_page.is_blueprint_present()

    def test_adding_blueprint_level_2(self):
        self.main_page.create_blueprint_from_template_level_2()
        self.main_page.adding_blueprint_name()
        self.main_page.adding_blueprint_description()
        self.main_page.adding_blueprint_confirmation()
        self.main_page.is_blueprint_present()

    def test_adding_blueprint_viewing_details(self):
        self.main_page.create_blueprint_from_template_level_2()
        self.main_page.click_blueprint_use_this_template()
        self.main_page.adding_blueprint_name()
        self.main_page.adding_blueprint_description()
        self.main_page.adding_blueprint_confirmation()
        self.main_page.is_blueprint_present()

    def test_search_blueprint(self):
        self.main_page.type_into_search_field()
        self.main_page.is_blueprint_present()