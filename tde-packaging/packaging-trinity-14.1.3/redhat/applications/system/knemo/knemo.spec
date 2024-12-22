#
# spec file for package knemo (version R14)
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
%define tde_pkg knemo
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
Version:	0.4.8
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Network interfaces monitor for the Trinity systray
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/
#URL:		http://beta.smileaf.org/projects

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

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	libtool

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

BuildRequires:	gettext

%if 0%{?fedora} >= 18 || 0%{?suse_version} || 0%{?mgaversion}
BuildRequires:	net-tools
Requires:		net-tools
%endif

%if 0%{?suse_version} > 1320
BuildRequires:	net-tools-deprecated
Requires:		net-tools-deprecated
%endif

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

# Wireless support
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



%description
KNemo displays an icon in the systray for every network interface.
Tooltips and an info dialog provide further information about the
interface.  Passive popups inform about interface changes.
A traffic plotter is also integrated.

knemo polls the network interface status every second using the
ifconfig, route and iwconfig tools. 

Homepage: http://extragear.kde.org/apps/knemo/

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


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
  %{!?with_wifi:-DWITH_LIBIW=OFF} \
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


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcm_knemo.la
%{tde_tdelibdir}/kcm_knemo.so
%{tde_tdelibdir}/kded_knemod.la
%{tde_tdelibdir}/kded_knemod.so
%{tde_tdeappdir}/kcm_knemo.desktop
%{tde_datadir}/apps/knemo/
%{tde_datadir}/icons/crystalsvg/*/*/*.png
%{tde_datadir}/locale/*/LC_MESSAGES/knemod.mo
%{tde_datadir}/locale/*/LC_MESSAGES/kcm_knemo.mo
%{tde_datadir}/services/kded/knemod.desktop
%{tde_tdedocdir}/HTML/en/kcontrol/knemo/


%changelog
