pkgname = "mosquitto"
pkgver = "2.0.21"
pkgrel = 0
build_style = "makefile"
make_build_args = [
        "prefix=/usr",
        "WITH_CLIENTS=yes",
        "WITH_BROKER=no",
        "WITH_APPS=no",
        "WITH_PLUGINS=no",
        "DOCUMENTATION=yes"
        ]
hostmakedepends = ["pkgconf"]
makedepends = ["openssl3-devel", "cjson-devel", "cunit-devel", "gsed"]
pkgdesc = "Open source MQTT broker"
license = "EPL-1.0 OR EPL-2.0"
url = "https://mosquitto.org"
source = f"https://mosquitto.org/files/source/mosquitto-{pkgver}.tar.gz"
sha256 = "7ad5e84caeb8d2bb6ed0c04614b2a7042def961af82d87f688ba33db857b899d"
# TODO: no checks on partial buld
options = ["!check"]
exec_wrappers = [("/usr/bin/gsed","sed")]

def post_install(self):
    self.mv(f"{self.destdir}/usr/local/*", f"{self.destdir}/usr/", glob = True)
    self.mv(f"{self.destdir}/usr/sbin/*", f"{self.destdir}/usr/bin", glob = True)

@subpackage("mosquitto-devel")
def _(self):
    return ["usr/include"]

@subpackage("mosquitto-clients")
def _(self):
    self.subdesc = "client binaries"
    return ["usr/bin/mosquitto_pub", "usr/bin/mosquitto_sub", "usr/bin/mosquitto_rr"]

@subpackage("mosquitto-libs")
def _(self):
    return ["usr/lib"]
