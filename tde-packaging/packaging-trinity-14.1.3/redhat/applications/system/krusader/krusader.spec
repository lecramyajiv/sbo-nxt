#
# spec file for package krusader (version R14)
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
%define tde_pkg krusader
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
Version:	1.90.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Twin-panel (commander-style) file manager for TDE (and other desktops)
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
BuildRequires:	trinity-tdebindings-devel >= %{tde_version}

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


%description
Krusader is a simple, easy, powerful, twin-panel (commander-style) file
manager for TDE and other desktops, similar to Midnight Commander (C) or Total
Commander (C).

It provides all the file management features you could possibly want.

Plus: extensive archive handling, mounted filesystem support, FTP,
advanced search module, viewer/editor, directory synchronisation,
file content comparisons, powerful batch renaming and much much more.

It supports archive formats: ace, arj, bzip2, deb, iso, lha, rar, rpm, tar,
zip and 7-zip.

It handles KIOSlaves such as smb:// or fish://.

Almost completely customizable, Krusader is very user friendly, fast and looks
great on your desktop.


##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}

# Updates applications categories for openSUSE
%if 0%{?suse_version}
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"
%suse_update_desktop_file krusader            System FileManager
%suse_update_desktop_file krusader_root-mode  System FileManager
%endif


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING FAQ README TODO
%{tde_bindir}/krusader
%{tde_tdelibdir}/tdeio_krarc.la
%{tde_tdelibdir}/tdeio_krarc.so
%{tde_tdelibdir}/tdeio_virt.la
%{tde_tdelibdir}/tdeio_virt.so
%{tde_tdeappdir}/krusader.desktop
%{tde_tdeappdir}/krusader_root-mode.desktop
%{tde_datadir}/apps/krusader
%{tde_datadir}/apps/tdeconf_update/krusader_tqt_selection.upd
%{tde_datadir}/icons/crystalsvg/*/apps/*.png
%{tde_datadir}/icons/locolor/*/apps/*.png
%{tde_datadir}/services/krarc.protocol
%{tde_datadir}/services/virt.protocol
%{tde_mandir}/man1/krusader.1
%{tde_tdedocdir}/HTML/en/krusader/
%{tde_tdedocdir}/HTML/en/tdeioslave/krarc/
%{tde_tdedocdir}/HTML/en/tdeioslave/virt/
%lang(ru) %{tde_tdedocdir}/HTML/ru/krusader/


%changelog
