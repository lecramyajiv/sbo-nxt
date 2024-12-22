%if 0%{?fedora} >= 23
%define _hardened_ldflags %nil
%endif

#
# spec file for package tdenetwork (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg tdenetwork
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_sbindir %{tde_prefix}/sbin
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

# Avoids relinking, which breaks consolehelper
%define dont_relink 1

# Disable AIM support
%define with_aim 1

Name:			trinity-%{tde_pkg}
Summary:		Trinity Desktop Environment - Network Applications
Group:			Applications/Internet
Version:		%{tde_version}
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:	kppp.pamd
Source2:	ktalk
Source3:	trinity-tdenetwork-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	libtqca-devel >= %{tde_epoch}:1.0

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gettext
BuildRequires:	coreutils 
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# for set_permissions macro
%if 0%{?suse_version}
PreReq: permissions
%endif

# AVAHI support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_avahi 1
BuildRequires:	libavahi-tqt-devel >= 1:0.6.30
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}avahi-client-devel
Requires:		%{_lib}avahi-client3
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	avahi-devel
Requires:		avahi
%endif
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# TLS support
BuildRequires:	gnutls-devel

# SQLITE support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	sqlite3-devel
%else
BuildRequires:	sqlite-devel
%endif

# GADU support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_gadu 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}gadu-devel
%else
BuildRequires:	libgadu-devel
%endif
%endif

# PCRE support
BuildRequires:	pcre-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# XTST support
%if 0%{?fedora} >= 5 || 0%{?rhel} >= 5 || 0%{?suse_version} >= 1210
BuildRequires:	libXtst-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	libxtst-devel
%endif

# XMU support
%if 0%{?suse_version} == 1140
BuildRequires:	xorg-x11-libXmu-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version} >= 1210
BuildRequires: libXmu-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion} >= 4
BuildRequires: %{_lib}xmu-devel
%endif
%if 0%{?mgaversion} == 2 || 0%{?mgaversion} == 3
BuildRequires:	%{_lib}xmu%{?mgaversion:6}-devel
%endif

# Other stuff
%if 0%{?fedora} >= 5 || 0%{?rhel} >= 5
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXxf86vm-devel
%endif

# Fedora review:  http://bugzilla.redhat.com/195486

## Conditional build:
# RHEL6: xmms is outdated !
#define _with_xmms --with-xmms

# Wifi support
%if 0%{?fedora} >= 6 || 0%{?rhel} >= 5
%define wifi_devel wireless-tools-devel
%endif
%if 0%{?mgaversion} == 2 || 0%{?mdkversion}
%define wifi_devel %{_lib}iw29-devel
%endif
%if 0%{?rhel} == 5 || 0%{?suse_version}
%define wifi_devel wireless-tools
%endif
%if 0%{?suse_version} || 0%{?mgaversion} >= 3
%define wifi_devel libiw-devel
%endif
%if 0%{?mdkver}
%define wifi_devel %nil
%endif
%if "%{wifi_devel}" != ""
%define with_wifi 1
BuildRequires:	%{wifi_devel}
%endif

# OpenSLP support
%if 0%{?rhel} == 5 || 0%{?rhel} == 6 || 0%{?rhel} == 7 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_openslp 1
BuildRequires: openslp-devel
%endif

%ifarch %{ix86}
# BR: /usr/include/valgrind/valgrind.h
BuildRequires: valgrind
%endif

%{?_with_xmms:BuildRequires: xmms-devel}

# V4L support
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15 || 0%{?suse_version}
BuildRequires:	libv4l-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}v4l-devel
%endif
%if 0%{?rhel} == 5
BuildRequires:	kernel-headers
%endif

# XML support
BuildRequires:	libxml2-devel

# XSLT support
%if 0%{?mdkver}
BuildRequires:	%{_lib}xslt-devel
%else
BuildRequires:	libxslt-devel
%endif

#jabber
BuildRequires:	libidn-devel
#jabber/jingle
%if 0%{?suse_version}
BuildRequires:	libexpat-devel
%else
BuildRequires:	expat-devel
%endif
BuildRequires:	glib2-devel
BuildRequires:	speex-devel
# jabber/ssl
#{?fedora:Requires(hint): qca-tls}
#Requires:		jasper

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# MEANWHILE support
%if 0%{?rhel} == 6 || 0%{?rhel} == 7 || 0%{?fedora} >= 15 || 0%{?suse_version}
%define with_meanwhile 1
BuildRequires:	meanwhile-devel
%endif

# SPEEX support
%if 0%{?rhel} >= 5 || 0%{?fedora} >= 15 || 0%{?suse_version} || 0%{?mdkversion} || 0%{?mgaversion}
%define with_speex 1
BuildRequires:	speex-devel
%endif

# CONSOLEHELPER (usermode) support
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_consolehelper 1

# XINETD support
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
# No xinetd
%else
%define with_xinetd 1
Requires:		xinetd
%endif

# Avoids relinking, which breaks consolehelper
%define dont_relink 1
%endif

# Build kopete motionaway plugin
%if 0%{?rhel} != 5
%define build_kopete_motionaway 1
%endif

Obsoletes:	trinity-kdenetwork < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdenetwork-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdenetwork-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork-extras = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdenetwork < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdenetwork = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: trinity-dcoprss = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-filesharing = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kdict = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdefile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kget = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-knewsticker = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kopete = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kopete-nowlistening = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpf = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kppp = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-krdc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-krfb = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksirc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktalkd = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?with_wifi}
Requires: trinity-kwifimanager = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: trinity-librss = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-lisa = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This metapackage includes a collection of network and networking related
applications provided with the official release of Trinity.

