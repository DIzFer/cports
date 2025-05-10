pkgname = "sanoid"
pkgver = "2.2.0"
pkgrel = 0
depends = [
        "perl",
        "perl-config-inifiles",
        "perl-capture-tiny",
        "zfs",
        "procps"
        ]
pkgdesc = "Policy-driven snapshot management and replication tools for ZFS"
license = "GPL-3.0-only"
url = "https://github.com/jimsalterjrs/sanoid"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a997552e3c5f9fc8407fd20fa1adc99fc37a1f61547f738114c96a1ea1658fe2"

def install(self):
    self.install_bin("sanoid")
    self.install_file("sanoid.defaults.conf", "etc/sanoid")
    self.install_file("sanoid.conf", "usr/share/example/sanoid")
    self.install_bin("syncoid")
    self.install_bin("findoid")

@subpackage("syncoid")
def _(self):
    self.depends = ["perl", "perl-capture-tiny", "zfs"]
    self.subdesc = "replication tool"
    return ["cmd:syncoid"];

@subpackage("findoid")
def _(self):
    self.depends = ["perl", "zfs"]
    self.subdesc = "snapshot file version helper"
    return ["cmd:findoid"];

@subpackage("syncoid-recommends")
def _(self):
    self.depends = [
            "openssh",
            "pv",
            "cmd:gzip!chimerautils",
            #"lzop", # Not packaged
            "mbuffer"
            ]
    self.subdesc = "recommended dependencies for syncoid"
    self.install_if = ["syncoid"]
    self.options = ["empty"]
    return []
