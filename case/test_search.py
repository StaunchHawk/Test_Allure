from Base.__init__driver import init_driver_method
from page.search import Page_1


class Test_AA:
    def setup_class(self):
        self.driver = init_driver_method()
        self.search_obj = Page_1(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_a1(self):
        self.search_obj.search_click()

    def test_a2(self):
        self.search_obj.search_input('wlan')
