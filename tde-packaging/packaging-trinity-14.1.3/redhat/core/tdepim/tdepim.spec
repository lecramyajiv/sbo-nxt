#
# spec file for package tdepim (version R14)
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
%define tde_pkg tdepim
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

# TDEPIM optional features
#define		with_kitchensync 1

Name:		trinity-%{tde_pkg}
Summary:	Personal Information Management apps from the official Trinity release
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Group:		Applications/Productivity
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:	%{name}-rpmlintrc

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	libcaldav-devel >= %{tde_epoch}:0.6.5
BuildRequires:	libcarddav-devel >= %{tde_epoch}:0.6.2

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	fdupes
BuildRequires:	desktop-file-utils
BuildRequires:	make

BuildRequires:	gpgme-devel
BuildRequires:	flex
BuildRequires:	boost-devel
BuildRequires:	pcre-devel
BuildRequires:	libidn-devel

# ICAL support
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}ical-devel
%else
BuildRequires:	libical-devel
%endif

# GPG-ERROR support
%if 0%{?mdkver}
BuildRequires:	%{_lib}gpg-error-devel
%else
BuildRequires:	libgpg-error-devel
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# KDEPIM specific features
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
%define with_gnokii 1
BuildRequires:	gnokii-devel
%endif
%endif


# FLEX support
%if 0%{?fedora} >= 15
BuildRequires:	flex-static
%endif

# BISON support
BuildRequires:	bison

# CURL support
BuildRequires:	curl-devel

# GLIB2 support
BuildRequires:	glib2-devel

# SASL support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
%if 0%{?mdkver} >= 5000000
BuildRequires:	%{_lib}sasl-devel
%else
BuildRequires:	%{_lib}sasl2-devel
%endif
%else
BuildRequires:	cyrus-sasl-devel
%endif

# XCOMPOSITE support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xcomposite-devel
%else
BuildRequires:	%{_lib}xcomposite%{?mgaversion:1}-devel
%endif
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXcomposite-devel
%endif

# XSCREENSAVER support
#  RHEL 4: disabled
#  RHEL 6: available in EPEL
#  RHEL 7: available in NUX
#  RHEL 8: available in EPEL
#  RHEL 9: available in EPEL
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version}
%define with_xscreensaver 1

%if 0%{?fedora} || 0%{?rhel} >= 5
BuildRequires:	libXScrnSaver-devel
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
BuildRequires:	xscreensaver-extras
%if 0%{?fedora}
BuildRequires:	xscreensaver-extras-base
%endif
BuildRequires:	xscreensaver-gl-base
BuildRequires:	xscreensaver-gl-extras
%endif

%if 0%{?suse_version}
BuildRequires:	libXScrnSaver-devel
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-data
BuildRequires:	xscreensaver-data-extra
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xscrnsaver-devel
%else
BuildRequires:	%{_lib}xscrnsaver%{?mgaversion:1}-devel
%endif
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
%if 0%{?pclinuxos} == 0
BuildRequires:	xscreensaver-extrusion
%endif
BuildRequires:	xscreensaver-gl
%endif
%endif


Requires:	trinity-libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-wizards = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-akregator = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kalarm = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kandy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-karm = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmail = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmailcvt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmobile = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knode = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kode = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-konsolekalendar = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kontact = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korn = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ktnef = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libindex = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkgantt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkmime = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimexchange = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libksieve = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libmimelib = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdepim < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdepim < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdepim = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This metapackage includes a collection of Personal Information Management
(PIM) applications provided with the official release of Trinity.

%files
%defattr(-,root,root,-)

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries/Other

Obsoletes:	tdepim-cmake < %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdepim-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdepim-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-akregator-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kaddressbook-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-karm-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmail-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knode-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knotes-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kode-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kontact-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korganizer-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libindex-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkgantt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkleopatra-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkmime-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimexchange-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimidentities-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libksieve-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libmimelib-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This metapackage includes all development files for TDE PIM.
It also contains the CMAKE macros.

%files devel
%defattr(-,root,root,-)
%{tde_datadir}/cmake/*

##########

%package -n trinity-akregator
Summary:	RSS feed aggregator for TDE
Group:		Applications/Internet
Requires:	trinity-libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-akregator
aKregator is a fast, lightweight, and intuitive feed reader program
for TDE.  It allows you to quickly browse through hundreds of
thousands of internet feeds in a quick, efficient, and familiar way.

%files -n trinity-akregator
%defattr(-,root,root,-)
%{tde_bindir}/akregator
%{tde_tdelibdir}/libakregatorpart.la
%{tde_tdelibdir}/libakregatorpart.so
%{tde_tdelibdir}/libakregator_mk4storage_plugin.la
%{tde_tdelibdir}/libakregator_mk4storage_plugin.so
%{tde_libdir}/libakregatorprivate.so.*
%{tde_tdeappdir}/akregator.desktop
%{tde_datadir}/apps/akregator
%{tde_datadir}/config.kcfg/akregator.kcfg
%{tde_datadir}/config.kcfg/mk4config.kcfg
%{tde_datadir}/icons/crystalsvg/*/actions/rss_tag.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/akregator_empty.png
%{tde_datadir}/icons/hicolor/*/apps/akregator.png
%{tde_datadir}/icons/hicolor/scalable/apps/akregator.svgz
%{tde_datadir}/services/akregator_mk4storage_plugin.desktop
%{tde_datadir}/services/akregator_part.desktop
%{tde_datadir}/services/feed.protocol
%{tde_datadir}/services/kontact/akregatorplugin*.desktop
%{tde_datadir}/servicetypes/akregator_plugin.desktop
%{tde_tdedocdir}/HTML/en/akregator/
%{tde_tdedocdir}/HTML/en/tdeioslave/feed/

##########

%package -n trinity-akregator-devel
Summary:	Development files for trinity-akregator
Group:		Development/Libraries/Other
Requires:	trinity-akregator = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-akregator-devel
%{summary}

%files -n trinity-akregator-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/akregator/
%{tde_libdir}/libakregatorprivate.la
%{tde_libdir}/libakregatorprivate.so

##########

%package -n trinity-kaddressbook
Summary:	TDE addressbook application
Group:		Applications/Communications
Requires:	trinity-tdebase-tdeio-pim-plugins
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kaddressbook
KAddressBook is the main address book application for TDE; it enables you
to manage your contacts efficiently and comfortably. It can load and save
your contacts to many different locations, including the local file system,
LDAP servers, and SQL databases.

%files -n trinity-kaddressbook
%defattr(-,root,root,-)
%{tde_bindir}/tdeabc2mutt
%{tde_bindir}/kaddressbook
%{tde_bindir}/tdeabcdistlistupdater
%{tde_tdelibdir}/kcm_kabconfig.la
%{tde_tdelibdir}/kcm_kabconfig.so
%{tde_tdelibdir}/kcm_kabcustomfields.la
%{tde_tdelibdir}/kcm_kabcustomfields.so
%{tde_tdelibdir}/kcm_kabldapconfig.la
%{tde_tdelibdir}/kcm_kabldapconfig.so
%{tde_tdelibdir}/ldifvcardthumbnail.la
%{tde_tdelibdir}/ldifvcardthumbnail.so
%{tde_tdelibdir}/libkaddrbk_*.la
%{tde_tdelibdir}/libkaddrbk_*.so
%{tde_tdelibdir}/libkaddressbookpart.la
%{tde_tdelibdir}/libkaddressbookpart.so
%{tde_libdir}/libkabinterfaces.so.*
%{tde_libdir}/libkaddressbook.so.*
%{tde_tdeappdir}/kaddressbook.desktop
%{tde_datadir}/apps/kaddressbook
%{tde_datadir}/icons/hicolor/*/apps/kaddressbook.png
%{tde_datadir}/services/kabconfig.desktop
%{tde_datadir}/services/kabcustomfields.desktop
%{tde_datadir}/services/kabldapconfig.desktop
%{tde_datadir}/services/kaddressbook
%{tde_datadir}/services/kontact/kaddressbookplugin.desktop
%{tde_datadir}/services/tderesources/tdeabc/imap.desktop
%{tde_datadir}/services/ldifvcardthumbnail.desktop
%{tde_datadir}/servicetypes/dcopaddressbook.desktop
%{tde_datadir}/servicetypes/kaddressbook_contacteditorwidget.desktop
%{tde_datadir}/servicetypes/kaddressbookimprotocol.desktop
%{tde_datadir}/servicetypes/kaddressbook_extension.desktop
%{tde_datadir}/servicetypes/kaddressbook_view.desktop
%{tde_datadir}/servicetypes/kaddressbook_xxport.desktop
%{tde_tdedocdir}/HTML/en/kaddressbook/
%{tde_datadir}/autostart/tdeabcdistlistupdater.desktop
%{tde_tdeincludedir}/kaddressbook/
%{tde_tdeincludedir}/tdeabc/

