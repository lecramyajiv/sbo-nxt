#
# spec file for package koffice (version R14)
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
%define tde_pkg koffice
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

# Disable Kross support for RHEL <= 5 (python is too old)
%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_kross 1
%endif

# Ruby support
%define with_ruby 1

# Ruby 1.9 includes are located in strance directories ... (taken from ruby 1.9 spec file)
%global	_normalized_cpu	%(echo %{_target_cpu} | sed 's/^ppc/powerpc/;s/i.86/i386/;s/sparcv./sparc/;s/armv.*/arm/')

# Required for Mageia 2: removes the ldflag '--no-undefined'
%global _disable_ld_no_undefined 1

%if 0%{?mdkver} >= 5000000
%global build_cxxflags %optflags -Wl,--allow-shlib-undefined
%endif


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.6.3
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	An integrated office suite
Group:		Applications/Productivity
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

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:	trinity-koffice-rpmlintrc

# BuildRequires: world-devel ;)
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tdegraphics-devel >= %{tde_version}
BuildRequires:	trinity-libpoppler-tqt-devel >= %{tde_version}

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

BuildRequires:	fontconfig-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	zlib-devel
BuildRequires:	pcre-devel
BuildRequires:	gettext-devel
BuildRequires:	mysql-devel
BuildRequires:	perl
BuildRequires:	doxygen
BuildRequires:	aspell-devel
BuildRequires:	readline-devel

# EXIF support
%if 0%{?mdkver}
BuildRequires:	%{_lib}exif-devel
%else
BuildRequires:	libexif-devel
%endif

# IMAGEMAGICK support
%if 0%{?mdkver}
BuildRequires:	%{_lib}magick-devel
%else
BuildRequires:	ImageMagick-devel
%endif

# JPEG support
%if 0%{?mdkver}
%define libjpeg %{_lib}jpeg
%else
%define libjpeg libjpeg
%endif
BuildRequires: %{libjpeg}-devel

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# OPENEXR support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openexr-devel
%else
BuildRequires:	OpenEXR-devel
%endif

# TIFF support
%if 0%{?mdkver}
BuildRequires:	%{_lib}tiff-devel
%else
BuildRequires:	libtiff-devel
%endif

# XSLT support
%if 0%{?mdkver}
BuildRequires:	%{_lib}xslt-devel
%else
BuildRequires:	libxslt-devel
%endif

# PYTHON support
#  lib/kross/configure.in.in :
#   WARNING: Building Kross python plugin is now prohibited at all times,
#   because it is not compatible with Python >= 3.
%define with_python 0
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%if 0%{?with_python}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel
%endif

# LCMS support
%if 0%{?suse_version} || 0%{?rhel} >= 7
BuildRequires: liblcms-devel
%else
BuildRequires: lcms-devel
%endif

# LCMS2 support
%if 0%{?suse_version}
BuildRequires:	liblcms2-devel
%endif

# BZIP2 support
%if 0%{?suse_version}
BuildRequires:	libbz2-devel
%else
BuildRequires:	bzip2-devel
%endif

# PAPER support
BuildRequires:	libpaper-devel

# RUBY support
%if 0%{?with_ruby}
BuildRequires:	ruby ruby-devel >= 1.8.1
%if 0%{?fedora} >= 19
BuildRequires:	rubypick
%endif
%endif

# FREETYPE support
%if 0%{?suse_version} == 1140
BuildRequires:	freetype2-devel
%else
BuildRequires:	freetype-devel
%endif

# LIBPNG support
%if 0%{?mdkver} || 0%{?mgaversion}
BuildRequires:	%{_lib}png-devel
%endif
%if 0%{?mdkversion} && 0%{?mdkver} < 5000000 && 0%{?pclinuxos} == 0
BuildRequires:	%{_lib}png15-devel
%endif
%if 0%{?suse_version} || 0%{?fedora} || 0%{?rhel}
BuildRequires:	libpng-devel
%endif

# GRAPHICSMAGICK support
%if 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?fedora} || 0%{?rhel} >= 5
%define with_graphicsmagick 1
%if 0%{?suse_version}
BuildRequires:	GraphicsMagick >= 1.1.0
%endif
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?fedora} || 0%{?rhel} >= 5 || 0%{?suse_version}
%if 0%{?mdkver}
BuildRequires:	%{_lib}graphicsmagick-devel
%else
BuildRequires:	GraphicsMagick-devel >= 1.1.0
%endif
%endif
%endif

# UTEMPTER support
%if 0%{?suse_version}
BuildRequires:	utempter-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	utempter
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}utempter-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 5
BuildRequires:	libutempter-devel
%endif

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

# POSTGRESQL support
#  Requires 'libpqxx', for kexi-driver-pgqsl
%if 0%{?mdkversion} || 0%{?fedora} || 0%{?suse_version}
%if 0%{?suse_version} != 1500 && 0%{?suse_version} != 1550 && 0%{?pclinuxos} == 0
%define with_postgresql 1
BuildRequires:	postgresql
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:	postgresql-server-devel
%else
BuildRequires:	postgresql-devel
%endif
%if 0%{?mdkver}
BuildRequires:	%{_lib}pqxx-devel
%else
BuildRequires:	libpqxx-devel
%endif
%endif
%endif
Obsoletes:		trinity-libpqxx < %{?epoch:%{epoch}:}%{version}-%{release}

