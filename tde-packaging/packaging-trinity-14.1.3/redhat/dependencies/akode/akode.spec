#
# spec file for package akode (version R14)
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

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libakode %{_lib}akode
%else
%define libakode libakode
%endif

Name:		trinity-akode 
Epoch:		%{tde_epoch}
Version:	2.0.2
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary: 	Audio-decoding framework
Group: 		System Environment/Libraries
URL:		http://www.kde-apps.org/content/show.php?content=30375
#URL:		http://carewolf.com/akode/  

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:  gcc-c++
BuildRequires:	libtool

# TQT support
BuildRequires:	libtqt4-devel
BuildRequires:	trinity-filesystem >= %{tde_version}

# FLAC support
%define _with_flac --with-flac
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires: %{_lib}flac12-devel
%else
BuildRequires: %{_lib}flac-devel
%endif
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: flac-devel
%endif

# JACK support
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define _with_jack --with-jack
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires: %{_lib}jack-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: jack-audio-connection-kit-devel
%endif
%endif

# SAMPLERATE support
%if 0%{?rhel} >= 4 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?suse_version}
%define _with_libsamplerate --with-libsamplerate
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: %{_lib}samplerate-devel
%else
BuildRequires: libsamplerate-devel
%endif
%endif

# PULSEAUDIO support
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 6 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define _with_pulseaudio --with-pulseaudio
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires: %{_lib}pulseaudio-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires: pulseaudio-libs-devel
%endif
%if 0%{?suse_version}
BuildRequires: pulseaudio-devel
%endif
%endif

# MAD support
%ifarch %{ix86} x86_64
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define _with_libmad --with-libmad
%if 0%{?mdkver}
BuildRequires:		%{_lib}mad-devel
%else
BuildRequires:		libmad-devel
%endif
%endif
%endif

# ALSA support
%if 0%{?suse_version}
BuildRequires: alsa-devel
%else
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}asound-devel
%else
BuildRequires: alsa-lib-devel
%endif
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

BuildRequires: speex-devel


%description
aKode is a simple audio-decoding frame-work that provides a uniform
interface to decode the most common audio-formats. It also has a direct
playback option for a number of audio-outputs.

aKode currently has the following decoder plugins:
* mpc: Decodes musepack aka mpc audio.
* xiph: Decodes FLAC, Ogg/FLAC, Speex and Ogg Vorbis audio. 

aKode also has the following audio outputs:
* alsa: Outputs to ALSA (dmix is recommended).
* jack
* pulseaudio