##########

%package -n trinity-kaddressbook-devel
Summary:	Development files for trinity-kaddressbook
Group:		Development/Libraries/Other
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kaddressbook-devel
%{summary}

%files -n trinity-kaddressbook-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkabinterfaces.la
%{tde_libdir}/libkabinterfaces.so
%{tde_libdir}/libkaddressbook.la
%{tde_libdir}/libkaddressbook.so

##########

%package -n trinity-kalarm
Summary:	Trinity alarm message, command and email scheduler
Group:		Applications/Communications
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kalarm
KAlarm provides a graphical interface to schedule personal timed events -
pop-up alarm messages, command execution and sending emails. There is a
range of options for configuring recurring events.

A pop-up alarm can show either a simple text message, or the contents of a
text or image file, It can optionally be spoken, or play a sound file. You
can choose its appearance, and set reminders. Among KAlarm's other
facilities, you can set up templates to allow KAlarm to be used as a 'tea
timer'.

As an alternative to using the graphical interface, alarms can be scheduled
from the command line or via DCOP calls from other programs. KAlarm is
TDE-based, but will also run on other desktops.

%files -n trinity-kalarm
%defattr(-,root,root,-)
%{tde_bindir}/kalarm
%{tde_bindir}/kalarmd
%{tde_tdeappdir}/kalarm.desktop
%{tde_datadir}/applnk/.hidden/kalarmd.desktop
%{tde_datadir}/applnk/Applications/kalarm.desktop
%{tde_datadir}/apps/kalarm
%{tde_datadir}/autostart/kalarm.tray.desktop
%{tde_datadir}/autostart/kalarmd.autostart.desktop
%{tde_datadir}/icons/crystalsvg/*/actions/kalarm.png
%{tde_datadir}/icons/hicolor/*/apps/kalarm.png
%{tde_tdedocdir}/HTML/en/kalarm/

##########

%package -n trinity-kandy
Summary:	Trinity mobile phone utility
Group:		Applications/Communications

%description -n trinity-kandy
At the moment Kandy is more or less a terminal program with some special
features to store commands and their parameters, but is also has a simple GUI
to access the phone book of a mobile phone and it is able to save this phone
book to the TDE address book.

Kandy is aimed at mobile phones with integrated (GSM) modems.

%files -n trinity-kandy
%defattr(-,root,root,-)
%{tde_bindir}/kandy
%{tde_bindir}/kandy_client
%{tde_tdeappdir}/kandy.desktop
%{tde_datadir}/applnk/Utilities/kandy.desktop
%{tde_datadir}/apps/kandy/
%{tde_datadir}/icons/crystalsvg/*/apps/kandy.png
%{tde_datadir}/icons/hicolor/*/apps/kandy.png
%{tde_datadir}/config.kcfg/kandy.kcfg
%{tde_tdedocdir}/HTML/en/kandy/

##########

%package -n trinity-karm
Summary:	Trinity time tracker tool
Group:		Applications/Productivity

%description -n trinity-karm
KArm is a time tracker for busy people who need to keep track of the amount of
time they spend on various tasks.

