pkgname = "darkman"
pkgver = "2.0.1"
pkgrel = 1
build_style = "go"
#make_build_args = ["./cmd/mpd-mpris"]
hostmakedepends = [
        "go",
        "scdoc"
        ]
#makedepends = [
#]
#checkdepends = [
#]
pkgdesc = "Daemon for dark-mode and light-mode transitions on Unix-like desktop"
license = "ISC"
url = "https://darkman.whynothugo.nl"
source = f"https://gitlab.com/WhyNotHugo/{pkgname}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "4d87ee5dcefcd237be43d2b3d27bea658d23ebe14b5b5951bc67942f1ec839e5"
# fail
options = ["!check"]

def post_prepare(self):
    self.do("make", allow_network=True)

def build(self):
    return

def install(self):
    self.install_bin("darkman")
    self.install_man("darkman.1")
    self.install_completion("_darkman.zsh", "zsh")
    self.install_completion("darkman.bash", "bash")
    self.install_completion("darkman.fish", "fish")
    self.install_file("contrib/dbus/nl.whynothugo.darkman.service", "usr/share/dbus-1/services")
    self.install_file("contrib/dbus/org.freedesktop.impl.portal.desktop.darkman.service", "usr/share/share/dbus-1/services/org.freedesktop.impl.portal.desktop.darkman.service")
    self.install_file("contrib/portal/darkman.portal", "usr/share/xdg-desktop-portal/portals/darkman.portal")
    self.install_file("darkman.desktop", "usr/share/applications")
    self.install_service("^/darkman.user")
    self.install_license("LICENCE")
    #self.install_service("^/mpd-mpris.user")
