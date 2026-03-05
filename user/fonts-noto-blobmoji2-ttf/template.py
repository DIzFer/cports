pkgname = "fonts-noto-blobmoji2-ttf"
pkgver = "17.1"
pkgrel = 0
provides = ["fonts-noto-emoji-ttf"]
pkgdesc = "Fork of googlefonts/noto-emoji updated to use C1710/blobmoji"
license = "OFL-1.1"
url = "https://github.com/DavidBerdik/blobmoji2"
source = f"{url}/releases/download/blobmoji-17r1/NotoColorEmoji.ttf"
sha256 = "ffc75f156f65027d61ea976b7ef6327641403913c89812371a3d064fd15c67f2"
# No copyright header in license text
options = ["!distlicense"]

def extract(self):
    pass

def install(self):
    self.install_file(
        "^/66-noto-color-emoji.conf",
        "usr/share/fontconfig/conf.avail",
    )
    self.install_file(self.sources_path / "NotoColorEmoji.ttf", "usr/share/fonts/blobmoji2")