%files -n trinity-karm
%defattr(-,root,root,-)
%{tde_bindir}/karm
%{tde_libdir}/libkarm.so.*
%{tde_tdelibdir}/libkarmpart.la
%{tde_tdelibdir}/libkarmpart.so
%{tde_tdeappdir}/karm.desktop
%{tde_datadir}/applnk/Utilities/karm.desktop
%{tde_datadir}/apps/karm/
%{tde_datadir}/apps/karmpart/
%{tde_datadir}/icons/hicolor/*/apps/karm.png
%{tde_datadir}/services/karm_part.desktop
%{tde_datadir}/services/kontact/karmplugin.desktop
%{tde_tdedocdir}/HTML/en/karm/

##########

%package -n trinity-karm-devel
Summary:	Development files for karm
Group:		Development/Libraries/Other

%description -n trinity-karm-devel
%{summary}

%files -n trinity-karm-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkarm.so
%{tde_libdir}/libkarm.la

##########

%package kfile-plugins
Summary:	TDE File dialog plugins for palm and vcf files
Group:		Environment/Libraries

Obsoletes:	tdepim-kfile-plugins < %{?epoch:%{epoch}:}%{version}-%{release}

%description kfile-plugins
File dialog plugins for palm and vcf files.

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/tdefile_ics.la
%{tde_tdelibdir}/tdefile_ics.so
%{tde_tdelibdir}/tdefile_vcf.la
%{tde_tdelibdir}/tdefile_vcf.so
%{tde_datadir}/services/tdefile_ics.desktop
%{tde_datadir}/services/tdefile_vcf.desktop

##########

%package tdeio-plugins
Summary:	Trinity PIM I/O Slaves
Group:		Environment/Libraries

Obsoletes:	tdepim-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdepim-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdepim-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This package includes the pim kioslaves. This includes imap4, sieve,
and mbox.

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/tdeio_groupwise.la
%{tde_tdelibdir}/tdeio_groupwise.so
%{tde_tdelibdir}/tdeio_imap4.la
%{tde_tdelibdir}/tdeio_imap4.so
%{tde_tdelibdir}/tdeio_mbox.la
%{tde_tdelibdir}/tdeio_mbox.so
%{tde_tdelibdir}/tdeio_scalix.la
%{tde_tdelibdir}/tdeio_scalix.so
%{tde_tdelibdir}/tdeio_sieve.la
%{tde_tdelibdir}/tdeio_sieve.so
%{tde_datadir}/services/groupwise.protocol
%{tde_datadir}/services/groupwises.protocol
%{tde_datadir}/services/imap4.protocol
%{tde_datadir}/services/imaps.protocol
%{tde_datadir}/services/mbox.protocol
%{tde_datadir}/services/scalix.protocol
%{tde_datadir}/services/scalixs.protocol
%{tde_datadir}/services/sieve.protocol
%{tde_tdedocdir}/HTML/en/tdeioslave/groupwise/
%{tde_tdedocdir}/HTML/en/tdeioslave/mbox/
%{tde_tdedocdir}/HTML/en/tdeioslave/scalix/

##########

%package tderesources
Summary:	Trinity pim resource plugins
Group:		Environment/Libraries
#Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libcaldav
Requires:	libcarddav

Obsoletes:	tdepim-kresources < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdepim-kresources < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdepim-kresources = %{?epoch:%{epoch}:}%{version}-%{release}

%description tderesources
This package includes several plugins needed to interface with groupware
servers. It also includes plugins for features such as blogging and
tracking feature plans.

%files tderesources
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcal_caldav.la
%{tde_tdelibdir}/kcal_caldav.so
%{tde_tdelibdir}/kcal_groupdav.la
%{tde_tdelibdir}/kcal_groupdav.so
%{tde_tdelibdir}/kcal_groupwise.la
%{tde_tdelibdir}/kcal_groupwise.so
%{tde_tdelibdir}/kcal_kolab.la
%{tde_tdelibdir}/kcal_kolab.so
%{tde_tdelibdir}/kcal_scalix.la
%{tde_tdelibdir}/kcal_scalix.so
%{tde_tdelibdir}/kcal_newexchange.la
%{tde_tdelibdir}/kcal_newexchange.so
%{tde_tdelibdir}/kcal_resourcefeatureplan.la
%{tde_tdelibdir}/kcal_resourcefeatureplan.so
%{tde_tdelibdir}/kcal_slox.la
%{tde_tdelibdir}/kcal_slox.so
%{tde_tdelibdir}/kcal_xmlrpc.la
%{tde_tdelibdir}/kcal_xmlrpc.so
%{tde_tdelibdir}/knotes_kolab.la
%{tde_tdelibdir}/knotes_kolab.so
%{tde_tdelibdir}/knotes_scalix.la
%{tde_tdelibdir}/knotes_scalix.so
%{tde_tdelibdir}/knotes_xmlrpc.la
%{tde_tdelibdir}/knotes_xmlrpc.so
%{tde_libdir}/libtdeabckolab.so.*
%{tde_libdir}/libtdeabcscalix.so.*
%{tde_libdir}/libtdeabc_groupdav.so.*
%{tde_libdir}/libtdeabc_groupwise.so.*
%{tde_libdir}/libtdeabc_newexchange.so.*
%{tde_libdir}/libtdeabc_slox.so.*
%{tde_libdir}/libtdeabc_xmlrpc.so.*
%{tde_libdir}/libkcalkolab.so.*
%{tde_libdir}/libkcalscalix.so.*
%{tde_libdir}/libkcal_caldav.so.*
%{tde_libdir}/libtdeabc_carddav.so.*
%{tde_libdir}/libkcal_groupdav.so.*
%{tde_libdir}/libkcal_groupwise.so.*
%{tde_libdir}/libkcal_newexchange.so.*
%{tde_libdir}/libkcal_resourcefeatureplan.so.*
%{tde_libdir}/libkcal_slox.so.*
%{tde_libdir}/libkcal_xmlrpc.so.*
%{tde_libdir}/libkgroupwarebase.so.*
%{tde_libdir}/libkgroupwaredav.so.*
%{tde_libdir}/libknoteskolab.so.*
%{tde_libdir}/libknotesscalix.so.*
%{tde_libdir}/libknotes_xmlrpc.so.*
%{tde_libdir}/libkslox.so.*
%{tde_libdir}/libgwsoap.so.*
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_groupdav.desktop
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_groupwise.desktop
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_newexchange.desktop
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_opengroupware.desktop
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_ox.desktop
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_slox.desktop
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_xmlrpc.desktop
%{tde_datadir}/services/tderesources/tdeabc/kolab.desktop
%{tde_datadir}/services/tderesources/tdeabc/scalix.desktop
%dir %{tde_datadir}/services/tderesources/kcal
%{tde_datadir}/services/tderesources/kcal/exchange.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_caldav.desktop
%{tde_datadir}/services/tderesources/tdeabc/tdeabc_carddav.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_groupdav.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_groupwise.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_newexchange.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_opengroupware.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_ox.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_resourcefeatureplan.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_slox.desktop
%{tde_datadir}/services/tderesources/kcal/kcal_xmlrpc.desktop
%{tde_datadir}/services/tderesources/kcal/kolab.desktop
%{tde_datadir}/services/tderesources/kcal/scalix.desktop
%dir %{tde_datadir}/services/tderesources/knotes
%{tde_datadir}/services/tderesources/knotes/knotes_xmlrpc.desktop
%{tde_datadir}/services/tderesources/knotes/kolabresource.desktop
%{tde_datadir}/services/tderesources/knotes/scalix.desktop

%{tde_datadir}/apps/tdeconf_update/upgrade-resourcetype.pl
%{tde_datadir}/apps/tdeconf_update/kolab-resource.upd

%{tde_tdelibdir}/tdeabc_carddav.la
%{tde_tdelibdir}/tdeabc_carddav.so
%{tde_tdelibdir}/tdeabc_groupdav.la
%{tde_tdelibdir}/tdeabc_groupdav.so
%{tde_tdelibdir}/tdeabc_groupwise.la
%{tde_tdelibdir}/tdeabc_groupwise.so
%{tde_tdelibdir}/tdeabc_kolab.la
%{tde_tdelibdir}/tdeabc_kolab.so
%{tde_tdelibdir}/tdeabc_newexchange.la
%{tde_tdelibdir}/tdeabc_newexchange.so
%{tde_tdelibdir}/tdeabc_scalix.la
%{tde_tdelibdir}/tdeabc_scalix.so
%{tde_tdelibdir}/tdeabc_slox.la
%{tde_tdelibdir}/tdeabc_slox.so
%{tde_tdelibdir}/tdeabc_xmlrpc.la
%{tde_tdelibdir}/tdeabc_xmlrpc.so

##########

%package tderesources-devel
Summary:	Development files for tderesources
Group:		Development/Libraries/Other
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libcaldav
Requires:	libcarddav

Obsoletes:	tdepim-tderesources-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdepim-kresources-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdepim-kresources-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description tderesources-devel
%{summary}

%files tderesources-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkslox.la
%{tde_libdir}/libkslox.so
%{tde_libdir}/libtdeabc_groupdav.la
%{tde_libdir}/libtdeabc_groupdav.so
%{tde_libdir}/libtdeabc_groupwise.la
%{tde_libdir}/libtdeabc_groupwise.so
%{tde_libdir}/libgwsoap.la
%{tde_libdir}/libgwsoap.so
%{tde_libdir}/libtdeabc_carddav.la
%{tde_libdir}/libtdeabc_carddav.so
%{tde_libdir}/libtdeabc_newexchange.la
%{tde_libdir}/libtdeabc_newexchange.so
%{tde_libdir}/libtdeabc_slox.la
%{tde_libdir}/libtdeabc_slox.so
%{tde_libdir}/libtdeabc_xmlrpc.la
%{tde_libdir}/libtdeabc_xmlrpc.so
%{tde_libdir}/libtdeabckolab.la
%{tde_libdir}/libtdeabckolab.so
%{tde_libdir}/libtdeabcscalix.la
%{tde_libdir}/libtdeabcscalix.so
%{tde_libdir}/libkcal_caldav.la
%{tde_libdir}/libkcal_caldav.so
%{tde_libdir}/libkcal_groupdav.la
%{tde_libdir}/libkcal_groupdav.so
%{tde_libdir}/libkcal_groupwise.la
%{tde_libdir}/libkcal_groupwise.so
%{tde_libdir}/libkcal_newexchange.la
%{tde_libdir}/libkcal_newexchange.so
%{tde_libdir}/libkcal_resourcefeatureplan.la
%{tde_libdir}/libkcal_resourcefeatureplan.so
%{tde_libdir}/libkcal_slox.la
%{tde_libdir}/libkcal_slox.so
%{tde_libdir}/libkcal_xmlrpc.la
%{tde_libdir}/libkcal_xmlrpc.so
%{tde_libdir}/libkcalkolab.la
%{tde_libdir}/libkcalkolab.so
%{tde_libdir}/libkcalscalix.la
%{tde_libdir}/libkcalscalix.so
%{tde_libdir}/libkgroupwarebase.la
%{tde_libdir}/libkgroupwarebase.so
%{tde_libdir}/libkgroupwaredav.la
%{tde_libdir}/libkgroupwaredav.so
%{tde_libdir}/libknotes_xmlrpc.la
%{tde_libdir}/libknotes_xmlrpc.so
%{tde_libdir}/libknoteskolab.la
%{tde_libdir}/libknoteskolab.so
%{tde_libdir}/libknotesscalix.la
%{tde_libdir}/libknotesscalix.so
%{tde_tdeincludedir}/kpimprefs.h

##########

%package wizards
Summary:	Trinity server configuration wizards
Group:		Applications/Communications

Obsoletes:	tdepim-wizards < %{?epoch:%{epoch}:}%{version}-%{release}

%description wizards
This package contains TDE-based wizards for configuring eGroupware,
Kolab, and SUSE Linux Openexchange servers.

%files wizards
%defattr(-,root,root,-)
%{tde_bindir}/egroupwarewizard
%{tde_bindir}/exchangewizard
%{tde_bindir}/groupwarewizard
%{tde_bindir}/groupwisewizard
%{tde_bindir}/kolabwizard
%{tde_bindir}/scalixadmin
%{tde_bindir}/scalixwizard
%{tde_bindir}/sloxwizard
%{tde_tdelibdir}/libegroupwarewizard.la
%{tde_tdelibdir}/libegroupwarewizard.so
%{tde_tdelibdir}/libexchangewizard.la
%{tde_tdelibdir}/libexchangewizard.so
%{tde_tdelibdir}/libgroupwisewizard.la
%{tde_tdelibdir}/libgroupwisewizard.so
%{tde_tdelibdir}/libkolabwizard.la
%{tde_tdelibdir}/libkolabwizard.so
%{tde_tdelibdir}/libscalixwizard.la
%{tde_tdelibdir}/libscalixwizard.so
%{tde_tdelibdir}/libsloxwizard.la
%{tde_tdelibdir}/libsloxwizard.so
%{tde_tdeappdir}/groupwarewizard.desktop
%{tde_datadir}/config.kcfg/egroupware.kcfg
%{tde_datadir}/config.kcfg/groupwise.kcfg
%{tde_datadir}/config.kcfg/kolab.kcfg
%{tde_datadir}/config.kcfg/scalix.kcfg
%{tde_datadir}/config.kcfg/slox.kcfg

##########

%if 0%{?with_kitchensync}
%package -n trinity-kitchensync
Summary:	Synchronization framework
Group:		Applications/Communications
BuildRequires:	opensync-devel
#Suggests: konqueror-trinity
#Conflicts: kdebluetooth-irmcsync-trinity (<< 0.99+1.0beta2-4.1), ksync-trinity

%description -n trinity-kitchensync
This package contains a synchronization framework, still under heavy
development (?).  Kitchensync uses opensync.

%files -n trinity-kitchensync
%defattr(-,root,root,-)
%{tde_bindir}/kitchensync
%{tde_tdelibdir}/libkitchensyncpart.la
%{tde_tdelibdir}/libkitchensyncpart.so
%{tde_datadir}/apps/kitchensync
%{tde_libdir}/libkitchensync.so.*
%{tde_libdir}/libqopensync.so.*
%{tde_tdeappdir}/kitchensync.desktop
%{tde_datadir}/icons/hicolor/*/apps/kitchensync.png
%endif

