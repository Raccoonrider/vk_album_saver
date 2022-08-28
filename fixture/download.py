from urllib.request import urlopen, Request
from urllib.error import HTTPError
from uuid import uuid4
from threading import Thread
import re


class Downloader:

    def __init__(self):
        self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                        "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;"
                        "q=0.9",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, "
                            "like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            }

        #Generate unique filename prefix
        self.filename_prefix = f"img/image_{str(uuid4())[:6]}_"
        self.extension_pattern = r"(\.[\w]{3})\?size"
        self.index = 0
        self.current_url = None
        self.threadpool = []
        

    def add_url(self, url):
        self.current_url = url
        thread = Thread(target=self.worker)
        thread.start()
        self.threadpool.append(thread)


    def worker(self):
        url = self.current_url
        self.index += 1
        extension = re.search(self.extension_pattern, url).group(1)
        filename = f"{self.filename_prefix}{self.index:05d}{extension}"
        try:
            req = Request(url, headers=self.headers)
            req = urlopen(req)
            with open(filename, mode="wb") as f:
                f.write(req.read())
        except HTTPError as e:
            print (e)    
