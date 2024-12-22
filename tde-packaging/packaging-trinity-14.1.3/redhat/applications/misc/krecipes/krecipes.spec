#
# spec file for package krecipes (version R14)
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
%define tde_pkg krecipes
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


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.0beta2
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Recipes manager for TDE
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

# MYSQL support
BuildRequires:	mysql-devel

# POSTGRESQL support
BuildRequires:	postgresql
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires: postgresql-server-devel
%else
BuildRequires: postgresql-devel
%endif

# SQLITE3 support
%if 0%{?mgaversion}
BuildRequires: sqlite3-devel
%else
BuildRequires: sqlite-devel
%endif


%description
Krecipes is a TDE application designed to manage recipes. It can help you to
do your shopping list, search through your recipes to find what you can do
with available ingredients and a diet helper. It can also import or export
recipes from files in various format (eg RecipeML or Meal-Master) or from
databases.

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --docdir=%{tde_tdedocdir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --with-sqlite \
  --with-mysql \
  --with-postgresql

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}

# Fix desktop file location
%__mkdir_p "%{?buildroot}%{tde_tdeappdir}"
%__mv -f "%{?buildroot}%{tde_datadir}/applnk/"*"/krecipes.desktop" "%{?buildroot}%{tde_tdeappdir}"

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r krecipes Education Chemistry
%endif

# Removes duplicate files
%fdupes "%{buildroot}%{tde_datadir}"


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/krecipes
%{tde_tdeappdir}/krecipes.desktop
%{tde_datadir}/apps/krecipes/
%{tde_datadir}/icons/crystalsvg/*/mimetypes/krecipes_file.png
%{tde_datadir}/icons/hicolor/*/apps/krecipes.png
%{tde_datadir}/mimelnk/application/x-krecipes-backup.desktop
%{tde_datadir}/mimelnk/application/x-krecipes-recipes.desktop
%lang(da) %{tde_tdedocdir}/HTML/da/
%lang(en) %{tde_tdedocdir}/HTML/en/
%lang(es) %{tde_tdedocdir}/HTML/es/
%lang(et) %{tde_tdedocdir}/HTML/et/
%lang(pt) %{tde_tdedocdir}/HTML/pt/
%lang(sv) %{tde_tdedocdir}/HTML/sv/
%{tde_mandir}/man1/krecipes.1*

%changelog
