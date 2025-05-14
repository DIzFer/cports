pkgname = "python-standard-chunk"
pkgver = "3.13.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
#checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Standard library chunk redistribution"
license = "PSF-2.0"
url = "https://github.com/youknowone/python-deadlib"
source = f"$(PYPI_SITE)/s/standard-chunk/standard_chunk-{pkgver}.tar.gz"
sha256 = "4ac345d37d7e686d2755e01836b8d98eda0d1a3ee90375e597ae43aaf064d654"
# fails?
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
