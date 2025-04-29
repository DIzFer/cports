pkgname = "swaylock-effects"
pkgver = "1.7.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "wayland-devel",
    "wayland-protocols",
    "libomp-devel"
]
pkgdesc = "Screen locker for Wayland"
license = "MIT"
url = "https://github.com/jirutka/swaylock-effects"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e94d79e189602694bedfbafb553ce3c6c976426e16f76d93bf7e226dc2876eb6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
