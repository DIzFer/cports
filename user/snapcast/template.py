pkgname = "snapcast"
pkgver = "0.31.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
        "cmake",
        "pkgconf",
        "ninja",
        ]
makedepends = [
        "alsa-lib-devel",
        "openssl3-devel",
        "boost-devel",
        "avahi-devel",
        "flac-devel",
        "libogg-devel",
        "libvorbis-devel",
        "opus-devel",
        "libpulse-devel",
        "soxr-devel"
        ]
pkgdesc = "Synchronous multiroom audio player"
license = "GPL-3.0-only"
url = "https://github.com/badaix/snapcast"
source = f"https://github.com/badaix/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "d38d576f85bfa936412413b6860875ba3b462a8e67405f3984a0485778f2fdac"
hardening = [
        "vis",
        "cfi"
        ]
options = ["empty"]

def post_install(self):
    self.install_service(self.files_path / "snapcast-server")
    #self.install_service(self.files_path / "snapcast-client@.user")
    # letting this in makes cbuild fail to create package ("info field 'provides' has invalid value: dependency format is invalid"). Not sure where in cbuild the issue is

@subpackage("snapcast-server")
def _(self):
    return [
            "usr/bin/snapserver",
            "etc/snapserver.conf",
            "usr/share/pixmaps/snapcast.svg",
            "usr/share/snapserver/index.html",
            "usr/share/snapserver/plug-ins/meta_librespot-java.py",
            "usr/share/snapserver/plug-ins/meta_mopidy.py",
            "usr/share/snapserver/plug-ins/meta_mpd.py",
            "usr/share/snapserver/snapweb/index.html",
            "usr/lib/dinit.d/snapcast-server"
            ]
@subpackage("snapcast-client")
def _(self):
    return [
            "usr/bin/snapclient",
            #"usr/lib/dinit.d/user/snapcast-client@"
            ]
