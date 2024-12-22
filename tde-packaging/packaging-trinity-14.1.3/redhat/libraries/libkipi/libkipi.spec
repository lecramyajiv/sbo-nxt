#
# spec file for package libkipi (version R14)
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
%define tde_pkg libkipi
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libkipi %{_lib}kipi
%else
%define libkipi libkipi
%endif


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.1.5
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Library for apps that want to use kipi-plugins (runtime version) [Trinity]
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires: trinity-tdelibs-devel >= %{tde_version}

BuildRequires: desktop-file-utils
BuildRequires: pkgconfig
BuildRequires: gettext
BuildRequires: gcc-c++

# LCMS support
%if 0%{?suse_version} || 0%{?rhel} >= 7
BuildRequires: liblcms-devel
%else
BuildRequires: lcms-devel
%endif

# JPEG support
%if 0%{?mdkver}
%define libjpeg %{_lib}jpeg
%else
%define libjpeg libjpeg
%endif
BuildRequires: %{libjpeg}-devel

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# IDN support
BuildRequires:	libidn-devel

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# CMAKE
BuildRequires:	trinity-tde-cmake >= %{tde_version}

%description
Libkipi is a library
- that contains common routines and widget used by kipi-plugins
- to ease implementation of the kipi-plugins interface in an application
  that wants to use kipi-plugins
    
Homepage: http://www.kipi-plugins.org/

##########

%package -n trinity-%{libkipi}0
Summary:	library for apps that want to use kipi-plugins (runtime version) [Trinity]
Group:		System/Libraries

Obsoletes:	trinity-%{tde_pkg} < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-%{tde_pkg} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-%{libkipi}0
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
Homepage: http://www.kipi-plugins.org/

%files -n trinity-%{libkipi}0 -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_libdir}/libkipi.so.0
%{tde_libdir}/libkipi.so.0.1.1
%{tde_datadir}/apps/kipi/
%{tde_datadir}/icons/hicolor/*/apps/kipi.png
%{tde_datadir}/servicetypes/kipiplugin.desktop

##########

%package -n trinity-%{libkipi}-devel
Group:		Development/Libraries/Other
Summary:	library for apps that want to use kipi-plugins (development version) [Trinity]
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-%{tde_pkg}-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-%{tde_pkg}-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-%{libkipi}-devel
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
This package contains development files and documentation for libkipi library.
Homepage: http://www.kipi-plugins.org/

%files -n trinity-%{libkipi}-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkipi.so
%{tde_libdir}/libkipi.la
%{tde_tdeincludedir}/libkipi/
%{tde_libdir}/pkgconfig/libkipi.pc

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
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DDATA_INSTALL_DIR="%{tde_datadir}/apps" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DSERVICETYPES_INSTALL_DIR="%{tde_datadir}/servicetypes" \
  -DICON_INSTALL_DIR="%{tde_datadir}/icons" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL=ON \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  \
  ..


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%changelog
