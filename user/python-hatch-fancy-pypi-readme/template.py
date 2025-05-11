pkgname = "python-hatch-fancy-pypi-readme"
pkgver = "25.1.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatchling"]
depends = ["python"]
pkgdesc = "Fancy PyPI READMEs with Hatch"
license = "MIT"
url = "https://pypi.org/project/hatch-fancy-pypi-readme"
source = f"$(PYPI_SITE)/h/hatch-fancy-pypi-readme/hatch_fancy_pypi_readme-{pkgver}.tar.gz"
sha256 = "9c58ed3dff90d51f43414ce37009ad1d5b0f08ffc9fc216998a06380f01c0045"
# tests fail
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
