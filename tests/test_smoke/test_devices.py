import time
import pytest

from ui_project.pages.devices_page import DevicesPage


class TestDevicesClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.devices_page = DevicesPage(browser, url)
        self.devices_page.open_page()

    def test_adding_devices(self):
        self.devices_page.adding_devices()
        self.devices_page.element_is_present()

    def test_adding_filter(self):
        self.devices_page.adding_filter()




