from Base.__init__driver import init_driver_method
from page.page_weibo import PageWeibo


class Test_W:
    def setup_class(self):
        self.driver = init_driver_method()
        self.w_obj = PageWeibo(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_w01(self):
        self.w_obj.weibo_login('18120583749')

