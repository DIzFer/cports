pkgname = "python-propcache"
pkgver = "0.3.1"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-setuptools", "python-installer", "python-cython", "python-expandvars", "python-devel"]
depends = ["python"]
pkgdesc = "Fast property caching"
license = "Apache-2.0"
url = "https://github.com/aio-libs/propcache"
source = f"$(PYPI_SITE)/p/propcache/propcache-{pkgver}.tar.gz"
sha256 = "40d980c33765359098837527e18eddefc9a24cea5b45e078a7f3bb5b032c6ecf"
# no tests, missing python-pytest-cov
options = ["!check"]
