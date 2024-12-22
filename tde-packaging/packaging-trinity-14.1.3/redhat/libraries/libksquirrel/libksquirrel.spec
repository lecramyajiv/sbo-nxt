%if 0%{?fedora} >= 23 || 0%{?rhel} >= 8
%define _hardened_ldflags %nil
%endif

#
# spec file for package libksquirrel (version R14)
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

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg libksquirrel
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
Version:	0.8.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Trinity image viewer
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:	%{name}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# CMAKE
BuildRequires: cmake libtool
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 5 || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif

# TRANSFIG support
BuildRequires:	transfig

# GHOSTSCRIPT support
%define with_ghostscript 1
BuildRequires:	ghostscript

# GETTEXT support
BuildRequires:	gettext
BuildRequires:	gettext-devel

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

# MNG support
%if 0%{?mdkver}
BuildRequires: %{_lib}mng-devel
%else
BuildRequires: libmng-devel
%endif

# DJVU support
%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_djvu 1
BuildRequires:	djvulibre
%endif

# XMEDCON support
#if 0%{?fedora}
#define with_xmedcon 1
#BuildRequires:	xmedcon
#BuildRequires:	xmedcon-devel
#endif

# RSVG support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_svg 1
%if 0%{?rhel} == 5
BuildRequires:	librsvg2-devel
%endif
%if 0%{?fedora} || 0%{?rhel} 
BuildRequires:	librsvg2
%endif
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildRequires:	librsvg2-tools
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mdkver}
BuildRequires:	%{_lib}rsvg2-devel
%endif
BuildRequires:	librsvg
%endif
%if 0%{?suse_version}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:	rsvg-convert
%else
BuildRequires:	rsvg-view
%endif
BuildRequires:	librsvg-devel
%endif
%endif

# JASPER support
%if 0%{?rhel} >=4 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_jasper 1
%if 0%{?suse_version}
BuildRequires:	libjasper-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}jasper-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	jasper-devel
%endif
%endif

# FREETYPE support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_freetype 1
%if 0%{?suse_version} == 1140
BuildRequires: freetype2-devel
%else
BuildRequires: freetype-devel
%endif
%endif

# WMF support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
BuildRequires:	%{_lib}wmf-devel
%else
BuildRequires:	libwmf-devel
%endif

# XML2 support
BuildRequires:	libxml2-devel

# NETPBM support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
BuildRequires:	netpbm
%else
BuildRequires:	netpbm-progs
%endif


