#
# spec file for package k3b (version R14)
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
%define tde_pkg k3b
%define tde_prefix /opt/trinity
%define tde_appdir %{tde_datadir}/applications
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


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		1.0.5
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		CD/DVD burning application
Group:			Applications/Archiving
URL:			http://www.trinitydesktop.org/

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

# ALSA supportl
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}asound-devel
%else
BuildRequires: alsa-lib-devel
%endif

BuildRequires:	audiofile-devel
BuildRequires:	gettext
BuildRequires:	taglib-devel
BuildRequires:	zlib-devel

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

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# ATTR support
%if 0%{?mgaversion} || 0%{?mdkversion}
%define libattr_devel %{_lib}attr-devel
%else
%define libattr_devel libattr-devel
%endif
BuildRequires: %{libattr_devel}

Requires(post): coreutils
Requires(postun): coreutils

Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-common = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?suse_version} >= 1310 && 0%{?suse_version} < 1500 || 0%{?fedora} >= 29
Requires:		wodim
REquires:		genisoimage
%else
Requires:		cdrecord
REquires:		mkisofs
%endif
Requires:		dvd+rw-tools

# CDRDAO support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 5
Requires:		cdrdao
%endif

# UDEV support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%if 0%{?mdkversion} || 0%{?mgaversion}
%if 0%{?pclinuxos}
BuildRequires:	%{_lib}udev1-devel
%else
BuildRequires:	%{_lib}udev-devel
%endif
%else
BuildRequires:	libudev-devel
%endif
%endif

# HAL support
%if 0%{?rhel} == 5
%define with_hal 0
BuildRequires:	hal-devel
%endif

# DBUS support
#  TQT bindings not available for RHEL4
%if 0%{?rhel} == 4
# Dbus bindings were rebuilt with Qt support
BuildRequires:	dbus-devel >= 0.22-12.EL.9p1
Requires:		dbus-qt >= 0.22-12.EL.9p1
%else
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63
Requires:		trinity-dbus-tqt >= 1:0.63
%endif

# SNDFILE support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 4
%define with_sndfile 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}sndfile-devel
%else
BuildRequires:	libsndfile-devel
%endif
%endif

# SAMPLERATE support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 4
%define with_samplerate 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: %{_lib}samplerate-devel
%else
BuildRequires: libsamplerate-devel
%endif
%endif

# DVDREAD support
%define with_dvdread 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}dvdread-devel
%else
BuildRequires:	libdvdread-devel
%endif

# FLAC support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:	libflac-devel
BuildRequires:	libflac++-devel
%else
BuildRequires:	%{_lib}flac-devel
BuildRequires:	%{_lib}flac++-devel
%endif
%else
BuildRequires:	flac-devel
%endif

# MAD support
%ifarch %{ix86} x86_64
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define with_libmad 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}mad-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:	libmad-devel
%endif
%endif
%endif

# LAME support
%if 0%{?opensuse_bs} == 0
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define with_lame 1
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:	liblame-devel
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

# FFMPEG support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define with_ffmpeg 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}ffmpeg-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:	ffmpeg-devel
%endif
%endif

# MUSEPACK
%if 0%{?fedora} == 0 || 0%{?fedora} <= 37
# Looking for mpc_decoder_setup in mpcdec - not found
%define with_musepack 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}mpcdec-devel
%else
BuildRequires:	libmpcdec-devel
%endif
%endif


%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.


