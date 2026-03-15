pkgname = "python-dunamai"
pkgver = "1.26.0"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-poetry-core", "python-installer", "python-devel"]
checkdepends = ["git", "python-pytest", "python-gitpython"]
depends = ["python"]
pkgdesc = "Library and command line tool for producing version strings"
license = "MIT"
url = "https://pypi.org/project/dunamai"
source = f"$(PYPI_SITE)/d/dunamai/dunamai-{pkgver}.tar.gz"
sha256 = "5396ac43aa20ed059040034e9f9798c7464cf4334c6fc3da3732e29273a2f97d"
# tests depend on properly configured git
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