%description
This package contains the runtime libraries for KSquirrel.

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE README
%dir %{tde_libdir}/ksquirrel-libs
%{tde_libdir}/ksquirrel-libs/libkls_avs.so.0
%{tde_libdir}/ksquirrel-libs/libkls_avs.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_bmp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_bmp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_camera.so.0
%{tde_libdir}/ksquirrel-libs/libkls_camera.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_cut.so.0
%{tde_libdir}/ksquirrel-libs/libkls_cut.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_dds.so.0
%{tde_libdir}/ksquirrel-libs/libkls_dds.so.0.8.0
%if 0%{?with_xmedcon}
%{tde_libdir}/ksquirrel-libs/libkls_dicom.so.0
%{tde_libdir}/ksquirrel-libs/libkls_dicom.so.0.8.0
%endif
%if 0%{?with_djvu}
%{tde_libdir}/ksquirrel-libs/libkls_djvu.so.0
%{tde_libdir}/ksquirrel-libs/libkls_djvu.so.0.8.0
%endif
%if 0%{?with_ghostscript}
%{tde_libdir}/ksquirrel-libs/libkls_eps.so.0
%{tde_libdir}/ksquirrel-libs/libkls_eps.so.0.8.0
%endif
%{tde_libdir}/ksquirrel-libs/libkls_fig.so.0
%{tde_libdir}/ksquirrel-libs/libkls_fig.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_fli.so.0
%{tde_libdir}/ksquirrel-libs/libkls_fli.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_gif.so.0
%{tde_libdir}/ksquirrel-libs/libkls_gif.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_hdr.so.0
%{tde_libdir}/ksquirrel-libs/libkls_hdr.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_ico.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ico.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_iff.so.0
%{tde_libdir}/ksquirrel-libs/libkls_iff.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_jbig.so.0
%{tde_libdir}/ksquirrel-libs/libkls_jbig.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.so.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.so.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_koala.so.0
%{tde_libdir}/ksquirrel-libs/libkls_koala.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_leaf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_leaf.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_lif.so.0
%{tde_libdir}/ksquirrel-libs/libkls_lif.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mac.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mac.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mdl.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mdl.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mng.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mng.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_msp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_msp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mtv.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mtv.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_neo.so.0
%{tde_libdir}/ksquirrel-libs/libkls_neo.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_openexr.so.0
%{tde_libdir}/ksquirrel-libs/libkls_openexr.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pcx.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pcx.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pi1.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pi1.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pi3.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pi3.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pix.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pix.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_png.so.0
%{tde_libdir}/ksquirrel-libs/libkls_png.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pnm.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pnm.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_psd.so.0
%{tde_libdir}/ksquirrel-libs/libkls_psd.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_psp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_psp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pxr.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pxr.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_ras.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ras.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.so.0
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_sct.so.0
%{tde_libdir}/ksquirrel-libs/libkls_sct.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_sgi.so.0
%{tde_libdir}/ksquirrel-libs/libkls_sgi.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_sun.so.0
%{tde_libdir}/ksquirrel-libs/libkls_sun.so.0.8.0
%if 0%{?with_svg}
%{tde_libdir}/ksquirrel-libs/libkls_svg.so.0
%{tde_libdir}/ksquirrel-libs/libkls_svg.so.0.8.0
%endif
%{tde_libdir}/ksquirrel-libs/libkls_tga.so.0
%{tde_libdir}/ksquirrel-libs/libkls_tga.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_tiff.so.0
%{tde_libdir}/ksquirrel-libs/libkls_tiff.so.0.8.0
%if 0%{?with_freetype}
%{tde_libdir}/ksquirrel-libs/libkls_ttf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ttf.so.0.8.0
%endif
%{tde_libdir}/ksquirrel-libs/libkls_utah.so.0
%{tde_libdir}/ksquirrel-libs/libkls_utah.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_wal.so.0
%{tde_libdir}/ksquirrel-libs/libkls_wal.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_wmf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_wmf.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xbm.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xbm.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xcf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xcf.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xcur.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xcur.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xim.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xim.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xpm.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xpm.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xwd.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xwd.so.0.8.0
%{tde_libdir}/libksquirrel-libs-png.so.0
%{tde_libdir}/libksquirrel-libs-png.so.0.8.0
%{tde_libdir}/libksquirrel-libs.so.0
%{tde_libdir}/libksquirrel-libs.so.0.8.0
%dir %{tde_datadir}/ksquirrel-libs
%{tde_datadir}/ksquirrel-libs/libkls_camera.so.ui
%if 0%{?with_djvu}
%{tde_datadir}/ksquirrel-libs/libkls_djvu.so.ui
%endif
%if 0%{?with_svg}
%{tde_datadir}/ksquirrel-libs/libkls_svg.so.ui
%endif
%{tde_datadir}/ksquirrel-libs/libkls_tiff.so.ui
%{tde_datadir}/ksquirrel-libs/libkls_xcf.so.ui
%{tde_datadir}/ksquirrel-libs/rgbmap
%{tde_mandir}/man1/ksquirrel-libs-camera2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-dcraw.1
%{tde_mandir}/man1/ksquirrel-libs-dicom2png.1
%{tde_mandir}/man1/ksquirrel-libs-fig2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-iff2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-leaf2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-ljpeg2ppm-s.1
%{tde_mandir}/man1/ksquirrel-libs-ljpeg2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-mac2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-neo2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-pi12ppm.1
%{tde_mandir}/man1/ksquirrel-libs-pi32ppm.1
%{tde_mandir}/man1/ksquirrel-libs-svg2png.1
%{tde_mandir}/man1/ksquirrel-libs-ttf2pnm.1
%{tde_mandir}/man1/ksquirrel-libs-utah2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-xcf2pnm.1
%{tde_mandir}/man1/ksquirrel-libs-xim2ppm.1

