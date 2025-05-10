pkgname = "blueblack"
pkgver = "1.0.6"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-poetry-core", "python-astral"]
checkdepends = ["python-pytest", "python-pyyaml", "python-pyxdg"]
depends = ["python"]
pkgdesc = "Automatically change to light and dark mode depending on your location"
license = "custom:none"
url = "https://github.com/smitropoulos/blueblack"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1ed0c7752d21b5f5429e90eec88edd47dd8dd9d2eab373d522482a3f31179049"
# missing deps
options = ["!check"]

def post_install(self):
    self.install_service("^/blueblack.user")