%files
%defattr(-,root,root,-)
%doc rpmdocs/* 
%{_bindir}/akodeplay
%{_libdir}/libakode.so.*
%{_libdir}/libakode_alsa_sink.la
%{_libdir}/libakode_alsa_sink.so
%{_libdir}/libakode_mpc_decoder.la
%{_libdir}/libakode_mpc_decoder.so
%{_libdir}/libakode_oss_sink.la
%{_libdir}/libakode_oss_sink.so
%{_libdir}/libakode_xiph_decoder.la
%{_libdir}/libakode_xiph_decoder.so

%post
/sbin/ldconfig

%postun 
/sbin/ldconfig

##########

%package devel
Summary: Headers for developing programs that will use %{name} 
Group:   Development/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%{?_with_jack:Requires: %{libakode}_jack_sink = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?_with_pulseaudio:Requires: %{libakode}_pulse_sink = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?_with_libsamplerate:Requires: %{libakode}_src_resampler = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?_with_libmad:Requires: %{libakode}_mpeg_decoder  = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: pkgconfig

%description devel
This package contains the development files for Akode.
It is needed if you intend to build an application linked against Akode.

%files devel
%defattr(-,root,root,-)
%{_bindir}/akode-config
%{_includedir}/*
%{_libdir}/libakode.la
%{_libdir}/libakode.so
%{_libdir}/pkgconfig/akode.pc

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

##########

%if "%{?_with_jack}" != ""

%package -n %{libakode}_jack_sink
Summary: Jack audio output backend for %{name}
Group:   Development/Libraries
Provides: libakode_jack_sink = %{version}-%{release}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libakode}_jack_sink
This package contains the Jack audio output backend for Akode.

%files -n %{libakode}_jack_sink
%defattr(-,root,root,-)
%{_libdir}/libakode_jack_sink.la
%{_libdir}/libakode_jack_sink.so

%post -n %{libakode}_jack_sink
/sbin/ldconfig

%postun -n %{libakode}_jack_sink
/sbin/ldconfig

%endif

##########

%if "%{?_with_pulseaudio}" != ""

%package -n %{libakode}_pulse_sink
Summary: Pulseaudio output backend for %{name}
Group:   Development/Libraries
Provides: libakode_pulse_sink = %{version}-%{release}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libakode}_pulse_sink
This package contains the pulseaudio backend for Akode.
Recommended for network transparent audio.

%files -n %{libakode}_pulse_sink
%defattr(-,root,root,-)
%{_libdir}/libakode_pulse_sink.la
%{_libdir}/libakode_pulse_sink.so

%post -n %{libakode}_pulse_sink
/sbin/ldconfig

%postun -n %{libakode}_pulse_sink
/sbin/ldconfig

%endif

##########

# Packaged separately to keep main/core %{akode} package LGPL-clean.
%if "%{?_with_libsamplerate:1}" == "1"

%package -n %{libakode}_src_resampler
Summary: Resampler based on libsamplerate for %{name}
Group:   Development/Libraries
Provides: libakode_src_resampler = %{version}-%{release}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libakode}_src_resampler 
This package contains the samplerate decoder for Akode.

%files -n %{libakode}_src_resampler
%defattr(-,root,root,-)
%{_libdir}/libakode_src_resampler.la
%{_libdir}/libakode_src_resampler.so

%post -n %{libakode}_src_resampler
/sbin/ldconfig

%postun -n %{libakode}_src_resampler 
/sbin/ldconfig

%endif

##########

%if "%{?_with_libmad}" != ""

%package -n %{libakode}_mpeg_decoder
Summary: Decoder based on libmad for %{name}
Group:   Development/Libraries
Provides: libakode_mpeg_decoder = %{version}-%{release}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libakode}_mpeg_decoder 
This package contains the mad decoder for Akode.

%files -n %{libakode}_mpeg_decoder
%defattr(-,root,root,-)
%{_libdir}/libakode_mpeg_decoder.la
%{_libdir}/libakode_mpeg_decoder.so

%post -n %{libakode}_mpeg_decoder
/sbin/ldconfig

%postun -n %{libakode}_mpeg_decoder 
/sbin/ldconfig

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

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
   \
  -DINCLUDE_INSTALL_DIR=%{_includedir} \
  -DLIB_INSTALL_DIR=%{_libdir} \
  \
  -DWITH_ALL_OPTIONS="ON" \
  -DWITH_LIBLTDL="OFF" \
  -DWITH_ALSA_SINK="ON" \
  %{!?_with_jack:-DWITH_JACK_SINK="OFF"} %{?_with_jack:-DWITH_JACK_SINK="ON"} \
  %{!?_with_pulseaudio:-DWITH_PULSE_SINK="OFF"} %{?_with_pulseaudio:-DWITH_PULSE_SINK="ON"} \
  -DWITH_OSS_SINK="ON" \
  -DWITH_SUN_SINK="OFF" \
  \
  -DWITH_FFMPEG_DECODER="OFF" \
  -DWITH_MPC_DECODER="ON" \
  %{!?_with_libmad:-DWITH_MPEG_DECODER="OFF"} %{?_with_libmad:-DWITH_MPEG_DECODER="ON"} \
  -DWITH_SRC_RESAMPLER="ON" \
  -DWITH_XIPH_DECODER="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{buildroot} 
%__make install DESTDIR=%{?buildroot} -C build

# rpmdocs
for file in AUTHORS COPYING NEWS README TODO ; do
  test -s  "$file" && install -p -m644 -D "$file" "rpmdocs/$file"
done


%clean
%__rm -rf %{buildroot} 


%changelog
