#
# spec file for package tdenetworkmanager (version R14)
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
%define tde_pkg tdenetworkmanager
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
Version:	0.9
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Trinity applet for Network Manager
Group:		Applications/Internet
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
Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires: libtool
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

Obsoletes:		trinity-knetworkmanager < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-knetworkmanager = %{?epoch:%{epoch}:}%{version}-%{release}

# NETWORKMANAGER support
%if 0%{?rhel} || 0%{?fedora}
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
Requires:		NetworkManager
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
BuildRequires:	NetworkManager-libnm-devel
%else
BuildRequires:		NetworkManager-devel
%endif
%else
Requires:		NetworkManager-gnome
%endif
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
Requires:		networkmanager
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} && 0%{?mgaversion} <= 7
BuildRequires:	%{_lib}nm-util-devel
%endif
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?mdkversion}
%if 0%{?pclinuxos} == 0
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
BuildRequires:	NetworkManager-libnm-devel
%else
%if 0%{?mdkver}
BuildRequires: %{_lib}nm-devel
%else
BuildRequires:	NetworkManager-glib-devel
%endif
%endif
%endif
%endif
%if 0%{?suse_version}
BuildRequires:	NetworkManager-devel
Requires:		NetworkManager
%endif

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# DBUS support
BuildRequires:	trinity-dbus-1-tqt-devel >= 1:0.9
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# UDEV support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}udev-devel
%else
BuildRequires:	libudev-devel
%endif
%endif

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif


%description
TDENetworkManager is a system tray applet for controlling network
connections on systems that use the NetworkManager daemon.

%post
# Prevent autostart of 'nm-applet', if installed.
if [ -r "/etc/xdg/autostart/nm-applet.desktop" ]; then
  if ! grep -qw "TDE" "/etc/xdg/autostart/nm-applet.desktop" ; then
    sed -i "/etc/xdg/autostart/nm-applet.desktop" -e "s|\(NotShowIn=.*\)|\1TDE;|"
  fi
fi

%files
%defattr(-,root,root,-)
%{tde_bindir}/tdenetworkmanager
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{_sysconfdir}/dbus-1/system.d/tdenetworkmanager.conf
%{tde_tdeappdir}/tdenetworkmanager.desktop
%{tde_datadir}/apps/tdenetworkmanager
%{tde_datadir}/icons/hicolor/*/apps/tdenetworkmanager*
%{tde_datadir}/servicetypes/tdenetworkmanager_plugin.desktop
%{tde_datadir}/servicetypes/tdenetworkmanager_vpnplugin.desktop
%{tde_datadir}/autostart/tdenetworkmanager.desktop
#{tde_datadir}/services/tdenetman_openvpn.desktop
#{tde_datadir}/services/tdenetman_pptp.desktop
#{tde_datadir}/services/tdenetman_strongswan.desktop
#{tde_datadir}/services/tdenetman_vpnc.desktop
#{tde_tdedocdir}/HTML/en/tdenetworkmanager/

##########

%package devel
Summary:		Common data shared among the MySQL GUI Suites
Group:			Development/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development headers for tdenetworkmanager

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_tdelibdir}/*.la
%{tde_tdelibdir}/*.so

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
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  ..
  
%__make %{?_smp_mflags} 


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=%{?buildroot} -C build

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r %{tde_pkg} Utility TrayIcon System Applet
%endif


%clean
%__rm -rf $RPM_BUILD_ROOT


%changelog
