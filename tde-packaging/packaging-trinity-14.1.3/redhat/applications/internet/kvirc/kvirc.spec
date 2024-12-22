%if 0%{?fedora} >= 23
%define _hardened_ldflags %nil
%endif

#
# spec file for package kvirc (version R14)
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
%define tde_pkg kvirc
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
Version:	3.4.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Trinity based next generation IRC client with module support
Group:		Applications/Utilities
URL:		http://kvirc.net/

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

Requires:		%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}


%description
A highly configurable graphical IRC client with an MDI interface,
built-in scripting language, support for IRC DCC, drag & drop file
browsing, and much more. KVIrc uses the TDE widget set, can be extended
using its own scripting language, integrates with TDE, and supports
custom plugins.

If you are a developer and you want to write a custom module for KVIrc,
you need to install the kvirc-dev package.

%package data
Group:			Applications/Utilities
Summary:		Data files for KVIrc
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description data
This package contains the architecture-independent data needed by KVIrc in
order to run, such as icons and images, language files, and shell scripts.
It also contains complete reference guides on scripting and functions
within KVIrc in its internal help format. Unless you want to use KVIrc only
as a very simple IRC client you are likely to want to write scripts to
tailor KVIrc to your needs.

KVIrc is a graphical IRC client based on the TDE widget set which integrates
with the Trinity Desktop Environment version 3.

%package devel
Group:			Development/Libraries
Summary:		Development files for KVIrc
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains KVIrc libraries and include files you need if you
want to develop plugins for KVIrc.

KVIrc is a graphical IRC client based on the TDE widget set which integrates
with the K Desktop Environment version 3.


##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# FTBFS on RHEL 5
%if 0%{?rhel} == 5
%__sed -i "admin/acinclude.m4.in" \
       -i "src/kvilib/tal/kvi_tal_application.cpp" \
       -e "/TDEApplication/ s|\")|\", true, true, true)|";
%endif


%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
./autogen.sh


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

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
  --enable-wall \
  \
  --with-pic \
  \
  --with-big-channels \
  --enable-perl \
  --with-ix86-asm \
  --with-kde-services-dir=%{tde_datadir}/services \
  --with-kde-library-dir=%{tde_libdir} \
  --with-kde-include-dir=%{tde_tdeincludedir} \
  --with-tqt-name=tqt \
  --with-tqt-library-dir=%{_libdir} \
  --with-tqt-include-dir=%{_includedir}/tqt3 \
  --with-tqt-moc=%{_bindir}/tmoc

# Symbolic links must exist prior to parallel building
%__make symlinks -C src/kvilib/build
%__make symlinks -C src/kvirc/build

%if 0%{?mgaversion} >= 6 || 0%{?pclinuxos} >= 2018
%__sed -i "src/modules/"*"/Makefile" -e "s|-Wl,--no-undefined||"
%endif

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Debian maintainer has renamed 'COPYING' file to 'EULA', so we do the same ...
%__mv \
  %{?buildroot}%{tde_datadir}/kvirc/3.4/license/COPYING \
  %{?buildroot}%{tde_datadir}/kvirc/3.4/license/EULA

# Move desktop file to XDG location
%__mkdir_p "%{?buildroot}%{tde_tdeappdir}"
%__mv -f "%{?buildroot}%{tde_datadir}/applnk/"*"/%{tde_pkg}.desktop" "%{?buildroot}%{tde_tdeappdir}"

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file kvirc Network IRCClient
%endif


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc ChangeLog FAQ README TODO
%{tde_bindir}/kvirc
%{tde_libdir}/*.so.*
%{tde_libdir}/kvirc/*/modules/*.so

%files data
%defattr(-,root,root,-)
%{tde_bindir}/kvi_run_netscape
%{tde_bindir}/kvi_search_help
%exclude %{tde_libdir}/kvirc/*/modules/*.la
%exclude %{tde_libdir}/kvirc/*/modules/*.so
%{tde_libdir}/kvirc/
%{tde_tdeappdir}/kvirc.desktop
%{tde_datadir}/apps/tdeconf_update/kvirc_soundsystem.upd
%{tde_datadir}/apps/tdeconf_update/kvirc_soundsystem_upd.sh
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.svgz
%{tde_datadir}/icons/hicolor/*/*/*.xpm
%{tde_datadir}/kvirc
%{tde_datadir}/mimelnk/text/*.desktop
%{tde_datadir}/services/*.protocol
%{tde_mandir}/man1/kvirc.1

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/kvirc-config
%{tde_includedir}/kvirc/
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/kvirc/*/modules/*.la


%changelog
