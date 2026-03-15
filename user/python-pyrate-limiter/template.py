pkgname = "python-pyrate-limiter"
pkgver = "4.0.2"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-hatchling", "python-installer", "python-devel", "python-uv-dynamic-versioning", "python-tomlkit", "python-dunamai", "python-jinja2"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Rate-Limiter using Leaky-Bucket Algorithm Family"
license = "MIT"
url = "https://pypi.org/project/pyrate-limiter"
source = f"$(PYPI_SITE)/p/pyrate-limiter/pyrate_limiter-{pkgver}.tar.gz"
sha256 = "b678841e2215f114ef6f98c7093755ca3b466de83cb5a881231fd6e321fa14b5"
# tests require redis????
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
