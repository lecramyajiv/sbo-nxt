#!/bin/bash

# Gets the RPM package name from the component name.
# This is useful because some RPM packages do not have prefix "trinity"
# while others do.
#
# E.g :
#  trinity-qt3 => qt3
#  trinity-tdelibs => trinity-tdelibs


PKGCATEGORY="${1%%/*}"
PKGNAME="${1##*/}"
DEVEL="$2"

# Some RPM packages have different name than the source tarball.

# Some runtime packages are prefixed with 'trinity-', some are not.
case "${PKGNAME}" in
  # In case prefix is already there, don't add it again.
  "trinity-"*) PREFIX="";;
  # Most TDE dependencies have no prefix
  "avahi-tqt"|"dbus-tqt"|"dbus-1-tqt"|"libart-lgpl"|"libcaldav"|"libcarddav"|"polkit-tqt"|"pytqt"|"sip4-tqt"|"qt3"|"tqscintilla"|"tqt3"|"tqtinterface"|"tqca"|"tqca-tls") PREFIX="";;
  # 3rd party dependencies
  "cscope"|"dirmngr"|"esound"|"exempi"|"exiv2"|"file"|"fileshareset"|"gmime"|"hk_classes"|"intltool"|"lcms"|"libbeagle"|"mp4v2"|"pinentry-tqt"|"python-qt3"|"rdesktop"|"recode"|"rdiff-backup"|"sword"|"tar") PREFIX="";;
  # Extra build stuff
  "autoconf"|"automake"|"brp-check-trinity"|"gnuchess"|"htdig"|"imlib1"|"libconfig"|"libotr3"|"libr"|"libtool2"|"lilypond"|"m4"|"mftrace"|"pan"|"pcsc-perl"|"torsocks"|"wv2"|"yaz") PREFIX="";;  # Other
  "curl") PREFIX="trinity-lib";;
  # Default case: add prefix
  *) PREFIX="trinity-";;
esac

# Runtime packages
if [ -r /etc/mandriva-release ]; then
  lib=$(rpm -E %_lib)
else
  lib="lib"
fi

case "${PKGNAME}" in
  # Some packages have different runtime name than source package.
  "avahi-tqt")        PKGRUNTIME="${lib}avahi-tqt1";;
  "dbus-tqt")         PKGRUNTIME="${lib}dbus-tqt-1-0";;
  "dbus-1-tqt")       PKGRUNTIME="${lib}dbus-1-tqt0";;
  "digikam")          PKGRUNTIME="digikam-i18n";;
  "esound")           PKGRUNTIME="${lib}esd0";;
  "exiv2")            PKGRUNTIME="${lib}exiv2_26";;
  "imlib1")           PKGRUNTIME="${lib}Imlib1";;
  "knetworkmanager8") PKGRUNTIME="knetworkmanager";;
  "koffice")          PKGRUNTIME="koffice-suite";;
  "lcms")             PKGRUNTIME="${lib}lcms1";;
  "libart-lgpl")      PKGRUNTIME="${lib}art_lgpl_2-2";;
  "libbeagle")        PKGRUNTIME="${lib}beagle1";;
  "libcaldav")        PKGRUNTIME="${lib}caldav0";;
  "libcarddav")       PKGRUNTIME="${lib}carddav0";;
  "libkdcraw")        PKGRUNTIME="${lib}kdcraw4";;
  "libkexiv2")        PKGRUNTIME="${lib}kexiv2-5";;
  "libkipi")          PKGRUNTIME="${lib}kipi0";;
  "libr")             PKGRUNTIME="${lib}r";;
  "mp4v2")            PKGRUNTIME="mp4v2";;
  "polkit-tqt")       PKGRUNTIME="${lib}polkit-tqt0";;
  "tqscintilla")      PKGRUNTIME="${lib}tqscintilla7";;
  "tqca")             PKGRUNTIME="${lib}tqca1";;
  "tqca-tls")         PKGRUNTIME="${lib}tqt3-mt-tqca-tls";;
  "tqt3")             PKGRUNTIME="${lib}tqt3-mt";;
  "tqtinterface")     PKGRUNTIME="${lib}tqt4";;
  "trinity-desktop")  PKGRUNTIME="${PKGNAME}-all";;
  "yaz")              PKGRUNTIME="${lib}yaz";;
  # Language package: install only French language package
  "k3b-i18n"|"koffice-i18n"|"tde-i18n")
                      PKGRUNTIME="${PKGNAME}-French";;
  # Default case: runtime package has same name as source package
  *)                  PKGRUNTIME="${PKGNAME}";;
