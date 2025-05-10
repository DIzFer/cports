pkgname = "discover-minimal"
pkgver = "0"
pkgrel = 0
build_style = "meta"
pkgdesc = "Trigger to remove non-flatpak backends from discover"
license = "custom:none"
url = "http://localhost"
self.triggers = ["/usr/lib/qt6/plugins/discover"]
