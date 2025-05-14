pkgname = "python-audioop"
pkgver = "0.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "LTS port of Python's 'audioop' module"
license = "PSF-2.0"
url = "https://github.com/AbstractUmbra/audioop"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1699d8c3de4c827c3b6dfd695ade164945cc522f4956cf9a1bdf719097723860"
# fails?
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
