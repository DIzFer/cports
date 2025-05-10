pkgname = "open-in-mpv"
pkgver = "2.4.3"
pkgrel = 1
#make_build_args = ["./cmd/mpd-mpris"]
hostmakedepends = [
        "git",
        "go",
        "gtar"
        ]
#makedepends = [
#]
#checkdepends = [
#]
pkgdesc = "Simple web extension to open videos in mpv"
license = "GPL-3.0-only"
url = "https://github.com/Baldomo/open-in-mpv"
source = f"{url}/releases/download/v{pkgver}/linux.tar"
sha256 = "021bd533e0fdb26e25d7f7c0943c4b6db2cc95e62623c8f53ba591b24d33616b"

def install(self):
    self.install_bin("open-in-mpv")
    self.install_bin("install-protocol.sh", name="open-in-mpv-install")
    self.install_file("open-in-mpv.desktop", "usr/share/applications")
