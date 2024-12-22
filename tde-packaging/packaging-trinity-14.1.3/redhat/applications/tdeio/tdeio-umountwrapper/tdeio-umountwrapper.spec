#
# spec file for package tdeio-umountwrapper (version R14)
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
%define tde_pkg tdeio-umountwrapper
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
Version:	0.2
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Progress dialog for safely removing devices in Trinity
Group:		Applications/Utilities
URL:		http://frode.kde.no/misc/tdeio_umountwrapper/

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
Source1:		media_safelyremove.desktop_tdeio


BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

Obsoletes:		trinity-kio-umountwrapper < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kio-umountwrapper = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# IDN support
BuildRequires:	libidn-devel

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
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
Wrapper around tdeio_media_mountwrapper.
Provides a progress dialog for Safely Removing of devices in Trinity.


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
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL=ON \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%__install -D -m 644 "%{SOURCE1}" %{?buildroot}%{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdeio-umountwrapper
%__install -D -m 644 "%{SOURCE1}" %{?buildroot}%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_tdeio-umountwrapper

%find_lang tdeio_umountwrapper


%clean
%__rm -rf %{buildroot}


%post
for f in konqueror d3lphin; do
  update-alternatives --install \
    %{tde_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop \
    media_safelyremove.desktop_${f} \
    %{tde_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop_tdeio-umountwrapper \
    20
done


%postun
if [ $1 -eq 0 ]; then
  for f in konqueror d3lphin; do
    update-alternatives --remove \
      media_safelyremove.desktop_${f} \
      %{tde_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop_tdeio-umountwrapper || :
  done
fi


%files -f tdeio_umountwrapper.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md
%{tde_bindir}/tdeio_umountwrapper
%{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdeio-umountwrapper
%dir %{tde_datadir}/apps/d3lphin
%dir %{tde_datadir}/apps/d3lphin/servicemenus
%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_tdeio-umountwrapper


%changelog
