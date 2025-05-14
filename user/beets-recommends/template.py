pkgname = "beets"
pkgver = "2.2.0"
pkgrel = 1
build_style = "python_pep517"
pkgdesc = "Extra plugin dependencies for beets"
license = "custom:meta"
url = "https://beets.io"
depends = [
        "chromaprint",
        "python-flask",
        "python-pyacoustid",
        "python-pylast",
        "python-httpx",
        "python-mpd2",
        "python-standard-aifc",
        "python-standard-chunk",
        "python-audioop",
        "python-standard-sunau"
        ]
install_if = [self.parent]
options = ["empty"]
