#
# spec file for package tdegraphics (version R14)
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
%define tde_pkg tdegraphics
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
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:    Trinity Desktop Environment - Graphics Applications
Group:      Productivity/Graphics/Viewers
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:		GPL-2.0+
%else
License:		GPLv2+
%endif

#Vendor:			Trinity Desktop
#Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:	%{name}-rpmlintrc

BuildRequires: trinity-tdelibs-devel >= %{tde_version}
BuildRequires: trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	libtool
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# LIBUSB support
%if 0%{?fedora} >= 37
BuildRequires:	libusb1-devel
BuildRequires:	libusb-compat-0.1-devel
%else
BuildRequires:	libusb-devel
%endif

# MNG support
%if 0%{?mdkver}
BuildRequires: %{_lib}mng-devel
%else
BuildRequires: libmng-devel
%endif

# TIFF support
%if 0%{?mdkver}
BuildRequires:	%{_lib}tiff-devel
%else
BuildRequires:	libtiff-devel
%endif

# PCRE support
BuildRequires: pcre-devel

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# GIF support
%if 0%{?suse_version} || 0%{?fedora} >= 28 || 0%{?rhel} >= 8
BuildRequires: giflib-devel
%else
%if 0%{?mdkver}
BuildRequires: %{_lib}gif-devel
%else
BuildRequires: libungif-devel
%endif
%endif

# GPHOTO2 support
%if 0%{?rhel} == 4 || 0%{?rhel} == 5 || 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mdkver}
BuildRequires:	%{_lib}gphoto-devel
%else
BuildRequires:	gphoto2-devel
%endif
%else
BuildRequires:	libgphoto2-devel
%endif

# PAPER support
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_paper 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}paper-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	libpaper-devel
%endif
%endif

# T1LIB support
%if 0%{?suse_version} && 0%{?suse_version} <= 1230
%define with_t1lib 1
BuildRequires:	t1lib-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion} || (0%{?rhel} >= 5 && 0%{?rhel} <= 7) || 0%{?fedora}
%define with_t1lib 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}t1lib-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	t1lib-devel
%endif
%endif

# SANE support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}sane1-devel
%else
BuildRequires:	sane-backends-devel
%endif

# LIBXXF86VM support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xxf86vm-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version} >= 1210
BuildRequires:	libXxf86vm-devel
%endif

# XMU support
%if 0%{?suse_version} == 1140
BuildRequires:	xorg-x11-libXmu-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version} >= 1210
BuildRequires: libXmu-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion} >= 4
BuildRequires: %{_lib}xmu-devel
%endif
%if 0%{?mgaversion} == 2 || 0%{?mgaversion} == 3
BuildRequires:	%{_lib}xmu%{?mgaversion:6}-devel
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

# DRM support
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%else
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}drm-devel
%else
BuildRequires: libdrm-devel
%endif
%endif

# OPENEXR support
%if 0%{?mdkver} >= 5000000
BuildRequires:	%{_lib}openexr-devel
%else
BuildRequires:	OpenEXR-devel
%endif

# POPPLER support
%define with_pdf 1
%if 0%{?with_pdf}
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
%endif

# LCMS support
%if 0%{?suse_version} || 0%{?rhel} >= 7
BuildRequires: liblcms-devel
%else
BuildRequires: lcms-devel
%endif

# FRIBIDI support
BuildRequires: fribidi-devel

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# kamera
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
%define build_kamera 1
%endif

# kmrml (deprecated)
#define build_kmrml 1
%if 0%{?build_kmrml}
#Requires:		gift
%else
Obsoletes:		trinity-kmrml < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

Obsoletes:	trinity-kdegraphics < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdegraphics = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdegraphics-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdegraphics-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdegraphics-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdegraphics-extras = %{?epoch:%{epoch}:}%{version}-%{release}


