pkgname = "shellcheck-bin"
pkgver = "0.10.0"
pkgrel = 0
pkgdesc = "Static analysis tool for shell scripts"
license = "GPL-3.0-only"
url = "https://www.shellcheck.net"
source = f"https://github.com/koalaman/shellcheck/releases/download/v{pkgver}/shellcheck-v{pkgver}.linux.{self.profile().arch}.tar.xz"
sha256 = "6c881ab0698e4e6ea235245f22832860544f17ba386442fe7e9d629f8cbedf87"

def install(self):
    self.install_bin('shellcheck')
