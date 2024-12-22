#!/bin/bash
set -e
tdesrc=$PWD
tdearch=$(uname -m)
rm -rf $tdesrc/out/${tdearch}

. $tdesrc/environment

compile_directory() {  
  cd $tdesrc/$1
  dir=$PWD
  for pkg in $2; do
    if [[ $pkg != .* ]]; then
      cd "$dir"/tde-"$pkg"
      makepkg -Lsci
    fi
  done
}

### Build Packages
compile_directory tde-core "cmake-trinity tqt3 tqtinterface arts dbus-tqt dbus-1-tqt tqca tqca-tls tqscintilla libart-lgpl avahi-tqt tdelibs tdebase"
compile_directory tde-libs "libcaldav libcarddav libkdcraw libkexiv2 libkipi"
compile_directory tde-base "i18n tdeartwork tdebindings tdegraphics tdeutils tdeadmin"
compile_directory tde-extra "akode tdepim tdemultimedia tdenetwork tdeedu tdegames tdetoys tdeaccessibility tdeaddons gtk-qt-engine gtk3-tqt-engine systemsettings abakus amarok basket dolphin ebook-reader filelight kbiff kchmviewer kcpuload kile kmplayer kmyfirewall kmymoney konversation kooldock krename krusader kshutdown ksplash-engine-moodin kvkbd style-baghira style-domino style-lipstik style-qtcurve tdeio-appinfo tdeio-ftps tdeio-locate tdenetworkmanager tdepowersave tdesudo tdmtheme tork twin-style-crystal twin-style-dekorator twin-style-machbunt twin-style-mallory xdg-desktop-portal-tde yakuake"
compile_directory tde-devel "tdesdk tdevelop tdewebdev kdbg kdiff3 kscope kxmleditor piklab universal-indent-gui-tqt"

### Copy completed packages to out/${tdearch} folder and download dependencies to out/${tdearch} folder
cd $tdesrc
mkdir -p $tdesrc/out/${tdearch}
cp $(find $tdesrc -name *.pkg.tar.zst) $tdesrc/out/${tdearch}
wget https://mirror.ppa.trinitydesktop.org/trinity/archlinux/${tdearch}/gnokii-0.6.31-19.1-${tdearch}.pkg.tar.zst -O $tdesrc/out/${tdearch}/gnokii-0.6.31-19.1-${tdearch}.pkg.tar.zst
wget https://mirror.ppa.trinitydesktop.org/trinity/archlinux/${tdearch}/htdig-3.2.0b6-11.1-${tdearch}.pkg.tar.zst -O $tdesrc/out/${tdearch}/htdig-3.2.0b6-11.1-${tdearch}.pkg.tar.zst
wget https://mirror.ppa.trinitydesktop.org/trinity/archlinux/${tdearch}/lcms-1.19-7.1-${tdearch}.pkg.tar.zst -O $tdesrc/out/${tdearch}/lcms-1.19-7.1-${tdearch}.pkg.tar.zst
wget https://mirror.ppa.trinitydesktop.org/trinity/archlinux/${tdearch}/pod2man-5.30.2-1-${tdearch}.pkg.tar.zst -O $tdesrc/out/${tdearch}/pod2man-5.30.2-1-${tdearch}.pkg.tar.zst

### Create trinity pacman repo
repo-add $tdesrc/out/${tdearch}/trinity.db.tar.gz $tdesrc/out/${tdearch}/*.pkg.tar.{xz,zst}