esac

# Finally, display the runtime package name.
echo "${PREFIX}${PKGRUNTIME}"

# Development package.
if [ -n "${DEVEL}" ]; then
  # Check if development package is required.
  case "${PKGCATEGORY}" in
    # Applications do NOT have 'devel' package, except K3B, Koffice.
    "applications") if [ "${PKGNAME}" != "k3b" ] && [ "${PKGNAME}" != "koffice" ]; then exit 0; fi;;
    # Extras packages do NOT have 'devel' package, except Akode
    "extras") if [ "${PKGNAME}" != "akode" ] && [ "${PKGNAME}" != "hk_classes" ]; then exit 0; fi;;
  esac

  # Some other packags NOT having development package
  case "${PKGNAME}" in
    "autoconf"|"automake"|"brp-check-trinity"|"cscope"|"gnuchess"|"hal-info"|"lilypond"|"m4"|"mftrace"|"pcsc-perl"|"rdesktop"|"recode"|"rdiff-backup"|"tde-cmake"|"torsocks") exit 0;;
    "tqca-tls"|"tdeadmin"|"tdetoys"|"tde-i18n"*|"tdeaddons"|"tdeartwork"|"libtqt-perl"|"kipi-plugins") exit 0;;
  esac

  # Some package have specific development package.
  case "${PKGNAME}" in
    "avahi-tqt")   PKGDEVEL="libavahi-tqt-devel";;
    "dbus-tqt")    PKGDEVEL="libdbus-tqt-1-devel";;
    "dbus-1-tqt")  PKGDEVEL="libdbus-1-tqt-devel";;
    "esound")      PKGDEVEL="libesd0-devel";;
    "exiv2")       PKGDEVEL="${lib}exiv2-devel-0.26";;
    "imlib1")      PKGDEVEL="${lib}Imlib-devel";;
    "koffice")     PKGDEVEL="koffice-devel";;
    "lcms")        PKGDEVEL="${lib}lcms-devel";;
    "libart-lgpl") PKGDEVEL="libart_lgpl-devel";;
    "libbeagle")   PKGDEVEL="${lib}beagle-devel";;
    "libcaldav")   PKGDEVEL="${lib}caldav-devel";;
    "libcarddav")  PKGDEVEL="${lib}carddav-devel";;
    "libkdcraw")   PKGDEVEL="${lib}kdcraw-devel";;
    "libkexiv2")   PKGDEVEL="${lib}kexiv2-devel";;
    "libkipi")     PKGDEVEL="${lib}kipi-devel";;
    "libr")        PKGDEVEL="${lib}r-devel";;
    "mp4v2")       PKGDEVEL="${lib}mp4v2-devel";;
    "pan")         PKGDEVEL="uulib-devel";;
    "polkit-tqt")  PKGDEVEL="${lib}polkit-tqt-devel";;
    "tqca")        PKGDEVEL="${lib}tqca-devel";;
    "tqscintilla") PKGDEVEL="${lib}tqscintilla-devel";;
    "tqt3")        PKGDEVEL="tqt3-dev-tools tqt3-apps-devel tqt3-compat-headers ${lib}tqt3-mt-sqlite3";;
    "yaz")         PKGDEVEL="${lib}yaz-devel";;
    # Default case: development package has same name as runtime package, plus '-devel' suffix.
    *)             PKGDEVEL="${PKGRUNTIME}-devel";;
  esac

  # Finally, other packages do have a '-devel'
  echo "${PREFIX}${PKGDEVEL}"
fi