Networking applications, including:
* dcoprss: RSS utilities for Trinity
* filesharing: Network filesharing configuration module for Trinity
* kdict: Dictionary client for Trinity
* tdefile-plugins: Torrent metainfo plugin for Trinity
* kget: downloader manager
* knewsticker: RDF newsticker applet
* kopete: chat client
* kopete-nowlistening: (xmms) plugin for Kopete.
* kpf: Public fileserver for Trinity
* kppp: dialer and front end for pppd
* krdc: a client for Desktop Sharing and other VNC servers
* krfb: Desktop Sharing server, allow others to access your desktop via VNC
* ksirc: IRC client for Trinity
* ktalkd: Talk daemon for Trinity
%if 0%{?with_wifi}
* kwifimanager: Wireless lan manager for Trinity
%endif
* librss: RSS library for Trinity
* lisa: lan information server

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README


##########

%package -n trinity-dcoprss
Summary:		RSS utilities for Trinity
Group:			Applications/Internet

%description -n trinity-dcoprss
dcoprss is a RSS to DCOP bridge, allowing all
DCOP aware applications to access RSS news feeds. There is also
a few sample utilities provided.
RSS is a standard for publishing news headlines.
DCOP is the TDE interprocess communication protocol.

%files -n trinity-dcoprss
%defattr(-,root,root,-)
%{tde_bindir}/feedbrowser
%{tde_bindir}/rssclient
%{tde_bindir}/rssservice
%{tde_datadir}/services/rssservice.desktop

##########

%package devel
Summary:		Development files for the Trinity network module
Group:			Development/Libraries/Other
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-kdict = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-kopete = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-ksirc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-librss = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-tdelibs-devel >= %{tde_version}

Obsoletes:	trinity-kdenetwork-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdenetwork-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdenetwork-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This is the development package which contains the headers for the TDE RSS
library as well as the Kopete chat client, as well as miscellaneous
development-related files for the TDE network module.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kopete/
%{tde_tdeincludedir}/rss/
%{tde_libdir}/libkopete.la
%{tde_libdir}/libkopete.so
%if 0%{?with_aim}
%{tde_libdir}/libkopete_msn_shared.la
%{tde_libdir}/libkopete_msn_shared.so
%endif
%{tde_libdir}/libkopete_oscar.la
%{tde_libdir}/libkopete_oscar.so
%{tde_libdir}/libkopete_videodevice.la
%{tde_libdir}/libkopete_videodevice.so
%{tde_libdir}/librss.la
%{tde_libdir}/librss.so

##########

%package filesharing
#Recommends:	perl-suid
Summary:		Network filesharing configuration module for Trinity
Group:   		Applications/Internet

Obsoletes:		tdenetwork-filesharing < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		tdenetwork-filesharing = %{?epoch:%{epoch}:}%{version}-%{release}

%description filesharing
This package provides a Trinity Control Center module to configure
NFS and Samba.

%files filesharing
%defattr(-,root,root,-)
%{tde_tdelibdir}/fileshare_propsdlgplugin.la
%{tde_tdelibdir}/fileshare_propsdlgplugin.so
%{tde_tdelibdir}/kcm_fileshare.la
%{tde_tdelibdir}/kcm_fileshare.so
%{tde_tdelibdir}/kcm_kcmsambaconf.la
%{tde_tdelibdir}/kcm_kcmsambaconf.so
%{tde_tdeappdir}/fileshare.desktop
%{tde_tdeappdir}/kcmsambaconf.desktop
%{tde_datadir}/icons/hicolor/*/apps/kcmfileshare.png
%{tde_datadir}/icons/hicolor/*/apps/kcmsambaconf.png
%{tde_datadir}/services/fileshare_propsdlgplugin.desktop
%{tde_tdedocdir}/HTML/en/kcontrol/fileshare/
%{tde_tdedocdir}/HTML/en/kcontrol/kcmsambaconf/

##########

%package -n trinity-kdict
Summary:		Dictionary client for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-kdict
KDict is an advanced TDE graphical client for the DICT Protocol, with full
Unicode support. It enables you to search through dictionary databases for a
word or phrase, then displays suitable definitions. KDict tries to ease
basic as well as advanced queries.

