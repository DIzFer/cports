pkgname = "beets-recommends"
pkgver = "2.7.1"
pkgrel = 0
depends = [
        "flac",
        "chromaprint",
        "python-audioop",
        "python-beautifulsoup",
        "python-flask",
        "python-httpx",
        "python-mpd2",
        "python-requests-ratelimiter",
        "python-six",
        "python-standard-aifc",
        "python-standard-chunk",
        "python-standard-sunau",
        "python-langdetect",
        "python-pyacoustid",
        "python-pylast",
        "python-soupsieve",
        ]
install_if = ["beets=2.7.1-r0"]
pkgdesc = "Extra plugin dependencies for beets"
license = "custom:meta"
url = "https://beets.io"
options = ["empty"]

def install(self):
    return
