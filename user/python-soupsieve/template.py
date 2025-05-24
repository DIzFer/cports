pkgname = "python-soupsieve"
pkgver = "2.7"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-hatchling"]
checkdepends = ["python-pytest", "python-installer", "python-beautifulsoup"]
depends = ["python", "python-beautifulsoup"]
pkgdesc = "Modern CSS selector implementation for Beautiful Soup"
license = "MIT"
url = "https://pypi.org/project/soupsieve"
source = f"$(PYPI_SITE)/s/soupsieve/soupsieve-{pkgver}.tar.gz"
sha256 = "ad282f9b6926286d2ead4750552c8a6142bc4c783fd66b0293547c8fe6ae126a"

def post_install(self):
    self.install_license("LICENSE.md")
