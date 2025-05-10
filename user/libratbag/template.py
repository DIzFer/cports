pkgname = "libratbag"
pkgver = "0.18"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
    "-Dlogind-provider=elogind"
    ]
hostmakedepends = [
        "meson",
        "pkgconf"
        ]
makedepends = [
        "udev-devel",
        "libevdev-devel",
        "glib-devel",
        "json-glib-devel",
        "libunistring-devel",
        "elogind-devel",
        "check-devel",
        "python-devel",
        "python-gobject-devel",
        "swig"
        ]
checkdepends = ["python-evdev"]
pkgdesc = "DBus daemon to configure gaming mice"
license = "MIT"
url = "https://github.com/libratbag/libratbag"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8a7f8bf00c21ef5ad534e2804ed537f2fc6521a3932dd822c438e561a85a1bcd"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")
