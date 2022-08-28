from selenium import webdriver

from fixture.album import Album
from fixture.download import Downloader

class Application:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("user-data-dir=C:\\Users\\Thor\\AppData\\Local\\Google\\Chrome\\User Data")
        self.url = "https://vk.com/album175533500_285018858"

    def __enter__(self, *args, **kwargs):
        self.wd = webdriver.Chrome(chrome_options=self.options)
        self.wd.implicitly_wait(15)
        self.album = Album(self)
        self.dl = Downloader()
        return self

    def __exit__(self, *args, **kwargs):
        for thread in self.dl.threadpool:
            thread.join()
        self.wd.quit()

    