%files -n trinity-kdict
%defattr(-,root,root,-)
%{tde_bindir}/kdict
%{tde_tdelibdir}/kdict.*
%{tde_tdelibdir}/kdict_panelapplet.*
%{tde_libdir}/libtdeinit_kdict.*
%{tde_tdeappdir}/kdict.desktop
%{tde_datadir}/apps/kdict
%{tde_datadir}/apps/kicker/applets/kdictapplet.desktop
%{tde_datadir}/icons/hicolor/*/apps/kdict.*
%{tde_tdedocdir}/HTML/en/kdict
%{tde_mandir}/man1/kdict.1*

##########

%package tdefile-plugins
Summary:		Torrent metainfo plugin for Trinity
Group:			Applications/Internet

Obsoletes:		tdenetwork-kfile-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		tdenetwork-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-tdenetwork-kfile-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-tdenetwork-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdefile-plugins
This package provides a metainformation plugin for bittorrent files.
TDE uses tdefile-plugins to provide metainfo tab in the files properties
dialog in konqueror and other file-handling applications.

%files tdefile-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/tdefile_torrent.la
%{tde_tdelibdir}/tdefile_torrent.so
%{tde_datadir}/services/tdefile_torrent.desktop

##########

%package -n trinity-kget
Summary:		Download manager for Trinity
Group:			Applications/Internet
Requires:		trinity-tdebase-data >= %{tde_version}
Requires:		trinity-konqueror >= %{tde_version}

%description -n trinity-kget
KGet is a a download manager similar to GetRight or Go!zilla. It keeps
all your downloads in one dialog and you can add and remove transfers.
Transfers can be paused, resumed, queued or scheduled.
Dialogs display info about status of transfers - progress, size, speed
and remaining time. Program supports drag & drop from TDE
applications and Netscape.

%files -n trinity-kget
%defattr(-,root,root,-)
%{tde_bindir}/kget
%{tde_tdelibdir}/tdehtml_kget.la
%{tde_tdelibdir}/tdehtml_kget.so
%{tde_tdeappdir}/kget.desktop
%{tde_datadir}/apps/kget
%{tde_datadir}/apps/tdehtml/kpartplugins/kget_plug_in.desktop
%{tde_datadir}/apps/tdehtml/kpartplugins/kget_plug_in.rc
%{tde_datadir}/apps/konqueror/servicemenus/kget_download.desktop
%{tde_datadir}/icons/crystalsvg/*/actions/tdehtml_kget.png
%{tde_datadir}/icons/crystalsvg/*/apps/kget.png
%{tde_datadir}/icons/crystalsvg/*/mimetypes/kget_list.png
%{tde_datadir}/icons/hicolor/*/apps/kget.png
%{tde_datadir}/mimelnk/application/x-kgetlist.desktop
%{tde_datadir}/sounds/KGet_Added.ogg
%{tde_datadir}/sounds/KGet_Finished.ogg
%{tde_datadir}/sounds/KGet_Finished_All.ogg
%{tde_datadir}/sounds/KGet_Started.ogg
%{tde_tdedocdir}/HTML/en/kget
%{tde_mandir}/man1/kget.1*

##########

%package -n trinity-knewsticker
Summary:		News ticker applet for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-knewsticker
This is a news ticker applet for the Trinity panel. It can scroll news from
your favorite news sites, such as lwn.net, /. and freshmeat.net.
To achieve this, KNewsTicker requires the news sites to provide a
RSS feed to newsitems. KNewsTicker already comes with a selection of
good news sources which provide such files.

%files -n trinity-knewsticker
%defattr(-,root,root,-)
%{tde_bindir}/knewstickerstub
%{tde_tdelibdir}/knewsticker_panelapplet.la
%{tde_tdelibdir}/knewsticker_panelapplet.so
%{tde_tdelibdir}/libkntsrcfilepropsdlg.la
%{tde_tdelibdir}/libkntsrcfilepropsdlg.so
%{tde_tdeappdir}/knewsticker-standalone.desktop
%{tde_datadir}/applnk/.hidden/knewstickerstub.desktop
%{tde_datadir}/apps/tdeconf_update/knewsticker.upd
%{tde_datadir}/apps/tdeconf_update/knt-0.1-0.2.pl
%{tde_datadir}/apps/kicker/applets/knewsticker.desktop
%{tde_datadir}/apps/knewsticker/
%{tde_datadir}/icons/hicolor/*/apps/knewsticker.png
%{tde_datadir}/services/kntsrcfilepropsdlg.desktop
%{tde_tdedocdir}/HTML/en/knewsticker

##########

%package -n trinity-kopete
Summary:		Instant messenger for Trinity
Group:			Applications/Internet
Requires:		trinity-tdebase-bin >= %{tde_version}
Requires:		trinity-tdebase-data >= %{tde_version}
Requires:		trinity-filesystem >= %{tde_version}

%description -n trinity-kopete
Kopete is an instant messenger program which can communicate with a variety
of IM systems, such as Yahoo, ICQ, IRC and Jabber.

Support for more IM protocols can be added through a plugin system.

