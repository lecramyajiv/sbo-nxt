#
# spec file for package kbarcode (version R14)
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
%define tde_pkg kbarcode
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
Version:		2.0.7
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		barcode and label printing application for Trinity
Group:			Applications/Utilities
URL:			http://www.kbarcode.net

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

# PCRE support
BuildRequires:	pcre-devel

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

Requires:		%{name}-tdefile-plugin = %{?epoch:%{epoch}:}%{version}-%{release}


%description
KBarcode is a barcode and label printing application for Trinity. It can be used
to print everything from simple business cards up to complex labels with
several barcodes (e.g. article descriptions).

KBarcode comes with an easy to use WYSIWYG label designer, a setup wizard,
batch import of data for batch printing labels (directly from the delivery
note), thousands of predefined labels, database management tools and
translations in many languages. Even printing more than 10.000 labels in one
go is no problem for KBarcode. Data for printing can be imported from several
different data sources, including SQL databases, CSV files and the TDE address
book.

Additionally it is a simple barcode generator (similar to the old xbarcode you
might know). All major types of barcodes like EAN, UPC, CODE39 and ISBN are
supported. Even complex 2D barcodes are supported using third party tools. The
generated barcodes can be directly printed or you can export them into images
to use them in another application.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{tde_bindir}/kbarcode
%{tde_tdeappdir}/kbarcode-batch.desktop
%{tde_tdeappdir}/kbarcode-editor.desktop
%{tde_tdeappdir}/kbarcode-single.desktop
%{tde_tdeappdir}/kbarcode.desktop
%{tde_datadir}/mimelnk/application/kbarcode-label.desktop
%{tde_datadir}/apps/kbarcode/
%{tde_datadir}/icons/hicolor/*/actions/barcode.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodeellipse.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodegrid.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodelinetool.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcoderect.png
%{tde_datadir}/icons/hicolor/*/apps/kbarcode.png
%{tde_mandir}/man1/*.1*
%{tde_tdedocdir}/HTML/en/kbarcode/

##########

%package tdefile-plugin
Summary:		tdefile-plugin for %{name}
Group:			Applications/Utilities

%description tdefile-plugin
%{summary}.

%files tdefile-plugin
%defattr(-,root,root,-)
%{tde_tdelibdir}/tdefile_kbarcode.la
%{tde_tdelibdir}/tdefile_kbarcode.so
%{tde_datadir}/services/tdefile_kbarcode.desktop

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
  -DWITH_NATIVE_GNU_BARCODE=OFF \
  -DWITH_JAVASCRIPT=ON \
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

%find_lang %{tde_pkg}

# Fix invalid icon path
%__sed -i "%{buildroot}%{tde_tdeappdir}/kbarcode.desktop" -e "s|Icon=.*|Icon=kbarcode|"

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r "%{buildroot}%{tde_tdeappdir}/kbarcode.desktop"        Utility PrintingUtility
%suse_update_desktop_file -r "%{buildroot}%{tde_tdeappdir}/kbarcode-batch.desktop"  Utility PrintingUtility
%suse_update_desktop_file -r "%{buildroot}%{tde_tdeappdir}/kbarcode-editor.desktop" Utility PrintingUtility
%suse_update_desktop_file -r "%{buildroot}%{tde_tdeappdir}/kbarcode-single.desktop" Utility PrintingUtility
%endif


%clean
%__rm -rf %{buildroot}


%changelog
