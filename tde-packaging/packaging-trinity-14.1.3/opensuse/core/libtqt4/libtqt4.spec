#
# spec file for package tqtinterface
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

Name:		libtqt4
License:	GPLv2+
Group:		Graphical Desktop/TDE
Summary:	Interface and abstraction library for Qt and Trinity
Version:	R13.99
Release:	1
Source0:	tqtinterface-%{version}.tar.bz2
URL:		http://www.trinitydesktop.org/

BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%define with_qt3 1
%define with_qt4 0

%if %{with_qt3}
BuildRequires: qt3-devel >= 3.4.0
Requires: qt3 >= 3.4.0
%endif

%if %{with_qt4}
BuildRequires: libqt4-devel >= 4.8.0
Requires: libqt4-x11 >= 4.8.0
%endif

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: gcc-c++

%description
This package includes libraries that abstract the underlying Qt system
from the actual Trinity code, allowing easy, complete upgrades to new
versions of Qt.

It also contains various functions that have been removed from newer
versions of Qt, but are completely portable and isolated from other
APIs such as Xorg. This allows the Trinity project to efficiently
perform certain operations that are infeasible or unneccessarily
difficult when using pure Qt4 or above.

Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    Robert Xu <rxu@lincomlinux.org>
    Tim Williams <tim@my-place.org.uk>
    Serghei Amelian <serghei@thel.ro>

%package devel
Summary: TQtinterface header files
Group: Development/Libraries/TDE
Requires: libtqt4 = %{version}
%if %{with_qt3}
Requires: qt3-devel >= 3.4.0
%endif
%if %{with_qt4}
Requires: libqt4-devel >= 4.8.0
%endif
%description devel
This package contains Trinity specific window options and commands.
You need this package to compile Trinity modules. (TQT headers)


Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    Robert Xu <rxu@lincomlinux.org>
    Tim Williams <tim@my-place.org.uk>
    Serghei Amelian <serghei@thel.ro>


%prep
%setup -qn tqtinterface-%{version}

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;
mkdir build
cd build
cmake \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
	-DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
	-DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
%if "%{?_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DBUILD_SHARED_LIBS:BOOL=ON \
%if %{with_qt3}
	-DQT_VERSION=3 \
%endif
%if %{with_qt4}
	-DQT_VERSION=4 \
%endif
	-DQT_LIBRARY_DIRS=/usr/lib/qt3/%{_lib} \
	-DQT_INCLUDE_DIRS=/usr/lib/qt3/include \
	-DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig \
	../

make %{?_smp_mflags} VERBOSE=1

%install
cd build
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{_libdir}/*.la

# What is this? Leftovers?!
rm -rf %{buildroot}/%{_libdir}/debug

# Shebang, please.
echo "#!/bin/bash" > %{buildroot}%{_bindir}/convert_qt_tqt1.new
cat %{buildroot}%{_bindir}/convert_qt_tqt1 >> %{buildroot}%{_bindir}/convert_qt_tqt1.new
rm -f %{buildroot}%{_bindir}/convert_qt_tqt1
mv -v %{buildroot}%{_bindir}/convert_qt_tqt1.new %{buildroot}%{_bindir}/convert_qt_tqt1
chmod +x %{buildroot}%{_bindir}/convert_qt_tqt1


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,755)
%{_libdir}/libtqt.so.*
%{_libdir}/libtqassistantclient.so.*

%files devel
%defattr(-,root,root,755)
%dir %{_includedir}/Qt
%{_includedir}/Qt/q*.h
%{_includedir}/tq*.h
%{_libdir}/pkgconfig/tqt.pc
%{_libdir}/pkgconfig/tqtqui.pc
%{_libdir}/libtqt.so
%{_libdir}/libtqassistantclient.so
%{_bindir}/convert_qt_tqt1
%{_bindir}/convert_qt_tqt2
%{_bindir}/convert_qt_tqt3
%{_bindir}/dcopidl-tqt
%{_bindir}/dcopidl2cpp-tqt
%{_bindir}/dcopidlng-tqt
%{_bindir}/mcopidl-tqt
%{_bindir}/moc-tqt
%{_bindir}/tmoc
%{_bindir}/tqt-replace
%{_bindir}/tqt-replace-stream
%{_bindir}/uic-tqt

%changelog