%files -n trinity-kopete
%defattr(-,root,root,-)
# nowlistening support
%exclude %{tde_datadir}/apps/kopete/*nowlisteningchatui*
%exclude %{tde_datadir}/apps/kopete/*nowlisteningui*
%exclude %{tde_datadir}/config.kcfg/nowlisteningconfig.kcfg
%exclude %{tde_datadir}/services/tdeconfiguredialog/*nowlistening*
%exclude %{tde_datadir}/services/*nowlistening*
%exclude %{tde_tdelibdir}/*nowlistening*
# Main kopete package
%{tde_bindir}/kopete
%{tde_bindir}/kopete_latexconvert.sh
%{tde_libdir}/tdeconf_update_bin/kopete-account-tdeconf_update
%{tde_libdir}/tdeconf_update_bin/kopete-nameTracking-tdeconf_update
%{tde_libdir}/tdeconf_update_bin/kopete-pluginloader2-tdeconf_update
%{tde_tdelibdir}/kcm_kopete_*.so
%{tde_tdelibdir}/kcm_kopete_*.la
%{tde_tdelibdir}/tdeio_jabberdisco.la
%{tde_tdelibdir}/tdeio_jabberdisco.so
%{tde_tdelibdir}/kopete_*.la
%{tde_tdelibdir}/kopete_*.so
%{tde_tdelibdir}/libkrichtexteditpart.la
%{tde_tdelibdir}/libkrichtexteditpart.so
%{tde_libdir}/libkopete_oscar.so.*
%{tde_libdir}/libkopete.so.*
%{tde_libdir}/libkopete_videodevice.so.*
%{tde_tdeappdir}/kopete.desktop
%{tde_datadir}/apps/tdeconf_update/kopete-*
%{tde_datadir}/apps/kopete/
%{tde_datadir}/apps/kopete_*/
%{tde_datadir}/apps/kopeterichtexteditpart/
%{tde_datadir}/config.kcfg/historyconfig.kcfg
%{tde_datadir}/config.kcfg/kopeteidentityconfigpreferences.kcfg
%{tde_datadir}/config.kcfg/kopete.kcfg
%{tde_datadir}/config.kcfg/latexconfig.kcfg
%{tde_datadir}/icons/crystalsvg/*/actions/voicecall.png
%{tde_datadir}/icons/crystalsvg/*/actions/webcamreceive.png
%{tde_datadir}/icons/crystalsvg/*/actions/webcamsend.png
%{tde_datadir}/icons/crystalsvg/*/actions/account_offline_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/add_user.png
%{tde_datadir}/icons/crystalsvg/*/actions/contact_away_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/contact_busy_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/contact_food_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/contact_invisible_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/contact_phone_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/contact_xa_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/delete_user.png
%{tde_datadir}/icons/crystalsvg/*/actions/edit_user.png
%{tde_datadir}/icons/crystalsvg/*/actions/emoticon.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_away.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_chatty.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_connecting.mng
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_group.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_invisible.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_na.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_offline.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_online.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_raw.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_serv_off.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_serv_on.png
%{tde_datadir}/icons/crystalsvg/*/actions/jabber_xa.png
%{tde_datadir}/icons/crystalsvg/*/actions/kopeteavailable.png
%{tde_datadir}/icons/crystalsvg/*/actions/kopeteaway.png
%{tde_datadir}/icons/crystalsvg/*/actions/kopeteeditstatusmessage.png
%{tde_datadir}/icons/crystalsvg/*/actions/kopetestatusmessage.png
%{tde_datadir}/icons/crystalsvg/*/actions/metacontact_away.png
%{tde_datadir}/icons/crystalsvg/*/actions/metacontact_offline.png
%{tde_datadir}/icons/crystalsvg/*/actions/metacontact_online.png
%{tde_datadir}/icons/crystalsvg/*/actions/metacontact_unknown.png
%{tde_datadir}/icons/crystalsvg/*/actions/newmsg.png
%{tde_datadir}/icons/crystalsvg/*/actions/search_user.png
%{tde_datadir}/icons/crystalsvg/*/actions/show_offliners.png
%{tde_datadir}/icons/crystalsvg/*/actions/status_unknown_overlay.png
%{tde_datadir}/icons/crystalsvg/*/actions/status_unknown.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_aim.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_gadu.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_http-ws.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_icq.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_irc.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_msn.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_qq.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_smtp.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_tlen.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_gateway_yahoo.png
%{tde_datadir}/icons/crystalsvg/*/apps/jabber_protocol.png
%{tde_datadir}/icons/crystalsvg/*/apps/kopete_all_away.png
%{tde_datadir}/icons/crystalsvg/*/apps/kopete_offline.png
%{tde_datadir}/icons/crystalsvg/*/apps/kopete_some_away.png
%{tde_datadir}/icons/crystalsvg/*/apps/kopete_some_online.png
%{tde_datadir}/icons/crystalsvg/*/mimetypes/kopete_emoticons.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/account_offline_overlay.svgz
%{tde_datadir}/icons/hicolor/*/apps/kopete.png
%{tde_datadir}/icons/hicolor/*/actions/emoticon.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_away.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_chatty.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_connecting.mng
%{tde_datadir}/icons/hicolor/*/actions/jabber_group.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_invisible.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_na.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_offline.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_online.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_raw.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_serv_off.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_serv_on.png
%{tde_datadir}/icons/hicolor/*/actions/jabber_xa.png
%{tde_datadir}/icons/hicolor/*/actions/kopeteavailable.png
%{tde_datadir}/icons/hicolor/*/actions/kopeteaway.png
%{tde_datadir}/icons/hicolor/*/actions/newmsg.png
%{tde_datadir}/icons/hicolor/*/actions/status_unknown_overlay.png
%{tde_datadir}/icons/hicolor/*/actions/status_unknown.png
%{tde_datadir}/icons/hicolor/*/apps/jabber_protocol.png
%{tde_datadir}/icons/hicolor/scalable/apps/kopete2.svgz
%{tde_datadir}/icons/crystalsvg/*/actions/newmessage.mng
%{tde_datadir}/icons/hicolor/*/actions/newmessage.mng
%{tde_datadir}/icons/crystalsvg/*/apps/icq_protocol.png
%{tde_datadir}/icons/crystalsvg/*/apps/irc_protocol.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_away.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_connecting.mng
%{tde_datadir}/icons/crystalsvg/*/actions/icq_dnd.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_ffc.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_invisible.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_na.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_occupied.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_offline.png
%{tde_datadir}/icons/crystalsvg/*/actions/icq_online.png
%{tde_datadir}/icons/crystalsvg/*/actions/irc_away.png
%{tde_datadir}/icons/crystalsvg/*/actions/irc_channel.png
%{tde_datadir}/icons/crystalsvg/*/actions/irc_connecting.mng
%{tde_datadir}/icons/crystalsvg/*/actions/irc_normal.png
%{tde_datadir}/icons/crystalsvg/*/actions/irc_online.png
%{tde_datadir}/icons/crystalsvg/*/actions/irc_op.png
%{tde_datadir}/icons/crystalsvg/*/actions/irc_server.png
%{tde_datadir}/icons/crystalsvg/*/actions/irc_voice.png
%{tde_datadir}/icons/hicolor/*/actions/icq_away.png
%{tde_datadir}/icons/hicolor/*/actions/icq_connecting.mng
%{tde_datadir}/icons/hicolor/*/actions/icq_dnd.png
%{tde_datadir}/icons/hicolor/*/actions/icq_ffc.png
%{tde_datadir}/icons/hicolor/*/actions/icq_invisible.png
%{tde_datadir}/icons/hicolor/*/actions/icq_na.png
%{tde_datadir}/icons/hicolor/*/actions/icq_occupied.png
%{tde_datadir}/icons/hicolor/*/actions/icq_offline.png
%{tde_datadir}/icons/hicolor/*/actions/icq_online.png
%{tde_datadir}/icons/hicolor/*/apps/icq_protocol.png
%{tde_datadir}/mimelnk/application/x-icq.desktop
%{tde_datadir}/mimelnk/application/x-kopete-emoticons.desktop
%{tde_datadir}/services/chatwindow.desktop
%{tde_datadir}/services/emailwindow.desktop
%{tde_datadir}/services/jabberdisco.protocol
%{tde_datadir}/services/tdeconfiguredialog/kopete_*.desktop
%{tde_datadir}/services/kopete_*.desktop
%{tde_datadir}/icons/crystalsvg/16x16/apps/jabber_gateway_sms.png
%{tde_datadir}/servicetypes/kopete*.desktop
%{tde_datadir}/sounds/Kopete_*.ogg
%{tde_tdedocdir}/HTML/en/kopete
# jingle support for kopete
%{tde_bindir}/relayserver
%{tde_bindir}/stunserver
# winpopup support for kopete
%{tde_bindir}/winpopup-install.sh
%{tde_bindir}/winpopup-send.sh
%if 0%{?build_kopete_motionaway}
# motionaway plugin for kopete
%{tde_datadir}/config.kcfg/motionawayconfig.kcfg
%endif
# smpp plugin for kopete
%{tde_datadir}/config.kcfg/smpppdcs.kcfg
# aim support is deprecated in TDE 14.1.x
%if 0%{?with_aim}
%{tde_datadir}/icons/crystalsvg/*/apps/aim_protocol.png
%{tde_datadir}/icons/crystalsvg/*/actions/aim_away.png
%{tde_datadir}/icons/crystalsvg/*/actions/aim_connecting.mng
%{tde_datadir}/icons/crystalsvg/*/actions/aim_offline.png
%{tde_datadir}/icons/crystalsvg/*/actions/aim_online.png
%{tde_datadir}/icons/hicolor/*/actions/aim_away.png
%{tde_datadir}/icons/hicolor/*/actions/aim_connecting.mng
%{tde_datadir}/icons/hicolor/*/actions/aim_offline.png
%{tde_datadir}/icons/hicolor/*/actions/aim_online.png
%{tde_datadir}/icons/hicolor/*/apps/aim_protocol.png
%{tde_datadir}/services/aim.protocol
%{tde_libdir}/libkopete_msn_shared.so.0
%{tde_libdir}/libkopete_msn_shared.so.0.0.0
%endif
%{tde_mandir}/man1/kopete.1*

##########

%package -n trinity-kopete-nowlistening
Summary:		Nowlistening (xmms) plugin for Kopete
Group:			Applications/Internet
Requires:		trinity-kopete = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-filesystem >= %{tde_version}

%description -n trinity-kopete-nowlistening
Kopete includes the "Now Listening" plug-in that can report what music you
are currently listening to, in a number of different players, including
noatun, kscd, juk, kaffeine and amarok.

%files -n trinity-kopete-nowlistening
%defattr(-,root,root,-)
%{tde_datadir}/apps/kopete/*nowlisteningchatui*
%{tde_datadir}/apps/kopete/*nowlisteningui*
%{tde_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{tde_datadir}/services/tdeconfiguredialog/*nowlistening*
%{tde_datadir}/services/*nowlistening*
%{tde_tdelibdir}/*nowlistening*

##########

%package -n trinity-kpf
Summary:		Public fileserver for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-kpf
kpf provides simple file sharing using HTTP. kpf is strictly a public
fileserver, which means that there are no access restrictions to shared
files. Whatever you select for sharing is available to anyone. kpf is
designed to be used for sharing files with friends.

%files -n trinity-kpf
%defattr(-,root,root,-)
%{tde_tdelibdir}/kpf*
%{tde_datadir}/apps/kicker/applets/kpfapplet.desktop
%{tde_datadir}/icons/crystalsvg/*/apps/kpf.*
%{tde_datadir}/services/kpfpropertiesdialogplugin.desktop
%{tde_tdedocdir}/HTML/en/kpf

