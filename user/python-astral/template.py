pkgname = "python-astral"
pkgver = "3.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-poetry-core"]
checkdepends = ["python-pytest", "python-freezegun"]
depends = ["python"]
pkgdesc = "Python calculations for the position of the sun and moon"
license = "Apache-2.0"
url = "https://github.com/sffjunkie/astral"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b7ab8ff08af69edac3d54e93b034f553f2bdb4b16ec2a60f82e8adbc46ae2ce4"

def post_install(self):
    self.install_license("LICENSE")
