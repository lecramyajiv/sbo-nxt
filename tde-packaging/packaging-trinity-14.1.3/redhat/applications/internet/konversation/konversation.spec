#
# spec file for package konversation (version R14)
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

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg konversation
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	User friendly Internet Relay Chat (IRC) client for TDE
Group:		Applications/Utilities
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

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# IDN support
BuildRequires:	libidn-devel

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# PYTHON support
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# XSLT support
%if 0%{?mdkver}
BuildRequires:	%{_lib}xslt-devel
%else
BuildRequires:	libxslt-devel
%endif

%if 0%{?suse_version}
BuildRequires:	docbook-xsl-stylesheets
%else
BuildRequires:	docbook-style-xsl
%endif

# LIBXI support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%endif
%if 0%{?rhel} >= 5|| 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXi-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%endif

# XSCREENSAVER support
#  RHEL 4: disabled
#  RHEL 5: available in centos-extras
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


%description
Konversation is a client for the Internet Relay Chat (IRC) protocol.
It is easy to use and well-suited for novice IRC users, but novice
and experienced users alike will appreciate its many features:

 * Standard IRC features
 * Easy to use graphical interface
 * Multiple server and channel tabs in a single window
 * IRC color support
 * Pattern-based message highlighting and OnScreen Display
 * Multiple identities for different servers
 * Multi-language scripting support (with DCOP)
 * Customizable command aliases
 * NickServ-aware log-on (for registered nicknames)
 * Smart logging
 * Traditional or enhanced-shell-style nick completion
 * DCC file transfer with resume support


##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?mgaversion} >= 8
%__sed -i "konversation/scripts/media" \
          "konversation/scripts/weather" \
  -e "s|/usr/bin/env python|/usr/bin/env %{python}|"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

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
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL=ON \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/konversation
%{tde_tdeappdir}/konversation.desktop
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-appearance.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-colorcodes.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-colors.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-custombrowser.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-notifylists.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-sortorder.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-tabplacement.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.20-customfonts.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.20-quickbuttons.pl
%{tde_datadir}/apps/tdeconf_update/konversation.upd
%{tde_datadir}/apps/konversation/
%{tde_datadir}/config.kcfg/konversation.kcfg
%{tde_datadir}/services/konvirc.protocol
%{tde_datadir}/services/konvirc6.protocol
%{tde_tdedocdir}/HTML/*/konversation/
%{tde_datadir}/icons/crystalsvg/*/actions/tdeimproxyaway.png
%{tde_datadir}/icons/crystalsvg/*/actions/tdeimproxyoffline.png
%{tde_datadir}/icons/crystalsvg/*/actions/tdeimproxyonline.png
%{tde_datadir}/icons/crystalsvg/*/actions/char.png
%{tde_datadir}/icons/crystalsvg/*/actions/konv_message.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/tdeimproxyaway.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/tdeimproxyoffline.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/tdeimproxyonline.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/konv_message.svgz
%{tde_datadir}/icons/hicolor/*/apps/konversation.png
%{tde_datadir}/icons/hicolor/scalable/apps/konversation.svgz
%{tde_mandir}/man1/konversation.1*
%{tde_mandir}/man1/konversationircprotocolhandler.1*


%changelog
