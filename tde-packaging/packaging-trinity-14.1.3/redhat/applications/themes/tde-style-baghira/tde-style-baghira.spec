#
# spec file for package tde-style-baghira (version R14)
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
%define tde_pkg tde-style-baghira
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
Version:	0.8
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDE style for Apple junkies :)
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
BuildRequires:          %{libjpeg}-devel
%else
BuildRequires:          jpeg-devel
%endif

%description
Based upon mosfet-liquid0.9.6pre4... the last heir of mosfet.
Baghira includes both an style (custom widgets) and twin decoration as
well as colour schemes.

Baghira (panther, in german) makes TDE resemble Apple's MacOS X's Aqua,
Panther and Jaguar looks, and also includes its own 'Baghira' look


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
%{tde_bindir}/bab
%{tde_libdir}/libbaghirastarter.la
%{tde_libdir}/libbaghirastarter.so
%{tde_tdelibdir}/b_menu_panelapplet.la
%{tde_tdelibdir}/b_menu_panelapplet.so
%{tde_tdelibdir}/plugins/styles/baghira.la
%{tde_tdelibdir}/plugins/styles/baghira.so
%{tde_tdelibdir}/tdestyle_baghira_config.la
%{tde_tdelibdir}/tdestyle_baghira_config.so
%{tde_tdelibdir}/twin3_baghira.la
%{tde_tdelibdir}/twin3_baghira.so
%{tde_tdelibdir}/twin_baghira_config.la
%{tde_tdelibdir}/twin_baghira_config.so
%{tde_libdir}/usermanager_panelapplet.la
%{tde_libdir}/usermanager_panelapplet.so
%{tde_tdeappdir}/bab.desktop
%{tde_datadir}/apps/baghira/
%{tde_datadir}/apps/kicker/applets/baghira-starter.desktop
%{tde_datadir}/apps/kicker/applets/baghira-usermanager.desktop
%{tde_datadir}/apps/tdedisplay/color-schemes/AquaBlue.kcsrc
%{tde_datadir}/apps/tdedisplay/color-schemes/AquaGraphite.kcsrc
%{tde_datadir}/apps/tdestyle/themes/baghira.themerc
%{tde_datadir}/apps/twin/baghira.desktop
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/128x128/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/16x16/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter_down.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter_hover.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_itunes.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_jaguar.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_milk.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_panther.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bab_tiger.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/22x22/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/32x32/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/48x48/apps/baghira_yellow.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_blue.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_grey.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_white.png
%{tde_datadir}/icons/crystalsvg/64x64/apps/baghira_yellow.png
%lang(de) %{tde_datadir}/locale/de/LC_MESSAGES/baghira-starter.mo
%lang(pl) %{tde_datadir}/locale/pl/LC_MESSAGES/baghira-usermanager.mo
%lang(pt_BR) %{tde_datadir}/locale/pt_BR/LC_MESSAGES/baghira-usermanager.mo
%lang(ru) %{tde_datadir}/locale/ru/LC_MESSAGES/baghira-kmenuapplet.mo
%lang(ru) %{tde_datadir}/locale/ru/LC_MESSAGES/baghira-switcher.mo
%{tde_mandir}/man1/bab.1*


%changelog
