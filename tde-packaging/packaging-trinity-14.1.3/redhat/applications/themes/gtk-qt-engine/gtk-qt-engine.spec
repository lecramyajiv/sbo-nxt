#
# spec file for package gtk-qt-engine (version R14)
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
%define tde_pkg gtk-qt-engine
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
Version:		0.8
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Theme engine using Qt for GTK+ 2.x and Trinity
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
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	libtool

# GTK2 support
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:	gtk2-devel
%endif
%if 0%{?mgaversion} >= 5
BuildRequires:	%{_lib}gtk+2.0-devel
%endif
%if 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:	%{_lib}gtk+2.0_0-devel
%else
%if 0%{?mdkver}
BuildRequires:	%{_lib}gtk+2.0-devel
%else
BuildRequires:	gtk+2.0-devel
%endif
%endif
%endif

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif


%description
The GTK-Qt Theme Engine (also known as gtk-qt-engine) is a GTK 2 theme engine
that calls Qt to do the actual drawing. This makes your GTK 2 applications
look almost like real Qt applications and gives you a more unified desktop
experience.

Please note that this package is targeted at Trinity users and therefore provides
a way to configure it from within KControl.


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
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes the KCM not to work at all !
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
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DDATA_INSTALL_DIR=%{tde_datadir}/apps \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{tde_tdelibdir}/kcm_kcmgtk.la
%{tde_tdelibdir}/kcm_kcmgtk.so
%{tde_tdeappdir}/kcmgtk.desktop
%{tde_tdedocdir}/HTML/en/kcontrol/gtk/

# The following files are outside TDE's directory
%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/2.10.0
%dir %{_libdir}/gtk-2.0/2.10.0/engines
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.la
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.so
%dir %{_datadir}/themes
%dir %{_datadir}/themes/Qt
%dir %{_datadir}/themes/Qt/gtk-2.0
%{_datadir}/themes/Qt/gtk-2.0/gtkrc


%changelog
