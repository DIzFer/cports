pkgname = "fcron"
pkgver = "3.4.0"
pkgrel = 0
build_style = "configure"
configure_args = [
        "--with-sendmail=no", # until, uh, nullmailer i guess?
        "--with-username=_fcron",
        "--with-groupname=_fcron",
        "--with-answer-all=no",
        "--with-boot-install=no",
        "--sbindir=/usr/libexec",
        "--bindir=/usr/bin",
        "--sysconfdir=/etc/fcron",
        "--datarootdir=/usr/share",
        "--localstatedir=/var",
        "--with-piddir=/run",
        "--with-fifodir=/run",
        "--with-editor=/usr/bin/vis"
        ]
hostmakedepends = ["autoconf", "automake"]
provides = ["cronie"] # should cronie and this provide cron instead
triggers = ["/usr/share/fcron/systab.orig"]
pkgdesc = "Feature-rich cron implementation"
license = "GPL-2.0-only"
url = "http://fcron.free.fr"
source = f"http://fcron.free.fr/archives/{pkgname}-{pkgver}.src.tar.gz"
sha256 = "f4e7fc553cdd70ff4b3b6ac9138b3b7cffab9198b8c266d97af0a87506e0e1b5"
file_modes = {
        # "ERROR Could not change euid to _fcron[0]: Operation not permitted"
        # TODO: not sure why
        "usr/bin/fcrontab": ("_fcron", "_fcron", 0o6755),
        "usr/bin/fcrondyn": ("_fcron", "_fcron", 0o6755),
        }
hardening = ["vis", "cfi"]
# no checks
options = ["!check"]

def post_install(self):
    self.install_file(self.files_path / "fcron-systab-wrapper", "usr/libexec", 0o755)

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "fcron")

    self.install_file("files/*.pam", "usr/lib/pam.d", glob = True)
    self.mv(self.destdir / "etc/fcron", self.destdir / "usr/share")
    self.install_file(self.files_path / "systab.orig", "usr/share/fcron")
