pkgname = "python-standard-aifc"
pkgver = "3.13.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
#checkdepends = ["python-pytest", "python-installer", "python-trio", "python-trustme"]
depends = ["python"]
pkgdesc = "Next generation HTTP client for Python"
license = "PSF-2.0"
url = "https://pypi.org/project/httpx"
source = f"$(PYPI_SITE)/s/standard-aifc/standard_aifc-{pkgver}.tar.gz"
sha256 = "64e249c7cb4b3daf2fdba4e95721f811bde8bdfc43ad9f936589b7bb2fae2e43"
# missing deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