# WPD support
#  For chalk and filters
%if 0%{?mdkver}
BuildRequires:	%{_lib}wpd-devel
%else
BuildRequires:	libwpd-devel
%endif
Obsoletes:		trinity-libwpd < %{?epoch:%{epoch}:}%{version}-%{release}

# WV2 support
%if 0%{?mgaversion} || 0%{?mdkversion}
%define with_wv2 1
%if 0%{mdkver} >= 5000000
BuildRequires:	wv2-devel
%else
BuildRequires:	%{_lib}wv2-devel
%endif
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define with_wv2 1
BuildRequires:	wv2-devel
%endif

# MESA support
%if 0%{?fedora} || 0%{?rhel}
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
%endif
%if 0%{?mgaversion} || 0%{?pclinuxos}
BuildRequires: %{_lib}mesaglu1-devel
%endif
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}glu-devel
%endif
%if 0%{?suse_version}
BuildRequires: Mesa-libGL-devel
BuildRequires: Mesa-libGLU-devel
%endif

# LIBXI support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	libXi-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%endif
%if 0%{?suse_version} >= 1220
BuildRequires:	libXi-devel
%endif

# SQLITE support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	sqlite3-devel
%else
BuildRequires:	sqlite-devel
%endif


%description
KOffice is an integrated office suite.

##########

%package suite
Summary:		An integrated office suite
Group:			Applications/Productivity
Obsoletes:      %{name} <= %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release} 
Requires:		%{name}-kword = %{?epoch:%{epoch}:}%{version}-%{release} 
Requires:		%{name}-kspread = %{?epoch:%{epoch}:}%{version}-%{release} 
Requires:		%{name}-kpresenter = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kivio = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-karbon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kugar = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kexi = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kexi-driver-mysql = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_postgresql:Requires:       %{name}-kexi-driver-pgsql = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires:		%{name}-kchart = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kformula = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-filters = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kplato = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-chalk = %{?epoch:%{epoch}:}%{version}-%{release}

%description suite
KOffice is an integrated office suite.

%files suite
#empty => virtual package

##########

%package core
Summary:		Core support files for %{name} 
Group:			Applications/Productivity
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		perl

%description core
%{summary}.

