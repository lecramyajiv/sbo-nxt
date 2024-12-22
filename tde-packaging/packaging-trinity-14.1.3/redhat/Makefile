SHELL := /bin/bash
PATH := $(PATH):$(shell pwd)/build
TDE_VERSION := $(shell echo $${TDE_VERSION:-14.1.2})
TDE_GIT_DIR := $(shell cd ../..; pwd)
TDE_PACKAGING_DIR := $(shell [ -n "$${TDE_PACKAGING_DIR}" ] && cd "$${TDE_PACKAGING_DIR}" || cd ..; pwd)
RPMDIR := "$(shell rpm -E %{_rpmdir}.tde-$(TDE_VERSION))"
DIST := $(shell ./build/rpmdist.sh --dist)

buildpkg = \
  @echo "Now processing '$(1)' [from $(TDE_PACKAGING_DIR)]."; \
  export TDE_PACKAGING_DIR=$(TDE_PACKAGING_DIR); \
  if [ "${REBUILD}" = "$(1)" ] || ! is_latest_package_installed.sh "$(1)" ${TDE_VERSION}; then \
    echo "  Package '${1}' is not yet installed."; \
    if [ "${REBUILD}" = "$(1)" ] || ! is_latest_package_built.sh "$(1)" ${TDE_VERSION}; then \
      echo "  Building package."; \
      build_rpm_package.sh "$(1)" ${TDE_VERSION} || exit 1; \
      echo "  Updating repository."; \
      update_repository.sh ${TDE_VERSION}; \
    fi; \
    echo "Now installing package '$(1)'"; \
    install_rpm_package.sh "$(1)" || exit 2; \
  fi; \
  echo


all: dependencies core libraries applications i18n meta external
dependencies: tde-cmake tqt3 tqtinterface akode arts libart_lgpl libcaldav libcarddav polkit-tqt pytqt sip4-tqt tqca tqscintilla avahi-tqt dbus-tqt dbus-1-tqt
core: tdelibs tdebase tdeaccessibility tdeadmin tdegames tdemultimedia tdepim tdetoys tdevelop tdeaddons tdeartwork tdebindings tdeedu tdegraphics tdenetwork tdesdk tdeutils tdewebdev
libraries: kipi-plugins libkdcraw libkexiv2 libkipi libksquirrel libtdeldap libtqt-perl pytdeextensions pytde
applications: abakus amarok basket bibletime codeine digikam dolphin filelight gtk3-tqt-engine gtk-qt-engine gwenview k3b k9copy kaffeine kaffeine-mozilla kasablanca katapult kbarcode kbfx kbibtex kbiff kbookreader kchmviewer kcmautostart kcmldap kcmldapcontroller kcmldapmanager kcpuload kdbg kdbusnotification kdiff3 kdirstat keep kerberostray keximdb kftpgrabber kile kima kiosktool kkbswitch klamav klcddimmer kmplayer kmyfirewall kmymoney knemo knetload knetstats knights knmap knowit knutclient koffice kommando kompose konversation kooldock kopete-otr kpicosim kpilot kplayer krecipes krename krusader kscope ksensors kshowmail kshutdown ksplash-engine-moodin ksquirrel kstreamripper ksystemlog ktechlab ktorrent kvirc kvkbd kvpnc kxmleditor mathemagics mplayerthumbs piklab polkit-agent-tde potracegui qalculate-tde qt4-tqt-theme-engine rosegarden smartcardauth smb4k soundkonverter tdebluez tde-ebook-reader tde-guidance tdeio-appinfo tdeio-apt tdeio-ftps tdeio-gopher tastymenu tdedocker tdeio-locate tdeio-sword tdeio-umountwrapper tdenetworkmanager tdepacman tdepowersave tderadio tdesshaskpass tde-style-baghira tde-style-domino tde-style-ia-ora tde-style-lipstik tde-style-polyester tde-style-qtcurve tdesudo tdesvn tde-systemsettings tdmtheme tellico tork twin-style-crystal twin-style-dekorator twin-style-fahrenheit twin-style-machbunt twin-style-mallory twin-style-suse2 wlassistant yakuake
i18n: gwenview-i18n k3b-i18n koffice-i18n tde-i18n

