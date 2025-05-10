pkgname = "python-validators"
pkgver = "0.35.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-setuptools", "python-installer"]
depends = ["python"]
pkgdesc = "Python3 Data Validation for Humans"
license = "MIT"
url = "https://github.com/python-validators/validators"
source = f"$(PYPI_SITE)/v/validators/validators-{pkgver}.tar.gz"
sha256 = "992d6c48a4e77c81f1b4daba10d16c3a9bb0dbb79b3a19ea847ff0928e70497a"
# no test, missing python-eth-hash
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
