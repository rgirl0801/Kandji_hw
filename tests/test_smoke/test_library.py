import time
import pytest

from ui_project.pages.library_page import LibraryPage


class TestLibraryClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.library_page = LibraryPage(browser, url)
        self.library_page.open_page()

    def test_liftoff_library_item(self):
        self.library_page.click_add_library_item()
        self.library_page.click_liftoff()
        self.library_page.click_add_and_configure()
        self.library_page.is_liftoff_panel_present()

    def test_liftoff_library_item_see_more(self):
        self.library_page.click_add_library_item()
        self.library_page.click_liftoff_see_more()
        self.library_page.click_add_and_configure()
        self.library_page.is_liftoff_panel_present()




