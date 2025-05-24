pkgname = "beets-recommends"
pkgver = "2.2.0"
pkgrel = 5
depends = [
        "flac",
        "chromaprint",
        "python-flask",
        "python-pyacoustid",
        "python-pylast",
        "python-httpx",
        "python-mpd2",
        "python-standard-aifc",
        "python-standard-chunk",
        "python-audioop",
        "python-standard-sunau",
        "python-langdetect",
        "python-beautifulsoup",
        "python-soupsieve"
        ]
install_if = ["beets"]
pkgdesc = "Extra plugin dependencies for beets"
license = "custom:meta"
url = "https://beets.io"
options = ["empty"]

def install(self):
    return
