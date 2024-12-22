#
# spec file for package tdesvn (version R14)
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
%define tde_pkg tdesvn
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
Version:	1.0.4
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Subversion client with tight TDE integration
Group:		Applications/Utilities
URL:		http://www.elliptique.net/~ken/kima/

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

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires: libtool
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

# SVN support
BuildRequires:	subversion-devel

# SQLITE3 support
%if 0%{?mgaversion}
BuildRequires: sqlite3-devel
%else
BuildRequires: sqlite-devel
%endif
BuildRequires:	libtqt3-mt-sqlite3

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif


Requires:		%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-libsvnqt = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdesvn < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdesvn = %{?epoch:%{epoch}:}%{version}-%{release}


%description
TDESvn is a graphical client for the subversion revision control
system (svn).

Besides offering common and advanced svn operations, it features
a tight integration into TDE and can be embedded into other TDE 
applications like konqueror via the TDE component technology KParts.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{tde_bindir}/tdesvn
%{tde_bindir}/tdesvnaskpass
%{tde_tdelibdir}/tdesvnpart.la
%{tde_tdelibdir}/tdesvnpart.so
%{tde_datadir}/applications/tde/tdesvn.desktop
%{tde_datadir}/apps/tdeconf_update/tdesvn-use-external-update.sh
%{tde_datadir}/apps/tdeconf_update/tdesvnpartrc-use-external.upd
%{tde_datadir}/apps/tdesvn/
%{tde_datadir}/apps/tdesvnpart/
%{tde_datadir}/apps/konqueror/servicemenus/tdesvn_subversion.desktop
%{tde_datadir}/config.kcfg/tdesvn_part.kcfg
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.svgz
%{tde_mandir}/man1/tdesvn.1*
%{tde_mandir}/man1/tdesvnaskpass.1*
%lang(en) %{tde_tdedocdir}/HTML/en/tdesvn/
%lang(nl) %{tde_tdedocdir}/HTML/nl/tdesvn/
%{tde_libdir}/libksvnwidgets.la
%{tde_libdir}/libksvnwidgets.so
%{tde_libdir}/libsvnfrontend.la
%{tde_libdir}/libsvnfrontend.so
%{tde_libdir}/libtdesvncfgreader.la
%{tde_libdir}/libtdesvncfgreader.so
%{tde_libdir}/libtdesvnevents.la
%{tde_libdir}/libtdesvnevents.so
%{tde_libdir}/libtdesvnhelpers.la
%{tde_libdir}/libtdesvnhelpers.so

##########

%package -n trinity-libsvnqt
Group:			Development/Libraries
Summary:		Qt wrapper library for subversion [Trinity]

%description -n trinity-libsvnqt
This package provides svnqt, a Qt wrapper library around the 
subversion library.

It is based on the RapidSvn SvnCpp library, a subversion client API 
written in C++.

%files -n trinity-libsvnqt
%defattr(-,root,root,-)
%{tde_libdir}/libsvnqt.so.4
%{tde_libdir}/libsvnqt.so.4.2.2

##########

%package -n trinity-libsvnqt-devel
Group:			Development/Libraries
Requires:		trinity-libsvnqt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		qt-devel
Requires:		subversion-devel
Summary:		Qt wrapper library for subversion (development files) [Trinity]

%description -n trinity-libsvnqt-devel
This package contains the header files and symbolic links that developers
using svnqt will need.

%files -n trinity-libsvnqt-devel
%defattr(-,root,root,-)
%{tde_includedir}/svnqt
%{tde_libdir}/libsvnqt.so

##########

%package tdeio-plugins
Group:			Development/Libraries
Conflicts:	trinity-kdesdk-tdeio-plugins
Summary:		subversion I/O slaves for Trinity

Obsoletes:	trinity-kdesvn-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdesvn-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdesvn-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdesvn-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This packages includes TDEIO slaves for svn, svn+file, svn+http, 
svn+https, svn+ssh. This allows you to access subversion repositories 
inside any TDEIO enabled TDE application.

This package is part of tdesvn-trinity.

%post tdeio-plugins
for proto in svn+file svn+http svn+https svn+ssh svn; do
  update-alternatives --install \
    %{tde_datadir}/services/${proto}.protocol \
    ${proto}.protocol \
    %{tde_datadir}/services/${proto}.protocol_tdesvn \
    20
done

%preun tdeio-plugins
if [ $1 -eq 0 ]; then
  for proto in svn+file svn+http svn+https svn+ssh svn; do
    update-alternatives --remove \
      ${proto}.protocol \
      %{tde_datadir}/services/${proto}.protocol_tdesvn || :
  done
fi

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_datadir}/services/kded/tdesvnd.desktop
%{tde_datadir}/services/ksvn+file.protocol
%{tde_datadir}/services/ksvn+http.protocol
%{tde_datadir}/services/ksvn+https.protocol
%{tde_datadir}/services/ksvn+ssh.protocol
%{tde_datadir}/services/ksvn.protocol
%{tde_datadir}/services/svn+file.protocol_tdesvn
%{tde_datadir}/services/svn+http.protocol_tdesvn
%{tde_datadir}/services/svn+https.protocol_tdesvn
%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%{tde_datadir}/services/svn.protocol_tdesvn
%{tde_tdelibdir}/tdeio_ksvn.la
%{tde_tdelibdir}/tdeio_ksvn.so
%{tde_tdelibdir}/kded_tdesvnd.la
%{tde_tdelibdir}/kded_tdesvnd.so

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

rm -f src/svnqt/CMakeLists.txt.orig
#rm -fr src/svnqt/cache/sqlite3/


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export CMAKE_INCLUDE_PATH="%{tde_tdeincludedir}"

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
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DMAN_INSTALL_DIR=%{tde_mandir} \
  -DPKGCONFIG_INSTALL_DIR=%{tde_tdelibdir}/pkgconfig \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  ..

# SMP safe !
%__make %{?_smp_mflags} || %__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Installs SVN protocols as alternatives
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+file.protocol %{?buildroot}%{tde_datadir}/services/svn+file.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+http.protocol %{?buildroot}%{tde_datadir}/services/svn+http.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+https.protocol %{?buildroot}%{tde_datadir}/services/svn+https.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn.protocol %{?buildroot}%{tde_datadir}/services/svn.protocol_tdesvn

# Locales
%find_lang %{tde_pkg}

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -G "SVN Client" %{tde_pkg} Development RevisionControl
%endif


%clean
%__rm -rf %{buildroot}


%changelog
