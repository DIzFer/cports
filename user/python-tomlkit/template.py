pkgname = "python-tomlkit"
pkgver = "0.14.0"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-poetry-core", "python-installer", "python-devel"]
checkdepends = ["python-pytest", "python-pyyaml"]
depends = ["python"]
pkgdesc = "Python TOML library"
license = "MIT"
url = "https://pypi.org/project/tomlkit"
source = f"$(PYPI_SITE)/t/tomlkit/tomlkit-{pkgver}.tar.gz"
sha256 = "cf00efca415dbd57575befb1f6634c4f42d2d87dbba376128adb42c121b87064"

def post_install(self):
    self.install_license("LICENSE")
