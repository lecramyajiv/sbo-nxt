#
# spec file for package tqtinterface (version R14)
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
%define tde_pkg tqtinterface

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libtqt4 %{_lib}tqt4
%else
%define libtqt4 libtqt4
%endif

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	4.2.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	The Trinity Qt Interface Libraries
Group:		System/GUI/Other
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	libtqt3-mt-devel >= 3.5.0
BuildRequires:	tqt3-dev-tools >= 3.5.0
BuildRequires:	trinity-tde-cmake >= %{tde_version}

BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# UUID support
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 6
%define uuid_devel libuuid-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%define uuid_devel %{_lib}uuid-devel
%endif
%if 0%{?rhel} == 5
%define uuid_devel e2fsprogs-devel
%endif
%{?uuid_devel:BuildRequires: %{uuid_devel}}

# PTHREAD support
%if 0%{?mdkversion} || 0%{?mgaversion}
%if 0%{?mgaversion} >= 7 || 0%{?mdkversion}
BuildRequires:	%{_lib}npth-devel
%else
BuildRequires:	pth-devel
%endif
%endif
%if 0%{?fedora} && 0%{?fedora} <= 26
BuildRequires:	pth-devel
%endif
%if 0%{?rhel} >= 5 && 0%{?rhel} <= 7
BuildRequires:	pth-devel
%endif
%if 0%{?suse_version} && 0%{?suse_version} < 1500
BuildRequires:	libpth-devel
%endif

# MESA support
%if 0%{?fedora} || 0%{?rhel}
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
%endif
%if 0%{?mgaversion} || 0%{?pclinuxos}
BuildRequires: %{_lib}mesaglu1-devel
%endif
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}glu-devel
%endif
%if 0%{?suse_version}
BuildRequires: Mesa-libGL-devel
BuildRequires: Mesa-libGLU-devel
%endif

# X11 libraries
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%endif
%if 0%{?suse_version} >= 1220 || 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	libXi-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%endif

%description
The Trinity Qt Interface is a library that abstracts Qt from Trinity.
This allows the Trinity code to rapidly port from one version of Qt to another.
This is primarily accomplished by defining old functions in terms of new functions,
although some code has been added for useful functions that are no longer part of Qt.


##########

%package -n %{libtqt4}
Group:		System/GUI/Other
Summary:	The Trinity Qt Interface Libraries
Provides:	libtqt4 = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	libtqt3-mt >= 3.5.0

Obsoletes:	trinity-tqtinterface < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tqtinterface = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libtqt4}
The Trinity Qt Interface is a library that abstracts Qt from Trinity.
This allows the Trinity code to rapidly port from one version of Qt to another.
This is primarily accomplished by defining old functions in terms of new functions,
although some code has been added for useful functions that are no longer part of Qt.

%files -n %{libtqt4}
%defattr(-,root,root,-)
%{_libdir}/libtqt.so.4
%{_libdir}/libtqt.so.4.2.0

%post -n %{libtqt4}
/sbin/ldconfig || :

%postun -n %{libtqt4}
/sbin/ldconfig || :

##########

%package -n %{libtqt4}-devel
Group:		Development/Libraries/X11
Summary:	The Trinity Qt Interface Libraries (Development Files)
Provides:	libtqt4-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	%{libtqt4} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libtqt3-mt-devel >= 3.5.0
Requires:	tqt3-dev-tools >= 3.5.0
Requires:	trinity-tde-cmake >= %{version}-%{release}

Obsoletes:	trinity-tqtinterface-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tqtinterface-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libtqt4}-devel
The Trinity Qt Interface is a library that abstracts Qt from Trinity.
This allows the Trinity code to rapidly port from one version of Qt to another.
This is primarily accomplished by defining old functions in terms of new functions,
although some code has been added for useful functions that are no longer part of Qt.

%post -n %{libtqt4}-devel
/sbin/ldconfig || :

%postun -n %{libtqt4}-devel
/sbin/ldconfig || :

%files -n %{libtqt4}-devel
%defattr(-,root,root,-)
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
%{_bindir}/uic-tqt
%{_includedir}/tqt/
%{_libdir}/libtqt.la
%{_libdir}/libtqt.so
%{_libdir}/pkgconfig/tqt.pc
%{_libdir}/pkgconfig/tqtqui.pc

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
  -DQTDIR="%{_datadir}/tqt3" \
  -DQT_INCLUDE_DIR="%{_includedir}/tqt3" \
  -DQT_LIBRARY_DIR="%{_libdir}" \
  \
  -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
  -DPKGCONFIG_INSTALL_DIR="%{_libdir}/pkgconfig" \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/tqt \
  -DLIB_INSTALL_DIR=%{_libdir} \
  -DBIN_INSTALL_DIR=%{_bindir} \
  \
  -DCMAKE_LIBRARY_PATH="%{_libdir}" \
  -DCMAKE_INCLUDE_PATH="%{_includedir}" \
  \
  -DWITH_QT3="ON" \
  -DBUILD_ALL="ON" \
  -DUSE_QT3="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf "%{?buildroot}"
%__make install DESTDIR="%{?buildroot}" -C build


%clean
%__rm -rf "%{?buildroot}"


%changelog
