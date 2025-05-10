pkgname = "piper"
pkgver = "0.8"
pkgrel = 0
build_style = "meson"
#configure_args = [
#    "-Dsystemd=false",
#    "-Dlogind-provider=elogind"
#    ]
hostmakedepends = [
        "meson",
        "pkgconf"
        ]
makedepends = [
        "libratbag",
        "gettext",
        "python-gobject-devel",
        "python-lxml",
        "python-evdev",
        "python-cairo",
        "python-gobject",
        "gtk+3-update-icon-cache",
        "desktop-file-utils"
        ]
checkdepends = [
        "bash"
        ]
pkgdesc = "GTK+ application to configure gaming mice using ratbag"
license = "GPL-2.0-only"
url = "https://github.com/libratbag/piper"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "78becb1861f102057f7cac26c90bde2f4ef5027680c0d2758a7c2700b51dd73d"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")
