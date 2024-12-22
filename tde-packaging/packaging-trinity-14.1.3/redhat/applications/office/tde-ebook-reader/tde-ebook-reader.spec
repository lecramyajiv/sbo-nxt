#
# spec file for package tde-ebook-reader (version R14)
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
%define tde_pkg tde-ebook-reader
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
Version:		0.99.6
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		e-book reader for TDE
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

# UNIBREAK support
%if 0%{?mgaversion} || 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}unibreak-devel
%else
BuildRequires: libunibreak-devel
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
tde-ebook-reader is an e-book reader for TDE.

Main features:
 * supports several open e-book formats: fb2, html, chm, plucker,
   palmdoc, ztxt, tcr (psion text), rtf, oeb, openreader, non-DRM'ed
   mobipocket, plain text, epub, eReader
 * reads directly from tar, zip, gzip, bzip2 archives (you can have
   several books in one archive)
 * supports a structured view of your e-book collection
 * automatically determines encodings
 * automatically generates a table of contents
 * keeps the last open book and the last read positions for all open books
   between runs
 * automatic hyphenation (patterns for several languages are included)
 * searching and downloading books from www.feedbooks.com and www.litres.ru
 * partial CSS support for epub files

%files
%defattr(-,root,root,-)
%{tde_bindir}/tde-ebook-reader
%{tde_tdeappdir}/tde-ebook-reader.desktop
%{tde_datadir}/apps/tde-ebook-reader/
%{tde_mandir}/man1/tde-ebook-reader.1*

##########

%package -n libzlcore-tqt
Requires:	libzlcore-data-tqt
Summary:	Summary:  TQt3-based development library (shared library)

%description -n libzlcore-tqt
This is the core of Summary: , the library that tde-ebook-reader is based on.

%files -n libzlcore-tqt
%{tde_libdir}/libzlcore-tqt.so.*

##########

%package -n libzlcore-tqt-devel
Requires:	libzlcore-tqt
Summary:	TQt3-based development library (development files)

%description -n libzlcore-tqt-devel
This package contains development files for the Summary:  core.

%files -n libzlcore-tqt-devel
%{tde_includedir}/zlibrary-tqt/core
%{tde_libdir}/libzlcore-tqt.la
%{tde_libdir}/libzlcore-tqt.so

##########

%package -n libzlcore-data-tqt
Summary:	TQt3-based development library (support files)

%description -n libzlcore-data-tqt
This package contains the support files for the core of Summary: , the library
that the fbreader e-book reader is based on.

%files -n libzlcore-data-tqt
%{tde_datadir}/zlibrary-tqt/keynames.desktop-tqt.xml
%{tde_datadir}/zlibrary-tqt/languagePatterns.zip
%{tde_datadir}/zlibrary-tqt/unicode.xml.gz
%{tde_datadir}/zlibrary-tqt/default/
%{tde_datadir}/zlibrary-tqt/encodings/
%{tde_datadir}/zlibrary-tqt/resources/

##########

%package -n libzltext-tqt
Requires:	libzlcore-tqt
Requires:	libzltext-data-tqt
Summary:	TQt3-based text model/viewer part (shared library)

%description -n libzltext-tqt
This package provides text model/viewer part of Summary: .

%files -n libzltext-tqt
%{tde_libdir}/libzltext-tqt.so.*

##########

%package -n libzltext-tqt-devel
Requires:	libzltext-tqt
Summary:	TQt3-based text model/viewer part (development files)

%description -n libzltext-tqt-devel
This package contains development files for the Summary:  text model/viewer
library.

%files -n libzltext-tqt-devel
%{tde_includedir}/zlibrary-tqt/text
%{tde_libdir}/libzltext-tqt.la
%{tde_libdir}/libzltext-tqt.so

##########

%package -n libzltext-data-tqt
Summary:	TQt3-based text model/viewer part (support files)

%description -n libzltext-data-tqt
This package contains the support files for the text model/viewer part
of Summary: .

%files -n libzltext-data-tqt
%{tde_datadir}/zlibrary-tqt/hyphenationPatterns.zip

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



%clean
%__rm -rf %{buildroot}



%changelog
