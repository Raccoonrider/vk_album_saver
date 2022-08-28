from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Album:

    def __init__(self, app):
        self.app = app

    def __iter__(self):
        self.open_first_picture()
        self.first_url = None
        return self

    def __next__(self):
        url = self.get_picture_url()
        if self.first_url == url:
            raise StopIteration
        if self.first_url is None:
            self.first_url = url
        self.open_next_picture()
        return url

    def open_first_picture(self):
        wd = self.app.wd
        wd.get(self.app.url)
        wd.find_element(By.XPATH, "//a[contains(@href, '/photo')]").click()

    def open_next_picture(self):
        wd = self.app.wd
        wd.find_element(By.ID, "pv_photo").click()
        # button = wd.find_element(By.ID, "pv_nav_btn_right")
        # ActionChains(wd).move_to_element(button).perform()
        # button.click()

    def get_picture_url(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "a.pv_actions_more").click()
        sleep(0.2)
        url = wd.find_element(By.ID, "pv_more_act_download").get_attribute("href")
        return url




    