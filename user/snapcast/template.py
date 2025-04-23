pkgname = "snapcast"
pkgver = "0.35.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_PIPEWIRE=ON", "-DBUILD_TESTS=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "avahi-devel",
    "boost-devel",
    "dinit-chimera",
    "flac-devel",
    "libexpat-devel",
    "libogg-devel",
    "libvorbis-devel",
    "openssl3-devel",
    "opus-devel",
    "pipewire-devel",
    "pipewire-dinit",
    "soxr-devel",
]
pkgdesc = "Synchronous multiroom audio player"
license = "GPL-3.0-only"
url = "https://github.com/badaix/snapcast"
source = f"https://github.com/badaix/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "cb75a71479bf52910bf5f47ae8120ec41c89459b0d77d7cd560e674e437ef050"
hardening = ["vis"]
# flaky tests
options = ["empty", "!check"]


def post_install(self):
    self.install_service(self.files_path / "snapcast-server")
    # letting this in makes cbuild fail to create package ("info field 'provides' has invalid value: dependency format is invalid"). Not sure where in cbuild the issue is
    self.install_service(self.files_path / "snapcast-client.user")


@subpackage("snapcast-server")
def _(self):
    return [
        "usr/bin/snapserver",
        "etc/snapserver.conf",
        "usr/share/snapserver/index.html",
        "usr/share/snapserver/plug-ins/meta_go-librespot.py",
        "usr/share/snapserver/plug-ins/meta_librespot-java.py",
        "usr/share/snapserver/plug-ins/meta_mopidy.py",
        "usr/share/snapserver/plug-ins/meta_mpd.py",
        "usr/share/snapserver/snapweb/index.html",
        "usr/lib/dinit.d/snapcast-server",
    ]


@subpackage("snapcast-client")
def _(self):
    return [
        "usr/bin/snapclient",
        "usr/share/icons/hicolor/snapcast.svg",
        "usr/lib/dinit.d/user/snapcast-client",
    ]
