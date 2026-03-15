pkgname = "python-requests-ratelimiter"
pkgver = "0.9.2"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-hatchling", "python-installer", "python-requests"]
depends = ["python", "python-pyrate-limiter"]
pkgdesc = "Wrapper for pyrate-limiter to integrate with the requests library"
license = "MIT"
url = "https://pypi.org/project/requests-ratelimiter"
source = f"$(PYPI_SITE)/r/requests-ratelimiter/requests_ratelimiter-{pkgver}.tar.gz"
sha256 = "1d9ede92dd4bebd0d5d449ec4a779dda08d50e424e4a051349263bfc42afad97"
# cbf to look into what requests_mock is
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
