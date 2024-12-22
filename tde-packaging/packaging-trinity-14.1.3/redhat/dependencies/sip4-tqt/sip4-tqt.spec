#
# spec file for package sip4-tqt (version R14)
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

# Note for RHEL6 / Fedora:
#  Do *NOT* use 'byacc' to build sip4-tqt.
#  Instead, use 'bison' with a wrapper shell script.
#  e.g. /usr/local/bin/yacc
#   contains 'bison --yacc $@'

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg sip4-tqt
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
Version:	4.10.5
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Python/C++ bindings generator runtime library
Group:		Development/Tools/Building
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

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	libtqt4-devel >= %{?epoch:%{epoch}:}4.2.0
BuildRequires:	trinity-filesystem >= %{tde_version}

BuildRequires:	gcc-c++

# BISON support
BuildRequires:  bison

# FLEX support
BuildRequires:	flex

# PYTHON support
%if "%{python}" == ""
%global python python3
%endif
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

# YACC support
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 31
BuildRequires:  byacc
%endif

%description

SIP is a tool for generating bindings for C++ classes with some ideas
borrowed from SWIG, but capable of tighter bindings because of its
specificity towards C++ and Python.

##########

%package -n sip4-tqt
Summary:	Python/C++ bindings generator (Runtime Library)
Group:		Development/Tools/Building
Requires:	trinity-filesystem >= %{tde_version}
Requires:	%{python}

%description -n sip4-tqt
SIP is a tool for generating bindings for C++ classes with some ideas
borrowed from SWIG, but capable of tighter bindings because of its
specificity towards C++ and Python.

%files -n sip4-tqt
%defattr(-,root,root,-)
%{python_sitearch}/sip_tqt.so
%if 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?rhel} == 7 || 0%{?suse_version}
%{python_sitearch}/sip_tqt_config.py*
%{python_sitearch}/sip_tqt_distutils.py*
%if 0%{?rhel} == 7
%{python_sitearch}/__pycache__/sip_tqt_config.*.pyc
%{python_sitearch}/__pycache__/sip_tqt_distutils.*.pyc
%endif
%else
%pycached %{python_sitearch}/sip_tqt_config.py
%pycached %{python_sitearch}/sip_tqt_distutils.py
%endif

##########

%package -n sip4-tqt-devel
Summary:		Python/C++ bindings generator (Development Files)
Group:			Development/Libraries/Python
Requires:		sip4-tqt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{python}-devel

%description -n sip4-tqt-devel
SIP is a tool for generating bindings for C++ classes with some ideas
borrowed from SWIG, but capable of tighter bindings because of its
specificity towards C++ and Python.

SIP was originally designed to generate Python bindings for KDE and so
has explicit support for the signal slot mechanism used by the Qt/KDE
class libraries.

Features:
- connecting TQt signals to Python functions and class methods
- connecting Python signals to TQt slots
- overloading virtual member functions with Python class methods
- protected member functions
- abstract classes
- enumerated types
- global class instances
- static member functions.

This package contains the code generator tool and the development headers
needed to develop Python bindings with sip.

%files -n sip4-tqt-devel
%defattr(-,root,root,-)
%{tde_bindir}/sip-tqt
%{tde_includedir}/sip-tqt.h

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

mkdir build
cd build
%__python ../configure.py \
	-b %{tde_bindir} \
	-d %{python_sitearch} \
	-e %{tde_includedir} \
	-u STRIP="" \
	CFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt -I%{_includedir}/tqt3 -I${PWD}/../sipgen -DYYERROR_VERBOSE" \
	CXXFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt -I%{_includedir}/tqt3 -I${PWD}/../sipgen -DYYERROR_VERBOSE"


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build


%clean
%__rm -rf %{?buildroot}


%changelog
