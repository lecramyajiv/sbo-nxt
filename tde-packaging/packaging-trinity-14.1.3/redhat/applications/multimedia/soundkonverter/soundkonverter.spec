#
# spec file for package soundkonverter (version R14)
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
%define tde_pkg soundkonverter
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
Version:	0.3.8
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Audio converter frontend for Trinity
Group:		Application/Multimedia
URL:		http://potracegui.sourceforge.net

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

# TAGLIB support
BuildRequires:	taglib-devel

# CDDA support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mdkver}
BuildRequires:	%{_lib}cdda-devel
%else
BuildRequires:	libcdda-devel
%endif
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	cdparanoia-devel
%endif


%description
soundKonverter is a frontend to various audio converters.

The key features are:
 - Audio conversion
 - Replay Gain calculation
 - CD ripping

soundKonverter supports reading and writing tags for many formats, so the tags
are preserved when converting files.

It comes with an Amarok script.

See 'soundkonverter-amarok' package for more informations.

See README.Debian for more informations on supported formats.


%package amarok
Summary:		audio converter frontend for Trinity (Amarok script)
Group:			Application/Multimedia
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-amarok

%description amarok
Amarok script for soundKonverter. It allows you to easily transcode files when
transferring them to your media device.

See the 'trinity-soundkonverter' package for more information.


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
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}

# Updates applications categories for openSUSE
%if 0%{?suse_version}
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"
%endif


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{tde_bindir}/soundkonverter
%{tde_tdeappdir}/soundkonverter.desktop
%{tde_datadir}/apps/konqueror/servicemenus/audiocd_extract_with_soundkonverter.desktop
%{tde_datadir}/apps/soundkonverter
%exclude %{tde_datadir}/apps/soundkonverter/amarokscript/
%{tde_tdedocdir}/HTML/en/soundkonverter/
%{tde_datadir}/icons/hicolor/*/apps/soundkonverter*.png
%{tde_datadir}/mimelnk/application/x-la.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-ofc.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-ofr.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-ofs.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-shorten.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/amr.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-ape.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-bonk.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-pac.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-tta.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-wavpack-correction.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-wavpack.soundkonverter.desktop
%{tde_datadir}/mimelnk/video/x-flv.soundkonverter.desktop

%files amarok
%defattr(-,root,root,-)
%{tde_datadir}/apps/soundkonverter/amarokscript/


%changelog
