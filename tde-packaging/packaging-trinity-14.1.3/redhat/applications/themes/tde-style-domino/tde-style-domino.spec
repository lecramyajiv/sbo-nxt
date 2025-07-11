#
# spec file for package domino (version R14)
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
%define tde_pkg tde-style-domino
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

# Required for Mageia and PCLinuxOS: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.4
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Domino widget style and twin decoration for TDE
Group:		Graphical desktop/TDE
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

BuildRequires:          trinity-tdelibs-devel >= %{tde_version}
BuildRequires:          trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	libtool

# JPEG support
%if 0%{?mdkver}
%define libjpeg %{_lib}jpeg
%else
%define libjpeg libjpeg
%endif
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version}
BuildRequires:	%{libjpeg}-devel
%else
BuildRequires:	jpeg-devel
%endif

%description
Domino is a style with a soft look. It allows to fine adjust the shininess
of the widgets by customizable color gradients.


%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
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
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DDATA_INSTALL_DIR=%{tde_datadir}/apps \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%clean
%__rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{tde_tdelibdir}/plugins/styles/domino.la
%{tde_tdelibdir}/plugins/styles/domino.so
%{tde_tdelibdir}/tdestyle_domino_config.la
%{tde_tdelibdir}/tdestyle_domino_config.so
%{tde_tdelibdir}/twin3_domino.la
%{tde_tdelibdir}/twin3_domino.so
%{tde_tdelibdir}/twin_domino_config.la
%{tde_tdelibdir}/twin_domino_config.so
%{tde_datadir}/apps/tdedisplay/color-schemes/Domino.kcsrc
%{tde_datadir}/apps/tdestyle/themes/domino.themerc
%{tde_datadir}/apps/twin/domino.desktop
%lang(de) %{tde_datadir}/locale/de/LC_MESSAGES/tdestyle_domino_config.mo


%changelog