### Trinity Dependencies

akode: tqtinterface trinity-filesystem
	$(call buildpkg,dependencies/akode)

arts: tqtinterface trinity-filesystem
	$(call buildpkg,dependencies/arts)

avahi-tqt: tqtinterface
	$(call buildpkg,dependencies/avahi-tqt)

dbus-1-tqt: tqtinterface
	$(call buildpkg,dependencies/dbus-1-tqt)

dbus-tqt: tqtinterface
	$(call buildpkg,dependencies/dbus-tqt)

libart_lgpl: tqtinterface
	$(call buildpkg,dependencies/libart-lgpl)

libcaldav: tqtinterface
	$(call buildpkg,dependencies/libcaldav)

libcarddav: tqtinterface
	$(call buildpkg,dependencies/libcarddav)

polkit-tqt: tqtinterface dbus-1-tqt
ifeq (,$(filter $(DIST), .el5 .el6 ))
	$(call buildpkg,dependencies/polkit-tqt)
endif

pytqt: sip4-tqt tdelibs tqscintilla
	$(call buildpkg,dependencies/pytqt)

sip4-tqt:
	$(call buildpkg,dependencies/sip4-tqt)

tde-cmake:
	$(call buildpkg,dependencies/tde-cmake)

tqca: tqtinterface
	$(call buildpkg,dependencies/tqca)

tqscintilla: tqca tdelibs
	$(call buildpkg,dependencies/tqscintilla)

tqt3:
	$(call buildpkg,dependencies/tqt3)

tqtinterface: tqt3
	$(call buildpkg,dependencies/tqtinterface)

# Core packages
tdeaccessibility: tdebase tdemultimedia
	$(call buildpkg,core/tdeaccessibility)

tdeaddons: tdebase tdegames tdemultimedia tdenetwork tdepim
	$(call buildpkg,core/tdeaddons)

tdeadmin: tdebase
	$(call buildpkg,core/tdeadmin)

tdeartwork: tdebase
	$(call buildpkg,core/tdeartwork)

tdebase: tdelibs htdig fileshareset pinentry-tqt
	$(call buildpkg,core/tdebase)

tdebindings: tdebase tqscintilla
	$(call buildpkg,core/tdebindings)

tdeedu: tdebase
	$(call buildpkg,core/tdeedu)

tdegames: tdebase tdemultimedia
	$(call buildpkg,core/tdegames)

tdegraphics: tdebase lcms
	$(call buildpkg,core/tdegraphics)

tdelibs: brp-check-trinity tqt3 tqtinterface arts dbus-tqt dbus-1-tqt avahi-tqt fileshareset trinity-filesystem libart_lgpl tde-cmake
	$(call buildpkg,core/tdelibs)

tdemultimedia: tdebase akode
	$(call buildpkg,core/tdemultimedia)

tdenetwork: tdebase rdesktop tqca
	$(call buildpkg,core/tdenetwork)

tdepim: tdebase libcaldav libcarddav
	$(call buildpkg,core/tdepim)

tdesdk: tdebase tdebindings tdepim
	$(call buildpkg,core/tdesdk)

tdetoys: tdebase
	$(call buildpkg,core/tdetoys)

tdeutils: tdebase
	$(call buildpkg,core/tdeutils)

tdevelop: tdebase tdesdk
	$(call buildpkg,core/tdevelop)

tdewebdev: tdebase tdesdk
	$(call buildpkg,core/tdewebdev)

### 3rd party libraries and tools
brp-check-trinity:
ifneq (,$(filter $(DIST), .oss151 .oss152 .oss153 .oss154 .oss155 .oss156 .osstw ))
	$(call buildpkg,3rdparty/brp-check-trinity)
endif

htdig:
ifneq (,$(filter $(DIST), .el7 .el8 .el9 .fc38 .fc39 .fc40 .fc41 .mga6 .mga7 .mga8 .mga9 .omv2490 .omv5000 ))
	$(call buildpkg,extras/htdig)
endif

imlib1:
ifneq (,$(filter $(DIST), .mga6 .mga7 .oss151 .osstw ))
	$(call buildpkg,3rdparty/imlib1)
endif

