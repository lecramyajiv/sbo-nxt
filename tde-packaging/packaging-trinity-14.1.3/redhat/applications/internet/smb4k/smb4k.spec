#
# spec file for package smb4k (version R14)
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
%define tde_pkg smb4k
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
Version:	0.9.4
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	A Samba (SMB) share advanced browser for Trinity
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org

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
BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif


%description
Smb4K is a SMB (Windows) share browser for TDE. It uses the Samba software 
suite to access the SMB shares of the local network neighborhood. Its purpose
is to provide a program that's easy to use and has as many features as 
possible.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/smb4k
%{tde_bindir}/smb4k_cat
%{tde_bindir}/smb4k_kill
%{tde_bindir}/smb4k_mount
%{tde_bindir}/smb4k_mv
%{tde_bindir}/smb4k_umount
%{tde_libdir}/libsmb4kcore.so.2
%{tde_libdir}/libsmb4kcore.so.2.0.0
%{tde_libdir}/libsmb4kdialogs.la
%{tde_libdir}/libsmb4kdialogs.so
%{tde_tdelibdir}/konqsidebar_smb4k.la
%{tde_tdelibdir}/konqsidebar_smb4k.so
%{tde_tdelibdir}/libsmb4tdeconfigdialog.la
%{tde_tdelibdir}/libsmb4tdeconfigdialog.so
%{tde_tdelibdir}/libsmb4knetworkbrowser.la
%{tde_tdelibdir}/libsmb4knetworkbrowser.so
%{tde_tdelibdir}/libsmb4ksearchdialog.la
%{tde_tdelibdir}/libsmb4ksearchdialog.so
%{tde_tdelibdir}/libsmb4ksharesiconview.la
%{tde_tdelibdir}/libsmb4ksharesiconview.so
%{tde_tdelibdir}/libsmb4kshareslistview.la
%{tde_tdelibdir}/libsmb4kshareslistview.so
%{tde_tdeappdir}/smb4k.desktop
%{tde_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{tde_datadir}/apps/smb4k/
%{tde_datadir}/apps/smb4knetworkbrowserpart/
%{tde_datadir}/apps/smb4ksharesiconviewpart/
%{tde_datadir}/apps/smb4kshareslistviewpart/
%{tde_datadir}/config.kcfg/smb4k.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/smb4k.png
%{tde_tdedocdir}/HTML/en/smb4k/

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

%description devel
%{summary}

%files devel
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libsmb4kcore.la
%{tde_libdir}/libsmb4kcore.so

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes FTBFS [Bug #1285]
%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
 -DBUILD_ALL="ON" \
 -DWITH_ALL_OPTIONS="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -fr $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT -C build

%find_lang %{tde_pkg}

# Updates applications categories for openSUSE
%if 0%{?suse_version}
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"
%suse_update_desktop_file -r %{tde_pkg} System Network
%endif

# Removes duplicate files
%fdupes -s %buildroot


%clean
%__rm -rf %{buildroot}


%changelog
