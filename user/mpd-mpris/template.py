pkgname = "mpd-mpris"
pkgver = "0.4.1"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/mpd-mpris"]
hostmakedepends = [
        "go"
        ]
#makedepends = [
#]
#checkdepends = [
#]
pkgdesc = "Implementation of the MPRIS protocol for MPD"
license = "MIT"
url = "https://github.com/natsukagami/mpd-mpris"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "85d33ab66e8bda50270cc5d3e3701a333542e931a17f7d3116a902b8f82818d0"
# checks fail
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_service("^/mpd-mpris.user")
