from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def ele_loc(self, loc):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*loc))

    def eles_loc(self, loc, num):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements(*loc)[num])

    def ele_click(self, loc):
        self.ele_loc(loc).click()

    def eles_click(self, loc, num):
        self.eles_loc(loc, num).click()

    def ele_input(self, loc, text):
        ele1 = self.ele_loc(loc)
        ele1.clear()
        ele1.send_keys(text)

    def eles_input(self, loc, text):
        ele2 = self.ele_loc(loc)
        ele2.clear()
        ele2.input(text)
