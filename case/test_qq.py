from Base.__init__driver import init_driver_method
from page.login_page import LoginPage


class Test_Qq:
    def setup_class(self):
        self.driver = init_driver_method()
        self.login_obj = LoginPage(self.driver)
    def teardown_class(self):
        self.driver.quit()

    def test_qq(self):
        self.login_obj.login_input('2832195319')