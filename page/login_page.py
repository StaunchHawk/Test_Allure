import page
from Base.base import Base


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_obj = Base(self.driver)

    def login_input(self, text):
        self.base_obj.ele_input(page.s_1, text)
