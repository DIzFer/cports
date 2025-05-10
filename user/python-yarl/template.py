pkgname = "python-yarl"
pkgver = "1.20.0"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-setuptools", "python-installer", "python-cython", "python-expandvars", "python-devel"]
depends = ["python"]
pkgdesc = "Yet Another URL Library"
license = "Apache-2.0"
url = "https://github.com/aio-libs/yarl"
source = f"$(PYPI_SITE)/y/yarl/yarl-{pkgver}.tar.gz"
sha256 = "686d51e51ee5dfe62dec86e4866ee0e9ed66df700d55c828a615640adc885307"
# no tests, missing python-pytest-cov
options = ["!check"]
