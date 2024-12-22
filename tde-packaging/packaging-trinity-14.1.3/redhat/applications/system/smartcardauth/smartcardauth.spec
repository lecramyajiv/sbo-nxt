#
# spec file for package smartcardauth (version R14)
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
%define tde_pkg smartcardauth
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

%if 0%{?fedora} >= 27 || 0%{?mgaversion}
%define debug_package %{nil}
%endif

%define dont_check_desktop_files 1

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	SmartCard Login and LUKS Decrypt, Setup Utility
Group:		Applications/System
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
Source1:		trinity-%{tde_pkg}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
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

# PCSC support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
Requires:	perl-pcsc-perl
%endif
%if 0%{?rhel} || 0%{?fedora}
Requires:	pcsc-perl
%endif
%if 0%{?suse_version}
Requires:	perl-pcsc
%endif

# PKCS11 support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}pkcs11-helper-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	pkcs11-helper-devel
%endif

# DB4/DB5 support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version} >= 1220 || 0%{?mdkversion} || 0%{?mgaversion}
%define with_db 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:  db5-devel
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires:  libdb-devel
BuildRequires:  libdb-cxx-devel
%endif
%if 0%{?suse_version}
BuildRequires:  libdb-4_8-devel
%endif
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires:  db4-devel
%endif
%endif

# PAM support
BuildRequires:	pam-devel

# TLS support
%if 0%{?suse_version}
BuildRequires:	libgnutls-devel
%else
BuildRequires:	gnutls-devel
%endif

# The 'pp' utility
BuildRequires:	perl-PAR-Packer


%description
This utility will allow you to set up your computer to accept a SmartCard as an authentication source for:
- Your encrypted LUKS partition
- TDE, including automatic login, lock, and unlock features

It is designed to work with any ISO 7816-1,2,3,4 compliant smartcard
Examples of such cards are:
- The Schlumberger MultiFlex
- The ACS ACOS5 / ACOS6 series of cryptographic ISO 7816 cards

If a card is chosen that has PKSC support, such as the ACOS cards, this utility can run
simultaneously with the certificate reading program(s) to provide single sign on
in addition to the PKCS certificate functionality


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
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
%if 0%{?mgaversion} || 0%{?pclinuxos}
  -DPERL_PAR_PACKER="pp.pl" \
%endif
%if 0%{?mgaversion} == 6 || 0%{?pclinuxos}
  -DPERL_LIB_CHIPCARD="%{perl_sitearch}" \
%endif
%if 0%{?suse_version}
  -DPERL_LIB_CHIPCARD="%{perl_vendorarch}" \
%endif
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
%__make install DESTDIR="%{?buildroot}" -C build

# Debian stuff
%__rm -f %{buildroot}/usr/share/initramfs-tools/hooks/cryptlukssc


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc gpl.txt
%{_bindir}/cardpincheck
%{_bindir}/cryptosmartcard.sh


%changelog