%{?build_kamera:Requires: trinity-kamera = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: trinity-kcoloredit = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kdvi = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kfax = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kfaxview = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kgamma = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kghostview = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kiconedit = %{?epoch:%{epoch}:}%{version}-%{release}
%{?build_kmrml:Requires: trinity-kmrml = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: trinity-kolourpaint = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kooka = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpdf = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpovmodeler = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kruler = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksnapshot = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksvg = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kview = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kviewshell = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libkscan = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?with_pdf}
Requires: trinity-libpoppler-tqt = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description
Graphics applications for the Trinity Desktop Environment, including
%if 0%{?build_kamera}
* kamera (digital camera support)
%endif
* kcoloredit (palette editor and color chooser)
* kdvi (displays TeX .dvi files)
* kfax
* kfaxview
* kghostview (displays postscript files)
* kiconedit (icon editor)
* kooka (scanner application)
* kpdf (displays PDF files)
* kpovmodler
* kruler (screen ruler and color measurement tool)
* ksnapshot (screen capture utility)
* kview (image viewer for GIF, JPEG, TIFF, etc.)

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README

##########

%if 0%{?build_kamera}

%package -n trinity-kamera
Summary:	Digital camera io_slave for Konqueror
Group:		Hardware/Camera

%description -n trinity-kamera
This is a digital camera io_slave for TDE which uses gphoto2 and libgpio
to allow access to your camera's pictures with the URL camera:/

%files -n trinity-kamera
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcm_kamera.la
%{tde_tdelibdir}/kcm_kamera.so
%{tde_tdelibdir}/tdeio_kamera.la
%{tde_tdelibdir}/tdeio_kamera.so
%{tde_tdeappdir}/kamera.desktop
%{tde_datadir}/services/camera.protocol
%{tde_tdedocdir}/HTML/en/kamera/
%{tde_tdedocdir}/HTML/en/tdeioslave/camera/

%endif

##########

%package -n trinity-kcoloredit
Summary:	A color palette editor and color picker for TDE
Group:		Productivity/Graphics/Viewers

%description -n trinity-kcoloredit
This package contains two programs, a color palette editor and also a color
picker.

%files -n trinity-kcoloredit
%defattr(-,root,root,-)
%{tde_bindir}/kcolorchooser
%{tde_bindir}/kcoloredit
%{tde_tdeappdir}/kcolorchooser.desktop
%{tde_tdeappdir}/kcoloredit.desktop
%{tde_datadir}/apps/kcoloredit/
%{tde_datadir}/icons/hicolor/*/apps/kcolorchooser.png
%{tde_datadir}/icons/hicolor/*/apps/kcoloredit.png
%{tde_tdedocdir}/HTML/en/kcoloredit/
%{tde_mandir}/man1/kcolorchooser.1*
%{tde_mandir}/man1/kcoloredit.1*

##########

%package kfile-plugins
Summary:	TDE metainfo plugins for graphic files
Group:		System/GUI/Other
 
%description kfile-plugins
This packages provides meta information for graphic files (file sizes,
tags, etc. all from within the file manager).

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/gsthumbnail.la
%{tde_tdelibdir}/gsthumbnail.so
%{tde_tdelibdir}/tdefile_bmp.la
%{tde_tdelibdir}/tdefile_bmp.so
%{tde_tdelibdir}/tdefile_dds.la
%{tde_tdelibdir}/tdefile_dds.so
%{tde_tdelibdir}/tdefile_dvi.la
%{tde_tdelibdir}/tdefile_dvi.so
%{tde_tdelibdir}/tdefile_exr.la
%{tde_tdelibdir}/tdefile_exr.so
%{tde_tdelibdir}/tdefile_gif.la
%{tde_tdelibdir}/tdefile_gif.so
%{tde_tdelibdir}/tdefile_ico.la
%{tde_tdelibdir}/tdefile_ico.so
%{tde_tdelibdir}/tdefile_jpeg.la
%{tde_tdelibdir}/tdefile_jpeg.so
%{tde_tdelibdir}/tdefile_pcx.la
%{tde_tdelibdir}/tdefile_pcx.so
%if 0%{?with_pdf}
%{tde_tdelibdir}/tdefile_pdf.la
%{tde_tdelibdir}/tdefile_pdf.so
%endif
%{tde_tdelibdir}/tdefile_png.la
%{tde_tdelibdir}/tdefile_png.so
%{tde_tdelibdir}/tdefile_pnm.la
%{tde_tdelibdir}/tdefile_pnm.so
%{tde_tdelibdir}/tdefile_ps.la
%{tde_tdelibdir}/tdefile_ps.so
%{tde_tdelibdir}/tdefile_raw.la
%{tde_tdelibdir}/tdefile_raw.so
%{tde_tdelibdir}/tdefile_rgb.la
%{tde_tdelibdir}/tdefile_rgb.so
%{tde_tdelibdir}/tdefile_tga.la
%{tde_tdelibdir}/tdefile_tga.so
%{tde_tdelibdir}/tdefile_tiff.la
%{tde_tdelibdir}/tdefile_tiff.so
%{tde_tdelibdir}/tdefile_xbm.la
%{tde_tdelibdir}/tdefile_xbm.so
%{tde_tdelibdir}/tdefile_xpm.la
%{tde_tdelibdir}/tdefile_xpm.so
%{tde_datadir}/services/gsthumbnail.desktop
%{tde_datadir}/services/tdefile_bmp.desktop
%{tde_datadir}/services/tdefile_dds.desktop
%{tde_datadir}/services/tdefile_dvi.desktop
%{tde_datadir}/services/tdefile_exr.desktop
%{tde_datadir}/services/tdefile_gif.desktop
%{tde_datadir}/services/tdefile_ico.desktop
%{tde_datadir}/services/tdefile_jpeg.desktop
%{tde_datadir}/services/tdefile_pcx.desktop
%if 0%{?with_pdf}
%{tde_datadir}/services/tdefile_pdf.desktop
%endif
%{tde_datadir}/services/tdefile_png.desktop
%{tde_datadir}/services/tdefile_pnm.desktop
%{tde_datadir}/services/tdefile_ps.desktop
%{tde_datadir}/services/tdefile_raw.desktop
%{tde_datadir}/services/tdefile_rgb.desktop
%{tde_datadir}/services/tdefile_tga.desktop
%{tde_datadir}/services/tdefile_tiff.desktop
%{tde_datadir}/services/tdefile_xbm.desktop
%{tde_datadir}/services/tdefile_xpm.desktop

##########

%package -n trinity-kdvi
Summary:	Dvi viewer for TDE
Group:		Productivity/Graphics/Viewers

%description -n trinity-kdvi
This program and KPart allow the user to display *.DVI files from TeX.

%files -n trinity-kdvi
%defattr(-,root,root,-)
%{tde_bindir}/kdvi
%{tde_tdelibdir}/kdvipart.la
%{tde_tdelibdir}/kdvipart.so
%{tde_tdeappdir}/kdvi.desktop
%{tde_datadir}/apps/kdvi/
%{tde_datadir}/config.kcfg/kdvi.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kdvi.png
%{tde_datadir}/icons/hicolor/scalable/apps/kdvi.svgz
%{tde_datadir}/services/kdvimultipage.desktop
%{tde_tdedocdir}/HTML/en/kdvi/
%{tde_mandir}/man1/kdvi.1*

##########

%package -n trinity-kfax
Summary:	G3/G4 fax viewer for Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-kfax
A fax viewer for Trinity, supporting the display of raw and tiffed fax images
(g3, g3-2d, g4).

%files -n trinity-kfax
%defattr(-,root,root,-)
%{tde_bindir}/kfax
%{tde_tdeappdir}/kfax.desktop
%{tde_datadir}/apps/kfax/
%{tde_datadir}/icons/hicolor/??x??/apps/kfax.png
%{tde_datadir}/icons/hicolor/scalable/apps/kfax.svgz
%{tde_tdedocdir}/HTML/en/kfax/
%{tde_mandir}/man1/kfax.1*

##########

%package -n trinity-kfaxview
Summary:	G3/G4 fax viewer for Trinity using kviewshell
Group:		Productivity/Publishing/TeX/Frontends

%description -n trinity-kfaxview
A fax viewer for Trinity, supporting the display of raw and tiffed fax images
(g3, g3-2d, g4).

This faxviewer uses kviewshell and is intended to replace the standalone
kfax application once it reproduces all of kfax's features.

%files -n trinity-kfaxview
%defattr(-,root,root,-)
%{tde_bindir}/kfaxview
%{tde_libdir}/libkfaximage.so.*
%{tde_tdelibdir}/kfaxviewpart.*
%{tde_tdeappdir}/kfaxview.desktop
%{tde_datadir}/apps/kfaxview/
%{tde_datadir}/icons/hicolor/??x??/apps/kfaxview.png
%{tde_datadir}/icons/hicolor/scalable/apps/kfaxview.svgz
%{tde_datadir}/services/kfaxmultipage.desktop
%{tde_datadir}/services/kfaxmultipage_tiff.desktop
%{tde_tdedocdir}/HTML/en/kfaxview/
%{tde_mandir}/man1/kfaxview.1*

##########

%package -n trinity-kgamma
Summary:	Gamma correction module for the Trinity Control Center
Group:		Productivity/Graphics/Viewers

%description -n trinity-kgamma
KGamma is a Trinity Control Center module for gamma calibration/correction
of XFree86. With proper gamma settings, your display (websites, images,
etc.) will look the same on your monitor as on other monitors.

Homepage: http://kgamma.berlios.de/index2.php

%files -n trinity-kgamma
%defattr(-,root,root,-)
%{tde_bindir}/xf86gammacfg
%{tde_tdelibdir}/kcm_kgamma.la
%{tde_tdelibdir}/kcm_kgamma.so
%{tde_datadir}/applnk/.hidden/kgamma.desktop
%{tde_datadir}/apps/kgamma/
%{tde_datadir}/icons/hicolor/*/apps/kgamma.png
%{tde_tdedocdir}/HTML/en/kgamma/

##########

%package -n trinity-kghostview
Summary:	PostScript viewer for Trinity
Group:		Productivity/Graphics/Viewers
Requires:	ghostscript

%description -n trinity-kghostview
KGhostview is Trinity's PostScript viewer. It is a port of Tim Theisen's
Ghostview program which is used to view documents prepared in Adobe's
PostScript page description language. PostScript is the major page
description language for printing on UNIX systems, and this application is
useful to preview material intended for printing, or for reading documents
online.

%files -n trinity-kghostview
%defattr(-,root,root,-)
%{tde_bindir}/kghostview
%{tde_tdelibdir}/libkghostviewpart.la
%{tde_tdelibdir}/libkghostviewpart.so
%{tde_libdir}/libkghostviewlib.so.*
%{tde_tdeappdir}/kghostview.desktop
%{tde_datadir}/apps/tdeconf_update/kghostview.upd
%{tde_datadir}/apps/tdeconf_update/update-to-xt-names.pl
%{tde_datadir}/apps/kghostview/
%{tde_datadir}/config.kcfg/kghostview.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kghostview.png
%{tde_datadir}/services/kghostview_part.desktop
%{tde_tdedocdir}/HTML/en/kghostview/
%{tde_mandir}/man1/kghostview.1*

##########

%package -n trinity-tdeiconedit
Summary:	An icon editor for Trinity
Group:		Productivity/Graphics/Viewers

Obsoletes:	trinity-kiconedit < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kiconedit = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdeiconedit
TDEIconedit allows you easily to create and edit icons.

%files -n trinity-tdeiconedit
%defattr(-,root,root,-)
%{tde_bindir}/tdeiconedit
%{tde_tdeappdir}/tdeiconedit.desktop
%{tde_datadir}/apps/tdeiconedit/
%{tde_datadir}/icons/hicolor/*/apps/tdeiconedit.png
%{tde_tdedocdir}/HTML/en/tdeiconedit/
%{tde_mandir}/man1/tdeiconedit.1*

##########

%if 0%{?build_kmrml}

%package -n trinity-kmrml
Summary: 	A Konqueror plugin for searching pictures
Group:		Productivity/Graphics/Viewers

%description -n trinity-kmrml
MRML is short for Multimedia Retrieval Markup Language, which defines a
protocol for querying a server for images based on their content. See 
http://www.mrml.net about MRML and the GNU Image Finding Tool (GIFT), an 
MRML server.

%files -n trinity-kmrml
%defattr(-,root,root,-)
%{tde_bindir}/mrmlsearch
%{tde_tdelibdir}/kcm_kmrml.la
%{tde_tdelibdir}/kcm_kmrml.so
%{tde_tdelibdir}/kded_daemonwatcher.la
%{tde_tdelibdir}/kded_daemonwatcher.so
%{tde_tdelibdir}/tdeio_mrml.la
%{tde_tdelibdir}/tdeio_mrml.so
%{tde_tdelibdir}/libkmrmlpart.la
%{tde_tdelibdir}/libkmrmlpart.so
%{tde_tdelibdir}/mrmlsearch.la
%{tde_tdelibdir}/mrmlsearch.so
%{tde_libdir}/libtdeinit_mrmlsearch.so
%{tde_tdeappdir}/kcmkmrml.desktop
%{tde_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{tde_datadir}/mimelnk/text/mrml.desktop
%{tde_datadir}/services/kded/daemonwatcher.desktop
%{tde_datadir}/services/mrml.protocol
%{tde_datadir}/services/mrml_part.desktop

%endif

##########

%package -n trinity-kolourpaint
Summary:	A simple paint program for Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-kolourpaint
KolourPaint is a very simple paint program for Trinity. It aims to be
conceptually simple to understand; providing a level of functionality
targeted towards the average user. It's designed for daily tasks like:

* Painting - drawing diagrams and "finger painting" 
* Image Manipulation - editing screenshots and photos; applying effects 
* Icon Editing - drawing clipart and logos with transparency 

It's not an unusable and monolithic program where simple tasks like
drawing lines become near impossible. Nor is it so simple that it lacks
essential features like Undo/Redo.

Homepage: http://kolourpaint.sourceforge.net

%files -n trinity-kolourpaint
%defattr(-,root,root,-)
%{tde_bindir}/kolourpaint
%{tde_tdeappdir}/kolourpaint.desktop
%{tde_datadir}/apps/kolourpaint/
%{tde_datadir}/icons/hicolor/*/apps/kolourpaint.png
%{tde_datadir}/icons/hicolor/scalable/apps/kolourpaint.svgz
%{tde_tdedocdir}/HTML/en/kolourpaint/
%{tde_mandir}/man1/kolourpaint.1*

##########

%package -n trinity-kooka
Summary:	Scanner program for Trinity
Group:		Hardware/Scanner

%description -n trinity-kooka
Kooka is an open source GNU/Linux scan program based on SANE and
KScan library.

Kooka helps you to handle the most important scan parameters, find the
correct image file format to save and manage your scanned images. It
offers support for different OCR modules. Libkscan, a autonomous part
of Kooka, provides a scan service for easy and consistent use to all
KDE applications.

Install ocrad or gocr if you wish to enable optical character recognition
in kooka.

Homepage: http://kooka.kde.org/

%files -n trinity-kooka
%defattr(-,root,root,-)
%{tde_bindir}/kooka
%{tde_tdeappdir}/kooka.desktop
%{tde_datadir}/apps/kooka/
%config(noreplace) %{tde_confdir}/kookarc
%{tde_datadir}/icons/hicolor/*/apps/kooka.png
%{tde_tdedocdir}/HTML/en/kooka/
%{tde_mandir}/man1/kooka.1*

##########

%package -n trinity-kpdf
Summary:	PDF viewer for Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-kpdf
KPDF allows you to view PDF (Portable Document Format) files. This package
includes kpdfpart so you can embed in konqueror or run as a standalone
application.

%files -n trinity-kpdf
%defattr(-,root,root,-)
%{tde_bindir}/kpdf
%{tde_tdelibdir}/libkpdfpart.la
%{tde_tdelibdir}/libkpdfpart.so
%{tde_tdeappdir}/kpdf.desktop
%{tde_datadir}/apps/kpdf/
%{tde_datadir}/apps/kpdfpart/
%{tde_datadir}/config.kcfg/kpdf.kcfg
%{tde_tdedocdir}/HTML/en/kpdf/
%{tde_datadir}/icons/hicolor/*/apps/kpdf.png
%{tde_datadir}/icons/hicolor/scalable/apps/kpdf.svgz
%{tde_datadir}/services/kpdf_part.desktop
%{tde_mandir}/man1/kpdf.1*

##########

%package -n trinity-kpovmodeler
Summary:	A graphical editor for povray scenes
Group:		Productivity/Graphics/Viewers
#Requires:	povray

%description -n trinity-kpovmodeler
KPovmodeler is KDE's graphical editor for povray scenes. KPovModeler is a
modeling and composition program for creating POV-Ray scenes in KDE.

For most modelers, POV-Ray is nothing but a rendering engine. This greatly
limits the innate possibilities of the POV-Ray scripted language. This
is not the case for KPovModeler, which allows you to use all the features
of POV-Ray through the translation of POV-Ray language into a graphical
tree.

kpovmodeler uses the povray package, currently available only in Debian's
non-free, unsupported repository.

Homepage: http://www.kpovmodeler.org

%files -n trinity-kpovmodeler
%defattr(-,root,root,-)
%{tde_bindir}/kpovmodeler
%{tde_libdir}/libkpovmodeler.so.*
%{tde_tdelibdir}/libkpovmodelerpart.*
%{tde_tdeappdir}/kpovmodeler.desktop
%{tde_datadir}/apps/kpovmodeler/
%{tde_datadir}/icons/crystalsvg/*/mimetypes/kpovmodeler_doc.*
%{tde_datadir}/icons/hicolor/*/apps/kpovmodeler.*
%doc %{tde_tdedocdir}/HTML/en/kpovmodeler/
%{tde_mandir}/man1/kpovmodeler.1*

##########

%package -n trinity-kruler
Summary:	A screen ruler and color measurement tool for Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-kruler
Kruler is a screen ruler (using pixels) and color measurement tool for KDE.

%files -n trinity-kruler
%defattr(-,root,root,-)
%{tde_bindir}/kruler
%{tde_tdeappdir}/kruler.desktop
%{tde_datadir}/applnk/Graphics/kruler.desktop
%{tde_datadir}/apps/kruler/
%{tde_datadir}/icons/hicolor/*/apps/kruler.png
%{tde_tdedocdir}/HTML/en/kruler/
%{tde_mandir}/man1/kruler.1*

##########

%package -n trinity-ksnapshot
Summary:	Screenshot utility for Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-ksnapshot
KSnapshot is a simple applet for taking screenshots. It is capable of 
capturing images of either the whole desktop or just a single window. 
The images can then be saved in a variety of formats.

%files -n trinity-ksnapshot
%defattr(-,root,root,-)
%{tde_bindir}/ksnapshot
%{tde_tdeappdir}/ksnapshot.desktop
%{tde_datadir}/icons/hicolor/*/apps/ksnapshot.png
%{tde_datadir}/icons/hicolor/scalable/apps/ksnapshot.svgz
%{tde_tdedocdir}/HTML/en/ksnapshot/
%{tde_mandir}/man1/ksnapshot.1*

##########

%package -n trinity-ksvg
Summary:	SVG viewer for Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-ksvg
KSVG allows you view SVG (scalable vector graphics) files. This package
includes kpart so you can embed it in konqueror and a standalone
application.

%files -n trinity-ksvg
%defattr(-,root,root,-)
%{tde_bindir}/printnodetest
%{tde_bindir}/svgdisplay
%{tde_tdelibdir}/libksvgplugin.la
%{tde_tdelibdir}/libksvgplugin.so
%{tde_tdelibdir}/libksvgrendererlibart.la
%{tde_tdelibdir}/libksvgrendererlibart.so
%{tde_tdelibdir}/svgthumbnail.la
%{tde_tdelibdir}/svgthumbnail.so
%{tde_libdir}/libksvg.so.0
%{tde_libdir}/libksvg.so.0.0.1
%{tde_libdir}/libtext2path.so.0
%{tde_libdir}/libtext2path.so.0.0.0
%{tde_datadir}/apps/ksvg/
%{tde_datadir}/services/ksvglibartcanvas.desktop
%{tde_datadir}/services/ksvgplugin.desktop
%{tde_datadir}/services/svgthumbnail.desktop
%{tde_datadir}/servicetypes/ksvgrenderer.desktop

##########

%package -n trinity-kview
Summary:	Simple image viewer/converter for Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-kview
KView is a simple image viewer and converter application. It supports
a number of plugins, which add an array of basic editing capabilities
as well.

%files -n trinity-kview
%defattr(-,root,root,-)
%{tde_bindir}/kview
%{tde_tdelibdir}/kcm_kviewcanvasconfig.la
%{tde_tdelibdir}/kcm_kviewcanvasconfig.so
%{tde_tdelibdir}/kcm_kviewgeneralconfig.la
%{tde_tdelibdir}/kcm_kviewgeneralconfig.so
%{tde_tdelibdir}/kcm_kviewpluginsconfig.la
%{tde_tdelibdir}/kcm_kviewpluginsconfig.so
%{tde_tdelibdir}/kcm_kviewpresenterconfig.la
%{tde_tdelibdir}/kcm_kviewpresenterconfig.so
%{tde_tdelibdir}/kcm_kviewviewerpluginsconfig.la
%{tde_tdelibdir}/kcm_kviewviewerpluginsconfig.so
%{tde_tdelibdir}/kview.la
%{tde_tdelibdir}/kview.so
%{tde_tdelibdir}/kview_browserplugin.la
%{tde_tdelibdir}/kview_browserplugin.so
%{tde_tdelibdir}/kview_effectsplugin.la
%{tde_tdelibdir}/kview_effectsplugin.so
%{tde_tdelibdir}/kview_presenterplugin.la
%{tde_tdelibdir}/kview_presenterplugin.so
%{tde_tdelibdir}/kview_scannerplugin.la
%{tde_tdelibdir}/kview_scannerplugin.so
%{tde_tdelibdir}/libkviewcanvas.la
%{tde_tdelibdir}/libkviewcanvas.so
%{tde_tdelibdir}/libkviewviewer.la
%{tde_tdelibdir}/libkviewviewer.so
%{tde_libdir}/libtdeinit_kview.so
%{tde_libdir}/libkimageviewer.so.*
%{tde_tdelibdir}/libphotobook.la
%{tde_tdelibdir}/libphotobook.so
%{tde_tdeappdir}/kview.desktop
%{tde_datadir}/apps/kview/
%{tde_datadir}/apps/kviewviewer/
%{tde_datadir}/apps/photobook/
%{tde_datadir}/icons/crystalsvg/*/apps/photobook.png
%{tde_datadir}/icons/hicolor/*/apps/kview.png
%{tde_datadir}/services/tdeconfiguredialog/
%{tde_datadir}/services/kviewcanvas.desktop
%{tde_datadir}/services/kviewviewer.desktop
%{tde_datadir}/services/photobook.desktop
%{tde_datadir}/servicetypes/kimageviewer.desktop
%{tde_datadir}/servicetypes/kimageviewercanvas.desktop
%{tde_tdedocdir}/HTML/en/kview/
%{tde_mandir}/man1/kview.1*

##########

%package -n trinity-kviewshell
Summary:	Generic framework for viewer applications in Trinity
Group:		Productivity/Graphics/Viewers

%description -n trinity-kviewshell
KViewShell is a generic viewing framework that allows the graphical
applications, such as the kview image viewer, to be embedded in other
KDE applications, such as Konqueror.

KViewShell comes with a djvuviewpart plugin included, for viewing
DjVu images.

%files -n trinity-kviewshell
%defattr(-,root,root,-)
%{tde_bindir}/kviewshell
%{tde_libdir}/libdjvu.la
%{tde_libdir}/libdjvu.so
%{tde_tdelibdir}/djvuviewpart.so
%{tde_tdelibdir}/djvuviewpart.la
%{tde_tdelibdir}/emptymultipagepart.la
%{tde_tdelibdir}/emptymultipagepart.so
%{tde_tdelibdir}/kviewerpart.la
%{tde_tdelibdir}/kviewerpart.so
%{tde_libdir}/libtdemultipage.so.*
%{tde_datadir}/apps/djvumultipage.rc
%{tde_datadir}/apps/kviewerpart/
%{tde_datadir}/apps/kviewshell/
%{tde_datadir}/config.kcfg/djvumultipage.kcfg
%{tde_datadir}/config.kcfg/kviewshell.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/kviewshell.png
%{tde_datadir}/services/emptymultipage.desktop
%{tde_datadir}/services/djvumultipage.desktop
%{tde_datadir}/servicetypes/tdemultipage.desktop
%{tde_mandir}/man1/kviewshell.1*

##########

%package -n trinity-libkscan
Summary:	Scanner library for Trinity
Group:		Hardware/Scanner

%description -n trinity-libkscan
KScan is TDE's scanner library. It's used by kooka and by koffice currently.
It provides an easy-to-use library, which allows you to access your scanner
(as long as it's sane compatible).

%files -n trinity-libkscan
%defattr(-,root,root,-)
%{tde_libdir}/libkscan.so.*
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_color.png
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_gray.png
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_halftone.png
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_lineart.png
%{tde_datadir}/services/scanservice.desktop

##########

%package -n trinity-libkscan-devel
Summary:	Development files for the Trinity scanner library
Group:		Development/Libraries/Other
Requires:	trinity-libkscan = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkscan-devel
This package contains development files for Trinity's scanner library.

%files -n trinity-libkscan-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkscan.la
%{tde_libdir}/libkscan.so

##########

%if 0%{?with_pdf}
%package -n trinity-libpoppler-tqt
Summary:	TQt support for Poppler
Group:		Productivity/Graphics/Viewers
Obsoletes:	poppler-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	poppler-tqt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	%{name}-libpoppler-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	%{name}-libpoppler-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libpoppler-tqt
TQt support library for Poppler.
This library is used by the Trinity graphics file plugins for PDF support.

%files -n trinity-libpoppler-tqt
%defattr(-,root,root,-)
%{tde_libdir}/libpoppler-tqt.so.*
%endif

##########

%if 0%{?with_pdf}
%package -n trinity-libpoppler-tqt-devel
Summary:	Development files for TQt support for Poppler
Group:		Development/Libraries/Other
Requires:	trinity-libpoppler-tqt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	poppler-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	poppler-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	%{name}-libpoppler-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	%{name}-libpoppler-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libpoppler-tqt-devel
Development files of TQt support library for Poppler.
This package contains the development files needed to compile applications against poppler-tqt.

%files -n trinity-libpoppler-tqt-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/poppler-link-qt3.h
%{tde_tdeincludedir}/poppler-page-transition.h
%{tde_tdeincludedir}/poppler-qt.h
%{tde_libdir}/libpoppler-tqt.la
%{tde_libdir}/libpoppler-tqt.so
%{tde_libdir}/pkgconfig/poppler-tqt.pc
%endif

##########

%package devel
Summary:	Development files for tdegraphics
Group:		Development/Libraries/Other

Obsoletes:	trinity-kdegraphics-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdegraphics-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libkscan-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?with_pdf}
Requires: trinity-libpoppler-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description devel
This package contains the development files needed to compile 
applications against tdegraphics libraries.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/dom/
%{tde_tdeincludedir}/kfaximage.h
%{tde_tdeincludedir}/tdemultipageInterface.h
%{tde_tdeincludedir}/ksvg/
%{tde_tdeincludedir}/kviewshell/
%{tde_tdeincludedir}/libtext2path-0.1/
%{tde_libdir}/libtdeinit_kview.la
%if 0%{?build_kmrml}
%{tde_libdir}/libtdeinit_mrmlsearch.la
%endif
%{tde_libdir}/libkghostviewlib.la
%{tde_libdir}/libkghostviewlib.so
%{tde_libdir}/libkimageviewer.la
%{tde_libdir}/libkimageviewer.so
%{tde_libdir}/libtdemultipage.la
%{tde_libdir}/libtdemultipage.so
%{tde_libdir}/libkpovmodeler.la
%{tde_libdir}/libkpovmodeler.so
%{tde_libdir}/libksvg.la
%{tde_libdir}/libksvg.so
%{tde_libdir}/libtext2path.la
%{tde_libdir}/libtext2path.so
# kfaxview
%{tde_libdir}/libkfaximage.so
%{tde_libdir}/libkfaximage.la
# cmake
%{tde_datadir}/cmake/*

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

%if 0%{?build_kamera} == 0
%__rm -rf doc/kamera/
%endif

# Fix applications icons
%__sed -i "kooka/kooka.desktop" -e "s|^Icon=.*|Icon=kooka|"

# Fix FTBFS in RHEL 5
%if 0%{?rhel} && 0%{?rhel} <= 5
%__sed -i "kpdf/xpdf/aconf.h" \
       -e "s|#define HAVE_MKSTEMPS 1|#define HAVE_MKSTEMPS 0|"
%__sed -i "tdefile-plugins/dependencies/poppler-tqt/CMakeLists.txt" \
       -e "/link_directories/ s|$|\n  \${POPPLER_LIBRARY_DIRS}|" \
       -e "/{POPPLER_INCLUDE_DIRS/ s|$|\n  \${POPPLER_INCLUDE_DIRS}/..|"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes FTBFS [Bug #1285]
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
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  \
  %{?with_t1lib:-DWITH_T1LIB=ON} \
  %{?with_paper:-DWITH_LIBPAPER=ON} \
  -DWITH_TIFF=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_PDF=%{?with_pdf:ON}%{?!with_pdf:OFF} \
  -DBUILD_ALL=ON \
  -DBUILD_KUICKSHOW=OFF \
  %{!?build_kmrml:-DBUILD_KMRML=OFF} \
  %{!?build_kamera:-DBUILD_KAMERA=OFF} \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Adds missing icons in 'hicolor' theme
%__mkdir_p "%{?buildroot}%{tde_datadir}/icons/hicolor/"{16x16,32x32,48x48,64x64}"/apps/"
pushd "%{?buildroot}%{tde_datadir}/icons"
for i in {16,32,48,64}; do %__cp $BUILD_ROOT%{tde_datadir}/icons/crystalsvg/"$i"x"$i"/devices/scanner.png %{buildroot}%{tde_datadir}/icons/hicolor/"$i"x"$i"/apps/kooka.png; done
popd

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kpovmodeler.desktop    Graphics 3DGraphics
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kolourpaint.desktop    Graphics RasterGraphics
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/tdeiconedit.desktop    Graphics RasterGraphics
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kview.desktop          Graphics Viewer
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kooka.desktop          Graphics Scanning
%suse_update_desktop_file -r %{?buildroot}%{tde_tdeappdir}/kruler.desktop         Utility DesktopUtility
%suse_update_desktop_file -r %{?buildroot}%{tde_tdeappdir}/ksnapshot.desktop      Utility DesktopUtility
%suse_update_desktop_file -r %{?buildroot}%{tde_tdeappdir}/kcolorchooser.desktop  Utility DesktopUtility
%suse_update_desktop_file -r %{?buildroot}%{tde_tdeappdir}/kcoloredit.desktop     Utility DesktopUtility
%suse_update_desktop_file -u %{?buildroot}%{tde_tdeappdir}/kfax.desktop           Office Viewer
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kghostview.desktop     Office Viewer
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kdvi.desktop           Office Viewer
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kpdf.desktop           Office Viewer
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kfaxview.desktop       Office Viewer
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kamera.desktop
%endif

# Links duplicate files
%fdupes "%{?buildroot}"


%clean
%__rm -rf %{buildroot}


%changelog
