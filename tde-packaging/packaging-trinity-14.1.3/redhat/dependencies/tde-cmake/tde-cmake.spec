#
# spec file for package cmake-trinity (version R14)
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
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg tde-cmake

%if 0%{?rhel} == 6 || 0%{?rhel} == 7
%define cmake_datadir %{_datadir}/cmake3
%else
%define cmake_datadir %{_datadir}/cmake
%endif


Name:		trinity-%{tde_pkg}
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDE CMake modules
Group:		Development/Libraries/C and C++
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	cmake
BuildRequires:	desktop-file-utils

Requires:		cmake

Obsoletes:		trinity-cmake < %{version}-%{release}
Provides:		trinity-cmake = %{version}-%{release}

%description
TDE uses its own set of modules and macros to simplify CMake rules.

This also includes the TDEL10n module that is used to generate and
update templates for translations and the modified version of
intltool-merge used to merge translations into desktop files.


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
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL="ON" \
  -DWITH_ALL_OPTIONS="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install -C build DESTDIR=%{?buildroot}


%clean
%__rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{cmake_datadir}/Modules/FindTDE.cmake
%{cmake_datadir}/Modules/FindTQt.cmake
%{cmake_datadir}/Modules/FindTQtQUI.cmake
%{cmake_datadir}/Modules/TDEL10n.cmake
%{cmake_datadir}/Modules/TDEMacros.cmake
%{cmake_datadir}/Modules/TDESetupPaths.cmake
%{cmake_datadir}/Modules/TDEVersion.cmake
%{cmake_datadir}/Modules/tde_automoc.cmake
%{cmake_datadir}/Modules/tde_l10n_merge.pl
%{cmake_datadir}/Modules/tde_uic.cmake
%{cmake_datadir}/Templates/tde_dummy_cpp.cmake
%{cmake_datadir}/Templates/tde_export_library.cmake
%{cmake_datadir}/Templates/tde_libtool_file.cmake
%{cmake_datadir}/Templates/tde_tdeinit_executable.cmake
%{cmake_datadir}/Templates/tde_tdeinit_module.cmake


%changelog
