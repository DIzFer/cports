pkgname = "python-multidict"
pkgver = "6.4.3"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-setuptools", "python-installer", "python-devel"]
checkdepends = ["python-pytest", "python-installer"]
depends = ["python"]
pkgdesc = "Multidict implementation"
license = "Apache-2.0"
url = "https://github.com/aio-libs/multidict"
source = f"$(PYPI_SITE)/m/multidict/multidict-{pkgver}.tar.gz"
sha256 = "3ada0b058c9f213c5f95ba301f922d402ac234f1111a7d8fd70f1b99f3c281ec"
# no tests, missing python-pytest-cov
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
