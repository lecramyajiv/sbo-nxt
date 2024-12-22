#
# spec file for package trinity-desktop (version R14)
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

%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _docdir %{_datadir}/doc
%define tde_datadir %{tde_prefix}/share
%endif

Name:		trinity-desktop
Version:	%{tde_version}
Release:	1%{?dist}
Summary:	Meta-package to install TDE
Group:		User Interface/Desktops
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Source0:	trinity-3.5.13-fedora.repo
Source1:	trinity-3.5.13-rhel.repo
Source2:	RPM-GPG-KEY-trinity

%if 0%{?fedora} >= 32 || 0%{?mdkver} >= 5000000 || 0%{?mgaversion} >= 7 || 0%{?pclinuxos} || 0%{?rhel} >= 8 || 0%{?suse_version}
Requires:	pinentry-tqt
%endif
Requires:	trinity-tdeaccessibility >= %{version}
Requires:	trinity-tdeaddons >= %{version}
Requires:	trinity-tdeadmin >= %{version}
Requires:	trinity-tdeartwork >= %{version}
Requires:	trinity-tdebase >= %{version}
Requires:	trinity-tdebindings >= %{version}
Requires:	trinity-tdeedu >= %{version}
Requires:	trinity-tdegames >= %{version}
Requires:	trinity-tdegraphics >= %{version}
Requires:	trinity-tdemultimedia >= %{version}
Requires:	trinity-tdenetwork >= %{version}
Requires:	trinity-tdepim >= %{version}
Requires:	trinity-tdetoys >= %{version}
Requires:	trinity-tdeutils >= %{version}

%if 0%{?rhel} || 0%{?fedora}
# YUM configuration file
Requires:	trinity-repo >= %{version}
%endif

%description
The TDE project aims to keep the KDE3.5 computing style alive, as well as
polish off any rough edges that were present as of KDE 3.5.10. Along
the way, new useful features will be added to keep the environment
up-to-date.
Toward that end, significant new enhancements have already been made in
areas such as display control, network connectivity, user
authentication, and much more!

%files

##########

%package devel
Group:		User Interface/Desktops
Summary:	Meta-package to install TDE development tools

Requires:	trinity-tdesdk >= %{version}
Requires:	trinity-tdevelop >= %{version}
Requires:	trinity-tdewebdev >= %{version}

%description devel
%{summary}

%files devel

##########

%package applications
Group:		User Interface/Desktops
Summary:	Meta-package to install all TDE applications

# Warning, k9copy requires ffmpeg

Requires: trinity-abakus
Requires: trinity-amarok
Requires: trinity-basket
Requires: trinity-bibletime
Requires: trinity-codeine
Requires: trinity-digikam
Requires: trinity-dolphin
Requires: trinity-filelight
Requires: trinity-gwenview
Requires: trinity-k3b
Requires: trinity-k9copy
Requires: trinity-kaffeine
Requires: trinity-kaffeine-mozilla
Requires: trinity-kasablanca
Requires: trinity-katapult
Requires: trinity-kbarcode
Requires: trinity-kbfx
Requires: trinity-kbibtex
Requires: trinity-kbiff
Requires: trinity-kbookreader
Requires: trinity-kchmviewer
Requires: trinity-kcmautostart
Requires: trinity-kcmldap
Requires: trinity-kcmldapcontroller
Requires: trinity-kcmldapmanager
Requires: trinity-kcpuload
Requires: trinity-kdbg
Requires: trinity-kdbusnotification
Requires: trinity-kdiff3
Requires: trinity-kdirstat
Requires: trinity-keep
Requires: trinity-kerberostray
Requires: trinity-keximdb
Requires: trinity-kftpgrabber
Requires: trinity-kile
Requires: trinity-kima
Requires: trinity-kiosktool
Requires: trinity-kkbswitch
%if 0%{?fedora} || 0%{?mgaversion} >= 7 || 0%{?pclinuxos} || 0%{?rhel} >= 7 || 0%{?suse_version}
Requires: trinity-klamav
%endif
Requires: trinity-klcddimmer
Requires: trinity-kmplayer
Requires: trinity-kmyfirewall
Requires: trinity-kmymoney
Requires: trinity-knemo
Requires: trinity-knetload
Requires: trinity-knetstats
Requires: trinity-knights
Requires: trinity-knowit
Requires: trinity-knmap
Requires: trinity-knutclient
Requires: trinity-koffice-suite
Requires: trinity-kommando
Requires: trinity-kompose
Requires: trinity-konversation
Requires: trinity-kooldock
Requires: trinity-kopete-otr
Requires: trinity-kpicosim
%if 0%{?sle_version} <= 150300 && 0%{?suse_version} != 1599 && 0%{?suse_version} != 1699
%if 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?fedora} || 0%{?rhel} >= 6
Requires: trinity-kpilot
%endif
%endif
Requires: trinity-kplayer
Requires: trinity-krecipes
Requires: trinity-krename
Requires: trinity-krusader
Requires: trinity-kscope
Requires: trinity-ksensors
Requires: trinity-kshowmail
Requires: trinity-kshutdown
Requires: trinity-ksplash-engine-moodin
Requires: trinity-ksquirrel
Requires: trinity-kstreamripper
Requires: trinity-ksystemlog
Requires: trinity-ktechlab
Requires: trinity-ktorrent
Requires: trinity-kvirc
Requires: trinity-kvkbd
Requires: trinity-kvpnc
Requires: trinity-kxmleditor
Requires: trinity-mathemagics
Requires: trinity-mplayerthumbs
Requires: trinity-piklab
%if 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?fedora} || 0%{?rhel} >= 7
# On RHEL6, polkit is too old
Requires: trinity-polkit-agent-tde
%endif
Requires: trinity-potracegui
Requires: trinity-qalculate-tde
# On RHEL, lilypond is not available, so no rosegarden :'-(
%if 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?fedora}
Requires: trinity-rosegarden
%endif
Requires: trinity-smb4k
Requires: trinity-smartcardauth
Requires: trinity-soundkonverter
Requires: trinity-tastymenu
Requires: trinity-tdebluez
Requires: trinity-tde-ebook-reader
Requires: trinity-tde-guidance
Requires: trinity-tde-style-baghira
Requires: trinity-tde-style-domino
Requires: trinity-tde-style-ia-ora
Requires: trinity-tde-style-lipstik
Requires: trinity-tde-style-qtcurve
Requires: trinity-tde-style-polyester
Requires: trinity-tde-systemsettings
Requires: trinity-tdedocker
%if 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?fedora} || 0%{?rhel} >= 7
Requires: trinity-tdeio-appinfo
%endif
Requires: trinity-tdeio-apt
Requires: trinity-tdeio-ftps
Requires: trinity-tdeio-gopher
Requires: trinity-tdeio-locate
Requires: trinity-tdeio-sword
Requires: trinity-tdeio-umountwrapper
Requires: trinity-tdenetworkmanager
Requires: trinity-tdepacman
%if 0%{?rhel} != 5
Requires: trinity-tdepowersave
%endif
Requires: trinity-tderadio
Requires: trinity-tdesshaskpass
Requires: trinity-tdesudo
Requires: trinity-tdesvn
Requires: trinity-tdmtheme
Requires: trinity-tellico
Requires: trinity-tork
Requires: trinity-twin-style-crystal
Requires: trinity-twin-style-dekorator
Requires: trinity-twin-style-fahrenheit
Requires: trinity-twin-style-machbunt
Requires: trinity-twin-style-mallory
Requires: trinity-twin-style-suse2
Requires: trinity-wlassistant
Requires: trinity-yakuake

