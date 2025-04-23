pkgname = "kmix"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf"
]
makedepends = [
        "qt6-qtbase-devel",
        "kconfig-devel",
        "kconfigwidgets-devel",
        "kcrash-devel",
        "kcoreaddons-devel",
        "kdbusaddons-devel",
        "kdoctools-devel",
        "kglobalaccel-devel",
        "ki18n-devel",
        "knotifications-devel",
        "solid-devel",
        "kstatusnotifieritem-devel",
        "kwindowsystem-devel",
        "kxmlgui-devel",

]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE File Manager"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kmix"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/{pkgname}-{pkgver}.tar.xz"
sha256 = "dd729b774339e7c5a95028aa55b6293407a90eac1f56d6805cbcee5f4090b9ff"
hardening = ["vis", "cfi"]
