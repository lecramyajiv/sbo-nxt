#
# spec file for package katapult (version R14)
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
%define tde_pkg katapult
%define tde_prefix /opt/trinity
%define tde_appdir %{tde_datadir}/applications
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


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		0.3.2.1
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Faster access to applications, bookmarks, and other items.
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

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

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

%description
Katapult is an application for TDE, designed to allow faster access to
applications, bookmarks, and other items. It is plugin-based, so it can
launch anything that is has a plugin for. Its display is driven by
plugins as well, so its appearance is completely customizable. It was
inspired by Quicksilver for OS X. 


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
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}

# Removes useless files (-devel ?)
%__rm -f %{?buildroot}%{tde_libdir}/*.so
%__rm -f %{?buildroot}%{tde_libdir}/*.la

# Fix desktop files (openSUSE only)
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"
%if 0%{?suse_version}
%suse_update_desktop_file -G "Application Launcher" "%{?buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop" DesktopUtility
%endif


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/katapult
%{tde_libdir}/libkatapult.so.2
%{tde_libdir}/libkatapult.so.2.0.0
%{tde_tdelibdir}/katapult_amarokcatalog.la
%{tde_tdelibdir}/katapult_amarokcatalog.so
%{tde_tdelibdir}/katapult_bookmarkcatalog.la
%{tde_tdelibdir}/katapult_bookmarkcatalog.so
%{tde_tdelibdir}/katapult_calculatorcatalog.la
%{tde_tdelibdir}/katapult_calculatorcatalog.so
%{tde_tdelibdir}/katapult_documentcatalog.la
%{tde_tdelibdir}/katapult_documentcatalog.so
%{tde_tdelibdir}/katapult_execcatalog.la
%{tde_tdelibdir}/katapult_execcatalog.so
%{tde_tdelibdir}/katapult_glassdisplay.la
%{tde_tdelibdir}/katapult_glassdisplay.so
%{tde_tdelibdir}/katapult_googlecatalog.la
%{tde_tdelibdir}/katapult_googlecatalog.so
%{tde_tdelibdir}/katapult_o2display.la
%{tde_tdelibdir}/katapult_o2display.so
%{tde_tdelibdir}/katapult_programcatalog.la
%{tde_tdelibdir}/katapult_programcatalog.so
%{tde_tdelibdir}/katapult_puredisplay.la
%{tde_tdelibdir}/katapult_puredisplay.so
%{tde_tdelibdir}/katapult_spellcatalog.la
%{tde_tdelibdir}/katapult_spellcatalog.so
%{tde_tdeappdir}/katapult.desktop
%{tde_datadir}/icons/crystalsvg/128x128/actions/katapultspellcheck.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/katapultspellcheck.svgz
%{tde_datadir}/icons/hicolor/128x128/actions/checkmark.png
%{tde_datadir}/icons/hicolor/128x128/actions/no.png
%{tde_datadir}/icons/hicolor/128x128/apps/xcalc.png
%{tde_datadir}/icons/hicolor/*/apps/katapult.png
%{tde_datadir}/icons/hicolor/scalable/apps/katapult.svgz
%{tde_datadir}/services/katapult_amarokcatalog.desktop
%{tde_datadir}/services/katapult_bookmarkcatalog.desktop
%{tde_datadir}/services/katapult_calculatorcatalog.desktop
%{tde_datadir}/services/katapult_documentcatalog.desktop
%{tde_datadir}/services/katapult_execcatalog.desktop
%{tde_datadir}/services/katapult_glassdisplay.desktop
%{tde_datadir}/services/katapult_googlecatalog.desktop
%{tde_datadir}/services/katapult_o2display.desktop
%{tde_datadir}/services/katapult_programcatalog.desktop
%{tde_datadir}/services/katapult_puredisplay.desktop
%{tde_datadir}/services/katapult_spellcatalog.desktop
%{tde_datadir}/servicetypes/katapultcatalog.desktop
%{tde_datadir}/servicetypes/katapultdisplay.desktop
%{tde_mandir}/man1/*.1*
%{tde_tdedocdir}/HTML/en/katapult/


%changelog