lcms:
ifneq (,$(filter $(DIST), .el7 .el8 .el9 .mga7 .mga8 .mga9 .oss151 .oss152 .oss153 .oss154 .oss155 .oss156 .osstw ))
	$(call buildpkg,3rdparty/lcms)
endif

rdesktop:
ifneq (,$(filter $(DIST), .oss150 ))
	$(call buildpkg,3rdparty/rdesktop)
endif

rdiff-backup:
# Only for PCLINUXOS
ifneq ($(wildcard /etc/pclinuxos-release),)
	$(call buildpkg,3rdparty/rdiff-backup)
endif

recode:
# Build on OpenSUSE >= 15.0 only (not tw)
ifneq (,$(filter $(DIST),.oss150 .oss151))
	$(call buildpkg,3rdparty/recode)
endif

wv2:
ifneq (,$(filter $(DIST), .el5 .el6 .el7 .el8 .el9 .fc30 .fc31 .fc32 .fc33 .fc34 .fc35 .fc36 .fc37 .fc38 .fc39 .fc40 .fc41 .omv2490 .omv5000))
	$(call buildpkg,3rdparty/wv2)
endif


### Trinity Libraries
kipi-plugins: tqtinterface tdelibs tdepim libkdcraw libkexiv2 libkipi
	$(call buildpkg,libraries/kipi-plugins)

libkdcraw: tqtinterface lcms
	$(call buildpkg,libraries/libkdcraw)

libkexiv2: tqtinterface tdelibs
	$(call buildpkg,libraries/libkexiv2)

libkipi: tqtinterface
	$(call buildpkg,libraries/libkipi)

libksquirrel: tdelibs
	$(call buildpkg,libraries/libksquirrel)

libtdeldap: tqtinterface
	$(call buildpkg,libraries/libtdeldap)

libtqt-perl: tqtinterface
	$(call buildpkg,libraries/libtqt-perl)

mlt: tqtinterface
	$(call buildpkg,libraries/mlt)

pytdeextensions: tqtinterface pytde
	$(call buildpkg,libraries/pytdeextensions)

pytde: tqtinterface pytqt sip4-tqt
	$(call buildpkg,libraries/pytde)

### Trinity Applications
abakus: tdebase
	$(call buildpkg,applications/utilities/abakus)

adept: tdebase
	$(call buildpkg,applications/system/adept)

amarok: tdebase
	$(call buildpkg,applications/multimedia/amarok)

basket: tdebase tdepim
	$(call buildpkg,applications/office/basket)

bibletime: tdebase
	$(call buildpkg,applications/misc/bibletime)

codeine: tdebase
	$(call buildpkg,applications/multimedia/codeine)

compizconfig-backend-tdeconfig: tdebase
	$(call buildpkg,applications/misc/compizconfig-backend-tdeconfig)

desktop-effects-tde: tdebase
	$(call buildpkg,applications/misc/desktop-effects-tde)

digikam: tdebase libkdcraw libkexiv2 libkipi libksquirrel
	$(call buildpkg,applications/graphics/digikam)

dolphin: tdebase
	$(call buildpkg,applications/system/dolphin)

filelight: tdebase
	$(call buildpkg,applications/utilities/filelight)

filelight-l10n: tdebase
	$(call buildpkg,applications/filelight-l10n)

fusion-icon: tdebase
	$(call buildpkg,applications/misc/fusion-icon)

gtk3-tqt-engine: tdebase
ifeq (,$(filter $(DIST),.el5 .el6))
	$(call buildpkg,applications/themes/gtk3-tqt-engine)
endif

gtk-qt-engine: tdebase
ifeq (,$(filter $(DIST),.el5))
	$(call buildpkg,applications/themes/gtk-qt-engine)
endif

gwenview: tdebase libkipi
	$(call buildpkg,applications/graphics/gwenview)

k3b: tdebase
	$(call buildpkg,applications/multimedia/k3b)

k9copy: tdebase k3b
	$(call buildpkg,applications/multimedia/k9copy)

kaffeine: tdebase
	$(call buildpkg,applications/multimedia/kaffeine)

kaffeine-mozilla: tdebase kaffeine
	$(call buildpkg,applications/multimedia/kaffeine-mozilla)