# Power management
Obsoletes: trinity-tde-guidance-powermanager < %{?epoch:%{epoch}:}%{version}-%{release}

# Decoration-related stuff (not installed by default)
#Requires: trinity-kgtk-qt3
#Requires: trinity-gtk-qt-engine
#Requires: trinity-gtk3-tqt-engine
#Requires: trinity-qt4-tqt-theme-engine

# Compiz-related stuff does not work (obsolete)
#Requires: trinity-compizconfig-backend-kconfig
#Requires: trinity-desktop-effects-kde
#Requires: trinity-fusion-icon


%description applications
%{summary}

%files  applications

##########

%package all
Group:		User Interface/Desktops
Summary:	Meta-package to install all TDE packages

Requires:	%{name} = %{version}
Requires:	%{name}-applications = %{version}
Requires:	%{name}-devel = %{version}

%description all
%{summary}

%files all

##########

%if 0%{?rhel} || 0%{?fedora}
%package -n trinity-repo
Group:		User Interface/Desktops
Summary:	Yum configuration files for Trinity
Requires(pre):	coreutils

%description -n trinity-repo
%{summary}

%pre -n trinity-repo
# Make sure every Trinity related repository is deleted before installing new one.
%__rm -f %{_sysconfdir}/yum.repos.d/trinity-*.repo

%files -n trinity-repo
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-trinity
%endif

##########

%prep


%build


%install
%__rm -rf %{?buildroot}
%__mkdir_p "%{?buildroot}%{_sysconfdir}/yum.repos.d"

# FEDORA configuration for YUM
%if 0%{?fedora}
%__sed %{SOURCE0} \
  -e 's/\$releasever/%{fedora}/g' \
  -e 's/-fedora/-f%{fedora}/g' \
  >"%{?buildroot}%{_sysconfdir}/yum.repos.d/trinity.repo"
%endif

# RHEL configuration for YUM
# $releasever is replaced with its value
%if 0%{?rhel}
%__sed %{SOURCE1} \
  -e 's/\$releasever/%{rhel}/g' \
  >"%{?buildroot}%{_sysconfdir}/yum.repos.d/trinity.repo"
%endif

%if 0%{?fedora} || 0%{?rhel}
%__sed -i %{?buildroot}%{_sysconfdir}/yum.repos.d/*.repo -e "s|3.5.13|r14|g"
%__chmod 644 %{?buildroot}%{_sysconfdir}/yum.repos.d/*.repo
%endif

# RPM signing key
%if 0%{?rhel} || 0%{?fedora}
%__install -D -m 644 "%{SOURCE2}" "%{?buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-trinity"
%endif


%changelog
