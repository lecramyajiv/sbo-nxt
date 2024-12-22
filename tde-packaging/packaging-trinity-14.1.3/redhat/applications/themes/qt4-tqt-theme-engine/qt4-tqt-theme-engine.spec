#
# spec file for package qt4-tqt-theme-engine (version R14)
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
%define tde_pkg qt4-tqt-theme-engine
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

%if "%{?_qt4_plugindir}" == ""
%define _qt4_plugindir %{_libdir}/qt4/plugins
%endif

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDE theme engine for Qt4
Group:		Applications/Utilities
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

BuildRequires:	autoconf automake libtool m4
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

# QT4 support
%if 0%{?suse_version}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:	libqt4-devel
%else
BuildRequires:	qt-devel
%endif
%else
BuildRequires:	qt4-devel
%endif


%description
TDE theme engine for Qt4


##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Fix compilation with 'lib64'
%if "%_lib" == "lib64"
%__sed -i */*.pro -e "s|/opt/trinity/lib|/opt/trinity/lib64|g"
%endif

# Fix TDE include directory
%__sed -i */*.pro -e "s|INCLUDEPATH += /opt/trinity/include|INCLUDEPATH += %{tde_tdeincludedir}|"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

if [ -x "%{_libdir}/qt4/bin/qmake" ]; then
  export PATH="%{_libdir}/qt4/bin:${PATH}"
fi

# Use QT4's qmake
qmake


# Not SMP SAFE !
%__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install INSTALL_ROOT=%{buildroot}

# Unwanted files (-devel ?)
%__rm -f %{?buildroot}%{_libdir}/libtdeqt4interface.so


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/libtdeqt4interface.so.1
%{_libdir}/libtdeqt4interface.so.1.0
%{_libdir}/libtdeqt4interface.so.1.0.0
%dir %{_qt4_plugindir}/styles/
%{_qt4_plugindir}/styles/libsimplestyleplugin.so


%changelog
