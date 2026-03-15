pkgname = "python-uv-dynamic-versioning"
pkgver = "0.13.0"
pkgrel = 0
build_style = "python_pep517"
makedepends = ["python-build", "python-hatchling", "python-installer", "python-devel"]
checkdepends = ["git", "python-pytest", "python-gitpython", "python-dunamai"]
depends = ["python"]
pkgdesc = "Dynamic versioning for uv/hatch similar to poetry-dynamic-versioning"
license = "MIT"
url = "https://pypi.org/project/uv-dynamic-versioning"
source = f"$(PYPI_SITE)/u/uv-dynamic-versioning/uv_dynamic_versioning-{pkgver}.tar.gz"
sha256 = "3220cbf10987d862d78e9931957782a274fa438d33efb1fa26b8155353749e06"

def post_install(self):
    self.install_license("LICENSE")
