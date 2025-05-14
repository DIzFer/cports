pkgname = "python-standard-sunau"
pkgver = "3.13.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
#checkdepends = ["python-pytest", "python-installer", "python-trio", "python-trustme"]
depends = ["python"]
pkgdesc = "Standard library sunau redistribution"
license = "PSF-2.0"
url = "https://pypi.org/project/standard-sunau"
source = f"$(PYPI_SITE)/s/standard-sunau/standard_sunau-{pkgver}.tar.gz"
sha256 = "b319a1ac95a09a2378a8442f403c66f4fd4b36616d6df6ae82b8e536ee790908"
# missing deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
