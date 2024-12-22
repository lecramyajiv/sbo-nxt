#
# spec file for package libdbus-1-tqt0
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


Name:           libdbus-1-tqt0
Url:            http://www.freedesktop.org/wiki/Software/DBusBindings
%define appname dbus-1-tqt
BuildRequires:  dbus-1-devel libtqt4-devel cmake
License:        GPL v2 or later
Group:          Development/Libraries/C and C++
AutoReqProv:    on
Version:        R13.99
Release:        1
Summary:        TQt DBus Bindings
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{appname}-%{version}.tar.bz2
Provides:	libdbus-1-tqt-0

%description
This library provides TQt-classes for accessing the DBus

Authors:
--------
    Kevin Krammer <kevin.krammer@gmx.at>

%package devel
License:        GPL v2 or later
Summary:        Development files for libdbus-1-tqt
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       dbus-1-devel libtqt4-devel

%description devel
This library provides TQt-classes for accessing the DBus.

This package holds the development files for libdbus-1-tqt.



Authors:
--------
    Kevin Krammer <kevin.krammer@gmx.at>

%package -n dbusxml2qt3
License:        GPL v2 or later
Summary:        Generate Qt3-classes from DBus-introspection data
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description -n dbusxml2qt3
dbusxml2tqt allows to generate TQt-compatible Qt3 classes from DBus-introspection data



Authors:
--------
    Kevin Krammer <kevin.krammer@gmx.at>

%prep
%setup -n %{appname}-%{version} -q

%build
mkdir build
cd build
  cmake -DCMAKE_SKIP_RPATH=ON \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \
        -DLIBEXEC_INSTALL_DIR:PATH=%{_libexecdir} \
        -DLIB_SUFFIX=`$(echo %_lib | cut -b4-)` \
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig \
        -DMAN_INSTALL_DIR=%{_mandir} \
        -DINFO_INSTALL_DIR=%{_infodir} \
        ../

%{__make} %{?jobs:-j%jobs}

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT
#install -D -m 0755 ./tools/dbusxml2qt3/dbusxml2qt3 $RPM_BUILD_ROOT%{_bindir}/dbusxml2tqt
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING INSTALL
%{_libdir}/libdbus-1-tqt.so.0
%{_libdir}/libdbus-1-tqt.so.0.0.0

%files devel
%defattr(-,root,root)
%{_libdir}/libdbus-1-tqt.so
%{_includedir}/tqdbusconnection.h
%{_includedir}/tqdbusdata.h
%{_includedir}/tqdbusdataconverter.h
%{_includedir}/tqdbusdatalist.h
%{_includedir}/tqdbusdatamap.h
%{_includedir}/tqdbuserror.h
%{_includedir}/tqdbusmacros.h
%{_includedir}/tqdbusmessage.h
%{_includedir}/tqdbusobject.h
%{_includedir}/tqdbusobjectpath.h
%{_includedir}/tqdbusproxy.h
%{_includedir}/tqdbusvariant.h
%{_libdir}/pkgconfig/dbus-1-tqt.pc

%files -n dbusxml2qt3
%defattr(-,root,root)
%{_bindir}/dbusxml2qt3

%changelog

