#
# spec file for package tderadio (version R14)
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

%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_lirc 1
%endif

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg tderadio
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
Version:	0.1.1.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Comfortable Radio Application for TDE
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

BuildRequires:	cmake
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

%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}sndfile-devel
%else
BuildRequires:	libsndfile-devel
%endif

%{?with_lirc:BuildRequires:	lirc-devel}

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

Obsoletes:		trinity-kradio < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kradio = %{?epoch:%{epoch}:}%{version}-%{release}


%description
TDERadio is a comfortable radio application for Trinity with support for 
V4L and V4L2 radio cards drivers.

TDERadio currently provides

 * V4L/V4L2 radio support
%if 0%{?with_lirc}
 * Remote control support (LIRC)
%endif
 * Alarms, sleep Countdown
 * Several GUI Controls (Docking Menu, Station Quickbar, Radio Display)
 * Recording capabilities, including MP3 and Ogg/Vorbis encoding
 * Timeshifter functionality
 * Extendable plugin architecture

This package also includes a growing collection of station preset
files for many cities around the world contributed by TDERadio users.

As TDERadio is based on an extendable plugin architecture, contributions
of new plugins (e.g. Internet Radio Streams, new cool GUIs) are welcome.


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
  \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -G "Radio Tuner" %{tde_pkg} AudioVideo Tuner
%endif

# Remove devel files
%__rm -f %{?buildroot}%{tde_libdir}/libtderadio.la
%__rm -f %{?buildroot}%{tde_libdir}/libtderadio.so

# Remove pixmas
%__rm -fr %{?buildroot}%{tde_datadir}/pixmaps/


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_bindir}/convert-presets
%{tde_bindir}/tderadio
%{tde_libdir}/libtderadio.so.0
%{tde_libdir}/libtderadio.so.0.0.0
%dir %{tde_libdir}/tderadio
%dir %{tde_libdir}/tderadio/plugins
%{tde_libdir}/tderadio/plugins/*.la
%{tde_libdir}/tderadio/plugins/*.so
%{tde_tdeappdir}/tderadio.desktop
%{tde_datadir}/apps/tderadio/
%dir %{tde_datadir}/icons/hicolor/256x256
%dir %{tde_datadir}/icons/hicolor/256x256/actions
%{tde_datadir}/icons/hicolor/*/*/tderadio*.png
%{tde_datadir}/icons/locolor/*/*/tderadio*.png
%lang(de) %{tde_datadir}/locale/de/LC_MESSAGES/*.mo
%lang(es) %{tde_datadir}/locale/es/LC_MESSAGES/*.mo
%lang(it) %{tde_datadir}/locale/it/LC_MESSAGES/*.mo
%lang(nl) %{tde_datadir}/locale/nl/LC_MESSAGES/*.mo
%lang(pl) %{tde_datadir}/locale/pl/LC_MESSAGES/*.mo
%lang(pt) %{tde_datadir}/locale/pt/LC_MESSAGES/*.mo
%lang(ru) %{tde_datadir}/locale/ru/LC_MESSAGES/*.mo
%{tde_tdedocdir}/HTML/en/tderadio/
%{tde_mandir}/man1/convert-presets.1*
%{tde_mandir}/man1/tderadio.1*


%changelog