##########

%package devel
Group:		Development/Libraries/Other
Summary:	Trinity image viewer
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development libraries for KSquirrel.

%files devel
%defattr(-,root,root,-)
%dir %{tde_includedir}/ksquirrel-libs
%{tde_includedir}/ksquirrel-libs/error.h
%{tde_includedir}/ksquirrel-libs/fileio.h
%{tde_includedir}/ksquirrel-libs/fmt_codec_base.h
%{tde_includedir}/ksquirrel-libs/fmt_defs.h
%{tde_includedir}/ksquirrel-libs/fmt_types.h
%{tde_includedir}/ksquirrel-libs/fmt_utils.h
%{tde_includedir}/ksquirrel-libs/ksquirrel_libs_export.h
%{tde_includedir}/ksquirrel-libs/settings.h
%{tde_libdir}/ksquirrel-libs/libkls_avs.la
%{tde_libdir}/ksquirrel-libs/libkls_avs.so
%{tde_libdir}/ksquirrel-libs/libkls_bmp.la
%{tde_libdir}/ksquirrel-libs/libkls_bmp.so
%{tde_libdir}/ksquirrel-libs/libkls_camera.la
%{tde_libdir}/ksquirrel-libs/libkls_camera.so
%{tde_libdir}/ksquirrel-libs/libkls_cut.la
%{tde_libdir}/ksquirrel-libs/libkls_cut.so
%{tde_libdir}/ksquirrel-libs/libkls_dds.la
%{tde_libdir}/ksquirrel-libs/libkls_dds.so
%if 0%{?with_xmedcon}
%{tde_libdir}/ksquirrel-libs/libkls_dicom.la
%{tde_libdir}/ksquirrel-libs/libkls_dicom.so
%endif
%if 0%{?with_djvu}
%{tde_libdir}/ksquirrel-libs/libkls_djvu.la
%{tde_libdir}/ksquirrel-libs/libkls_djvu.so
%endif
%if 0%{?with_ghostscript}
%{tde_libdir}/ksquirrel-libs/libkls_eps.la
%{tde_libdir}/ksquirrel-libs/libkls_eps.so
%endif
%{tde_libdir}/ksquirrel-libs/libkls_fig.la
%{tde_libdir}/ksquirrel-libs/libkls_fig.so
%{tde_libdir}/ksquirrel-libs/libkls_fli.la
%{tde_libdir}/ksquirrel-libs/libkls_fli.so
%{tde_libdir}/ksquirrel-libs/libkls_gif.la
%{tde_libdir}/ksquirrel-libs/libkls_gif.so
%{tde_libdir}/ksquirrel-libs/libkls_hdr.la
%{tde_libdir}/ksquirrel-libs/libkls_hdr.so
%{tde_libdir}/ksquirrel-libs/libkls_ico.la
%{tde_libdir}/ksquirrel-libs/libkls_ico.so
%{tde_libdir}/ksquirrel-libs/libkls_iff.la
%{tde_libdir}/ksquirrel-libs/libkls_iff.so
%{tde_libdir}/ksquirrel-libs/libkls_jbig.la
%{tde_libdir}/ksquirrel-libs/libkls_jbig.so
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.la
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.so
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.la
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.so
%{tde_libdir}/ksquirrel-libs/libkls_koala.la
%{tde_libdir}/ksquirrel-libs/libkls_koala.so
%{tde_libdir}/ksquirrel-libs/libkls_leaf.la
%{tde_libdir}/ksquirrel-libs/libkls_leaf.so
%{tde_libdir}/ksquirrel-libs/libkls_lif.la
%{tde_libdir}/ksquirrel-libs/libkls_lif.so
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.la
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.so
%{tde_libdir}/ksquirrel-libs/libkls_mac.la
%{tde_libdir}/ksquirrel-libs/libkls_mac.so
%{tde_libdir}/ksquirrel-libs/libkls_mdl.la
%{tde_libdir}/ksquirrel-libs/libkls_mdl.so
%{tde_libdir}/ksquirrel-libs/libkls_mng.la
%{tde_libdir}/ksquirrel-libs/libkls_mng.so
%{tde_libdir}/ksquirrel-libs/libkls_msp.la
%{tde_libdir}/ksquirrel-libs/libkls_msp.so
%{tde_libdir}/ksquirrel-libs/libkls_mtv.la
%{tde_libdir}/ksquirrel-libs/libkls_mtv.so
%{tde_libdir}/ksquirrel-libs/libkls_neo.la
%{tde_libdir}/ksquirrel-libs/libkls_neo.so
%{tde_libdir}/ksquirrel-libs/libkls_openexr.la
%{tde_libdir}/ksquirrel-libs/libkls_openexr.so
%{tde_libdir}/ksquirrel-libs/libkls_pcx.la
%{tde_libdir}/ksquirrel-libs/libkls_pcx.so
%{tde_libdir}/ksquirrel-libs/libkls_pi1.la
%{tde_libdir}/ksquirrel-libs/libkls_pi1.so
%{tde_libdir}/ksquirrel-libs/libkls_pi3.la
%{tde_libdir}/ksquirrel-libs/libkls_pi3.so
%{tde_libdir}/ksquirrel-libs/libkls_pix.la
%{tde_libdir}/ksquirrel-libs/libkls_pix.so
%{tde_libdir}/ksquirrel-libs/libkls_png.la
%{tde_libdir}/ksquirrel-libs/libkls_png.so
%{tde_libdir}/ksquirrel-libs/libkls_pnm.la
%{tde_libdir}/ksquirrel-libs/libkls_pnm.so
%{tde_libdir}/ksquirrel-libs/libkls_psd.la
%{tde_libdir}/ksquirrel-libs/libkls_psd.so
%{tde_libdir}/ksquirrel-libs/libkls_psp.la
%{tde_libdir}/ksquirrel-libs/libkls_psp.so
%{tde_libdir}/ksquirrel-libs/libkls_pxr.la
%{tde_libdir}/ksquirrel-libs/libkls_pxr.so
%{tde_libdir}/ksquirrel-libs/libkls_ras.la
%{tde_libdir}/ksquirrel-libs/libkls_ras.so
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.la
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.so
%{tde_libdir}/ksquirrel-libs/libkls_sct.la
%{tde_libdir}/ksquirrel-libs/libkls_sct.so
%{tde_libdir}/ksquirrel-libs/libkls_sgi.la
%{tde_libdir}/ksquirrel-libs/libkls_sgi.so
%{tde_libdir}/ksquirrel-libs/libkls_sun.la
%{tde_libdir}/ksquirrel-libs/libkls_sun.so
%if 0%{?with_svg}
%{tde_libdir}/ksquirrel-libs/libkls_svg.la
%{tde_libdir}/ksquirrel-libs/libkls_svg.so
%endif
%{tde_libdir}/ksquirrel-libs/libkls_tga.la
%{tde_libdir}/ksquirrel-libs/libkls_tga.so
%{tde_libdir}/ksquirrel-libs/libkls_tiff.la
%{tde_libdir}/ksquirrel-libs/libkls_tiff.so
%if 0%{?with_freetype}
%{tde_libdir}/ksquirrel-libs/libkls_ttf.la
%{tde_libdir}/ksquirrel-libs/libkls_ttf.so
%endif
%{tde_libdir}/ksquirrel-libs/libkls_utah.la
%{tde_libdir}/ksquirrel-libs/libkls_utah.so
%{tde_libdir}/ksquirrel-libs/libkls_wal.la
%{tde_libdir}/ksquirrel-libs/libkls_wal.so
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.la
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.so
%{tde_libdir}/ksquirrel-libs/libkls_wmf.la
%{tde_libdir}/ksquirrel-libs/libkls_wmf.so
%{tde_libdir}/ksquirrel-libs/libkls_xbm.la
%{tde_libdir}/ksquirrel-libs/libkls_xbm.so
%{tde_libdir}/ksquirrel-libs/libkls_xcf.la
%{tde_libdir}/ksquirrel-libs/libkls_xcf.so
%{tde_libdir}/ksquirrel-libs/libkls_xcur.la
%{tde_libdir}/ksquirrel-libs/libkls_xcur.so
%{tde_libdir}/ksquirrel-libs/libkls_xim.la
%{tde_libdir}/ksquirrel-libs/libkls_xim.so
%{tde_libdir}/ksquirrel-libs/libkls_xpm.la
%{tde_libdir}/ksquirrel-libs/libkls_xpm.so
%{tde_libdir}/ksquirrel-libs/libkls_xwd.la
%{tde_libdir}/ksquirrel-libs/libkls_xwd.so
%{tde_libdir}/libksquirrel-libs-png.la
%{tde_libdir}/libksquirrel-libs-png.so
%{tde_libdir}/libksquirrel-libs.la
%{tde_libdir}/libksquirrel-libs.so
%{tde_libdir}/pkgconfig/ksquirrellibs.pc
%{tde_docdir}/ksquirrel-libs/

