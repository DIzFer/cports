pkgname = "python-pystray"
pkgver = "0.19.5"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-setuptools", "python-installer", "python-six", "python-pillow", "python-sphinx"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Allows to create a system tray icon"
license = "GPL-3.0-only"
url = "https://github.com/moses-palmer/pystray"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2ab6bd15c14b400c9e8271a82c9de8adc0f1a0cacfc14080bdd4fb42bb88ec92"
# no tests, missing python-pytest-cov
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")