##########

%package -n trinity-kleopatra
Summary:	Trinity Certificate Manager
Group:		Applications/Communications

# GPG support
%if 0%{?suse_version}
Requires:	gpg2
%endif
%if 0%{?rhel} == 4
Requires:	gnupg
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
Requires:	gnupg2
%endif

%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
Requires:	pinentry
%if 0%{?mdkver}
Requires:	gnupg
%else
Requires:	dirmngr
%endif
%endif

%description -n trinity-kleopatra
Kleopatra is the TDE tool for managing X.509 certificates in the gpgsm
keybox and for retrieving certificates from LDAP servers.

%files -n trinity-kleopatra
%defattr(-,root,root,-)
%{tde_bindir}/kleopatra
%{tde_bindir}/kwatchgnupg
%{tde_tdelibdir}/kcm_kleopatra.la
%{tde_tdelibdir}/kcm_kleopatra.so
%{tde_tdeappdir}/kleopatra_import.desktop
%{tde_datadir}/apps/kleopatra
%{tde_datadir}/apps/kwatchgnupg
%{tde_datadir}/services/kleopatra_config_*.desktop
%{tde_tdeappdir}/kleopatra.desktop
%{tde_tdedocdir}/HTML/en/kleopatra/
%{tde_tdedocdir}/HTML/en/kwatchgnupg/
%{tde_datadir}/icons/hicolor/*/apps/kleopatra.png
%{tde_datadir}/icons/hicolor/scalable/apps/kleopatra.svgz

##########

%package -n trinity-kmail
Summary:	Trinity Email client
Group:		Applications/Communications
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdebase-tdeio-pim-plugins >= %{tde_version}

# GPG support
%if 0%{?suse_version}
Requires:	gpg2
%endif
%if 0%{?rhel} == 4
Requires:	gnupg
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
Requires:	gnupg2
%endif

# Pinentry
%if 0%{?suse_version} || 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
Requires:	pinentry
%endif

Requires:	procmail
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdebase-tdeio-pim-plugins >= %{tde_version}

Provides: imap-client, mail-reader

%description -n trinity-kmail
KMail is a fully-featured email client that fits nicely into the TDE
desktop. It has features such as support for IMAP, POP3, multiple accounts,
mail filtering and sorting, PGP/GnuPG privacy, and inline attachments.

You need to install %{name}-tdeio-plugins if you want to use IMAP or
mbox files, and/or trinity-tdebase-tdeio-plugins if you want to use POP3.

%files -n trinity-kmail
%defattr(-,root,root,-)
%config(noreplace) %{tde_confdir}/kmail.antispamrc
%config(noreplace) %{tde_confdir}/kmail.antivirusrc
%{tde_bindir}/kmail
%{tde_bindir}/kmail_*.sh
%{tde_tdelibdir}/kcm_kmail.la
%{tde_tdelibdir}/kcm_kmail.so
%{tde_tdelibdir}/libkmail_bodypartformatter_application_octetstream.la
%{tde_tdelibdir}/libkmail_bodypartformatter_application_octetstream.so
%{tde_tdelibdir}/libkmail_bodypartformatter_text_calendar.la
%{tde_tdelibdir}/libkmail_bodypartformatter_text_calendar.so
%{tde_tdelibdir}/libkmail_bodypartformatter_text_vcard.la
%{tde_tdelibdir}/libkmail_bodypartformatter_text_vcard.so
%{tde_tdelibdir}/libkmail_bodypartformatter_text_xdiff.la
%{tde_tdelibdir}/libkmail_bodypartformatter_text_xdiff.so
%{tde_tdelibdir}/libkmailpart.la
%{tde_tdelibdir}/libkmailpart.so
%{tde_tdeappdir}/KMail.desktop
%{tde_tdeappdir}/kmail_view.desktop
%{tde_datadir}/apps/tdeconf_update/kmail-3.1-update-new-mail-notification-settings.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.1-use-UOID-for-identities.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.1.4-dont-use-UOID-0-for-any-identity.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.2-misc.sh
%{tde_datadir}/apps/tdeconf_update/kmail-3.2-update-loop-on-goto-unread-settings.sh
%{tde_datadir}/apps/tdeconf_update/kmail-3.3-aegypten.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.3-misc.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.3-move-identities.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.3-split-sign-encr-keys.sh
%{tde_datadir}/apps/tdeconf_update/kmail-3.3-use-ID-for-accounts.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.3b1-misc.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.4-misc.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.4.1-update-status-filters.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.5-trigger-flag-migration.pl
%{tde_datadir}/apps/tdeconf_update/kmail-3.5-filter-icons.pl
%{tde_datadir}/apps/tdeconf_update/kmail-pgpidentity.pl
%{tde_datadir}/apps/tdeconf_update/kmail-upd-identities.pl
%{tde_datadir}/apps/tdeconf_update/kmail.upd
%{tde_datadir}/apps/tdeconf_update/upgrade-signature.pl
%{tde_datadir}/apps/tdeconf_update/upgrade-transport.pl
%{tde_datadir}/apps/kmail
%{tde_datadir}/apps/konqueror/servicemenus/email.desktop
%{tde_datadir}/config.kcfg/custommimeheader.kcfg
%{tde_datadir}/config.kcfg/kmail.kcfg
%{tde_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{tde_datadir}/config.kcfg/replyphrases.kcfg
%{tde_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/kmaillight.png
%{tde_datadir}/icons/hicolor/*/apps/kmail.png
%{tde_datadir}/icons/hicolor/scalable/apps/kmail.svgz
%{tde_datadir}/services/kmail_config_*.desktop
%{tde_datadir}/services/kontact/kmailplugin.desktop
%{tde_datadir}/servicetypes/dcopimap.desktop
%{tde_datadir}/servicetypes/dcopmail.desktop
# 'libkmailprivate.so' is required at runtime, not devel !
%{tde_libdir}/libkmailprivate.so
%{tde_libdir}/libkmailprivate.la
%{tde_tdedocdir}/HTML/en/kmail/

