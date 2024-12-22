#
# spec file for package pytqt (version R14)
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
%define tde_pkg pytqt
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
Version:	3.18.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TQt bindings for Python
Group:		Development/Libraries/Python
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

Obsoletes:		trinity-PyQt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-python-qt3 < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-python-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-python-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	tqt3-apps-devel >= 3.5.0
BuildRequires:	libtqt4-devel >= %{?epoch:%{epoch}:}4.2.0
BuildRequires:	trinity-filesystem >= %{tde_version}
BuildRequires:	sip4-tqt-devel >= %{?epoch:%{epoch}:}4.10.5
BuildRequires:	libtqscintilla-devel >= %{?epoch:%{epoch}:}1.7.1

BuildRequires:	gcc-c++

# PYTHON support
%if "%{python}" == ""
%global python python3
%endif
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

# MESA support
%if 0%{?fedora} || 0%{?rhel}
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
%endif
%if 0%{?mgaversion} || 0%{?pclinuxos}
BuildRequires: %{_lib}mesaglu1-devel
%endif
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}glu-devel
%endif
%if 0%{?suse_version}
BuildRequires: Mesa-libGL-devel
BuildRequires: Mesa-libGLU-devel
%endif

# XMU support
%if 0%{?suse_version} == 1140
BuildRequires:	xorg-x11-libXmu-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version} >= 1210
BuildRequires: libXmu-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion} >= 4
BuildRequires: %{_lib}xmu-devel
%endif
%if 0%{?mgaversion} == 2 || 0%{?mgaversion} == 3
BuildRequires:	%{_lib}xmu%{?mgaversion:6}-devel
%endif

%description
Python binding module that allows use of TQt X Window toolkit v3.
You can use it to create portable graphics-capable scripts.

At this moment pytqt offers a vast subset of TQt API. There are
some minor issues related to the differences between C++ and Python
(types, etc), but usually you'll be able to write code pretty much the
same way in both languages (with syntax differences, of course)

##########

%package -n pytqt
Summary:	TQt bindings for Python
Group:		Development/Libraries/Python
Requires:	trinity-filesystem >= %{tde_version}
Requires:	sip4-tqt >= %{?epoch:%{epoch}:}4.10.5
Requires:	libtqt4 >= %{?epoch:%{epoch}:}4.2.0
Obsoletes:	python-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt
Python binding module that allows use of TQt X Window toolkit v3.
You can use it to create portable graphics-capable scripts.

At this moment pytqt offers a vast subset of TQt API. There are
some minor issues related to the differences between C++ and Python
(types, etc), but usually you'll be able to write code pretty much the
same way in both languages (with syntax differences, of course)

%files -n pytqt
%defattr(-,root,root,-)
%doc NEWS README
%dir %{python_sitearch}/PyTQt
%if 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?rhel} == 7 || 0%{?suse_version}
%{python_sitearch}/PyTQt/__init__.py*
%if 0%{?rhel} == 7
%{python_sitearch}/PyTQt/__pycache__/__init__.*.pyc
%endif
%else
%pycached %{python_sitearch}/PyTQt/__init__.py
%endif
%{python_sitearch}/PyTQt/tqt.so
%{python_sitearch}/PyTQt/tqtcanvas.so
%{python_sitearch}/PyTQt/tqtnetwork.so
%{python_sitearch}/PyTQt/tqtsql.so
%{python_sitearch}/PyTQt/tqttable.so
%{python_sitearch}/PyTQt/tqtui.so
%{python_sitearch}/PyTQt/tqtxml.so

##########

%package -n pytqt-gl
Summary:	TQt OpenGL bindings for Python
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	python-tqt-gl < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt-gl = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt-gl
Python binding module that allows use of the OpenGL facilities
offered by the TQt X Window toolkit v3. You can use it to create
portable graphics-capable scripts.

%files -n pytqt-gl
%defattr(-,root,root,-)
%{python_sitearch}/PyTQt/tqtgl.so

##########

%package -n pytqt-tqtext
Summary:	TQtext extensions for pytqt
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	python-tqt-tqtext < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt-tqtext = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt-tqtext
pytqt Extensions. Contains:

* TQScintilla: a featureful TQt source code editing component based
              on Scintilla.

%files -n pytqt-tqtext
%defattr(-,root,root,-)
%{python_sitearch}/PyTQt/tqtext.so

##########

%package -n trinity-pytqt-tools
Summary:	Pyuic and pylupdate for TQt
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-pytqt-tools
pyuic is the PyQt counterpart for TQt's uic. It takes an XML
user interface file and generates Python code.

pylupdate is the counterpart for TQt's lupdate. It updates TQt
Linguist translation files from Python code.

%files -n trinity-pytqt-tools
%defattr(-,root,root,-)
%{tde_bindir}/pytqlupdate
%{tde_bindir}/pytquic

##########

%package -n pytqt-devel
Summary:	TQt bindings for Python - Development files
Group:		Development/Libraries/Python
Requires:	pytqt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-pytqt-tools = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libtqt4-devel >= %{?epoch:%{epoch}:}4.2.0
Obsoletes:	python-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	python-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n pytqt-devel
Development .sip files with definitions of PyQt classes. They
are needed to build PyQt, but also as building blocks of other
packages based on them, like PyTDE.

%files -n pytqt-devel
%defattr(-,root,root,-)
%if 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?rhel} == 7 || 0%{?suse_version}
%{python_sitearch}/PyTQt/pytqtconfig.py*
%if 0%{?rhel} == 7
%{python_sitearch}/PyTQt/__pycache__/pytqtconfig.*.pyc
%endif
%else
%pycached %{python_sitearch}/PyTQt/pytqtconfig.py
%endif
%dir %{_datadir}/sip
%{_datadir}/sip/tqt/

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

mkdir build
cd build

echo yes | %__python ../configure.py \
	-c -n %{_includedir}/tqt3 \
	-g %{_includedir}/tqt3 \
	-q %{_datadir}/tqt3 \
	-y tqt-mt \
	-o %{_libdir} -u -j 10 \
	-d %{python_sitearch}/PyTQt \
	-v %{_datadir}/sip/tqt \
	-b %{tde_bindir} \
	-w \
	CXXFLAGS_RELEASE="" CXXFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt" STRIP=""

%__make


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%__install -d %{?buildroot}%{_datadir}/sip/
%__cp -rf sip/* %{?buildroot}%{_datadir}/sip/tqt/


%clean


%changelog
