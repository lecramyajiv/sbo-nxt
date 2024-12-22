#
# spec file for package kcmldap (version R14)
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
%define tde_pkg kcmldap
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
Version:		0.5
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Kerberos control module for the TDE control center
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
#BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	trinity-libtdeldap-devel >= 0.5

Requires:		trinity-tde-ldap-cert-updater = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-kcontrol-ldap-bonding = %{?epoch:%{epoch}:}%{version}-%{release}

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

# OPENLDAP support
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
%if 0%{?mdkver} >= 5000000
BuildRequires:	lib64ldap-devel
%else
BuildRequires:	openldap-devel
%endif
%endif
%if 0%{?suse_version}
BuildRequires:	openldap2-devel
%endif
%if 0%{?rhel} == 5
BuildRequires:	openldap24-libs-devel
%endif

# KRB5 support
#BuildRequires:	krb5-devel

# HEIMDAL support
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	heimdal-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libheimdal-devel
%endif

# UDEV support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%define with_tdehwlib 1
%if 0%{?mdkversion} || 0%{?mgaversion}
%if 0%{?pclinuxos}
BuildRequires:	%{_lib}udev1-devel
%else
BuildRequires:	%{_lib}udev-devel
%endif
%else
BuildRequires:	libudev-devel
%endif
%endif

# LIBCOM_ERR support
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 6
BuildRequires:	libcom_err-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}ext2fs-devel
%endif


%description
This is a meta-package that installs all kcmldap related packages.

%files

##########

%package -n trinity-kcontrol-ldap-bonding
Summary:		Kerberos control module for the TDE control center
Group:			Applications/Utilities
Requires:		trinity-tde-ldap-cert-updater = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kcontrol-ldap-bonding
This is a TDE control center module to manage TDE connections to Kerberos realms.

%files -n trinity-kcontrol-ldap-bonding
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/tdeldapbonding
%{tde_tdelibdir}/kcm_ldapbonding.la
%{tde_tdelibdir}/kcm_ldapbonding.so
%{tde_tdeappdir}/ldapbonding.desktop
%dir %{tde_datadir}/pixmaps
%{tde_datadir}/pixmaps/kcmldapbonding_step1.png
%{tde_datadir}/pixmaps/kcmldapbonding_step3.png
%lang(ru) %{tde_datadir}/locale/ru/LC_MESSAGES/kcmldap.mo

##########

%package -n trinity-tde-ldap-cert-updater
Summary:		Service to keep LDAP certificates up-to-date
Group:			Applications/Utilities
Requires:		trinity-kcontrol-ldap-bonding = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tde-ldap-cert-updater
This is a small daemon which keeps the LDAP root certificate up to date with the LDAP server

%files -n trinity-tde-ldap-cert-updater
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/tdeldapcertupdater

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
  \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%clean
%__rm -rf %{buildroot}


%changelog