##########

%package -n trinity-kmail-devel
Summary:	Development files for kmail
Group:		Development/Libraries/Other

%description -n trinity-kmail-devel
%{summary}

%files -n trinity-kmail-devel
%defattr(-,root,root,-)
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kmail/
%{tde_tdeincludedir}/kmail*.h

##########
 
%package -n trinity-kmailcvt
Summary:	Trinity KMail mail folder converter
Group:		Applications/Communications
Requires:	trinity-kmail = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kmailcvt
Converts mail folders to KMail format.  Formats supported for import
include Outlook Express, Evolution, and plain mbox.

%files -n trinity-kmailcvt
%defattr(-,root,root,-)
%{tde_bindir}/kmailcvt
%{tde_datadir}/applnk/Utilities/kmailcvt.desktop
%{tde_datadir}/apps/kmailcvt
%{tde_datadir}/icons/crystalsvg/*/apps/kmailcvt.png

##########

%package -n trinity-knode
Summary:	Trinity news reader
Group:		Applications/Internet

%description -n trinity-knode
KNode is an easy-to-use, convenient newsreader. It is intended to be usable
by inexperienced users, but also includes support for such features as
MIME attachments, article scoring, and creating and verifying GnuPG
signatures.

%files -n trinity-knode
%defattr(-,root,root,-)
%{tde_bindir}/knode
%{tde_tdelibdir}/kcm_knode.la
%{tde_tdelibdir}/kcm_knode.so
%{tde_tdelibdir}/libknodepart.la
%{tde_tdelibdir}/libknodepart.so
%{tde_libdir}/libknodecommon.so.*
%{tde_tdeappdir}/KNode.desktop
%{tde_datadir}/apps/knode/
%{tde_datadir}/icons/hicolor/*/apps/knode.png
%{tde_datadir}/icons/hicolor/*/apps/knode2.png
%{tde_datadir}/services/knewsservice.protocol
%{tde_datadir}/services/knode_config_*.desktop
%{tde_datadir}/services/kontact/knodeplugin.desktop
%{tde_tdedocdir}/HTML/en/knode/

##########

%package -n trinity-knode-devel
Summary:	Development files for trinity-knode
Group:		Development/Libraries/Other
Requires:	trinity-knode = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-knode-devel
%{summary}

%files -n trinity-knode-devel
%defattr(-,root,root,-)
%{tde_libdir}/libknodecommon.la
%{tde_libdir}/libknodecommon.so

##########

%package -n trinity-knotes
Summary:	Trinity sticky notes
Group:		Applications/Utilities
Requires:	trinity-tdepim-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-knotes
KNotes is a program that lets you write sticky notes. The notes are saved
automatically when you exit the program, and they display when you open the
program.  The program supports printing and mailing your notes.

%files -n trinity-knotes
%defattr(-,root,root,-)
%{tde_bindir}/knotes
%{tde_tdelibdir}/knotes_local.la
%{tde_tdelibdir}/knotes_local.so
%{tde_libdir}/libknotes.so.*
%{tde_tdeappdir}/knotes.desktop
%{tde_datadir}/apps/knotes/
%{tde_datadir}/config.kcfg/knoteconfig.kcfg
%{tde_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{tde_datadir}/icons/hicolor/*/apps/knotes.png
%{tde_datadir}/services/tderesources/knotes/imap.desktop
%{tde_datadir}/services/tderesources/knotes/local.desktop
%{tde_datadir}/services/tderesources/knotes_manager.desktop
%{tde_datadir}/services/kontact/knotesplugin.desktop
%{tde_tdedocdir}/HTML/en/knotes/

##########

%package -n trinity-knotes-devel
Summary:	Development files for knots
Group:		Development/Libraries/Other
Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-knotes-devel
%{summary}

%files -n trinity-knotes-devel
%defattr(-,root,root,-)
%{tde_libdir}/libknotes.so
%{tde_libdir}/libknotes.la
%{tde_tdeincludedir}/KNotesAppIface.h
%{tde_tdeincludedir}/KNotesIface.h

##########

%package -n trinity-kode
Summary:	Helper library for programmatic generation of C++ code
Group:		Development/Libraries

%description -n trinity-kode
This package includes a program kode for generation of C++ template files
and kxml_compiler for generation of C++ classes representing XML data
described by RelaxNG schemes.

%files -n trinity-kode
%defattr(-,root,root,-)
%{tde_bindir}/kode
%{tde_bindir}/kxml_compiler
%{tde_libdir}/libkode.so.*

##########

%package -n trinity-kode-devel
Summary:	Development files for trinity-kode
Group:		Development/Libraries/Other
Requires:	trinity-kode = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kode-devel
%{summary}

%files -n trinity-kode-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkode.la
%{tde_libdir}/libkode.so

##########

%package -n trinity-konsolekalendar
Summary:	Trinity konsole personal organizer
Group:		Applications/Productivity

%description -n trinity-konsolekalendar
KonsoleKalendar is a command-line interface to TDE calendars.
Konsolekalendar complements the TDE KOrganizer by providing a console
frontend to manage your calendars.

%files -n trinity-konsolekalendar
%defattr(-,root,root,-)
%{tde_bindir}/konsolekalendar
%{tde_tdeappdir}/konsolekalendar.desktop
%{tde_datadir}/icons/crystalsvg/*/apps/konsolekalendar.png
%{tde_tdedocdir}/HTML/en/konsolekalendar/

##########

%package -n trinity-kontact
Summary:	Trinity pim application
Group:		Applications/Communications
Requires:	trinity-kmail = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knode = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-akregator = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kontact
Kontact is the integrated solution to your personal information management
needs. It combines TDE applications like KMail, KOrganizer, and
KAddressBook into a single interface to provide easy access to mail,
scheduling, address book and other PIM functionality.

%files -n trinity-kontact
%defattr(-,root,root,-)
%{tde_bindir}/kontact
%{tde_tdelibdir}/kcm_kmailsummary.la
%{tde_tdelibdir}/kcm_kmailsummary.so
%{tde_tdelibdir}/kcm_kontact.la
%{tde_tdelibdir}/kcm_kontact.so
%{tde_tdelibdir}/kcm_kontactknt.la
%{tde_tdelibdir}/kcm_kontactknt.so
%{tde_tdelibdir}/kcm_kontactsummary.la
%{tde_tdelibdir}/kcm_kontactsummary.so
%{tde_tdelibdir}/kcm_korgsummary.la
%{tde_tdelibdir}/kcm_korgsummary.so
%{tde_tdelibdir}/kcm_sdsummary.la
%{tde_tdelibdir}/kcm_sdsummary.so
%{tde_tdelibdir}/libkontact_*.la
%{tde_tdelibdir}/libkontact_*.so
%{tde_libdir}/libkontact.so.*
%{tde_libdir}/libkpinterfaces.so.*
%{tde_tdeappdir}/Kontact.desktop
%{tde_tdeappdir}/kontactdcop.desktop
%{tde_datadir}/apps/kontact/
%{tde_datadir}/apps/kontactsummary/
%{tde_datadir}/config.kcfg/kontact.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kontact.png
%{tde_datadir}/icons/crystalsvg/*/actions/kontact_*.png
%{tde_datadir}/services/kcmkmailsummary.desktop
%{tde_datadir}/services/kcmkontactknt.desktop
%{tde_datadir}/services/kcmkontactsummary.desktop
%{tde_datadir}/services/kcmkorgsummary.desktop
%{tde_datadir}/services/kcmsdsummary.desktop
%dir %{tde_datadir}/services/kontact
%{tde_datadir}/services/kontact/newstickerplugin.desktop
%{tde_datadir}/services/kontact/specialdatesplugin.desktop
%{tde_datadir}/services/kontact/summaryplugin.desktop
%{tde_datadir}/services/kontact/weatherplugin.desktop
%{tde_datadir}/services/kontactconfig.desktop
%{tde_datadir}/servicetypes/kontactplugin.desktop
%{tde_tdedocdir}/HTML/en/kontact/

