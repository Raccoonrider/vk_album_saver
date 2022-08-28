

from fixture.application import Application

application = Application()
with application as app:
    for url in app.album:
        print(url)
        app.dl.add_url(url)