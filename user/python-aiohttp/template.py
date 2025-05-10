pkgname = "python-aiohttp"
pkgver = "3.11.15"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-setuptools", "python-installer", "python-devel"]
depends = ["python"]
pkgdesc = "HTTP client/server for asyncio"
license = "Apache-2.0"
url = "https://pypi.org/project/aiohttp"
source = f"$(PYPI_SITE)/a/aiohttp/aiohttp-{pkgver}.tar.gz"
sha256 = "b9b9a1e592ac8fcc4584baea240e41f77415e0de98932fdf19565aa3b6a02d0b"
# no tests, missing python-pytest-cov
options = ["!check"]
