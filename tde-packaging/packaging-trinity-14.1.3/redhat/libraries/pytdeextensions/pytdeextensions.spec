#
# spec file for package pytdeextensions (version R14)
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
%define tde_pkg pytdeextensions
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.4.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Python packages to support TDE applications (scripts)
Group:		Development/Libraries/Python
URL:		http://www.trinitydesktop.org/
#URL:		http://www.simonzone.com/software/pykdeextensions

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

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	autoconf automake libtool m4
BuildRequires:	gcc-c++

BuildRequires:	pytqt-devel >= %{?epoch:%{epoch}:}3.18.1
BuildRequires:	trinity-pytde-devel
BuildRequires:	trinity-pytqt-tools
Requires:		pytqt
Requires:		trinity-pytde

Requires:		trinity-libpythonize0 = %{?epoch:%{epoch}:}%{version}-%{release}

# SIP
BuildRequires:	sip4-tqt-devel >= 4.10.5
Requires:		sip4-tqt >= 4.10.5

# PYTHON support
%if "%{python}" == ""
%global python python3
%endif
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel


Obsoletes:		trinity-pykdeextensions < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-pykdeextensions = %{?epoch:%{epoch}:}%{version}-%{release}


%description
PyTDE Extensions is a collection of software and Python packages
to support the creation and installation of TDE applications.


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_datadir}/apps/pytdeextensions/
%{tde_tdedocdir}/HTML/en/pytdeextensions/
%{python_sitearch}/*

##########

%package -n trinity-libpythonize0
Summary:	Python packages to support TDE applications (library)
Group:		Development/Libraries/Python

%description -n trinity-libpythonize0
PyTDE Extensions is a collection of software and Python packages
to support the creation and installation of TDE applications.

This package contains the libpythonize library files.

%files -n trinity-libpythonize0
%defattr(-,root,root,-)
%{tde_libdir}/libpythonize.so.*

##########

%package -n trinity-libpythonize-devel
Summary:	Python packages to support TDE applications (development)
Group:		Development/Libraries/Python
Requires:	trinity-libpythonize0 = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-libpythonize0-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libpythonize0-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libpythonize-devel
PyTDE Extensions is a collection of software and Python packages
to support the creation and installation of TDE applications.

This package contains the libpythonize development files.

%files -n trinity-libpythonize-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libpythonize.la
%{tde_libdir}/libpythonize.so

##########

%package devel
Summary:	Meta-package to install all pytdeextensions development files
Group:		Development/Libraries/Python
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libpythonize-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package is a meta-package to install all pytdeextensions development
files.

%files devel

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Changes library directory to 'lib64'
# Also other fixes for distributions ...
for f in src/*.py; do
  %__sed -i "${f}" \
    -e "s|'pytde-dir=',None,|'pytde-dir=','%{python_sitearch}',|g" \
    -e "s|self.pytde_dir = None|self.pytde_dir = \"%{python_sitearch}\"|g" \
    -e "s|'kde-lib-dir=',None,|'kde-lib-dir=','%{tde_libdir}',|g" \
    -e "s|self.kde_lib_dir = None|self.kde_lib_dir = \"%{tde_libdir}\"|g" \
    -e "s|'kde-kcm-lib-dir=',None,|'kde-kcm-lib-dir=','%{tde_libdir}/trinity',|g" \
    -e "s|self.kde_kcm_lib_dir = None|self.kde_kcm_lib_dir = \"%{tde_libdir}/trinity\"|g" \
    -e "s|%{tde_includedir}/tde|%{tde_tdeincludedir}|g" \
    -e 's|"/kde"|"/tde"|' \
    -e 's|"-I" + self.kde_inc_dir + "/tde"|"-I/opt/trinity/include"|' \
    -e "s|/usr/lib/pyshared/python\*|%{python_sitearch}|g"
done

# Fix FTBFS on RHEL 5
%if 0%{?rhel} == 5
%__sed -i "src/pythonize."* -e "s|const char \*object|char \*object|g"
%endif

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?mgaversion} >= 8 || 0%{?sle_version} >= 150600
%__sed -i "app_templates/kcontrol_module/setup.py" \
          "app_templates/kcontrol_module/src/kcontrol_module.py" \
          "app_templates/kdeapp/setup.py" \
          "app_templates/kdeapp/src/kdeapp.py" \
          "app_templates/kdeutility/setup.py" \
          "app_templates/kdeutility/src/kdeutility.py" \
          "app_templates/tdeioslave/setup.py" \
          "app_templates/tdeioslave/src/tdeioslave.py" \
  -e "s|/usr/bin/python|/usr/bin/env %{python}|"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%__mkdir_p build
%__python ./setup.py build_libpythonize


%install
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

# Avoids 'error: byte-compiling is disabled.' on Mandriva/Mageia
export PYTHONDONTWRITEBYTECODE=

%__rm -rf %{buildroot}

%__python ./setup.py install \
	--root=%{buildroot} \
	--prefix=%{tde_prefix} \
	--install-clib=%{tde_libdir} \
	--install-cheaders=%{tde_tdeincludedir} \
   -v

# Removes BUILDROOT directory reference in installed files
for f in \
	%{buildroot}%{tde_libdir}/libpythonize.la \
	%{buildroot}%{tde_datadir}/apps/pytdeextensions/app_templates/kcontrol_module/src/KcontrolModuleWidgetUI.py \
	%{buildroot}%{tde_datadir}/apps/pytdeextensions/app_templates/kdeutility/src/KDEUtilityDialogUI.py \
; do
	%__sed -i "${f}" -e "s|%{buildroot}||g"
:
done

# Moves PYTHON libraries to distribution directory
%__mkdir_p %{buildroot}%{python_sitearch}
%__mv -f %{buildroot}%{tde_prefix}/lib/python*/site-packages/* %{buildroot}%{python_sitearch}
%__rm -rf %{buildroot}%{tde_prefix}/lib/python*/site-packages

# Removes useless files
%__rm -rf %{?buildroot}%{tde_libdir}/*.a

# Fix permissions on include files
%__chmod 644 %{?buildroot}%{tde_tdeincludedir}/*.h


%clean
%__rm -rf %{buildroot}


%changelog
