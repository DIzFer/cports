pkgname = "python-httpx"
pkgver = "0.28.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatchling", "python-hatch-fancy-pypi-readme"]
#checkdepends = ["python-pytest", "python-installer", "python-trio", "python-trustme"]
depends = ["python"]
pkgdesc = "Next generation HTTP client for Python"
license = "BSD-3-Clause"
url = "https://pypi.org/project/httpx"
source = f"$(PYPI_SITE)/h/httpx/httpx-{pkgver}.tar.gz"
sha256 = "75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc"
# missing deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.md")
