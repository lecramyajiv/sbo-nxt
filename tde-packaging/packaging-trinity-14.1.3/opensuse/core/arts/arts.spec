#
# spec file for package arts
#
# Copyright (c) 2011 the Trinity Project (opensuse).
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
  
# Please submit bugfixes or comments via http://bugs.trinitydesktop.org/
#

# norootforbuild


Name:           arts
BuildRequires:  alsa-devel audiofile-devel cmake glib2-devel jack-devel libdrm-devel libjpeg-devel libvorbis-devel libtqt4-devel readline-devel update-desktop-files tde-filesystem
BuildRequires:	tde-filesystem
License:        GPLv2+
Group:          Productivity/Multimedia/Sound/Players
Summary:        Modular Software Synthesizer
PreReq:         permissions
Version:        R13.99
Release:        1
Source0:        %{name}-%{version}.tar.bz2
Source1:        artswrapper.7.gz
Source2:        baselibs.conf
Patch2:         no-informational-messages.diff
Patch5:         arts-vorbis-fix.dif
Patch7:         fortify_source.patch
Patch8:         arts-start-on-demand.diff
#Patch9:         avoid_la_files.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A modular software synthesizer that generates realtime audio streams,
includes midi support, is easily extendable, and uses CORBA for
separation of GUI and synthesis.



Authors:
--------
    Stefan Westerfeld <stefan@space.twc.de>

%package devel
License:        GPLv2+
# usefiles /opt/tde/bin/artsc-config /opt/tde/bin/mcopidl
Summary:        Include Files and Libraries mandatory for Development.
Group:          Development/Libraries/Other
Provides:       tdelibs:/opt/tde/include/artsc/artsc.h
Requires:       libtqt4-devel arts = %version glib2-devel jack-devel libogg-devel libvorbis-devel audiofile-devel libstdc++-devel
Requires:       alsa-devel tde-filesystem

%description devel
A modular software synthesizer that generates realtime audio streams,
supports MIDI, is easily extendable, and uses CORBA for separation of
the GUI and synthesis.



Authors:
--------
    Stefan Westerfeld <stefan@space.twc.de>
    
%package devel-static
License:        GPLv2+
Summary:        Include Files and Libraries mandatory for Development.
Group:          Development/Libraries/Other

%description devel-static
A modular software synthesizer that generates realtime audio streams,
supports MIDI, is easily extendable, and uses CORBA for separation of
the GUI and synthesis.



Authors:
--------
    Stefan Westerfeld <stefan@space.twc.de>

%package gmcop
License:        GPLv2+
# usesubdirs gmcop
Summary:        A Modular Software Synthesizer
Group:          Productivity/Multimedia/Sound/Players

%description gmcop
A modular software synthesizer that generates real-time audio streams,
supports midi, is easily extendable, and uses CORBA for separation of
GUI and synthesis.



Authors:
--------
    Stefan Westerfeld <stefan@space.twc.de>

%prep
%setup -qn arts-%{version}
%patch2
%patch5
%patch7
%patch8
#%patch9

%build
CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS -DNDEBUG" CFLAGS="$CXXFLAGS" %cmake_tdeusr -d build -- -DWITH_MAD=OFF -DCMAKE_SKIP_RPATH=OFF

# shut off MAD support because that is only available in packman

#%ifarch %ix86
# I trust in arts runtime checking ...
#echo "#define HAVE_X86_SSE 1" >> config.h
#%endif
# broken automake ?
#make -C flow/gsl gslconfig.h
# broken automake ?
#make %{?jobs:-j%jobs}

%make_tde -d build

%install
%makeinstall_tde -d build
%ifarch x86_64
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib
ln -sf ../lib64/mcop $RPM_BUILD_ROOT/%{_prefix}/lib/mcop
%endif
mkdir -p -m 755 $RPM_BUILD_ROOT/%_mandir/man7
cp %SOURCE1 $RPM_BUILD_ROOT/%_mandir/man7/

# unneeded
rm -rf %{buildroot}/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%run_permissions

%postun -p /sbin/ldconfig

%post gmcop -p /sbin/ldconfig

%postun gmcop
/sbin/ldconfig
%verifyscript
%verify_permissions -e %{_bindir}/artswrapper

%files
%defattr(-,root,root,755)
%doc COPYING.LIB COPYING
%dir %{_prefix}
%dir %{_bindir}
%{_bindir}/artscat
%{_bindir}/arts[dpsr]*
%verify(not mode) %{_bindir}/artswrapper
%dir %{_libdir}
%{_libdir}/libarts*.so.*
%{_libdir}/libkmedia2*.so.*
%{_libdir}/libmcop.so.*
%{_libdir}/libmcop_mt.so.*
%{_libdir}/libqtmcop.so.*
%{_libdir}/libsoundserver_idl.so.*
# these need to be in the base package for lt_dlopen()
%{_libdir}/*.so
%{_libdir}/mcop
%ifarch x86_64
%{_prefix}/lib
%endif
%{_mandir}/man7/artswrapper.7.gz

%files devel
%defattr(-,root,root)
%{_bindir}/artsc-config
%{_bindir}/mcopidl
%dir %{_includedir}
%{_includedir}/*
%{_libdir}/pkgconfig/arts.pc

%files devel-static
%defattr(-,root,root)
%{_libdir}/libartsgsl.a

%files gmcop
%defattr(-,root,root)
%{_libdir}/libgmcop.so.*

%changelog
