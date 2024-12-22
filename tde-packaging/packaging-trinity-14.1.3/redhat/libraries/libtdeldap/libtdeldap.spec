#
# spec file for package libtdeldap (version R14)
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

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg libtdeldap
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.5
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	LDAP interface library for TDE
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gcc-c++
BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	pkgconfig

# LIBTOOL
BuildRequires: automake
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 5 || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif

# SASL support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
%if 0%{?mdkver} >= 5000000
BuildRequires:	%{_lib}sasl-devel
%else
BuildRequires:	%{_lib}sasl2-devel
%endif
%endif
%if 0%{?suse_version}
BuildRequires:	cyrus-sasl-devel
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

# HEIMDAL support
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
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


%description
LDAP interface library for TDE management modules.

%files
%defattr(-,root,root,-)
%{tde_libdir}/libtdeldap.so.1
%{tde_libdir}/libtdeldap.so.1.0.0

##########

%package devel
Group:		Development/Libraries/Other
Summary:	Trinity image viewer
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
LDAP interface library for TDE management modules.

libtdeldap-trinity-dev contains development files and documentation.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/ldappasswddlg.h
%{tde_tdeincludedir}/libtdeldap.h
%{tde_libdir}/libtdeldap.la
%{tde_libdir}/libtdeldap.so

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

# openldap 2.4 includes (CentOS 5)
if [ -d "/usr/include/openldap24" ]; then
  RPM_OPT_FLAGS="-I%{_includedir}/openldap24 -L%{_libdir}/openldap24 ${RPM_OPT_FLAGS}"
fi

# heimdal pkgconfig (Fedora)
if [ -d "%{_libdir}/heimdal/lib/pkgconfig" ]; then
  PKG_CONFIG_PATH="%{_libdir}/heimdal/lib/pkgconfig:${PKG_CONFIG_PATH}"
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
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DPLUGIN_INSTALL_DIR="%{tde_tdelibdir}" \
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