kasablanca: tdebase
	$(call buildpkg,applications/internet/kasablanca)

katapult: tdebase
	$(call buildpkg,applications/system/katapult)

kbarcode: tdebase
	$(call buildpkg,applications/utilities/kbarcode)

kbfx: tdebase
	$(call buildpkg,applications/system/kbfx)

kbibtex: tdebase
	$(call buildpkg,applications/office/kbibtex)

kbiff: tdebase
	$(call buildpkg,applications/internet/kbiff)

kbookreader: tdebase
	$(call buildpkg,applications/office/kbookreader)

kchmviewer: tdebase
	$(call buildpkg,applications/utilities/kchmviewer)

kcmautostart: tdebase
	$(call buildpkg,applications/system/kcmautostart)

kcmldap: tdebase libtdeldap
	$(call buildpkg,applications/misc/kcmldap)

kcmldapcontroller: tdebase kcmldap
	$(call buildpkg,applications/misc/kcmldapcontroller)

kcmldapmanager: tdebase kcmldap
	$(call buildpkg,applications/misc/kcmldapmanager)

kcpuload: tdebase
	$(call buildpkg,applications/utilities/kcpuload)

kdbg: tdebase
	$(call buildpkg,applications/development/kdbg)

kdbusnotification: tdebase
	$(call buildpkg,applications/system/kdbusnotification)

kdiff3: tdebase
	$(call buildpkg,applications/development/kdiff3)

kdirstat: tdebase
	$(call buildpkg,applications/utilities/kdirstat)

kdpkg: tdebase
	$(call buildpkg,applications/settings/kdpkg)

keep: tdebase rdiff-backup
	$(call buildpkg,applications/utilities/keep)

kerberostray: tdebase
	$(call buildpkg,applications/misc/kerberostray)

keximdb: tdebase koffice
	$(call buildpkg,applications/office/keximdb)

kftpgrabber: tdebase
	$(call buildpkg,applications/internet/kftpgrabber)

kgtk-qt3: tdebase
	$(call buildpkg,applications/themes/kgtk-qt3)

kile: tdebase
	$(call buildpkg,applications/office/kile)

kima: tdebase
	$(call buildpkg,applications/settings/kima)

kiosktool: tdebase
	$(call buildpkg,applications/settings/kiosktool)

kkbswitch: tdebase
	$(call buildpkg,applications/settings/kkbswitch)

klamav: tdebase
# Requires clamav >= 0.101.0
ifeq (,$(filter $(DIST), .el5 .el6 .mga6))
	$(call buildpkg,applications/system/klamav)
endif

klcddimmer: tdebase
	$(call buildpkg,applications/settings/klcddimmer)

kmplayer: tdebase koffice
	$(call buildpkg,applications/multimedia/kmplayer)

kmyfirewall: tdebase
	$(call buildpkg,applications/settings/kmyfirewall)

kmymoney: tdebase recode
	$(call buildpkg,applications/office/kmymoney)

knemo: tdebase
	$(call buildpkg,applications/system/knemo)

knetload: tdebase
	$(call buildpkg,applications/system/knetload)

knetstats: tdebase
	$(call buildpkg,applications/system/knetstats)

knights: tdebase
	$(call buildpkg,applications/games/knights)

knmap: tdebase
	$(call buildpkg,applications/internet/knmap)

knowit: tdebase
	$(call buildpkg,applications/office/knowit)

knutclient: tdebase
	$(call buildpkg,applications/utilities/knutclient)

koffice: tdebase tdegraphics wv2
	$(call buildpkg,applications/office/koffice)

