#
# spec file for package kile (version R14)
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
%define tde_pkg kile
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


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		2.0.3
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		TDE Integrated LaTeX Environment [Trinity]
Group:			Applications/Publishing
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

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

Obsoletes: %{name}-i18n-ar < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-bg < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-br < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ca < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-cs < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-cy < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-da < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-de < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-el < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-engb < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-es < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-et < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-eu < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-fi < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-fr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ga < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-gl < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-hi < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-hu < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-is < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-it < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ja < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-lt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ms < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-mt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nb < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nds < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nl < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-nn < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-pa < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-pl < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-pt < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ptbr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ro < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ru < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-rw < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-sk < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-sr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-srlatin < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-sv < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-ta < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-th < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-tr < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-uk < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-i18n-zhcn < %{?epoch:%{epoch}:}%{version}-%{release}


%description
Kile is a user-friendly LaTeX source editor and TeX shell for TDE.

The source editor is a multi-document editor designed for .tex and .bib
files.  Menus, wizards and auto-completion are provided to assist with
tag insertion and code generation.  A structural view of the document
assists with navigation within source files.

The TeX shell integrates the various tools required for TeX processing.
It assists with LaTeX compilation, DVI and postscript document viewing,
generation of bibliographies and indices and other common tasks.

Kile can support large projects consisting of several smaller files.

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

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file kile Office WordProcessor
%endif


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/kile
%{tde_tdeappdir}/kile.desktop
%{tde_datadir}/apps/tdeconf_update
%{tde_datadir}/apps/kile
%{tde_datadir}/config.kcfg/kile.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kile.png
%{tde_datadir}/icons/hicolor/scalable/apps/kile.svgz
%{tde_tdedocdir}/HTML/en/kile
%{tde_datadir}/mimelnk/text/x-kilepr.desktop

%lang(da) %{tde_tdedocdir}/HTML/da/kile/
%lang(es) %{tde_tdedocdir}/HTML/es/kile/
%lang(et) %{tde_tdedocdir}/HTML/et/kile/
%lang(it) %{tde_tdedocdir}/HTML/it/kile/
%lang(nl) %{tde_tdedocdir}/HTML/nl/kile/
%lang(pt) %{tde_tdedocdir}/HTML/pt/kile/
%lang(sv) %{tde_tdedocdir}/HTML/sv/kile/

%{tde_mandir}/man1/kile.1*


%changelog
