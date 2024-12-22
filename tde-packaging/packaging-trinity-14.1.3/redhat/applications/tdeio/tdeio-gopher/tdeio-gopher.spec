#
# spec file for package tdeio-gopher (version R14)
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
%define tde_pkg tdeio-gopher
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


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.1.4
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	tdeio-slave for the gopher protocol
Group:		Productivity/Networking/Ftp/Clients
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# IDN support
BuildRequires:	libidn-devel

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif


%description
Adds support for the "gopher:" protocol
to Konqueror and other TDE applications.

This enables you to perform gopher searches in Konqueror.

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
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

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
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL=ON \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang tdeio_gopher


%clean
%__rm -rf %{?buildroot}


%files -f tdeio_gopher.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING FAQ README VERSION
%{tde_tdelibdir}/tdeio_gopher.la
%{tde_tdelibdir}/tdeio_gopher.so
%{tde_datadir}/services/gopher.protocol
%lang(ca) %{tde_tdedocdir}/HTML/ca/tdeioslave/
%lang(da) %{tde_tdedocdir}/HTML/da/tdeioslave/
%lang(de) %{tde_tdedocdir}/HTML/de/tdeioslave/
%lang(en) %{tde_tdedocdir}/HTML/en/tdeioslave/
%lang(en_GB) %{tde_tdedocdir}/HTML/en_GB/tdeioslave/
%lang(es) %{tde_tdedocdir}/HTML/es/tdeioslave/
%lang(et) %{tde_tdedocdir}/HTML/et/tdeioslave/
%lang(fr) %{tde_tdedocdir}/HTML/fr/tdeioslave/
%lang(gl) %{tde_tdedocdir}/HTML/gl/tdeioslave/
%lang(hu) %{tde_tdedocdir}/HTML/hu/tdeioslave/
%lang(it) %{tde_tdedocdir}/HTML/it/tdeioslave/
%lang(nl) %{tde_tdedocdir}/HTML/nl/tdeioslave/
%lang(pl) %{tde_tdedocdir}/HTML/pl/tdeioslave/
%lang(pt) %{tde_tdedocdir}/HTML/pt/tdeioslave/
%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/tdeioslave/
%lang(ro) %{tde_tdedocdir}/HTML/ro/tdeioslave/
%lang(ru) %{tde_tdedocdir}/HTML/ru/tdeioslave/
%lang(sk) %{tde_tdedocdir}/HTML/sk/tdeioslave/
%lang(sr) %{tde_tdedocdir}/HTML/sr/tdeioslave/
%lang(sr@Latn) %{tde_tdedocdir}/HTML/sr@Latn/tdeioslave/
%lang(sv) %{tde_tdedocdir}/HTML/sv/tdeioslave/
%lang(uk) %{tde_tdedocdir}/HTML/uk/tdeioslave/


%changelog