##########

%package -n trinity-kontact-devel
Summary:	Development files for kontact
Group:		Development/Libraries/Other
Requires:	trinity-kontact = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kontact-devel
%{summary}

%files -n trinity-kontact-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkontact.la
%{tde_libdir}/libkontact.so
%{tde_libdir}/libkpinterfaces.la
%{tde_libdir}/libkpinterfaces.so
%{tde_tdeincludedir}/kontact/

##########

%package -n trinity-korganizer
Summary:	Trinity personal organizer
Group:		Applications/Productivity
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimexchange = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	perl

%description -n trinity-korganizer
This package contains KOrganizer, a calendar and scheduling program.

KOrganizer aims to be a complete program for organizing appointments,
contacts, projects, etc. KOrganizer natively supports information interchange
with other calendar applications, through the industry standard vCalendar
personal data interchange file format. This eases the move from other
modern PIMs to KOrganizer.

KOrganizer offers full synchronization with Palm Pilots, if kpilot is
installed.

%files -n trinity-korganizer
%defattr(-,root,root,-)
%{tde_bindir}/ical2vcal
%{tde_bindir}/korgac
%{tde_bindir}/korganizer
%{tde_tdelibdir}/kcm_korganizer.la
%{tde_tdelibdir}/kcm_korganizer.so
%{tde_tdelibdir}/libkorg_*.la
%{tde_tdelibdir}/libkorg_*.so
%{tde_tdelibdir}/libkorganizerpart.la
%{tde_tdelibdir}/libkorganizerpart.so
%{tde_libdir}/libkocorehelper.so.*
%{tde_libdir}/libkorg_stdprinting.so.*
%{tde_libdir}/libkorganizer.so.*
%{tde_libdir}/libkorganizer_calendar.so.*
%{tde_libdir}/libkorganizer_eventviewer.so.*
%{tde_tdeappdir}/korganizer.desktop
%{tde_datadir}/apps/tdeconf_update/korganizer.upd
%{tde_datadir}/apps/korgac/
%{tde_datadir}/apps/korganizer/
%{tde_datadir}/autostart/korgac.desktop
%{tde_datadir}/config.kcfg/korganizer.kcfg
%{tde_datadir}/icons/hicolor/*/apps/korganizer.png
%dir %{tde_datadir}/services/kontact
%{tde_datadir}/services/kontact/korganizerplugin.desktop
%{tde_datadir}/services/kontact/journalplugin.desktop
%{tde_datadir}/services/kontact/todoplugin.desktop
%{tde_datadir}/services/korganizer_*.desktop
%{tde_datadir}/services/korganizer
%{tde_datadir}/services/webcal.protocol
%{tde_datadir}/servicetypes/calendardecoration.desktop
%{tde_datadir}/servicetypes/calendarplugin.desktop
%{tde_datadir}/servicetypes/dcopcalendar.desktop
%{tde_datadir}/servicetypes/korganizerpart.desktop
%{tde_datadir}/servicetypes/korgprintplugin.desktop
%{tde_tdedocdir}/HTML/en/korganizer/
%{tde_tdedocdir}/HTML/en/tdeioslave/webcal/

##########

%package -n trinity-korganizer-devel
Summary:	Development files for korganizer
Group:		Development/Libraries/Other
Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-korganizer-devel
%{summary}

%files -n trinity-korganizer-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/korganizer/
%{tde_tdeincludedir}/calendar/
%{tde_libdir}/libkocorehelper.la
%{tde_libdir}/libkocorehelper.so
%{tde_libdir}/libkorg_stdprinting.la
%{tde_libdir}/libkorg_stdprinting.so
%{tde_libdir}/libkorganizer.la
%{tde_libdir}/libkorganizer.so
%{tde_libdir}/libkorganizer_calendar.la
%{tde_libdir}/libkorganizer_calendar.so
%{tde_libdir}/libkorganizer_eventviewer.la
%{tde_libdir}/libkorganizer_eventviewer.so

##########

%package -n trinity-korn
Summary:	Trinity mail checker
Group:		Applications/Communications
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-korn
Korn is a TDE mail checker that can display a small summary in the Kicker
tray.  It supports checking mbox, pop3, imap4, and nntp sources.

Once mail is received you can have Korn run a third party program or change
the color/icon of the Kicker display.  In addition to this you can have
Korn run a program once you click on the docked icon in Kicker.

%files -n trinity-korn
%defattr(-,root,root,-)
%{tde_bindir}/korn
%{tde_libdir}/tdeconf_update_bin/korn-3-4-config_change
%{tde_tdeappdir}/KOrn.desktop
%{tde_datadir}/apps/tdeconf_update/korn-3-4-config_change.upd
%{tde_datadir}/apps/tdeconf_update/korn-3-5-metadata-update.pl
%{tde_datadir}/apps/tdeconf_update/korn-3-5-ssl-update.pl
%{tde_datadir}/apps/tdeconf_update/korn-3-5-update.upd
%{tde_datadir}/icons/hicolor/*/apps/korn.png
%{tde_tdedocdir}/HTML/en/korn/

##########

%package -n trinity-ktnef
Summary:	Trinity TNEF viewer
Group:		Applications/Communications

%description -n trinity-ktnef
The TNEF File Viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n trinity-ktnef
%defattr(-,root,root,-)
%{tde_bindir}/ktnef
%{tde_tdeappdir}/ktnef.desktop
%{tde_datadir}/apps/ktnef
%{tde_datadir}/icons/hicolor/*/apps/ktnef.png
%{tde_datadir}/icons/locolor/*/apps/ktnef.png
%{tde_datadir}/mimelnk/application/ms-tnef.desktop
%{tde_tdedocdir}/HTML/en/ktnef/

##########

%package -n trinity-libindex
Summary:	Trinity indexing library
Group:		Environment/Libraries

%description -n trinity-libindex
This library provides text indexing and is currently used by KMail
to implement fast searches in mail bodies.

This is the runtime package for programs that use the libindex library.

%files -n trinity-libindex
%defattr(-,root,root,-)
%{tde_libdir}/libindex.so.*

##########

%package -n trinity-libindex-devel
Summary:	Trinity indexing library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libindex = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libindex-devel
This library provides text indexing and is currently used by KMail
to implement searching through mail text.

This is the development package which contains the headers for the libindex-trinity
library.

%files -n trinity-libindex-devel
%defattr(-,root,root,-)
%{tde_bindir}/indexlib-config
%{tde_tdeincludedir}/index
%{tde_libdir}/libindex.la
%{tde_libdir}/libindex.so

##########

%package -n trinity-libkcal
Summary:	Trinity calendaring library
Group:		Environment/Libraries
#Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkmime = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkcal
This library provides a C++ API for handling the vCalendar and iCalendar
formats.

This is the runtime package for programs that use the libkcal-trinity library.

