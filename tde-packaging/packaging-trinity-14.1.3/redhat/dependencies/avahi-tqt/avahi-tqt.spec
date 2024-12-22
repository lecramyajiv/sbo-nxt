#
# spec file for package avahi-tqt (version R14)
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

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libavahi %{_lib}avahi
%else
%define libavahi libavahi
%endif


Name:		trinity-avahi-tqt
Epoch:		%{tde_epoch}
Version:	0.6.30
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Avahi TQt integration library
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	LGPL-2.0+
%else
License:	LGPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	libtqt4-devel >= %{tde_epoch}:4.2.0

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	libtool

# GLIB2 support
BuildRequires:	glib2-devel

# GETTEXT support
BuildRequires:	gettext-devel

# Xi support
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%endif
%if 0%{?suse_version} >= 1220 || 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	libXi-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%endif

# DBUS support
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	dbus-devel
%endif

# PCAP support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}cap-devel
%else
BuildRequires:	libcap-devel
%endif

# AVAHI support
%if 0%{?mgaversion} || 0%{?mdkversion}
%define avahi_devel %{_lib}avahi-client-devel
%endif
%if 0%{?suse_version} || 0%{?rhel} || 0%{?fedora}
%define avahi_devel avahi-devel
%endif
%{?avahi_devel:BuildRequires: %{avahi_devel}}

# EXPAT support
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	expat-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libexpat-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}expat-devel
%endif

# NAS support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_nas 1
BuildRequires: nas-devel
%endif

# XT support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXt-devel
%endif

%description
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

##########

%package -n %{libavahi}-tqt1
Summary:	Avahi TQt integration library
Group:		System/Libraries
Provides:	libavahi-tqt1 = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-avahi-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-avahi-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libavahi}-tqt1
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%post -n %{libavahi}-tqt1
/sbin/ldconfig || :

%postun -n %{libavahi}-tqt1
/sbin/ldconfig || :

%files -n %{libavahi}-tqt1
%defattr(-,root,root,-)
%{_libdir}/libavahi-tqt.so.1
%{_libdir}/libavahi-tqt.so.1.0.0

##########

%package -n %{libavahi}-tqt-devel
Summary:	Avahi TQt integration library (Development Files)
Group:		Development/Libraries/C and C++
Provides:	libavahi-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	%{libavahi}-tqt1 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libtqt4-devel >= %{tde_epoch}:4.2.0
%{?avahi_devel:Requires: %{avahi_devel}}

Obsoletes:		trinity-avahi-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-avahi-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libavahi}-tqt-devel
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%post -n %{libavahi}-tqt-devel
/sbin/ldconfig || :

%postun -n %{libavahi}-tqt-devel
/sbin/ldconfig || :

%files -n %{libavahi}-tqt-devel
%defattr(-,root,root,-)
%{_includedir}/avahi-tqt/
%{_libdir}/libavahi-tqt.a
%{_libdir}/libavahi-tqt.so
%{_libdir}/libavahi-tqt.la
%{_libdir}/pkgconfig/avahi-tqt.pc

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
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DLIB_INSTALL_DIR="%{_libdir}" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR="%{?buildroot}" -C build


%clean
%__rm -rf %{?buildroot}


%changelog
