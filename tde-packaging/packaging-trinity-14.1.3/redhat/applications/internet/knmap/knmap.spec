#
# spec file for package knmap (version R14)
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
%define tde_pkg knmap
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
Version:	2.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	An NMAP frontend for TDE
Group:		Applications/Internet
URL:		http://sourceforge.net/projects/knmap/

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
BuildRequires:	libtool

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

# NMAP support
Requires:		nmap


%description
Knmap is a TDE-based interface to the 'nmap' facility.

The main Knmap window provides for the entry of nmap options and the
display of nmap-generated output.

This program is a complete re-write of one by the same name written by
Alexandre Sagala. The last version of that program was 0.9 which was
released on 2003-03-09 and targeted the KDE 2.2 and QT 2.3 environments.

Not to mention that it did not cater for the full set of 'nmap' options.
Or, perhaps, 'nmap' progressed whilst that version of Knmap languished.

http://www.kde-apps.org/content/show.php?content=31108


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
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT -C build

%find_lang %{tde_pkg}

# Move desktop icon to XDG directory
if [ -d "%{buildroot}%{tde_datadir}/applnk" ]; then
  %__mkdir_p %{buildroot}%{tde_tdeappdir}
  %__mv "%{buildroot}%{tde_datadir}/applnk/"*"/%{tde_pkg}.desktop" "%{buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"
  %__rm -r "%{buildroot}%{tde_datadir}/applnk"
fi

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r %{tde_pkg} TDE System Network
%endif


%clean
%__rm -rf $RPM_BUILD_ROOT


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md ChangeLog
%{tde_bindir}/knmap
%{tde_tdeappdir}/knmap.desktop
%{tde_datadir}/apps/knmap/
%{tde_tdedocdir}/HTML/en/knmap/
%{tde_datadir}/icons/hicolor/*/apps/knmap.png
%{tde_datadir}/icons/hicolor/*/apps/knmapman.png
%{tde_datadir}/icons/hicolor/*/apps/localman.png
%{tde_datadir}/icons/hicolor/*/apps/manpage.png
%{tde_datadir}/icons/hicolor/*/apps/manstylesheet.png
%{tde_datadir}/icons/hicolor/*/apps/profilecopy.png
%{tde_datadir}/icons/hicolor/*/apps/profiledelete.png
%{tde_datadir}/icons/hicolor/*/apps/profileload.png
%{tde_datadir}/icons/hicolor/*/apps/profilerename.png
%{tde_datadir}/icons/hicolor/*/apps/profilesave.png
%{tde_datadir}/icons/hicolor/*/apps/profilesaveas.png
%{tde_datadir}/icons/hicolor/*/apps/scanclose.png
%{tde_datadir}/icons/hicolor/*/apps/scanduplicate.png
%{tde_datadir}/icons/hicolor/*/apps/scannew.png
%{tde_datadir}/icons/hicolor/*/apps/scanrename.png
%{tde_datadir}/icons/hicolor/*/apps/zoomcustom.png
%{tde_datadir}/icons/hicolor/*/apps/zoomin.png
%{tde_datadir}/icons/hicolor/*/apps/zoomout.png
%{tde_mandir}/man1/*.1*


%changelog