%files -n trinity-libkcal
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcal_tdeabc.la
%{tde_tdelibdir}/kcal_tdeabc.so
%{tde_tdelibdir}/kcal_localdir.la
%{tde_tdelibdir}/kcal_localdir.so
%{tde_tdelibdir}/kcal_local.la
%{tde_tdelibdir}/kcal_local.so
%{tde_tdelibdir}/kcal_remote.la
%{tde_tdelibdir}/kcal_remote.so
%{tde_libdir}/libkcal.so.*
%{tde_libdir}/libkcal_resourceremote.so.*
%{tde_libdir}/libkholidays.so.*
%{tde_datadir}/apps/libkholidays/
%dir %{tde_datadir}/services/tderesources/kcal
%{tde_datadir}/services/tderesources/kcal/imap.desktop
%{tde_datadir}/services/tderesources/kcal/tdeabc.desktop
%{tde_datadir}/services/tderesources/kcal/local.desktop
%{tde_datadir}/services/tderesources/kcal/localdir.desktop
%{tde_datadir}/services/tderesources/kcal/remote.desktop
%{tde_datadir}/services/tderesources/kcal_manager.desktop

##########

%package -n trinity-libkcal-devel
Summary:	Trinity calendaring library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkcal-devel
This library provides a C++ API for handling the vCalendar and iCalendar
formats.

This is the development package which contains the headers for the libkcal-trinity
library.

%files -n trinity-libkcal-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/libemailfunctions/
%{tde_tdeincludedir}/libkcal
%{tde_libdir}/libkcal.la
%{tde_libdir}/libkcal.so
%{tde_libdir}/libkcal_resourceremote.la
%{tde_libdir}/libkcal_resourceremote.so
%{tde_libdir}/libkholidays.la
%{tde_libdir}/libkholidays.so

##########

%package -n trinity-libtdepim
Summary:	Trinity PIM library
Group:		Environment/Libraries
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	libtdepim < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtdepim
This is the runtime package for programs that use the trinity-libtdepim library.

%files -n trinity-libtdepim
%defattr(-,root,root,-)
%{tde_tdelibdir}/plugins/designer/tdepimwidgets.la
%{tde_tdelibdir}/plugins/designer/tdepimwidgets.so
%{tde_tdelibdir}/plugins/designer/tdepartsdesignerplugin.la
%{tde_tdelibdir}/plugins/designer/tdepartsdesignerplugin.so
%{tde_libdir}/libtdepim.so.*
%{tde_datadir}/apps/tdepimwidgets
%{tde_datadir}/apps/libtdepim
%{tde_datadir}/apps/tdepim
%{tde_datadir}/config.kcfg/pimemoticons.kcfg
%{tde_datadir}/icons/crystalsvg/22x22/actions/button_fewer.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/button_more.png

##########

%package -n trinity-libtdepim-devel
Summary:	Trinity PIM library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdelibs-devel >= %{version}

Obsoletes:	libtdepim-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtdepim-devel
This is the development package which contains the headers for the libtdepim-trinity
library.

%files -n trinity-libtdepim-devel
%defattr(-,root,root,-)
%{tde_libdir}/libtdepim.la
%{tde_libdir}/libtdepim.so

##########

%package -n trinity-libkgantt
Summary:	Trinity gantt charting library
Group:		Environment/Libraries

%description -n trinity-libkgantt
This is the runtime package for programs that use the libkgantt-trinity library.

%files -n trinity-libkgantt
%defattr(-,root,root,-)
%{tde_libdir}/libkgantt.so.*
%{tde_datadir}/apps/kgantt

##########

%package -n trinity-libkgantt-devel
Summary:	Trinity gantt charting library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkgantt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkgantt-devel
This is the development package which contains the headers for the libkgantt-trinity
library.

%files -n trinity-libkgantt-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kgantt
%{tde_libdir}/libkgantt.la
%{tde_libdir}/libkgantt.so

##########

%package -n trinity-libkleopatra
Summary:	TDE GnuPG interface libraries
Group:		Environment/Libraries
Requires:	gnupg

%description -n trinity-libkleopatra
This library is used by several TDE applications to interface to the
GnuPG program.

This is the runtime package for programs that use the libkleopatra-trinity library.

%files -n trinity-libkleopatra
%defattr(-,root,root,-)
%config(noreplace) %{tde_confdir}/libkleopatrarc
%{tde_libdir}/libgpgme++.so.*
%{tde_libdir}/libkleopatra.so.*
%{tde_libdir}/libkpgp.so.*
%{tde_libdir}/libqgpgme.so.*
%{tde_datadir}/apps/tdeconf_update/kpgp-3.1-upgrade-address-data.pl
%{tde_datadir}/apps/tdeconf_update/kpgp.upd
%{tde_datadir}/apps/libkleopatra/
%{tde_datadir}/icons/crystalsvg/*/apps/dirmngr.png
%{tde_datadir}/icons/crystalsvg/*/apps/gpg.png
%{tde_datadir}/icons/crystalsvg/*/apps/gpg_agent.png
%{tde_datadir}/icons/crystalsvg/*/apps/gpgsm.png
%{tde_datadir}/icons/crystalsvg/*/apps/pinentry.png
%{tde_datadir}/icons/crystalsvg/*/apps/scdaemon.png

##########