##########

%package tools
Summary:	Trinity image viewer
Group:		System/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description tools
This package contains the tools for KSquirrel.

%files tools
%defattr(-,root,root,-)
%{tde_bindir}/ksquirrel-libs-camera2ppm
%{tde_bindir}/ksquirrel-libs-dcraw
%if 0%{?with_xmedcon}
%{tde_bindir}/ksquirrel-libs-dicom2png
%endif
%{tde_bindir}/ksquirrel-libs-fig2ppm
%{tde_bindir}/ksquirrel-libs-iff2ppm
%{tde_bindir}/ksquirrel-libs-leaf2ppm
%{tde_bindir}/ksquirrel-libs-ljpeg2ppm
%{tde_bindir}/ksquirrel-libs-ljpeg2ppm-s
%{tde_bindir}/ksquirrel-libs-mac2ppm
%{tde_bindir}/ksquirrel-libs-neo2ppm
%{tde_bindir}/ksquirrel-libs-pi12ppm
%{tde_bindir}/ksquirrel-libs-pi32ppm
%if 0%{?with_svg}
%{tde_bindir}/ksquirrel-libs-svg2png
%endif
%if 0%{?with_freetype}
%{tde_bindir}/ksquirrel-libs-ttf2pnm
%endif
%{tde_bindir}/ksquirrel-libs-utah2ppm
%{tde_bindir}/ksquirrel-libs-xcf2pnm
%{tde_bindir}/ksquirrel-libs-xim2ppm

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# FIXME: under PCLinuxOS, headers are under 'freetype2' not 'freetype'
if [ -r /usr/include/freetype2/ftbitmap.h ]; then
  %__sed -i "configure.ac" -e "s|freetype/ftbitmap.h|freetype2/ftbitmap.h|"
  %__sed -i "kernel/kls_ttf/ttf2pnm.cpp" -e "s|freetype/config/|freetype2/config/|"
fi


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
  -DINCLUDE_INSTALL_DIR="%{tde_includedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL=ON \
  -DBUILD_DICOM=OFF \
  -DBUILD_PICT=OFF \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make -C build install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%changelog