kommando: tdebase
	$(call buildpkg,applications/utilities//kommando)

kompose: tdebase
	$(call buildpkg,applications/utilities/kompose)

konversation: tdebase
	$(call buildpkg,applications/internet/konversation)

kooldock: tdebase
	$(call buildpkg,applications/system/kooldock)

kopete-otr: tdebase tdenetwork
	$(call buildpkg,applications/internet/kopete-otr)

kpicosim: tdebase
	$(call buildpkg,applications/development/kpicosim)

kpilot: tdebase tdepim
ifeq (,$(filter $(DIST),.el5 .oss154 .oss155 .oss156 .osstw))
	$(call buildpkg,applications/office/kpilot)
endif

kplayer: tdebase
	$(call buildpkg,applications/multimedia/kplayer)

kpowersave: tdebase
	$(call buildpkg,applications/system/kpowersave)

krecipes: tdebase
	$(call buildpkg,applications/misc/krecipes)

krename: tdebase
	$(call buildpkg,applications/utilities/krename)

krusader: tdebase tdebindings
	$(call buildpkg,applications/system/krusader)

kscope: tdebase
	$(call buildpkg,applications/development/kscope)

ksensors: tdebase
	$(call buildpkg,applications/utilities/ksensors)

kshowmail: tdebase tdepim
	$(call buildpkg,applications/internet/kshowmail)

kshutdown: tdebase
	$(call buildpkg,applications/system/kshutdown)

ksplash-engine-moodin: tdebase
	$(call buildpkg,applications/themes/ksplash-engine-moodin)

ksquirrel: tdebase libkipi libksquirrel
	$(call buildpkg,applications/graphics/ksquirrel)

kstreamripper: tdebase
	$(call buildpkg,applications/internet/kstreamripper)

ksystemlog: tdebase
	$(call buildpkg,applications/system/ksystemlog)

ktechlab: tdebase
	$(call buildpkg,applications/development/ktechlab)

ktorrent: tdebase
	$(call buildpkg,applications/internet/ktorrent)

kvirc: tdebase
	$(call buildpkg,applications/internet/kvirc)

kvkbd: tdebase
	$(call buildpkg,applications/system/kvkbd)

kvpnc: tdebase
	$(call buildpkg,applications/internet/kvpnc)

kxmleditor: tdebase
	$(call buildpkg,applications/development/kxmleditor)

mathemagics: tdebase
	$(call buildpkg,applications/utilities/mathemagics)

mplayerthumbs: tdebase
	$(call buildpkg,applications/multimedia/mplayerthumbs)

piklab: tdebase
	$(call buildpkg,applications/development/piklab)

polkit-agent-tde: tdebase polkit-tqt
ifeq (,$(filter $(DIST), .el5 .el6 ))
	$(call buildpkg,applications/system/polkit-agent-tde)
endif

potracegui: tdebase
	$(call buildpkg,applications/graphics/potracegui)

qalculate-tde:
	$(call buildpkg,applications/utilities/qalculate-tde)

qt4-tqt-theme-engine: tdebase
ifeq (,$(filter $(DIST),.el5 .el6 .el8 .el9 .omv2490 .omv5000 .oss153 .oss154 .oss155 .oss156 .osstw))
	$(call buildpkg,applications/themes/qt4-tqt-theme-engine)
endif

rosegarden: tdebase
ifeq (,$(filter $(DIST),.el5 .el6 .el7 .el8 .el9))
	$(call buildpkg,applications/multimedia/rosegarden)
endif

smartcardauth: tdebase
	$(call buildpkg,applications/system/smartcardauth)

smb4k: tdebase
	$(call buildpkg,applications/internet/smb4k)

soundkonverter: tdebase
	$(call buildpkg,applications/multimedia/soundkonverter)

tastymenu:
	$(call buildpkg,applications/system/tastymenu)

tdebluez:
	$(call buildpkg,applications/system/tdebluez)

tdedocker: tdebase
	$(call buildpkg,applications/system/tdedocker)

tde-ebook-reader:
	$(call buildpkg,applications/office/tde-ebook-reader)

tde-guidance: tdebase pytdeextensions
	$(call buildpkg,applications/settings/tde-guidance)

tdeio-appinfo: tdebase
ifeq (,$(filter $(DIST), .el5 .el6 ))
	$(call buildpkg,applications/tdeio/tdeio-appinfo)
endif

tdeio-apt: tdebase
	$(call buildpkg,applications/tdeio/tdeio-apt)

tdeio-ftps: tdebase
	$(call buildpkg,applications/tdeio/tdeio-ftps)

tdeio-gopher: tdebase
	$(call buildpkg,applications/tdeio/tdeio-gopher)

tdeio-locate: tdebase
	$(call buildpkg,applications/tdeio/tdeio-locate)

tdeio-sword: tdebase
	$(call buildpkg,applications/tdeio/tdeio-sword)

tdeio-umountwrapper: tdebase
	$(call buildpkg,applications/tdeio/tdeio-umountwrapper)

tdenetworkmanager: tdebase
ifeq (,$(filter $(DIST),.el5 .el6))
	$(call buildpkg,applications/settings/tdenetworkmanager)
endif

tdepacman: tdebase
	$(call buildpkg,applications/games/tdepacman)

tdepowersave: tdebase
ifeq (,$(filter $(DIST),.el5))
	$(call buildpkg,applications/system/tdepowersave)
endif

tderadio: tdebase
	$(call buildpkg,applications/multimedia/tderadio)

tdesshaskpass: tdebase
	$(call buildpkg,applications/system/tdesshaskpass)

tde-style-baghira: tdebase
	$(call buildpkg,applications/themes/tde-style-baghira)

tde-style-domino: tdebase
	$(call buildpkg,applications/themes/tde-style-domino)

tde-style-ia-ora: tdebase
	$(call buildpkg,applications/themes/tde-style-ia-ora)

tde-style-lipstik: tdebase
	$(call buildpkg,applications/themes/tde-style-lipstik)

tde-style-polyester: tdebase
	$(call buildpkg,applications/themes/tde-style-polyester)

tde-style-qtcurve: tdebase
	$(call buildpkg,applications/themes/tde-style-qtcurve)

tdesudo: tdebase
	$(call buildpkg,applications/settings/tdesudo)

tdesvn: tdebase
	$(call buildpkg,applications/development/tdesvn)

tde-systemsettings: tdebase
	$(call buildpkg,applications/settings/tde-systemsettings)

tdmtheme: tdebase
	$(call buildpkg,applications/tdmtheme)

tellico: tdebase tdegraphics tdemultimedia tdepim
	$(call buildpkg,applications/office/tellico)

tork: tdebase
	$(call buildpkg,applications/internet/tork)

twin-style-crystal: tdebase
	$(call buildpkg,applications/themes/twin-style-crystal)

twin-style-dekorator: tdebase
	$(call buildpkg,applications/themes/twin-style-dekorator)

twin-style-fahrenheit: tdebase
	$(call buildpkg,applications/themes/twin-style-fahrenheit)

twin-style-machbunt: tdebase
	$(call buildpkg,applications/themes/twin-style-machbunt)

twin-style-mallory: tdebase
	$(call buildpkg,applications/themes/twin-style-mallory)

twin-style-suse2: tdebase
	$(call buildpkg,applications/themes/twin-style-suse2)

wlassistant: tdebase
	$(call buildpkg,applications/settings/wlassistant)

yakuake: tdebase
	$(call buildpkg,applications/system/yakuake)

### Trinity Translations
gwenview-i18n: tdebase
	$(call buildpkg,applications/graphics/gwenview-i18n)

k3b-i18n: tdebase
	$(call buildpkg,applications/multimedia/k3b-i18n)

koffice-i18n: tdebase
	$(call buildpkg,applications/office/koffice-i18n)

tde-i18n: tdebase
	$(call buildpkg,tde-i18n)

### Meta packages
meta:
	$(call buildpkg,extras/trinity-desktop)

### Extra packages
fileshareset:
	$(call buildpkg,extras/fileshareset)

pinentry-tqt: tqtinterface
ifeq (,$(filter $(DIST), .el5 .el6 .el7 ))
	$(call buildpkg,extras/pinentry-tqt)
endif

trinity-filesystem:
	$(call buildpkg,extras/trinity-filesystem)


# Developers options
git:
	cd "$(TDE_GIT_DIR)" && ./scripts/switch_all_submodules_to_head_and_clean anonymous

tarballs:
	cd "$(TDE_GIT_DIR)" && COMPRESS=pigz SUFFIX=0 TARBALLS_BASE="${HOME}/tde/tarballs/${TDE_VERSION}" ./scripts/create_all_tarballs


# External packages
external:
	if [ -d "${HOME}/rpmbuild/RPMS" ]; then cp -rfv "${HOME}/rpmbuild/RPMS/"* "$(RPMDIR)"; fi
