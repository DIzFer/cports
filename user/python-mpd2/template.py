pkgname = "python-mpd2"
pkgver = "3.1.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-setuptools", "python-installer"]
depends = ["python"]
pkgdesc = "Next generation HTTP client for Python"
license = "GPL-3.0-only OR LGPL-3.0-only"
url = "https://pypi.org/project/mpd2"
source = f"$(PYPI_SITE)/p/python-mpd2/python-mpd2-{pkgver}.tar.gz"
sha256 = "4baec3584cc43ed9948d5559079fafc2679b06b2ade273e909b3582654b2b3f5"
# broken?
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
