pkgname = "python-pylast"
pkgver = "5.5.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatchling", "python-hatch_vcs"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python interface to Last.fm and Libre.fm"
license = "Apache-2.0"
url = "https://github.com/pylast/pylast"
source = f"$(PYPI_SITE)/p/pylast/pylast-{pkgver}.tar.gz"
sha256 = "b6e95cf11fb99779cd451afd5dd68c4036c44f88733cf2346ba27317c1869da4"
# no tests, missing python-pytest-cov
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
