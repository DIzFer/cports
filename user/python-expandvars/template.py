pkgname = "python-expandvars"
pkgver = "1.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-hatchling"]
checkdepends = ["python-pytest", "python-installer"]
depends = ["python"]
pkgdesc = "Expand system variables Unix style"
license = "MIT"
url = "https://pypi.org/project/expandvars"
source = f"$(PYPI_SITE)/e/expandvars/expandvars-{pkgver}.tar.gz"
sha256 = "f04070b8260264185f81142cd85e5df9ceef7229e836c5844302c4ccfa00c30d"

def post_install(self):
    self.install_license("LICENSE")
