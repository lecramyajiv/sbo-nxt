#
# spec file for package kasablanca (version R14)
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
%define tde_pkg kasablanca
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
Version:		0.4.0.2
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Graphical FTP client for Trinity
Group:			Applications/Internet 
Url:			http://kasablanca.berlios.de/ 

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

BuildRequires:	gettext 

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

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

# UTEMPTER support
%if 0%{?suse_version}
BuildRequires:	utempter-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}utempter-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
%if 0%{?rhel} == 4
%else
BuildRequires:	libutempter-devel
%endif
%endif

%description
Kasablanca is an ftp client, among its features are currently: 
* ftps encryption via AUTH TLS
* fxp (direct server to server transfer), supporting alternative mode.
* advanced bookmarking system.
* fast responsive multithreaded engine.
* concurrent connections to multiple hosts.
* interactive transfer queue, movable by drag and drop.
* small nifty features, like a skiplist.


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
%__rm -rf $RPM_BUILD_ROOT 
%__make install DESTDIR=$RPM_BUILD_ROOT -C build

# locale's
%find_lang %{tde_pkg}

# Fix desktop files (openSUSE only)
%if 0%{?suse_version}
%suse_update_desktop_file kasablanca Network FileTransfer
%endif


%clean
%__rm -rf $RPM_BUILD_ROOT 


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md
%{tde_bindir}/kasablanca
%{tde_datadir}/apps/kasablanca/
%{tde_datadir}/config.kcfg/kbconfig.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kasablanca.png
%{tde_tdedocdir}/HTML/en/kasablanca/
%{tde_tdeappdir}/kasablanca.desktop
%{tde_mandir}/man1/kasablanca.*


%changelog
