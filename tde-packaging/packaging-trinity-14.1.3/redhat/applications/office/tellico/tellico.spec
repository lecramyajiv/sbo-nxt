%if 0%{?fedora} >= 23 || 0%{?rhel} >= 9
%define _hardened_ldflags %nil
%endif

#
# spec file for package tellico (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that confolrms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg tellico
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
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
Version:	1.3.2.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Icollection manager for books, videos, music [Trinity]
Group:		Applications/Utilities
URL:		http://periapsis.org/tellico/

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
BuildRequires:	trinity-tdemultimedia-devel >= %{tde_version}
BuildRequires:	trinity-libkcal-devel >= %{tde_version}
BuildRequires:	trinity-libpoppler-tqt-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# POPPLER support
%if 0%{?rhel} >=6 || 0%{?fedora} >= 15 || 0%{?suse_version}
%if 0%{?suse_version} >= 1500
BuildRequires: libpoppler-devel >= 0.12
%else
BuildRequires: poppler-devel >= 0.12
%endif
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}poppler-devel
%endif
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
# On RHEL 5, the distro-provided poppler is too old. We built a newer one.
BuildRequires:	trinity-poppler-devel >= 0.12
%endif

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# YAZ support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	yaz
BuildRequires:	%{_lib}yaz-devel
%endif

# XML2 support
BuildRequires:  libxml2-devel

# XSLT support
%if 0%{?mdkver}
BuildRequires:	%{_lib}xslt-devel
%else
BuildRequires:	libxslt-devel
%endif

%if 0%{?rhel} == 4
# a bogus dep in libexslt.la file from EL-4 (WONTFIX bug http://bugzilla.redhat.com/142241)
BuildRequires:  libgcrypt-devel
%endif

# V4L support
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15 || 0%{?suse_version}
BuildRequires:	libv4l-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}v4l-devel
%endif

# EXEMPI support
%if 0%{?suse_version}
BuildRequires:	libexempi-devel
%else
BuildRequires:	exempi-devel
%endif

# PCRE support
BuildRequires:	pcre-devel

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

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# ATTR support
%if 0%{?mgaversion} || 0%{?mdkversion}
%define libattr_devel %{_lib}attr-devel
%else
%define libattr_devel libattr-devel
%endif
BuildRequires: %{libattr_devel}

# PYTHON support
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

# Readline support
BuildRequires:	readline-devel


Requires:		%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-scripts = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/tellico
%{tde_datadir}/applications
%config(noreplace) %{tde_confdir}/tellicorc
%{tde_mandir}/man1/tellico.1*

##########

%package data
Group:			Applications/Utilities
Summary:		collection manager for books, videos, music [data] [Trinity]

%description data
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

This package contains the architecture independent files, such data files and
documentation.

%files data
%defattr(-,root,root,-)
%dir %{tde_datadir}/apps/tellico
%{tde_datadir}/apps/tellico/*.xsl
%{tde_datadir}/apps/tellico/*.xml
%{tde_datadir}/apps/tellico/*.png
%{tde_datadir}/apps/tellico/entry-templates
%{tde_datadir}/apps/tellico/*.py*
%if 0%{?rhel} == 7 || 0%{?mgaversion} == 8
%{tde_datadir}/apps/tellico/__pycache__/
%endif
%{tde_datadir}/apps/tellico/pics
%{tde_datadir}/apps/tellico/report-templates
%{tde_datadir}/apps/tellico/tellico.dtd
%{tde_datadir}/apps/tellico/tellico.tips
%{tde_datadir}/apps/tellico/tellico2html.js
%{tde_datadir}/apps/tellico/tellicoui.rc
%{tde_datadir}/apps/tellico/welcome.html
%{tde_datadir}/config.kcfg
%{tde_tdedocdir}/HTML/*/tellico/
%{tde_datadir}/icons/hicolor/*/apps/tellico.png
%{tde_datadir}/icons/hicolor/*/mimetypes/application-x-tellico.png
%{tde_datadir}/icons/hicolor/scalable/apps/tellico.svg
%{tde_datadir}/icons/hicolor/scalable/mimetypes/application-x-tellico.svg
%{tde_datadir}/mime/packages/tellico.xml
%{tde_datadir}/mimelnk/application/x-tellico.desktop
%{tde_datadir}/apps/tdeconf_update/tellico-1-3-update.pl
%{tde_datadir}/apps/tdeconf_update/tellico-rename.upd
%{tde_datadir}/apps/tdeconf_update/tellico.upd

##########

%package scripts
Group:			Applications/Utilities
Summary:		collection manager for books, videos, music [scripts] [Trinity]

%description scripts
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

This package contains the scripts to import data from external sources, such
as websites. As the format of the data may change, these scripts are provided
as a separate package which can be updated through debian-volatile.

%files scripts
%defattr(-,root,root,-)
%{tde_datadir}/apps/tellico/data-sources
%{tde_datadir}/apps/tellico/z3950-servers.cfg

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

if [ -r /usr/include/libv4l1-videodev.h ]; then
%__sed -i "src/barcode/barcode_v4l.h" -e "s|linux/videodev.h|libv4l1.h|"
fi

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?mgaversion} >= 8
%__sed -i "src/fetch/scripts/dark_horse_comics.py" \
          "src/fetch/scripts/ministerio_de_cultura.py" \
          "src/fetch/scripts/fr.allocine.py" \
          "src/translators/griffith2tellico.py" \
  -e "s|/usr/bin/env python|/usr/bin/env %{python}|"
%endif


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
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_LIBKCDDB=ON \
  -DWITH_LIBKCAL=ON \
  -DWITH_LIBBTPARSE=OFF \
  -DWITH_SAX_LOADER=ON \
%if 0%{?rhel} == 5
  -DBUILD_WEBCAM_SUPPORT=OFF \
%endif
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=$RPM_BUILD_ROOT -C build

# Add svg icons to xdg directories
%__install -D -c -p -m 644 "icons/tellico.svg" "%{?buildroot}%{tde_datadir}/icons/hicolor/scalable/apps/tellico.svg"
%__install -D -c -p -m 644 "icons/tellico_mime.svg" "%{?buildroot}%{tde_datadir}/icons/hicolor/scalable/mimetypes/application-x-tellico.svg"

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%changelog
