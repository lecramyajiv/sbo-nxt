#
# spec file for package libdbus-tqt-1-0
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


Name:           libdbus-tqt-1-0
BuildRequires:  dbus-1 dbus-1-devel libtqt4-devel cmake
URL:            http://dbus.freedesktop.org/
License:        GPLv2+
Group:          Development/Libraries/TDE
Version:        R13.99
Release:        1
AutoReqProv:    on
Summary:        TQt/KDE bindings for D-Bus
Source0:        dbus-tqt-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         dbus-qt3-compile-fix-thoenig-01.patch
Patch1:         dbus-qt3-do-not-close-shared-connection-thoenig-01.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       dbus-1 >= %( echo `rpm -q --queryformat '%{VERSION}-%{RELEASE}' dbus-1`)
Provides:       dbus-tqt

%package devel
License:        Other uncritical OpenSource License
Summary:        Developer package for TQt/KDE bindings for D-Bus
Requires:       dbus-1 >= %( echo `rpm -q --queryformat '%{VERSION}-%{RELEASE}' dbus-1`)
Requires:       dbus-1-devel >= %( echo `rpm -q --queryformat '%{VERSION}-%{RELEASE}' dbus-1-devel`)
Requires:       %{name} = %{version}
Provides:       dbus-tqt-devel
AutoReqProv:    on
Group:          Development/Libraries/TDE

%description
TQt/KDE bindings for D-Bus.



Authors:
--------
    Olivier Andrieu <oliv__a@users.sourceforge.net>
    Philip Blundell <pb@nexus.co.uk>
    Anders Carlsson <andersca@gnome.org>
    Kristian Hogsberg  <krh@redhat.com>
    Alex Larsson <alexl@redhat.com>
    Michael Meeks <michael@ximian.com>
    Seth Nickell <seth@gnome.org>
    Havoc Pennington <hp@redhat.com>
    Harri Porten <porten@kde.org>
    Matthew Rickard <mjricka@epoch.ncsc.mil>
    Zack Rusin <zack@kde.org>
    Joe Shaw <joe@assbarn.com>
    Colin Walters <walters@gnu.org>
    David Zeuthen <david@fubar.dk>

%description devel
Developer package for TQt/KDE bindings for D-Bus.



Authors:
--------
    Olivier Andrieu <oliv__a@users.sourceforge.net>
    Philip Blundell <pb@nexus.co.uk>
    Anders Carlsson <andersca@gnome.org>
    Kristian Hogsberg  <krh@redhat.com>
    Alex Larsson <alexl@redhat.com>
    Michael Meeks <michael@ximian.com>
    Seth Nickell <seth@gnome.org>
    Havoc Pennington <hp@redhat.com>
    Harri Porten <porten@kde.org>
    Matthew Rickard <mjricka@epoch.ncsc.mil>
    Zack Rusin <zack@kde.org>
    Joe Shaw <joe@assbarn.com>
    Colin Walters <walters@gnu.org>
    David Zeuthen <david@fubar.dk>

%prep
%setup -n dbus-tqt-%{version} -q
#%patch0 -p0
#%patch1 -p0

%build
RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -fstack-protector -fno-strict-aliasing -fPIC"
export CFLAGS="${RPM_OPT_FLAGS}"
export CXXFLAGS="${RPM_OPT_FLAGS}"
mkdir build
cd build
  cmake -DCMAKE_SKIP_RPATH=ON \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
      -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
      -DLIB_INSTALL_DIR:PATH=%{_libdir} \
      -DLIBEXEC_INSTALL_DIR:PATH=%{_libexecdir} \
      -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
      -DCMAKE_VERBOSE_MAKEFILE=ON \
      -DQT_LIBRARY_DIRS=/usr/lib/qt3/%{_lib} \
      -DQT_INCLUDE_DIRS=/usr/lib/qt3/include \
      -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig \
      -DMAN_INSTALL_DIR=%{_mandir} \
      ../
make

%install
cd build
make DESTDIR=%{buildroot} install

%post
%{run_ldconfig}

%postun
%{run_ldconfig}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root)
%{_libdir}/libdbus-tqt-1.so.0*

%files devel
%defattr(-, root, root)
%dir %{_includedir}/dbus-1.0
%dir %{_includedir}/dbus-1.0/dbus
%{_includedir}/dbus-1.0/dbus/connection.h
%{_includedir}/dbus-1.0/dbus/dbus-qt.h
%{_includedir}/dbus-1.0/dbus/message.h
%{_includedir}/dbus-1.0/dbus/server.h
%{_libdir}/libdbus-tqt-1.la
%{_libdir}/libdbus-tqt-1.so
%{_libdir}/pkgconfig/dbus-tqt.pc

%changelog
