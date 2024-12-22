#
# spec file for package tde-systemsettings (version R14)
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
%define tde_pkg tde-systemsettings
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_sysconfdir %{_sysconfdir}/trinity
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.0svn20070312
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Easy to use control centre for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org

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
Source1:		tde-settings-laptops.directory


Provides:	trinity-kde-systemsettings = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kde-systemsettings < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-systemsettings = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-systemsettings < %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}
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

%if 0%{?suse_version} == 0 || 0%{?sle_version} <= 150300
Requires:		trinity-guidance
%endif


%description
System preferences is a replacement for the TDE
Control Centre with an improved user interface.

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
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes FTBFS [Bug #1285]
%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DSYSCONF_INSTALL_DIR="/etc/trinity" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%__install -D -m 644 %{SOURCE1} %{buildroot}%{tde_datadir}/desktop-directories/tde-settings-laptops.directory

# Unwanted files
%__rm -f %{buildroot}%{tde_datadir}/applications/tde/kcmfontinst.desktop
%__rm -f %{buildroot}%{tde_datadir}/desktop-directories/tde-settings-power.directory
%__rm -f %{buildroot}%{tde_datadir}/desktop-directories/tde-settings-system.directory

%__rm -f %{buildroot}%{tde_datadir}/applications/tde/laptop.desktop

echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/audioencoding.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/defaultapplication.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/kcm_knetworkconfmodule_ss.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/medianotifications.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/systemsettings.desktop"

# Fix translation names
for d in "%{buildroot}%{tde_datadir}/locale/"*"/LC_MESSAGES"; do
  mv "${d}/"*".mo" "${d}/%{tde_pkg}.mo"
done

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc README.md TODO
%dir %{tde_sysconfdir}/xdg
%dir %{tde_sysconfdir}/xdg/menus
%dir %{tde_sysconfdir}/xdg/menus/applications-merged
%{tde_sysconfdir}/xdg/menus/applications-merged/tde-system-settings-merge.menu
%{tde_sysconfdir}/xdg/menus/tde-system-settings.menu
%{tde_bindir}/systemsettings
%{tde_datadir}/applications/tde/audioencoding.desktop
%{tde_datadir}/applications/tde/defaultapplication.desktop
%{tde_datadir}/applications/tde/kcm_knetworkconfmodule_ss.desktop
%{tde_datadir}/applications/tde/medianotifications.desktop
%{tde_datadir}/applications/tde/systemsettings.desktop
%{tde_datadir}/apps/systemsettings/
%config(noreplace) %{tde_confdir}/systemsettingsrc
%{tde_datadir}/desktop-directories/*.directory
%{tde_datadir}/icons/crystalsvg/*/apps/systemsettings.png
%{tde_tdedocdir}/HTML/en/tde-systemsettings/
%{tde_mandir}/man1/systemsettings.1*

%changelog
