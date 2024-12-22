#
# spec file for package kaffeine-mozilla (version R14)
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

# Default version for this component
%define tde_pkg kaffeine-mozilla
%define tde_prefix /opt/trinity
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

%if 0%{?fedora} >= 27 || 0%{?mgaversion} >= 7 || 0%{?rhel} >= 8
%define debug_package %{nil}
%endif

Name:			trinity-%{tde_pkg}
Summary:		mozilla plugin that lanches kaffeine for supported media types [Trinity]
Version:		0.4.3.1
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}

License:		GPLv2+
Group:			Applications/Multimedia

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

%if 0%{?suse_version}
BuildRequires:	mozilla-nspr-devel
%else
%if 0%{?mdkver}
BuildRequires:	%{_lib}nspr-devel
%else
BuildRequires:	nspr-devel
%endif
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xaw-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXaw-devel
%endif

Requires:		trinity-kaffeine

%description
This mozilla plugin launches kaffeine, the xine-based media player for TDE,
when a page containing a supported media format is loaded.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

if [ -d "%{_includedir}/nspr4" ]; then
  RPM_OPT_FLAGS="-I%{_includedir}/nspr4 ${RPM_OPT_FLAGS}"
fi

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
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Remove useless filess
%__rm -f %{?buildroot}%{_libdir}/mozilla/plugins/kaffeineplugin.a


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
# These files are installed outside TDE prefix
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%{_libdir}/mozilla/plugins/kaffeineplugin.la
%{_libdir}/mozilla/plugins/kaffeineplugin.so


%changelog
