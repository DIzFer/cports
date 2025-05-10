pkgname = "python-truststore"
pkgver = "0.10.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
checkdepends = [
        "python-pytest",
        "python-requests",
        "python-pytest-asyncio",
        "python-aiohttp",
        "python-multidict",
        "python-attrs",
        "python-yarl",
        "python-propcache"
        ]
depends = ["python"]
pkgdesc = "Verify certificates using OS trust stores"
license = "MIT"
url = "https://github.com/sethmlarson/truststore"
source = f"$(PYPI_SITE)/t/truststore/truststore-{pkgver}.tar.gz"
sha256 = "eda021616b59021812e800fa0a071e51b266721bef3ce092db8a699e21c63539"
# no tests
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
