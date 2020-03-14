import page
from Base.base import Base


class PageWeibo:

    def __init__(self, driver):
        self.driver = driver
        self.base_obj = Base(self.driver)

    def weibo_login(self,text):
        self.base_obj.ele_input(page.w_1,text)

