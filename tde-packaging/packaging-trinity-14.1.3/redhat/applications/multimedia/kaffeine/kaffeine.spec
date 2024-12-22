#
# spec file for package kaffeine (version R14)
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
%define tde_pkg kaffeine
%define tde_prefix /opt/trinity
%define tde_appdir %{tde_datadir}/applications
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


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		0.8.8
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Xine-based media player
Group:			Applications/Multimedia
URL:			http://kaffeine.sourceforge.net/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# VORBIS support
%if 0%{?mdkver} || 0%{?mgaversion}
%if 0%{?pclinuxos}
%define libvorbis_devel %{_lib}vorbis0-devel
%else
%define libvorbis_devel %{_lib}vorbis-devel
%endif
%else
%define libvorbis_devel libvorbis-devel
%endif
BuildRequires: %{libvorbis_devel}

# CDDA support
BuildRequires:	libcdio-devel
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mdkver}
BuildRequires:	%{_lib}cdda-devel
%else
BuildRequires:	libcdda-devel
%endif
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	cdparanoia
BuildRequires:	cdparanoia-devel
%endif
%if 0%{?suse_version} >= 1210 || 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildRequires:	libcdio-paranoia-devel
%endif

# X11 stuff
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xext-devel
BuildRequires:	%{_lib}xtst-devel
BuildRequires:	%{_lib}xinerama-devel
%else
BuildRequires:	%{_lib}xext%{?mgaversion:6}-devel
BuildRequires:	%{_lib}xtst%{?mgaversion:6}-devel
BuildRequires:	%{_lib}xinerama%{?mgaversion:1}-devel
%endif
%endif
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel 
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXext-devel 
BuildRequires:	libXtst-devel
BuildRequires:	libXinerama-devel
%endif

# XCB support
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?pclinuxos} || 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos} == 0
%define with_xcb 1
%endif
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?pclinuxos}
BuildRequires:	libxcb-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos} == 0
BuildRequires:	%{_lib}xcb-devel
%endif
%endif
%endif

# GSTREAMER support
%if 0%{?rhel} >= 5 || 0%{?suse_version} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gstreamer 1
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mdkver} >= 5000000
BuildRequires:	%{_lib}gstreamer-devel
BuildRequires:	%{_lib}gst-plugins-base1.0-devel
%else
BuildRequires:	%{_lib}gstreamer1.0-devel
BuildRequires:	%{_lib}gstreamer-plugins-base1.0-devel
%endif
%endif
%if 0%{?rhel} == 4
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-devel
%endif
%if 0%{?rhel} == 5 || 0%{?rhel} == 6 || 0%{?suse_version}
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
%endif
%if 0%{?rhel} >= 7 || 0%{?fedora}
BuildRequires:	gstreamer1-devel >= 1.0
BuildRequires:	gstreamer1-plugins-base-devel >= 1.0
%endif
%endif

# XINE support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos} || 0%{?rhel} || 0%{?suse_version}
%define with_xine 1
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}xine-devel
%else
BuildRequires: %{_lib}xine1.2-devel
%endif
%endif
%if 0%{?fedora} || 0%{?rhel}
BuildRequires: xine-lib-devel
%endif
%if 0%{?suse_version}
BuildRequires: libxine-devel
%endif
%endif

# LAME support
%if 0%{?opensuse_bs} == 0
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} || 0%{?rhel}
%define with_lame 1

%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:		liblame-devel
%else
%if 0%{?mgaversion} >= 6
BuildRequires:		%{_lib}mp3lame-devel
%else
BuildRequires:		%{_lib}lame-devel
%endif
%endif
%endif
%if 0%{?suse_version}
BuildRequires:	libmp3lame-devel
%endif
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:	lame-devel
%endif
%endif
%endif

# DVB support
%if 0%{?rhel} != 5
%define with_dvb 1
%endif

# WTF support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos} == 0
BuildRequires:	kernel-headers
%endif
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	glibc-kernheaders 
%endif

Requires: %{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Kaffeine is a xine-based media player for TDE.  It plays back CDs,
and VCDs, and can decode all (local or streamed) multimedia formats 
supported by xine-lib.
Additionally, Kaffeine is fully integrated in TDE, it supports drag
and drop and provides an editable playlist, a bookmark system, a
Konqueror plugin, OSD and much more.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md TODO
%{tde_bindir}/kaffeine
%{tde_libdir}/libkaffeinepart.so
%{tde_tdelibdir}/lib*.*
%{tde_datadir}/appl*/*/*.desktop
%if 0%{?with_gstreamer}
%{tde_datadir}/apps/gstreamerpart/
%endif
%{tde_datadir}/apps/kaffeine/
%{tde_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_datadir}/apps/profiles/
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/mimelnk/*/*.desktop
%{tde_datadir}/service*/*.desktop
%{tde_tdedocdir}/HTML/en/kaffeine/
%{tde_mandir}/man1/kaffeine.1*

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-tdelibs-devel

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kaffeine/
%{tde_libdir}/lib*.so
%exclude %{tde_libdir}/libkaffeinepart.so

##########

%package libs
Summary:		%{name} runtime libraries
Group:			System Environment/Libraries

# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/lib*.so.*

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
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DWITH_ALL_OPTIONS=ON \
  %{?!with_dvb:-DWITH_DVB=OFF} \
  %{?!with_lame:-DWITH_LAME=OFF} \
  %{?!with_xcb:-DWITH_XCB=OFF} \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=%{buildroot} -C build

## File lists
# locale's
%find_lang %{tde_pkg}

# Unpackaged files
rm -f $RPM_BUILD_ROOT%{tde_libdir}/lib*.la
rm -f $RPM_BUILD_ROOT%{tde_datadir}/mimelnk/application/x-mplayer2.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%changelog