%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING TODO ChangeLog
%{tde_bindir}/k3b
%{tde_tdelibdir}/tdefile_k3b.la
%{tde_tdelibdir}/tdefile_k3b.so
%{tde_tdelibdir}/tdeio_videodvd.la
%{tde_tdelibdir}/tdeio_videodvd.so
%{tde_tdelibdir}/libk3balsaoutputplugin.la
%{tde_tdelibdir}/libk3balsaoutputplugin.so
%{tde_tdelibdir}/libk3bartsoutputplugin.la
%{tde_tdelibdir}/libk3bartsoutputplugin.so
%{tde_tdelibdir}/libk3baudiometainforenamerplugin.la
%{tde_tdelibdir}/libk3baudiometainforenamerplugin.so
%{tde_tdelibdir}/libk3baudioprojectcddbplugin.la
%{tde_tdelibdir}/libk3baudioprojectcddbplugin.so
%{tde_tdelibdir}/libk3bexternalencoder.la
%{tde_tdelibdir}/libk3bexternalencoder.so
%{tde_tdelibdir}/libk3bflacdecoder.la
%{tde_tdelibdir}/libk3bflacdecoder.so
%if 0%{?with_sndfile}
%{tde_tdelibdir}/libk3blibsndfiledecoder.la
%{tde_tdelibdir}/libk3blibsndfiledecoder.so
%endif
%if 0%{?with_musepack}
%{tde_tdelibdir}/libk3bmpcdecoder.la
%{tde_tdelibdir}/libk3bmpcdecoder.so
%endif
%{tde_tdelibdir}/libk3boggvorbisdecoder.la
%{tde_tdelibdir}/libk3boggvorbisdecoder.so
%{tde_tdelibdir}/libk3boggvorbisencoder.la
%{tde_tdelibdir}/libk3boggvorbisencoder.so
%{tde_tdelibdir}/libk3bsoxencoder.la
%{tde_tdelibdir}/libk3bsoxencoder.so
%{tde_tdelibdir}/libk3bwavedecoder.la
%{tde_tdelibdir}/libk3bwavedecoder.so
%lang(en) %{tde_tdedocdir}/HTML/en/k3b/
%{tde_mandir}/man1/k3b.1*

##########

%package common
Summary:		Common files of %{name}
Group:			Applications/Archiving
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion}
BuildArch: noarch
%endif

%description common
%{summary}.

%files common
%defattr(-,root,root,-)
%{tde_tdeappdir}/k3b.desktop
%{tde_datadir}/applnk/.hidden/k3b-cue.desktop
%{tde_datadir}/apps/k3b/
%{tde_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_audiocd_rip.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_cd_copy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_dvd_copy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_handle_empty_cd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_handle_empty_dvd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_videodvd_rip.desktop
%{tde_datadir}/mimelnk/application/x-k3b.desktop
%{tde_datadir}/icons/hicolor/*/apps/k3b.png
%{tde_datadir}/services/tdefile_k3b.desktop
%{tde_datadir}/services/videodvd.protocol
%{tde_datadir}/sounds/k3b_error1.wav
%{tde_datadir}/sounds/k3b_success1.wav
%{tde_datadir}/sounds/k3b_wait_media1.wav
%{tde_tdedocdir}/HTML/en/tdeioslave/videodvd/

##########

%package libs
Summary:		Runtime libraries for %{name}
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/libk3b.so.3
%{tde_libdir}/libk3b.so.3.0.0
%{tde_libdir}/libk3bdevice.so.5
%{tde_libdir}/libk3bdevice.so.5.0.0

##########

%package devel
Summary:		Files for the development of applications which will use %{name} 
Group:			Development/Libraries
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libk3b.so
%{tde_libdir}/libk3bdevice.so

##########

%if 0%{?with_libmad}
%package plugin-mad
Summary:		The MAD plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-mad
%{summary}.

MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2  extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%files plugin-mad
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3bmaddecoder.la
%{tde_tdelibdir}/libk3bmaddecoder.so
%endif

##########

%if 0%{?with_lame}
%package plugin-lame
Summary:		The LAME plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-lame
%{summary}.

Personal and commercial use of compiled versions of LAME (or any other mp3
encoder) requires a patent license in some countries.

This package is in tainted, as MP3 encoding is covered by software patents.

%files plugin-lame
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3blameencoder.la
%{tde_tdelibdir}/libk3blameencoder.so
%endif

##########

%if 0%{?with_ffmpeg}
%package plugin-ffmpeg
Summary:		The FFMPEG plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-ffmpeg
%{summary}.

ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

%files plugin-ffmpeg
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3bffmpegdecoder.la
%{tde_tdelibdir}/libk3bffmpegdecoder.so
%endif

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

%if 0%{?rhel} == 7
RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -std=c++11"
%endif

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
  -DWITH_ALL_OPTIONS="ON" \
  -DWITH_MUSICBRAINZ="OFF" \
  -DWITH_FFMPEG_ALL_CODECS="ON" \
  -DWITH_MUSEPACK="%{!?with_musepack:OFF}%{?with_musepack:ON}" \
  -DWITH_LAME="%{!?with_lame:OFF}%{?with_lame:ON}" \
  -DWITH_MAD="%{!?with_libmad:OFF}%{?with_libmad:ON}" \
%if 0%{?rhel} == 5
  -DWITH_HAL="ON" \
%endif
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{?buildroot} -C build

# remove the .la files
%__rm -f %{buildroot}%{tde_libdir}/libk3b*.la 


%clean
%__rm -rf %{buildroot}


%changelog