%package -n trinity-libkleopatra-devel
Summary:	Trinity GnuPG interface libraries [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkleopatra-devel
This library is used by several TDE applications to interface to the
GnuPG program.

This is the development package which contains the headers for the
libkleopatra-trinity library.

%files -n trinity-libkleopatra-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/gpgme++/
%{tde_tdeincludedir}/kleo/
%{tde_tdeincludedir}/qgpgme/
%{tde_libdir}/libgpgme++.la
%{tde_libdir}/libgpgme++.so
%{tde_libdir}/libkleopatra.la
%{tde_libdir}/libkleopatra.so
%{tde_libdir}/libkpgp.la
%{tde_libdir}/libkpgp.so
%{tde_libdir}/libqgpgme.la
%{tde_libdir}/libqgpgme.so

##########

%package -n trinity-libkmime
Summary:	Trinity MIME interface library
Group:		Environment/Libraries
#Conflicts:	trinity-libmimelib

%description -n trinity-libkmime
This library provides a C++ interface to MIME messages, parsing them into
an object tree.

%files -n trinity-libkmime
%defattr(-,root,root,-)
%{tde_libdir}/libkmime.so.*

##########

%package -n trinity-libkmime-devel
Summary:	Development files for libkmime
Group:		Development/Libraries/Other
Requires:	trinity-libkmime = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkmime-devel
%{summary}

%files -n trinity-libkmime-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkmime.la
%{tde_libdir}/libkmime.so

##########

%package -n trinity-libkpimexchange
Summary:	Trinity PIM Exchange library
Group:		Development/Libraries/Other

%description -n trinity-libkpimexchange
This is the runtime package for programs that use the libkpimexchange-trinity
library. 

%files -n trinity-libkpimexchange
%defattr(-,root,root,-)
%{tde_tdelibdir}/resourcecalendarexchange.la
%{tde_tdelibdir}/resourcecalendarexchange.so
%{tde_libdir}/libkpimexchange.so.*

##########

%package -n trinity-libkpimexchange-devel
Summary:	Trinity PIM Exchange library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkpimexchange = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkpimexchange-devel
This is the development package which contains the headers for the
libkpimexchange-trinity library.

%files -n trinity-libkpimexchange-devel
%defattr(-,root,root,-)
%dir %{tde_tdeincludedir}/tdepim
%{tde_tdeincludedir}/tdepim/exchangeaccount.h
%{tde_tdeincludedir}/tdepim/exchangeclient.h
%{tde_libdir}/libkpimexchange.la
%{tde_libdir}/libkpimexchange.so

##########

%package -n trinity-libkpimidentities
Summary:	Trinity PIM user identity information library
Group:		Environment/Libraries

%description -n trinity-libkpimidentities
This library provides information to TDE programs about user identity,
such as email address, organization, etc.

This is the runtime package for programs that use the libkpimidentities-trinity
library.

%files -n trinity-libkpimidentities
%defattr(-,root,root,-)
%{tde_libdir}/libkpimidentities.so.*

##########

%package -n trinity-libkpimidentities-devel
Summary:	Development files for libkpimidentities
Group:		Development/Libraries/Other
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkpimidentities-devel
%{summary}

%files -n trinity-libkpimidentities-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkpimidentities.la
%{tde_libdir}/libkpimidentities.so

##########

%package -n trinity-libksieve
Summary:	Trinity mail/news message filtering library
Group:		Environment/Libraries

%description -n trinity-libksieve
This is the runtime package for programs that use the libksieve-trinity library.

%files -n trinity-libksieve
%defattr(-,root,root,-)
%{tde_libdir}/libksieve.so.*
%{tde_tdedocdir}/HTML/en/tdeioslave/sieve/

##########

%package -n trinity-libksieve-devel
Summary:	Trinity mail/news message filtering library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libksieve = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libksieve-devel
This is the development package which contains the headers for the libksieve-trinity
library.

%files -n trinity-libksieve-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/ksieve
%{tde_libdir}/libksieve.la
%{tde_libdir}/libksieve.so

##########

%package -n trinity-libktnef
Summary:	Library for handling KTNEF email attachments
Group:		Environment/Libraries

%description -n trinity-libktnef
This library handles mail attachments using the TNEF format. These
attachments are usually found in mails coming from Microsoft mail
servers and embed the mail properties as well as the actual
attachments.
.
This is the runtime library for packages using the ktnef-trinity library.

%files -n trinity-libktnef
%defattr(-,root,root,-)
%{tde_libdir}/libktnef.so.*

##########

%package -n trinity-libktnef-devel
Summary:	KTNEF handler library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libktnef = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libktnef-devel
This library handles mail attachments using the TNEF format. These
attachments are usually found in mails coming from Microsoft mail
servers and embed the mail properties as well as the actual
attachments.

This is the development package which contains the headers for the
ktnef-trinity library.

%files -n trinity-libktnef-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/ktnef
%{tde_libdir}/libktnef.la
%{tde_libdir}/libktnef.so

##########

%package -n trinity-libmimelib
Summary:	Trinity mime library
Group:		Environment/Libraries

%description -n trinity-libmimelib
This library is used by several Trinity applications to handle mime types.

This is the runtime package for programs that use the libmimelib-trinity library.

%files -n trinity-libmimelib
%defattr(-,root,root,-)
%{tde_libdir}/libmimelib.so.*

##########

%package -n trinity-libmimelib-devel
Summary:	Trinity mime library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libmimelib = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libmimelib-devel
This library is used by several TDE applications to handle mime types.

This is the development package which contains the headers for the
libmimelib library.

%files -n trinity-libmimelib-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/mimelib/
%{tde_libdir}/libmimelib.la
%{tde_libdir}/libmimelib.so

##########

%package -n trinity-kmobile
Summary:	Synchronize and manage mobile phone with your PC.
Group:		Applications/Communications

%description -n trinity-kmobile
KMobileTools is a nice TDE-based application that allows to synchronize 
and manage mobile phones with your PC. It handles full SMS control, 
dialing calls, phonebook, and phone status monitoring.

%files -n trinity-kmobile
%defattr(-,root,root,-)
%{tde_bindir}/kmobile
%{tde_datadir}/icons/default.tde/32x32/devices/mobile_camera.png
%{tde_datadir}/icons/default.tde/32x32/devices/mobile_musicplayer.png
%{tde_datadir}/icons/default.tde/32x32/devices/mobile_organizer.png
%{tde_datadir}/icons/default.tde/32x32/devices/mobile_phone.png
%{tde_datadir}/icons/default.tde/32x32/devices/mobile_unknown.png
%{tde_datadir}/icons/hicolor/*/apps/kmobile.png
%{tde_datadir}/services/libkmobile_digicam.desktop
%{tde_datadir}/services/libkmobile_gammu.desktop
%{tde_datadir}/services/libkmobile_skeleton.desktop
%{tde_datadir}/servicetypes/libkmobile.desktop
%{tde_datadir}/apps/kmobile/
%{tde_tdeappdir}/kmobile.desktop
%{tde_tdelibdir}/libkmobile_skeleton.la
%{tde_tdelibdir}/libkmobile_skeleton.so
%{tde_libdir}/libkmobileclient.la
%{tde_libdir}/libkmobileclient.so
%{tde_libdir}/libkmobiledevice.la
%{tde_libdir}/libkmobiledevice.so
%{tde_tdedocdir}/HTML/en/kmobile/

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

# Fix 'ical2vcal' contains '/bin/perl' instead of '/usr/bin/perl'
if [ -x /usr/bin/perl ]; then
  %__sed -i "korganizer/ical2vcal.in" -e "s|@PERL@|/usr/bin/perl|"
fi


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Specific path for RHEL4
if [ -d "/usr/X11R6" ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes FTBFS [Bug #1285]
%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DCMAKE_PROGRAM_PATH="%{tde_bindir}" \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DWITH_ARTS=ON \
  -DWITH_SASL=ON \
  -DWITH_NEWDISTRLISTS=ON  \
  %{?with_gnokii:-DWITH_GNOKII=ON} \
  -DWITH_EXCHANGE=ON \
  -DWITH_EGROUPWARE=ON \
  -DWITH_KOLAB=ON \
  -DWITH_SLOX=ON \
  -DWITH_GROUPWISE=ON \
  -DWITH_FEATUREPLAN=ON \
  -DWITH_GROUPDAV=ON \
  -DWITH_BIRTHDAYS=ON \
  -DWITH_NEWEXCHANGE=ON \
  -DWITH_SCALIX=ON \
  -DWITH_CALDAV=ON \
  -DWITH_CARDDAV=ON \
  -DWITH_INDEXLIB=ON \
  %{?with_xscreensaver:-DWITH_XSCREENSAVER=ON} \
  %{?with_kitchensync:-DBUILD_KITCHENSYNC=ON} \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/akregator.desktop       Network  RSS-News
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/groupwarewizard.desktop Utility  DesktopSettings X-TDE-Utilities-PIM
%suse_update_desktop_file       %{?buildroot}%{tde_tdeappdir}/kaddressbook.desktop
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/kalarm.desktop          Utility  TimeUtility X-TDE-Utilities-PIM
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/kandy.desktop           Utility  Telephony X-TDE-Utilities-Peripherals
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/karm.desktop            Utility  TimeUtility X-TDE-Utilities-PIM
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/kleopatra.desktop       Network  System
%suse_update_desktop_file       %{?buildroot}%{tde_tdeappdir}/KNode.desktop
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/knotes.desktop          Utility  DesktopUtility X-TDE-Utilities-Desktop
%suse_update_desktop_file       %{?buildroot}%{tde_tdeappdir}/KMail.desktop
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/Kontact.desktop         Office   Core-Office
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/korganizer.desktop      Office   Calendar
%suse_update_desktop_file -r    %{?buildroot}%{tde_tdeappdir}/KOrn.desktop            Utility  Applet X-TDE-More
%suse_update_desktop_file -u    %{?buildroot}%{tde_tdeappdir}/ktnef.desktop           Network  Email
%if 0%{?with_kitchensync}
%suse_update_desktop_file       %{?buildroot}%{tde_tdeappdir}/kitchensync.desktop     Utility  X-SuSE-SyncUtility
%endif
%endif

# Adds missing icons in 'hicolor' theme
pushd "%{?buildroot}%{tde_datadir}/icons"
for i in {16,32,48};           do %__cp crystalsvg/"$i"x"$i"/apps/kandy.png                           hicolor/"$i"x"$i"/apps/kandy.png      ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/places/network.png  hicolor/"$i"x"$i"/apps/kleopatra.png  ;done
popd

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"


%clean
%__rm -rf %{?buildroot}


%changelog