%files core
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_bindir}/koshell
%{tde_bindir}/kthesaurus
%{tde_bindir}/koconverter
%{tde_libdir}/libtdeinit_koshell.so
%{tde_libdir}/libtdeinit_kthesaurus.so
%{tde_tdelibdir}/tdefile_koffice.*
%{tde_tdelibdir}/tdefile_ooo.*
%{tde_tdelibdir}/tdefile_abiword.*
%{tde_tdelibdir}/tdefile_gnumeric.*
%{tde_tdelibdir}/kodocinfopropspage.*
%{tde_tdelibdir}/kofficescan.*
%{tde_tdelibdir}/kofficethumbnail.*
%{tde_tdelibdir}/koshell.*
%{tde_tdelibdir}/kthesaurus.*
%{tde_tdelibdir}/kwmailmerge_classic.*
%{tde_tdelibdir}/kwmailmerge_tdeabc.*
%{tde_tdelibdir}/kwmailmerge_qtsqldb_power.*
%{tde_tdelibdir}/kwmailmerge_qtsqldb.*
%{tde_tdelibdir}/libkounavailpart.*
%{tde_tdelibdir}/libkprkword.*
%{tde_tdelibdir}/libthesaurustool.*
%{tde_tdelibdir}/clipartthumbnail.*
%{tde_datadir}/apps/koffice/
%{tde_datadir}/apps/konqueror/servicemenus/*
%{tde_datadir}/apps/koshell/
%{tde_datadir}/apps/thesaurus/
%{tde_datadir}/config.kcfg/koshell.kcfg
%{tde_tdedocdir}/HTML/en/koffice/
%{tde_tdedocdir}/HTML/en/koshell/
%{tde_tdedocdir}/HTML/en/thesaurus/
%{tde_datadir}/icons/crystalsvg/*/*/*
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/icons/locolor/*/*/*
%{tde_datadir}/services/clipartthumbnail.desktop
%{tde_datadir}/services/tdefile_abiword.desktop
%{tde_datadir}/services/tdefile_gnumeric.desktop
%{tde_datadir}/services/tdefile_koffice.desktop
%{tde_datadir}/services/tdefile_ooo.desktop
%{tde_datadir}/services/kwmailmerge*.desktop
%{tde_datadir}/services/kodocinfopropspage.desktop
%{tde_datadir}/services/kofficethumbnail.desktop
%{tde_datadir}/services/kounavail.desktop
%{tde_datadir}/services/kprkword.desktop
%{tde_datadir}/services/thesaurustool.desktop
%{tde_datadir}/servicetypes/kochart.desktop
%{tde_datadir}/servicetypes/kofficepart.desktop
%{tde_datadir}/servicetypes/koplugin.desktop
%{tde_datadir}/servicetypes/kwmailmerge.desktop
%{tde_datadir}/servicetypes/widgetfactory.desktop
%{tde_tdeappdir}/*koffice.desktop
%{tde_tdeappdir}/KThesaurus.desktop
%{tde_tdeappdir}/*koshell.desktop
%{tde_datadir}/apps/kofficewidgets/
%if 0%{?with_kross}
%if 0%{?with_python}
%{tde_datadir}/apps/kross/
%{tde_tdelibdir}/krosspython.*
%endif
%if 0%{?with_ruby}
%{tde_tdelibdir}/krossruby.*
%endif
%endif
%{tde_mandir}/man1/koconverter.1*
%{tde_mandir}/man1/koscript.1*
%{tde_mandir}/man1/koshell.1*
%{tde_mandir}/man1/kthesaurus.1*

##########

%package libs
Summary:		Runtime libraries for %{name} 
Group:			System Environment/Libraries
Conflicts:      %{name} <= %{version}-%{release}
Requires:		trinity-tdelibs
License:		LGPLv2+

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%doc COPYING.LIB
#_libdir/libk*common.so.*
%{tde_libdir}/libkarboncommon.so.*
%{tde_libdir}/libkspreadcommon.so.*
%{tde_libdir}/libkdchart.so.*
%{tde_libdir}/libkochart.so.*
%{tde_libdir}/libkofficecore.so.*
%{tde_libdir}/libkofficeui.so.*
%{tde_libdir}/libkotext.so.*
%{tde_libdir}/libkowmf.so.*
%{tde_libdir}/libkopainter.so.*
%{tde_libdir}/libkstore.so.*
%{tde_libdir}/libkwmailmerge_interface.so.*
%{tde_libdir}/libkwmf.so.*
%{tde_libdir}/libkformulalib.so.*
%{tde_libdir}/libkopalette.so.*
%{tde_libdir}/libkoproperty.so.*
%if 0%{?with_kross}
%{tde_libdir}/libkrossapi.so.*
%{tde_libdir}/libkrossmain.so.*
%endif
%{tde_mandir}/man1/kspread.1*

##########

%package devel
Summary:		Development files for %{name} 
Group:			Development/Libraries
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
License:		LGPLv2+

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/koffice-apidocs/
%{tde_includedir}/*
# FIXME: include only shlib symlinks we know/want to export
%{tde_libdir}/lib*.so
%exclude %{tde_libdir}/libtdeinit_*.so
%exclude %{tde_libdir}/libkudesignercore.so

##########

%package kword
Summary:		A frame-based word processor capable of professional standard documents
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kword
%{summary}.

%files kword
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kword/
%{tde_bindir}/kword
%{tde_libdir}/libtdeinit_kword.so
%{tde_libdir}/libkwordprivate.so.*
%{tde_tdelibdir}/libkwordpart.*
%{tde_tdelibdir}/kword.*
%{tde_datadir}/apps/kword/
%{tde_datadir}/services/kword*.desktop
%{tde_datadir}/services/kwserial*.desktop
%{tde_datadir}/templates/TextDocument.desktop
%{tde_datadir}/templates/.source/TextDocument.kwt
%{tde_tdeappdir}/*kword.desktop
%{tde_mandir}/man1/kword.1*

##########

%package kspread
Summary:		A powerful spreadsheet application
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kspread
%{summary}.

%files kspread
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kspread/
%{tde_bindir}/kspread
%{tde_libdir}/libtdeinit_kspread.so
%{tde_tdelibdir}/kspread.*
%{tde_tdelibdir}/libkspreadpart.*
%{tde_tdelibdir}/kwmailmerge_kspread.*
%{tde_tdelibdir}/libcsvexport.*
%{tde_tdelibdir}/libcsvimport.*
%{tde_tdelibdir}/libgnumericexport.*
%{tde_tdelibdir}/libgnumericimport.*
%{tde_tdelibdir}/libkspreadhtmlexport.*
%{tde_tdelibdir}/libkspreadinsertcalendar.*
%{tde_tdelibdir}/libopencalcexport.*
%{tde_tdelibdir}/libopencalcimport.*
%{tde_tdelibdir}/libqproimport.*
%{tde_datadir}/apps/kspread/
%{tde_datadir}/services/kspread*.desktop
%{tde_datadir}/templates/SpreadSheet.desktop
%{tde_datadir}/templates/.source/SpreadSheet.kst
%{tde_tdeappdir}/*kspread.desktop
%if 0%{?with_kross}
%{tde_tdelibdir}/kspreadscripting.*
%{tde_tdelibdir}/krosskspreadcore.*
%endif

##########

%package kpresenter
Summary:		A full-featured presentation program
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kpresenter
%{summary}.

%files kpresenter
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kpresenter/
%{tde_bindir}/kpresenter
%{tde_bindir}/kprconverter.pl
%{tde_libdir}/libtdeinit_kpresenter.so
%{tde_libdir}/libkpresenterimageexport.so.*
%{tde_libdir}/libkpresenterprivate.so.*
%{tde_tdelibdir}/*kpresenter*.*
%{tde_datadir}/apps/kpresenter/
%{tde_datadir}/services/kpresenter*.desktop
%{tde_datadir}/templates/Presentation.desktop
%{tde_datadir}/templates/.source/Presentation.kpt
%{tde_tdeappdir}/*kpresenter.desktop
%{tde_mandir}/man1/kprconverter.pl.1*
%{tde_mandir}/man1/kpresenter.1*

##########

%package kivio
Summary:		A flowcharting application
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      kivio < %{?epoch:%{epoch}:}%{version}-%{release}

%description kivio
%{summary}.

%files kivio
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kivio/
%{tde_bindir}/kivio
%{tde_libdir}/libtdeinit_kivio.so
%{tde_libdir}/libkiviocommon.so.*
%{tde_tdelibdir}/*kivio*.*
%{tde_tdelibdir}/straight_connector.*
%{tde_datadir}/apps/kivio/
%{tde_datadir}/config.kcfg/kivio.kcfg
%{tde_datadir}/services/kivio*.desktop
%{tde_tdeappdir}/*kivio.desktop
%{tde_mandir}/man1/kivio.1*

##########

%package karbon
Summary:		A vector drawing application
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description karbon
%{summary}.

%files karbon
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/karbon/
%{tde_bindir}/karbon
%{tde_libdir}/libtdeinit_karbon.so
%exclude %{tde_tdelibdir}/libkarbonepsimport.*
%{tde_tdelibdir}/*karbon*.*
%{tde_tdelibdir}/libwmfexport.*
%{tde_tdelibdir}/libwmfimport.*
%{tde_datadir}/apps/karbon/
%{tde_datadir}/services/karbon*
%{tde_datadir}/servicetypes/karbon_module.desktop
%{tde_datadir}/templates/Illustration.desktop
%{tde_datadir}/templates/.source/Illustration.karbon
%{tde_tdeappdir}/*karbon.desktop
%{tde_mandir}/man1/karbon.1*

##########

%package kugar
Summary:		A tool for generating business quality reports
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kugar
%{summary}.

%files kugar
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kugar/
%{tde_bindir}/kugar
%{tde_bindir}/kudesigner
%{tde_libdir}/libtdeinit_kugar.so
%{tde_libdir}/libtdeinit_kudesigner.so
%{tde_libdir}/libkugarlib.so.*
%{tde_libdir}/libkudesignercore.so
%{tde_tdelibdir}/kudesigner.*
%{tde_tdelibdir}/kugar.*
%{tde_tdelibdir}/libkudesignerpart.*
%{tde_tdelibdir}/libkugarpart.*
%{tde_datadir}/apps/kudesigner/
%{tde_datadir}/apps/kugar/
%{tde_datadir}/services/kugar*.desktop
%{tde_tdeappdir}/*kugar.desktop
%{tde_tdeappdir}/*kudesigner.desktop
%{tde_mandir}/man1/kudesigner.1*
%{tde_mandir}/man1/kugar.1*

##########

%package kexi
Summary:		An integrated environment for managing data
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?with_postgresql} == 0
Obsoletes:		%{name}-kexi-driver-pgsql < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description kexi
%{summary}.
For additional database drivers take a look at %{name}-kexi-driver-*

%files kexi
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kexi/
%{tde_bindir}/kexi*
%{tde_bindir}/ksqlite*
%{tde_libdir}/libtdeinit_kexi.so
%{tde_libdir}/libkexi*.so.*
%{tde_libdir}/libkformdesigner.so.*
%{tde_tdelibdir}/kformdesigner_*.*
%{tde_tdelibdir}/kexidb_sqlite2driver.*
%{tde_tdelibdir}/kexidb_sqlite3driver.*
%{tde_tdelibdir}/kexihandler_*.*
%{tde_tdelibdir}/kexi.*
# moved here to workaround bug #394101, alternative is to move libkexi(db|dbparser|utils) to -libs)
%{tde_tdelibdir}/libkspreadkexiimport.*
%config(noreplace) %{tde_confdir}/kexirc
%config(noreplace) %{tde_confdir}/magic/kexi.magic
%{tde_datadir}/mimelnk/application/*
%{tde_datadir}/servicetypes/kexi*.desktop
%{tde_datadir}/services/kexi/
%{tde_datadir}/apps/kexi/
%{tde_datadir}/services/kformdesigner/
%{tde_tdeappdir}/*kexi.desktop
%{tde_datadir}/services/kexidb_sqlite*driver.desktop
%if 0%{?with_kross}
%{tde_bindir}/krossrunner
%{tde_tdelibdir}/krosskexiapp.*
%{tde_tdelibdir}/krosskexidb.*
%endif
%config(noreplace) %{tde_confdir}/magic/kexi.magic.mgc

##########

%package kexi-driver-mysql
Summary:		Mysql-driver for kexi
Group:			Applications/Productivity
Requires:		%{name}-kexi = %{?epoch:%{epoch}:}%{version}-%{release}

%description kexi-driver-mysql
%{summary}.

%files kexi-driver-mysql
%defattr(-,root,root,-)
%{tde_tdelibdir}/kexidb_mysqldriver.*
%{tde_tdelibdir}/keximigrate_mysql.*
%{tde_datadir}/services/keximigrate_mysql.desktop
%{tde_datadir}/services/kexidb_mysqldriver.desktop

##########

%if 0%{?with_postgresql}

%package kexi-driver-pgsql
Summary:		Postgresql driver for kexi
Group:			Applications/Productivity
Requires:		%{name}-kexi = %{?epoch:%{epoch}:}%{version}-%{release}

%description kexi-driver-pgsql
%{summary}.

%files kexi-driver-pgsql
%defattr(-,root,root,-)
%{tde_tdelibdir}/kexidb_pqxxsqldriver.*
%{tde_tdelibdir}/keximigrate_pqxx.*
%{tde_datadir}/services/kexidb_pqxxsqldriver.desktop
%{tde_datadir}/services/keximigrate_pqxx.desktop

%endif

##########

%package kchart
Summary:		An integrated graph and chart drawing tool
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kchart
%{summary}.

%files kchart
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kchart/
%{tde_bindir}/kchart
%{tde_libdir}/libkchart*.so.*
%{tde_libdir}/libtdeinit_kchart.so
%{tde_tdelibdir}/*kchart*.*
%{tde_datadir}/apps/kchart/
%{tde_datadir}/services/kchart*.desktop
%{tde_tdeappdir}/*kchart.desktop
%{tde_mandir}/man1/kchart.1*

##########

%package kformula
Summary:		A powerful formula editor
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?mgaversion} || 0%{?mdkversion}
Requires:		fonts-ttf-dejavu
%else
%if 0%{?fedora} >= 11 || 0%{?rhel} == 6 || 0%{?rhel} == 7
Requires:		dejavu-lgc-sans-fonts
%endif
%if 0%{?fedora} >= 11 || 0%{?rhel} == 6 || 0%{?rhel} == 7
Requires:		lyx-cmex10-fonts
%endif
%if 0%{?rhel} == 5
Requires:		dejavu-lgc-fonts 
%endif
%if 0%{?suse_version} >= 1220
Requires:		dejavu-fonts 
%endif
%if 0%{?suse_version} == 1140
Requires:		dejavu
%endif
%endif

%description kformula
%{summary}.

%files kformula
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kformula/
%{tde_bindir}/kformula
%{tde_libdir}/libtdeinit_kformula.so
%{tde_tdelibdir}/*kformula*.*
%{tde_datadir}/apps/kformula/
%{tde_datadir}/services/kformula*.desktop
%{tde_tdeappdir}/*kformula.desktop
%{tde_mandir}/man1/kformula.1*

##########

%package filters
Summary:		Import and Export Filters for KOffice
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description filters
%{summary}.

%files filters
%defattr(-,root,root,-)
%{tde_libdir}/libkwordexportfilters.so.*
%{tde_tdelibdir}/libabiwordexport.*
%{tde_tdelibdir}/libabiwordimport.*
%{tde_tdelibdir}/libamiproexport.*
%{tde_tdelibdir}/libamiproimport.*
%{tde_tdelibdir}/libapplixspreadimport.*
%{tde_tdelibdir}/libapplixwordimport.*
%{tde_tdelibdir}/libasciiexport.*
%{tde_tdelibdir}/libasciiimport.*
%{tde_tdelibdir}/libdbaseimport.*
%{tde_tdelibdir}/libdocbookexport.*
%{tde_tdelibdir}/libexcelimport.*
%{tde_tdelibdir}/libgenerickofilter.*
%{tde_tdelibdir}/libhtmlexport.*
%{tde_tdelibdir}/libhtmlimport.*
%{tde_tdelibdir}/libkarbonepsimport.*
%{tde_tdelibdir}/libkfolatexexport.*
%{tde_tdelibdir}/libkfomathmlexport.*
%{tde_tdelibdir}/libkfomathmlimport.*
%{tde_tdelibdir}/libkfopngexport.*
%{tde_tdelibdir}/libkspreadlatexexport.*
%{tde_tdelibdir}/libkugarnopimport.*
%{tde_tdelibdir}/libkwordkword1dot3import.*
%{tde_tdelibdir}/libkwordlatexexport.*
%{tde_tdelibdir}/libmswriteexport.*
%{tde_tdelibdir}/libmswriteimport.*
%{tde_tdelibdir}/libooimpressexport.*
%{tde_tdelibdir}/libooimpressimport.*
%{tde_tdelibdir}/liboowriterexport.*
%{tde_tdelibdir}/liboowriterimport.*
%{tde_tdelibdir}/libpalmdocexport.*
%{tde_tdelibdir}/libpalmdocimport.*
%{tde_tdelibdir}/libpdfimport.*
%{tde_tdelibdir}/librtfexport.*
%{tde_tdelibdir}/librtfimport.*
%{tde_tdelibdir}/libwmlexport.*
%{tde_tdelibdir}/libwmlimport.*
%{tde_tdelibdir}/libwpexport.*
%{tde_tdelibdir}/libwpimport.*
%if 0%{?with_wv2}
%{tde_tdelibdir}/libmswordimport.*
%endif
%{tde_tdelibdir}/libxsltimport.*
%{tde_tdelibdir}/libxsltexport.*
%{tde_tdelibdir}/libhancomwordimport.*
%{tde_tdelibdir}/libkfosvgexport.*
%{tde_tdelibdir}/liboodrawimport.*
%{tde_tdelibdir}/libolefilter.*
%{tde_datadir}/apps/xsltfilter/
%{tde_datadir}/services/generic_filter.desktop
%{tde_datadir}/services/ole_powerpoint97_import.desktop
%{tde_datadir}/services/xslt*.desktop
%{tde_datadir}/servicetypes/kofilter*.desktop

##########

%package kplato
Summary:		An integrated project management and planning tool
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kplato
%{summary}.

%files kplato
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kplato/
%{tde_bindir}/kplato
%{tde_libdir}/libtdeinit_kplato.so
%{tde_tdelibdir}/kplato.*
%{tde_tdelibdir}/libkplatopart.*
%{tde_datadir}/apps/kplato/
%{tde_datadir}/services/kplatopart.desktop
%{tde_tdeappdir}/*kplato.desktop

##########

%package chalk
Summary:		pixel-based image manipulation program for the TDE Office Suite [Trinity]
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-chalk-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-filters = %{?epoch:%{epoch}:}%{version}-%{release}

%description chalk
Chalk is a painting and image editing application for KOffice. Chalk contains
both ease-of-use and fun features like guided painting.

This package is part of the TDE Office Suite.

%files chalk
%defattr(-,root,root,-)
%{tde_bindir}/chalk
%{tde_tdelibdir}/chalkblurfilter.la
%{tde_tdelibdir}/chalkblurfilter.so
%{tde_tdelibdir}/chalkbumpmap.la
%{tde_tdelibdir}/chalkbumpmap.so
%{tde_tdelibdir}/chalkcimg.la
%{tde_tdelibdir}/chalkcimg.so
%{tde_tdelibdir}/chalk_cmyk_*
%{tde_tdelibdir}/chalkcmykplugin.la
%{tde_tdelibdir}/chalkcmykplugin.so
%{tde_tdelibdir}/chalkcolorify.la
%{tde_tdelibdir}/chalkcolorify.so
%{tde_tdelibdir}/chalkcolorrange.la
%{tde_tdelibdir}/chalkcolorrange.so
%{tde_tdelibdir}/chalkcolorsfilters.la
%{tde_tdelibdir}/chalkcolorsfilters.so
%{tde_tdelibdir}/chalkcolorspaceconversion.la
%{tde_tdelibdir}/chalkcolorspaceconversion.so
%{tde_tdelibdir}/chalkconvolutionfilters.la
%{tde_tdelibdir}/chalkconvolutionfilters.so
%{tde_tdelibdir}/chalkdefaultpaintops.la
%{tde_tdelibdir}/chalkdefaultpaintops.so
%{tde_tdelibdir}/chalkdefaulttools.la
%{tde_tdelibdir}/chalkdefaulttools.so
%{tde_tdelibdir}/chalkdropshadow.la
%{tde_tdelibdir}/chalkdropshadow.so
%{tde_tdelibdir}/chalkembossfilter.la
%{tde_tdelibdir}/chalkembossfilter.so
%{tde_tdelibdir}/chalkexample.la
%{tde_tdelibdir}/chalkexample.so
%{tde_tdelibdir}/chalkextensioncolorsfilters.la
%{tde_tdelibdir}/chalkextensioncolorsfilters.so
%{tde_tdelibdir}/chalkfastcolortransfer.la
%{tde_tdelibdir}/chalkfastcolortransfer.so
%{tde_tdelibdir}/chalkfiltersgallery.la
%{tde_tdelibdir}/chalkfiltersgallery.so
%{tde_tdelibdir}/chalk_gray_*
%{tde_tdelibdir}/chalkgrayplugin.la
%{tde_tdelibdir}/chalkgrayplugin.so
%{tde_tdelibdir}/chalkhistogramdocker.la
%{tde_tdelibdir}/chalkhistogramdocker.so
%{tde_tdelibdir}/chalkhistogram.la
%{tde_tdelibdir}/chalkhistogram.so
%{tde_tdelibdir}/chalkimageenhancement.la
%{tde_tdelibdir}/chalkimageenhancement.so
%{tde_tdelibdir}/chalkimagesize.la
%{tde_tdelibdir}/chalkimagesize.so
%{tde_tdelibdir}/chalk.la
%{tde_tdelibdir}/chalklenscorrectionfilter.la
%{tde_tdelibdir}/chalklenscorrectionfilter.so
%{tde_tdelibdir}/chalklevelfilter.la
%{tde_tdelibdir}/chalklevelfilter.so
%{tde_tdelibdir}/chalk_lms_*
%{tde_tdelibdir}/chalkmodifyselection.la
%{tde_tdelibdir}/chalkmodifyselection.so
%{tde_tdelibdir}/chalknoisefilter.la
%{tde_tdelibdir}/chalknoisefilter.so
%{tde_tdelibdir}/chalkoilpaintfilter.la
%{tde_tdelibdir}/chalkoilpaintfilter.so
%{tde_tdelibdir}/chalkpixelizefilter.la
%{tde_tdelibdir}/chalkpixelizefilter.so
%{tde_tdelibdir}/chalkraindropsfilter.la
%{tde_tdelibdir}/chalkraindropsfilter.so
%{tde_tdelibdir}/chalkrandompickfilter.la
%{tde_tdelibdir}/chalkrandompickfilter.so
%{tde_tdelibdir}/chalk_rgb_*
%{tde_tdelibdir}/chalkrgbplugin.la
%{tde_tdelibdir}/chalkrgbplugin.so
%{tde_tdelibdir}/chalkrotateimage.la
%{tde_tdelibdir}/chalkrotateimage.so
%{tde_tdelibdir}/chalkroundcornersfilter.la
%{tde_tdelibdir}/chalkroundcornersfilter.so
%{tde_tdelibdir}/chalkselectiontools.la
%{tde_tdelibdir}/chalkselectiontools.so
%{tde_tdelibdir}/chalkselectopaque.la
%{tde_tdelibdir}/chalkselectopaque.so
%{tde_tdelibdir}/chalkseparatechannels.la
%{tde_tdelibdir}/chalkseparatechannels.so
%{tde_tdelibdir}/chalkshearimage.la
%{tde_tdelibdir}/chalkshearimage.so
%{tde_tdelibdir}/chalksmalltilesfilter.la
%{tde_tdelibdir}/chalksmalltilesfilter.so
%{tde_tdelibdir}/chalk.so
%{tde_tdelibdir}/chalkscreenshot.la
%{tde_tdelibdir}/chalkscreenshot.so
%{tde_tdelibdir}/chalksobelfilter.la
%{tde_tdelibdir}/chalksobelfilter.so
%{tde_tdelibdir}/chalksubstrate.la
%{tde_tdelibdir}/chalksubstrate.so
%{tde_tdelibdir}/chalktoolcrop.la
%{tde_tdelibdir}/chalktoolcrop.so
%{tde_tdelibdir}/chalktoolcurves.la
%{tde_tdelibdir}/chalktoolcurves.so
%{tde_tdelibdir}/chalktoolfilter.la
%{tde_tdelibdir}/chalktoolfilter.so
%{tde_tdelibdir}/chalktoolperspectivegrid.la
%{tde_tdelibdir}/chalktoolperspectivegrid.so
%{tde_tdelibdir}/chalktoolperspectivetransform.la
%{tde_tdelibdir}/chalktoolperspectivetransform.so
%{tde_tdelibdir}/chalktoolpolygon.la
%{tde_tdelibdir}/chalktoolpolygon.so
%{tde_tdelibdir}/chalktoolpolyline.la
%{tde_tdelibdir}/chalktoolpolyline.so
%{tde_tdelibdir}/chalktoolselectsimilar.la
%{tde_tdelibdir}/chalktoolselectsimilar.so
%{tde_tdelibdir}/chalktoolstar.la
%{tde_tdelibdir}/chalktoolstar.so
%{tde_tdelibdir}/chalktooltransform.la
%{tde_tdelibdir}/chalktooltransform.so
%{tde_tdelibdir}/chalkunsharpfilter.la
%{tde_tdelibdir}/chalkunsharpfilter.so
%{tde_tdelibdir}/chalkwavefilter.la
%{tde_tdelibdir}/chalkwavefilter.so
%{tde_tdelibdir}/chalkwetplugin.la
%{tde_tdelibdir}/chalkwetplugin.so
%{tde_tdelibdir}/chalk_ycbcr_*
%if 0%{?with_graphicsmagick}
%{tde_tdelibdir}/libchalkgmagickexport.la
%{tde_tdelibdir}/libchalkgmagickexport.so
%{tde_tdelibdir}/libchalkgmagickimport.la
%{tde_tdelibdir}/libchalkgmagickimport.so
%{tde_tdelibdir}/libchalkjpegexport.la
%{tde_tdelibdir}/libchalkjpegexport.so
%{tde_tdelibdir}/libchalkjpegimport.la
%{tde_tdelibdir}/libchalkjpegimport.so
%endif
%{tde_tdelibdir}/libchalk_openexr_export.la
%{tde_tdelibdir}/libchalk_openexr_export.so
%{tde_tdelibdir}/libchalk_openexr_import.la
%{tde_tdelibdir}/libchalk_openexr_import.so
%{tde_tdelibdir}/libchalkpart.la
%{tde_tdelibdir}/libchalkpart.so
%{tde_tdelibdir}/libchalkpdfimport.la
%{tde_tdelibdir}/libchalkpdfimport.so
%{tde_tdelibdir}/libchalkpngexport.la
%{tde_tdelibdir}/libchalkpngexport.so
%{tde_tdelibdir}/libchalkpngimport.la
%{tde_tdelibdir}/libchalkpngimport.so
%{tde_tdelibdir}/libchalk_raw_import.la
%{tde_tdelibdir}/libchalk_raw_import.so
%if 0%{?with_graphicsmagick}
%{tde_tdelibdir}/libchalktiffexport.la
%{tde_tdelibdir}/libchalktiffexport.so
%{tde_tdelibdir}/libchalktiffimport.la
%{tde_tdelibdir}/libchalktiffimport.so
%endif
%{tde_libdir}/libtdeinit_chalk.so
%{tde_libdir}/libchalk_cmyk_*.so.*
%{tde_libdir}/libchalkcolor.so.*
%{tde_libdir}/libchalkcommon.so.*
%{tde_libdir}/libchalkgrayscale.so.*
%{tde_libdir}/libchalk_gray_*.so.*
%{tde_libdir}/libchalkimage.so.*
%{tde_libdir}/libchalk_lms_*.so.*
%{tde_libdir}/libchalk_rgb_*.so.*
%{tde_libdir}/libchalkrgb.so.*
%{tde_libdir}/libchalkui.so.*
%{tde_libdir}/libchalk_ycbcr_*.so.*
%if 0%{?with_kross}
%{tde_tdelibdir}/krosschalkcore.la
%{tde_tdelibdir}/krosschalkcore.so
%{tde_tdelibdir}/chalkscripting.la
%{tde_tdelibdir}/chalkscripting.so
%{tde_libdir}/libchalkscripting.so.*
%endif

##########

%package chalk-data
Summary:		data files for Chalk painting program [Trinity]
Group:			Applications/Productivity

%description chalk-data
This package contains architecture-independent data files for Chalk,
the painting program shipped with the TDE Office Suite.

See the chalk package for further information.

This package is part of the TDE Office Suite.

%files chalk-data
%defattr(-,root,root,-)
%{tde_tdeappdir}/chalk.desktop
%{tde_datadir}/applnk/.hidden/chalk_*.desktop
%{tde_datadir}/apps/chalk/
%{tde_datadir}/apps/chalkplugins/
%lang(en) %{tde_tdedocdir}/HTML/en/chalk/
%{tde_datadir}/services/chalk*.desktop
%{tde_datadir}/servicetypes/chalk*.desktop

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%if 0%{?mdkver}
touch config.h.in
%endif

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"
export kde_confdir="%{tde_confdir}"

%if 0%{?suse_version} == 1220
RD=$(ruby -r rbconfig -e 'printf("%s",Config::CONFIG["rubyhdrdir"])')
CXXFLAGS="${CXXFLAGS} -I${RD}/%_normalized_cpu-linux"
%endif

%if 0%{?suse_version} >= 1550
CXXFLAGS="${CXXFLAGS} -std=c++11"
%endif

# FTBFS on RHEL 5
%if 0%{?rhel} == 5
%__sed -i "kexi/migration/keximigratetest.cpp" \
       -e "/TDEApplication/ s|\");|\", true, true, true);|"
%endif

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
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --with-extra-libs=%{tde_libdir} \
  --with-extra-includes=%{tde_includedir}/arts \
  \
  --disable-kexi-macros \
  %{?with_kross:--enable-scripting} %{!?with_kross:--disable-scripting} \
  %{?with_postgresql:--enable-pgsql} %{!?with_postgresql:--disable-pgsql} \

# Ensure PQXX was detected (required by kexidb/pgsql)
%if "%{?with_postgresql}" != ""
if grep 'S\["compile_pgsql_plugin_TRUE"\]="#"' config.status; then
  exit 1
fi
%endif

# Ensure WV2 was detected
%if 0%{?with_wv2}
if grep 'S\["include_wv2_msword_filter_TRUE"\]="#"' config.status; then
  exit 2
fi
%endif

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Fix desktop icon location
%__mv -f "%{?buildroot}%{tde_datadir}/applnk/"*"/KThesaurus.desktop" "%{?buildroot}%{tde_tdeappdir}"

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file kudesigner    Office FlowChart
%suse_update_desktop_file kivio		Office FlowChart
%suse_update_desktop_file kchart	Office FlowChart
%suse_update_desktop_file kexi		Office Database
%suse_update_desktop_file -r chalk	Graphics RasterGraphics
%suse_update_desktop_file -r karbon     Graphics VectorGraphics
%suse_update_desktop_file kpresenter	Office Presentation
%suse_update_desktop_file kspread	Office Spreadsheet
%suse_update_desktop_file -u KThesaurus Office
%suse_update_desktop_file -r kformula   Science Math
%suse_update_desktop_file kword		Office WordProcessor
%suse_update_desktop_file koshell    Office Core-Office
%suse_update_desktop_file kplato        Office ProjectManagement
%endif

# Apps that should stay in TDE
for i in kivio kplato; do
  echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/${i}.desktop"
done

# Links duplicate files
%fdupes %{buildroot}

## unpackaged files
# fonts
rm -rfv %{buildroot}%{tde_datadir}/apps/kformula/fonts/
# libtool archives
rm -f %{buildroot}%{tde_libdir}/lib*.la
# shouldn't these be in koffice-l10n? 
rm -f %{buildroot}%{tde_datadir}/locale/pl/LC_MESSAGES/kexi_{add,delete}_column_gui_transl_pl.sh


%clean
%__rm -rf %{buildroot}


%changelog