##########

%package -n trinity-kppp
Summary:		Modem dialer and ppp frontend for Trinity
Group:			Applications/Internet
BuildRequires:	ppp
Requires:		ppp

%if 0%{?with_consolehelper}
# package 'usermode' provides '/usr/bin/consolehelper-gtk'
%if 0%{?rhel} || 0%{?fedora}
Requires:	usermode-gtk
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
Requires:	usermode
%endif
%endif

%description -n trinity-kppp
KPPP is a dialer and front end for pppd. It allows for interactive
script generation and network setup. It will automate the dialing in
process to your ISP while letting you conveniently monitor the entire
process.

Once connected KPPP will provide a rich set of statistics and keep
track of the time spent online for you.

%files -n trinity-kppp
%defattr(-,root,root,-)
%if 0%{?with_consolehelper} == 0
# Some setuid binaries need special care
%if 0%{?suse_version}
%verify(not mode) %{tde_bindir}/kppp
%else
%attr(4711,root,root) %{tde_bindir}/kppp
%endif
%endif
%{tde_bindir}/kppplogview
%{tde_tdeappdir}/Kppp.desktop
%{tde_tdeappdir}/kppplogview.desktop
%{tde_datadir}/apps/kppp/
%{tde_datadir}/icons/hicolor/*/apps/kppp.png
%{tde_tdedocdir}/HTML/en/kppp/
%dir %{_sysconfdir}/ppp/peers
%{_sysconfdir}/ppp/peers/kppp-options

%if 0%{?with_consolehelper}
%config(noreplace) /etc/security/console.apps/kppp3
%config(noreplace) /etc/pam.d/kppp3
%{_sbindir}/kppp3
%{tde_bindir}/kppp3
%{tde_sbindir}/kppp3
%endif

%post -n trinity-kppp
%if 0%{?suse_version}
# Sets permissions on setuid files (openSUSE specific)
%set_permissions %{tde_bindir}/kppp
%endif

##########

%package -n trinity-krdc
Summary:		Remote Desktop Connection for Trinity
Group:			Applications/Internet
Requires:		rdesktop

%description -n trinity-krdc
krdc is an TDE graphical client for the rfb protocol, used by VNC,
and if rdesktop is installed, krdc can connect to Windows Terminal
Servers using RDP.

%files -n trinity-krdc
%defattr(-,root,root,-)
%{tde_bindir}/krdc
%{tde_tdeappdir}/krdc.desktop
%{tde_datadir}/apps/konqueror/servicemenus/smb2rdc.desktop
%{tde_datadir}/apps/krdc/
%{tde_datadir}/icons/crystalsvg/*/apps/krdc.png
%{tde_datadir}/icons/hicolor/*/apps/krdc.png
%{tde_datadir}/services/rdp.protocol
%{tde_datadir}/services/vnc.protocol
%{tde_tdedocdir}/HTML/en/krdc/
%{tde_tdedocdir}/HTML/en/tdeioslave/rdp/
%{tde_tdedocdir}/HTML/en/tdeioslave/vnc/

##########

%package -n trinity-krfb
Summary:		Desktop Sharing for Trinity
Group:			Applications/Internet

%description -n trinity-krfb
Desktop Sharing (krfb) is a server application that allows you to share
your current session with a user on another machine, who can use a
VNC client like krdc to view or even control the desktop. It doesn't
require you to start a new X session - it can share the current session.
This makes it very useful when you want someone to help you perform a
task.

%files -n trinity-krfb
%defattr(-,root,root,-)
%{tde_bindir}/krfb
%{tde_bindir}/krfb_httpd
%{tde_tdelibdir}/kcm_krfb.la
%{tde_tdelibdir}/kcm_krfb.so
%{tde_tdelibdir}/kded_kinetd.la
%{tde_tdelibdir}/kded_kinetd.so
%{tde_tdeappdir}/kcmkrfb.desktop
%{tde_tdeappdir}/krfb.desktop
%{tde_datadir}/apps/kinetd/
%{tde_datadir}/apps/krfb
%{tde_datadir}/icons/crystalsvg/*/apps/krfb.png
%{tde_datadir}/icons/hicolor/*/apps/krfb.png
%{tde_datadir}/icons/locolor/*/apps/krfb.png
%{tde_datadir}/services/kded/kinetd.desktop
%{tde_datadir}/services/kinetd_krfb.desktop
%{tde_datadir}/services/kinetd_krfb_httpd.desktop
%{tde_datadir}/servicetypes/kinetdmodule.desktop
%{tde_tdedocdir}/HTML/en/krfb/

