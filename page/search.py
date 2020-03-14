
import page
from Base.base import Base

class Page_1:
    def __init__(self, driver):
        self.driver = driver
        self.obj = Base(self.driver)

    def search_click(self):
        self.obj.ele_click(page.s_1)

    def search_input(self, text):
        self.obj.ele_input(page.s_2, text)

