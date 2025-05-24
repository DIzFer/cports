pkgname = "python-beautifulsoup"
pkgver = "4.13.4"
pkgrel = 2
build_style = "python_pep517"
makedepends = ["python-build", "python-hatchling"]
checkdepends = ["python-pytest", "python-installer", "python-typing_extensions"]
depends = ["python", "python-typing_extensions"]
pkgdesc = "Screen-scraping library"
license = "MIT"
url = "https://pypi.org/project/beautifulsoup4"
source = f"$(PYPI_SITE)/b/beautifulsoup4/beautifulsoup4-{pkgver}.tar.gz"
sha256 = "dbb3c4e1ceae6aefebdaf2423247260cd062430a410e38c66f2baa50a8437195"

def post_install(self):
    self.install_license("LICENSE")