##########

%package -n trinity-ksirc
Summary:		IRC client for Trinity
Group:			Applications/Internet

%description -n trinity-ksirc
KSirc is an IRC chat client for TDE. It supports scripting with Perl and has a
lot of compatibility with mIRC for general use.

If you want to connect to an IRC server via SSL, you will need to install the
recommended package libio-socket-ssl-perl.

%files -n trinity-ksirc
%defattr(-,root,root,-)
%{tde_bindir}/dsirc
%{tde_bindir}/ksirc
%{tde_libdir}/libtdeinit_ksirc.*
%{tde_tdelibdir}/ksirc.*
%{tde_tdeappdir}/ksirc.desktop
%{tde_datadir}/apps/ksirc/
%config(noreplace) %{tde_confdir}/ksircrc
%{tde_datadir}/icons/hicolor/*/apps/ksirc.*
%{tde_tdedocdir}/HTML/??/ksirc/

##########

%package -n trinity-ktalkd
Summary:		Talk daemon for Trinity
Group:			Applications/Internet
Requires:		trinity-kcontrol >= %{tde_version}
Requires:		trinity-tdebase-data >= %{tde_version}
%if 0%{?with_xinetd}
Requires:		xinetd
%endif

%description -n trinity-ktalkd
KTalkd is an enhanced talk daemon - a program to handle incoming talk
requests, announce them and allow you to respond to it using a talk
client. Note that KTalkd is designed to run on a single-user workstation,
and shouldn't be run on a multi-user machine.

%files -n trinity-ktalkd
%defattr(-,root,root,-)
%{tde_bindir}/ktalkd*
%{tde_bindir}/mail.local
%{tde_tdelibdir}/kcm_ktalkd.*
%{tde_tdeappdir}/kcmktalkd.desktop
%config(noreplace) %{tde_confdir}/ktalkdrc
%{tde_datadir}/icons/crystalsvg/*/apps/ktalkd.png
%{tde_datadir}/icons/hicolor/*/apps/ktalkd.png
%{tde_datadir}/sounds/ktalkd.wav
%if 0%{?with_xinetd}
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/ktalk
%endif
%{tde_tdedocdir}/HTML/en/kcontrol/kcmtalkd
%{tde_tdedocdir}/HTML/en/ktalkd

##########

%if 0%{?with_wifi}

%package -n trinity-kwifimanager
Summary:		Wireless lan manager for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-kwifimanager
KWiFiManager suite is a set of tools which allows you to manage your
wireless LAN connection under the K Desktop Environment. It provides
information about your current connection. KWiFiManager supports every
wavelan card that uses the wireless extensions interface.

%files -n trinity-kwifimanager
%defattr(-,root,root,-)
%{tde_bindir}/kwifimanager
%{tde_tdelibdir}/kcm_wifi.*
%{tde_libdir}/libkwireless.la
%{tde_libdir}/libkwireless.so
%{tde_tdeappdir}/kcmwifi.desktop
%{tde_tdeappdir}/kwifimanager.desktop
%{tde_datadir}/apps/kicker/applets/kwireless.desktop
%{tde_datadir}/apps/kwifimanager
%{tde_datadir}/icons/hicolor/*/apps/kwifimanager.png
%{tde_datadir}/icons/hicolor/*/apps/kwifimanager.svgz
%{tde_tdedocdir}/HTML/en/kwifimanager/
%{tde_tdedocdir}/HTML/en/kcontrol/kcmwifi/
%{tde_mandir}/man1/kwifimanager.1*

%endif

##########

%package -n trinity-librss
Summary:		RSS library for Trinity
Group:			Environment/Libraries

%description -n trinity-librss
This is the runtime package for programs that use the TDE RSS library.
End users should not need to install this, it should get installed
automatically when needed.

%files -n trinity-librss
%defattr(-,root,root,-)
%{tde_libdir}/librss.so.*
%{tde_datadir}/cmake/librss.cmake

##########

%package -n trinity-lisa
Summary:			LAN information server for Trinity
Group:				Applications/Internet
Requires:		trinity-konqueror >= %{tde_version}
Requires:		trinity-tdebase-data >= %{tde_version}

%description -n trinity-lisa
LISa is intended to provide TDE with a kind of "network neighborhood"
but relying only on the TCP/IP protocol.

%files -n trinity-lisa
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcm_lanbrowser.la
%{tde_tdelibdir}/kcm_lanbrowser.so
%{tde_tdelibdir}/tdeio_lan.la
%{tde_tdelibdir}/tdeio_lan.so
%{tde_datadir}/applnk/.hidden/kcmtdeiolan.desktop
%{tde_datadir}/applnk/.hidden/kcmlisa.desktop
%{tde_datadir}/applnk/.hidden/kcmreslisa.desktop
%{tde_datadir}/apps/konqsidebartng/virtual_folders/services/lisa.desktop
%{tde_datadir}/apps/konqueror/dirtree/remote/lan.desktop
%{tde_datadir}/apps/lisa/
%{tde_datadir}/apps/remoteview/lan.desktop
%{tde_tdedocdir}/HTML/en/kcontrol/lanbrowser/
%{tde_tdedocdir}/HTML/en/lisa/
%{tde_datadir}/services/lan.protocol
%{tde_datadir}/services/rlan.protocol
%{tde_bindir}/lisa
%{tde_bindir}/reslisa
%{tde_mandir}/man8/lisa.8*
%{tde_mandir}/man8/reslisa.8*

##########

%package -n trinity-kdnssd
Summary: Zeroconf support for TDE
Group:			Applications/Internet

%description -n trinity-kdnssd
A tdeioslave and tded module that provide Zeroconf support. Try
"zeroconf:/" in Konqueror.

%files -n trinity-kdnssd
%defattr(-,root,root,-)
%{tde_datadir}/services/zeroconf.protocol
%{tde_datadir}/services/invitation.protocol
%{tde_datadir}/services/kded/dnssdwatcher.desktop
%{tde_datadir}/apps/remoteview/zeroconf.desktop
%{tde_datadir}/apps/zeroconf/_http._tcp
%{tde_datadir}/apps/zeroconf/_ftp._tcp
%{tde_datadir}/apps/zeroconf/_ldap._tcp
%{tde_datadir}/apps/zeroconf/_webdav._tcp
%{tde_datadir}/apps/zeroconf/_nfs._tcp
%{tde_datadir}/apps/zeroconf/_ssh._tcp
%{tde_datadir}/apps/zeroconf/_rfb._tcp
%{tde_datadir}/apps/zeroconf/_sftp-ssh._tcp
%{tde_tdelibdir}/tdeio_zeroconf.so
%{tde_tdelibdir}/tdeio_zeroconf.la
%{tde_tdelibdir}/kded_dnssdwatcher.so
%{tde_tdelibdir}/kded_dnssdwatcher.la

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

# Workaround libiw detection failure on opensuse
%if 0%{?suse_version}
%if 0%{?with_wifi}
%__sed -i "wifi/ConfigureChecks.cmake" -e "s|^check_library_exists.*|set( HAVE_IW 1 )|"
%endif
%endif

# Update icons for some control center modules
%__sed -i "filesharing/simple/fileshare.desktop" -e "s|^Icon=.*|Icon=kcmfileshare|"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DWITH_JINGLE=ON \
  %{?with_speex:-DWITH_SPEEX=ON} \
  -DWITH_WEBCAM=ON \
  -DWITH_GSM=OFF \
  -DWITH_XMMS=OFF \
  -DWITH_ARTS=ON \
  %{!?with_openslp:-DWITH_SLP=OFF} \
  -DBUILD_ALL=ON \
  -DBUILD_KOPETE_PLUGIN_ALL=ON \
  -DBUILD_KOPETE_PROTOCOL_ALL=ON \
  %{!?build_kopete_motionaway:-DBUILD_KOPETE_PLUGIN_MOTIONAUTOAWAY=OFF} \
  %{!?with_gadu:-DBUILD_KOPETE_PROTOCOL_GADU=OFF} \
  %{!?with_meanwhile:-DBUILD_KOPETE_PROTOCOL_MEANWHILE=OFF} \
  %{!?with_wifi:-DBUILD_WIFI=OFF} \
  ..

# Tdenetwork is not smp safe !
%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Adds missing icons in 'hicolor' theme
# These icons are copied from 'crystalsvg' theme, provided by 'tdelibs'.
%__mkdir_p %{buildroot}%{tde_datadir}/icons/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps/
pushd %{buildroot}%{tde_datadir}/icons
for i in {16,22,32,48}; do        %__cp %{?buildroot}%{tde_datadir}/icons/crystalsvg/"$i"x"$i"/apps/kget.png    hicolor/"$i"x"$i"/apps/kget.png          ;done
for i in {32,48}; do              %__cp %{?buildroot}%{tde_datadir}/icons/crystalsvg/"$i"x"$i"/apps/krdc.png    hicolor/"$i"x"$i"/apps/krdc.png          ;done
for i in {16,32,48}; do           %__cp %{?buildroot}%{tde_datadir}/icons/crystalsvg/"$i"x"$i"/apps/krfb.png    hicolor/"$i"x"$i"/apps/krfb.png          ;done
for i in {16,22,32,48,128}; do    %__cp %{?buildroot}%{tde_datadir}/icons/crystalsvg/"$i"x"$i"/apps/ktalkd.png  hicolor/"$i"x"$i"/apps/ktalkd.png        ;done
for i in {16,22,32,48,64,128}; do %__cp $BUILD_ROOT%{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/share.png  hicolor/"$i"x"$i"/apps/kcmfileshare.png  ;done
popd

%if 0%{?with_consolehelper}
# Run kppp through consolehelper, and rename it to 'kppp3'
%__install -p -m644 -D %{SOURCE1} %{buildroot}/etc/pam.d/kppp3
%__mkdir_p %{buildroot}%{tde_sbindir} %{buildroot}%{_sbindir}
%__mv %{buildroot}%{tde_bindir}/kppp %{buildroot}%{tde_sbindir}/kppp3
%__ln_s %{_bindir}/consolehelper %{buildroot}%{tde_bindir}/kppp3
%if "%{tde_prefix}" != "/usr"
%__ln_s %{tde_sbindir}/kppp3 %{?buildroot}%{_sbindir}/kppp3
%endif
%__mkdir_p %{buildroot}%{_sysconfdir}/security/console.apps
cat > %{buildroot}%{_sysconfdir}/security/console.apps/kppp3 <<EOF
USER=root
PROGRAM=%{tde_sbindir}/kppp3
SESSION=true
EOF

# Renames 'kppp' as 'kppp3' in launch icon
%__sed -i %{buildroot}%{tde_tdeappdir}/Kppp.desktop -e "/Exec=/ s|kppp|kppp3|"
%endif

# Remove setuid bit on some binaries.
if [ -r "%{?buildroot}%{tde_bindir}/kppp" ]; then
  chmod 0755 "%{?buildroot}%{tde_bindir}/kppp"
fi

%if 0%{?with_xinetd}
# ktalk
%__install -p -m 0644 -D  %{SOURCE2} %{buildroot}%{_sysconfdir}/xinetd.d/ktalk
%endif

# Avoids conflict with trinity-kvirc
%__mv -f %{buildroot}%{tde_datadir}/services/irc.protocol %{buildroot}%{tde_datadir}/apps/kopete/

# Icons from TDE Control Center should only be displayed in TDE
for i in %{?buildroot}%{tde_tdeappdir}/*.desktop ; do
  if grep -q "^Categories=.*X-TDE-settings" "${i}"; then
    if ! grep -q "OnlyShowIn=TDE" "${i}" ; then
      echo "OnlyShowIn=TDE;" >>"${i}"
    fi
  fi
done

# Remove unwanted doc
%if 0%{?with_wifi} == 0
%__rm -rf "%{buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/kcmwifi/"
%__rm -rf "%{buildroot}%{tde_tdedocdir}/HTML/en/kwifimanager/"
%endif

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file    kcmkrfb
%suse_update_desktop_file    fileshare
%suse_update_desktop_file    kopete        Network  InstantMessaging
%suse_update_desktop_file    ksirc         Network  IRCClient
%suse_update_desktop_file    Kppp          Network  Dialup
%suse_update_desktop_file -r kppplogview   System   Monitor
%suse_update_desktop_file    kdict         Office   Dictionary
%suse_update_desktop_file -r krdc          System   RemoteAccess
%suse_update_desktop_file -r krfb          System   RemoteAccess
%suse_update_desktop_file -r kget          System   TrayIcon
%if 0%{?with_wifi}
%suse_update_desktop_file -r kwifimanager  System   Network
%suse_update_desktop_file    kcmwifi
%endif
%suse_update_desktop_file -u knewsticker-standalone Network  News
%suse_update_desktop_file %{buildroot}%{tde_datadir}/apps/remoteview/zeroconf.desktop
%endif

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"


%clean
%__rm -rf %{buildroot}


%if 0%{?suse_version}
# Check permissions on setuid files (openSUSE specific)
%verifyscript
%verify_permissions -e %{tde_bindir}/kppp
%endif


%changelog
