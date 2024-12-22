#
# spec file for package polkit-tqt (version R14)
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
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg polkit-tqt

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libpolkit_tqt %{_lib}%{tde_pkg}
%else
%define libpolkit_tqt lib%{tde_pkg}
%endif


Name:		trinity-%{tde_pkg}
Version:	0.103.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	PolicyKit-tqt library
Group:		Development/Libraries/C and C++
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	trinity-dbus-1-tqt-devel
BuildRequires:	libtqt4-devel

BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	gettext

%if 0%{?mdkver}
BuildRequires:	%{_lib}polkit1-devel
%else
BuildRequires:	polkit-devel
%endif

%description
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.

This package contains the files necessary for running applications that use
the libpolkit-tqt library.

##########

%package -n %{libpolkit_tqt}0
Summary:	TQt source code editing component based on Scintilla
Group:		Development/Libraries/C and C++
Provides:	libpolkit-tqt = %{version}-%{release}
Requires:	libtqt3-mt >= 3.5.0

%description -n %{libpolkit_tqt}0
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.

This package contains the files necessary for running applications that use
the libpolkit-tqt library.

%post -n %{libpolkit_tqt}0
/sbin/ldconfig

%postun -n %{libpolkit_tqt}0
/sbin/ldconfig

%files -n %{libpolkit_tqt}0
%defattr(-,root,root,-)
%{_libdir}/libpolkit-tqt-agent.so.0
%{_libdir}/libpolkit-tqt-agent.so.0.0.0
%{_libdir}/libpolkit-tqt-core.so.0
%{_libdir}/libpolkit-tqt-core.so.0.0.0
%{_libdir}/libpolkit-tqt-gui.so.0
%{_libdir}/libpolkit-tqt-gui.so.0.0.0

##########

%package -n %{libpolkit_tqt}-devel
Summary:	PolicyKit-tqt development files
Group:		Development/Libraries/C and C++
Provides:	libpolkit-tqt-devel = %{version}-%{release}
Requires:	%{libpolkit_tqt}0 = %{version}-%{release}
Requires:	libtqt3-mt-devel >= 3.5.0

%description -n %{libpolkit_tqt}-devel
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.
.
This package contains the development libraries and headers.

%post -n %{libpolkit_tqt}-devel
/sbin/ldconfig

%postun -n %{libpolkit_tqt}-devel
/sbin/ldconfig

%files -n %{libpolkit_tqt}-devel
%defattr(-,root,root,-)
%{_includedir}/polkit-tqt/
%{_libdir}/cmake/polkit-tqt.cmake
%{_libdir}/libpolkit-tqt-agent.so
%{_libdir}/libpolkit-tqt-core.so
%{_libdir}/libpolkit-tqt-gui.so
%{_libdir}/pkgconfig/polkit-tqt-agent.pc
%{_libdir}/pkgconfig/polkit-tqt-core.pc
%{_libdir}/pkgconfig/polkit-tqt-gui.pc
%{_libdir}/pkgconfig/polkit-tqt.pc

##########

%package -n %{libpolkit_tqt}-examples
Summary:	Polkit-tqt Documentation
Group:		Development/Libraries/C and C++
Provides:	libpolkit-tqt-doc = %{version}-%{release}
Requires:	%{libpolkit_tqt}0 = %{version}-%{release}
Requires:	trinity-filesystem >= %{tde_version}

%description -n %{libpolkit_tqt}-examples
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged (desktop) applications.

libpolkit-tqt provides convenience classes and methods for TQt/TDE
applications that want to use PolicyKit.

This package contains example files and applications.

%files -n %{libpolkit_tqt}-examples
%defattr(-,root,root,-)
%{_sysconfdir}/dbus-1/system.d/org.tqt.policykit.examples.conf
%{_bindir}/polkit-tqt-agent-example
%{_bindir}/polkit-tqt-example
%{_bindir}/polkit-tqt-example-helper
%{_datadir}/apps/polkit-tqt/
%{_datadir}/dbus-1/system-services/org.tqt.policykit.examples.service
%{_datadir}/polkit-1/actions/org.tqt.policykit.examples.policy

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL="ON" \
  -DWITH_ALL_OPTIONS="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install -C build DESTDIR=%{?buildroot}

# Unwanted files
%__rm -f %{buildroot}%{_libdir}/libpolkit-tqt-agent.la
%__rm -f %{buildroot}%{_libdir}/libpolkit-tqt-core.la
%__rm -f %{buildroot}%{_libdir}/libpolkit-tqt-gui.la


%clean
%__rm -rf $RPM_BUILD_ROOT


%changelog
