pkgname = "atool"
pkgver = "0.39.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake"]
pkgdesc = "Script for managing file archives of various types"
license = "GPL-2.0-or-later"
url = "https://savannah.nongnu.org/projects/atool"
source = (
    f"$(NONGNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "aaf60095884abb872e25f8e919a8a63d0dabaeca46faeba87d12812d6efc703b"
hardening = ["vis", "cfi"]
