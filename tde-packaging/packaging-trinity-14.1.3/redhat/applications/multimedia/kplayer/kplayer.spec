#
# spec file for package kplayer (version R14)
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
%define tde_pkg kplayer
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
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
Version:	0.6.3
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	KPlayer is a TDE multimedia player
Group:		Applications/Multimedia
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

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	libtool

# IDN support
BuildRequires:	libidn-devel

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

Requires:		mplayer


%description
KPlayer is a TDE multimedia player.
With KPlayer you can easily play a wide variety of video and audio  files and
streams using a rich and friendly interface that follows KDE standards.
This version was derived from the KDE3 branch 0.6.3 for the Trinity Desktop Environment

Features include

video, audio and subtitle playback from file, URL, DVD, VCD, audio CD, TV, DVB, and KDE I/O Slaves;
volume, contrast, brightness, hue and saturation controls;
zooming, full screen and fixed aspect options;
status and progress display and seeking;
multimedia library to organize your media files and streams;
configuration dialog;
file properties for setting file specific options.

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
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

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
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DPLUGIN_INSTALL_DIR=%{tde_tdelibdir} \
  -DBUILD_ALL=ON \
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
%{tde_bindir}/kplayer
%{tde_datadir}/apps/kplayer/
%{tde_datadir}/icons/hicolor/*/apps/kplayer.png
%{tde_datadir}/icons/locolor/*/apps/kplayer.png
%{tde_datadir}/services/kplayerpart.desktop
%{tde_tdelibdir}/libkplayerpart.la
%{tde_tdelibdir}/libkplayerpart.so
%{tde_tdeappdir}/kplayer.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kplayer-actions.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kplayer-directory.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kplayer-next.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kplayer-play-queue.desktop
%lang(da) %{tde_tdedocdir}/HTML/da/kplayer/
%lang(en) %{tde_tdedocdir}/HTML/en/kplayer/
%lang(es) %{tde_tdedocdir}/HTML/es/kplayer/
%lang(it) %{tde_tdedocdir}/HTML/it/kplayer/
%lang(pt) %{tde_tdedocdir}/HTML/pt/kplayer/
%lang(sv) %{tde_tdedocdir}/HTML/sv/kplayer/


%post


%postun


%changelog
