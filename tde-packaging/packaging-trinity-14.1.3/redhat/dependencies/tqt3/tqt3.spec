#
# spec file for package tqt3 (version R14)
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
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libtqt3 %{_lib}tqt3
%else
%define libtqt3 libtqt3
%endif


Name:		trinity-tqt3
Version:	3.5.0
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TQt GUI Library, Version 3
Group:		System/GUI/Other
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{tde_version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:	build-examples.sh
Source2:	trinity-tqt3-rpmlintrc

BuildRequires: glibc-devel
%if "%{?c_compiler}" != "clang"
BuildRequires: gcc-c++
%endif
BuildRequires: make

BuildRequires: desktop-file-utils
BuildRequires: perl
BuildRequires: sed
BuildRequires: findutils
BuildRequires: tar

# ZLIB support
BuildRequires: zlib-devel

# JPEG support
%if 0%{?mdkver} || 0%{?mgaversion}
%define libjpeg %{_lib}jpeg
%else
%define libjpeg libjpeg
%endif
%{?libjpeg:BuildRequires: %{libjpeg}-devel}

# MNG support
%if 0%{?mdkver} || 0%{?mgaversion}
%define libmng %{_lib}mng
%else
%define libmng libmng
%endif
%{?libmng:BuildRequires: %{libmng}-devel}

# PNG support
%if 0%{?mdkver} || 0%{?mgaversion}
%if 0%{?pclinuxos}
%define libpng %{_lib}png1.6
%else
%define libpng %{_lib}png
%endif
%else
%define libpng libpng
%endif
%{?libpng:BuildRequires: %{libpng}-devel}

# GIF support
BuildRequires: giflib-devel

# FREETYPE support
BuildRequires: freetype-devel

# FONTCONFIG support
BuildRequires: fontconfig-devel

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

# CUPS support
BuildRequires: cups-devel

# GLIB2 support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%define with_glibmainloop 1
%define glib2_devel glib2-devel
%endif
%{?glib2_devel:BuildRequires: %{glib2_devel}}

# UUID support
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 6
%define uuid_devel libuuid-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%define uuid_devel %{_lib}uuid-devel
%endif
%if 0%{?rhel} == 5
%define uuid_devel e2fsprogs-devel
%endif
%{?uuid_devel:BuildRequires: %{uuid_devel}}

# LIBAUDIO support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_nas 1
%if 0%{?mdkver} >= 5000000
%define libaudio_devel %{_lib}audio-devel nas-devel
%else
%define libaudio_devel nas-devel
%endif
%endif
%{?libaudio_devel:BuildRequires: %{libaudio_devel}}

# Xrender support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define xrender_devel libXrender-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define xrender_devel %{_lib}xrender-devel
%endif
%{?xrender_devel:BuildRequires: %{xrender_devel}}

# Xrandr support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define xrandr_devel libXrandr-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define xrandr_devel %{_lib}xrandr-devel
%endif
%if 0%{?pclinuxos}
%define xrandr_devel %{_lib}xrandr2-devel
%endif
%{?xrandr_devel:BuildRequires: %{xrandr_devel}}

# Xcursor support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define xcursor_devel libXcursor-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define xcursor_devel %{_lib}xcursor-devel
%endif
%{?xcursor_devel:BuildRequires: %{xcursor_devel}}

# Xinerama support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define xinerama_devel libXinerama-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define xinerama_devel %{_lib}xinerama-devel
%endif
%{?xinerama_devel:BuildRequires: %{xinerama_devel}}

# Xft support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define xft_devel libXft-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define xft_devel %{_lib}xft-devel
%endif
%{?xft_devel:BuildRequires: %{xft_devel}}

# XEXT support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define xext_devel libXext-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define xext_devel %{_lib}xext-devel
%endif
%{?xext_devel:BuildRequires: %{xext_devel}}

# X11 support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define x11_devel libX11-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define x11_devel %{_lib}x11-devel
%endif
%{?x11_devel:BuildRequires: %{x11_devel}}

# SM support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define sm_devel libSM-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define sm_devel %{_lib}sm-devel
%endif
%{?sm_devel:BuildRequires: %{sm_devel}}

# ICE support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%define ice_devel libICE-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
%define ice_devel %{_lib}ice-devel
%endif
%{?ice_devel:BuildRequires: %{ice_devel}}

# XT support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXt-devel
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

# XI support
%if 0%{?rhel} == 4
%define xi_devel xorg-x11-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%define xi_devel %{_lib}xi-devel
%endif
%if 0%{?suse_version} >= 1220 || 0%{?rhel} >= 5 || 0%{?fedora}
%define xi_devel libXi-devel
%endif
%if 0%{?suse_version} == 1140
%define xi_devel libXi6-devel
%endif
%{?xi_devel:BuildRequires: %{xi_devel}}

# Xorg support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: xorg-x11-proto-devel
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

# MYSQL support
BuildRequires: mysql-devel

# unixODBC support
BuildRequires: unixODBC-devel

# SQLITE3 support
%if 0%{?mgaversion}
BuildRequires: sqlite3-devel
%else
BuildRequires: sqlite-devel
%endif

# POSTGRESQL support
BuildRequires:	postgresql
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires: postgresql-server-devel
%else
BuildRequires: postgresql-devel
%endif

# Firebird support
%if 0%{?mdkversion} || 0%{?mgaversion}
%define with_ibase 1
BuildRequires:	firebird-devel
%endif

# FBCLIENT support
%if 0%{?mdkver} || 0%{?mgaversion} >= 6
BuildRequires:	%{_lib}fbclient-devel
%endif

# NIS support
%define with_nis 1

# RPC support
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 28
BuildRequires:		libnsl2-devel
BuildRequires:		libtirpc-devel
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:		libnsl-devel
BuildRequires:		libtirpc-devel
%endif
%if 0%{?mdkver} || 0%{?mgaversion}
BuildRequires:		%{_lib}nsl-devel
BuildRequires:		%{_lib}tirpc-devel
%endif

# x86_64 specific stuff
%if "%{_lib}" != "lib"
%if 0%{?mdkversion} || ( 0%{?mgaversion} && 0%{?mgaversion} <= 2)
BuildRequires: linux32
%else
BuildRequires: util-linux
%endif
%endif

%description
This is the Trolltech TQt library, version 3. It's necessary for
applications that link against the libtqt-mt.so.3, e.g. all Trinity
applications.

##########

%package -n %{libtqt3}-mt
Summary:	TQt GUI Library (Threaded runtime version), Version 3
Group:		System/GUI/Other
Provides:	libtqt3-mt = %{version}-%{release}
Provides:	trinity-tqt3 = %{version}-%{release}

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: coreutils
Requires: fontconfig >= 2.0

%description -n %{libtqt3}-mt
This is the Trolltech TQt library, version 3. It's necessary for
applications that link against the libtqt-mt.so.3, e.g. all Trinity
applications.

%post -n %{libtqt3}-mt
/sbin/ldconfig || :

%postun -n %{libtqt3}-mt
/sbin/ldconfig || :

%files -n %{libtqt3}-mt
%defattr(-,root,root,-)
%doc FAQ LICENSE* README* changes*
%dir %{_datadir}/tqt3/
%dir %{_datadir}/tqt3/doc/
%dir %{_datadir}/tqt3/doc/html/
%dir %{_datadir}/tqt3/tools/
%dir %{_libdir}/tqt3/
%dir %{_libdir}/tqt3/plugins/
%dir %{_libdir}/tqt3/plugins/designer/
%dir %{_libdir}/tqt3/plugins/imageformats/
%dir %{_libdir}/tqt3/plugins/inputmethods/
%dir %{_libdir}/tqt3/plugins/sqldrivers/
%dir %{_sysconfdir}/tqt3
%{_libdir}/libtqt-mt.so.3
%{_libdir}/libtqt-mt.so.3.5
%{_libdir}/libtqt-mt.so.3.5.0
%{_libdir}/libtqui.so.1
%{_libdir}/libtqui.so.1.0
%{_libdir}/libtqui.so.1.0.0
%{_libdir}/tqt3/plugins/imageformats/libqmng.so
%{_libdir}/tqt3/plugins/inputmethods/libqimsw-multi.so
%{_libdir}/tqt3/plugins/inputmethods/libqimsw-none.so
%{_libdir}/tqt3/plugins/inputmethods/libqsimple.so
%{_libdir}/tqt3/plugins/inputmethods/libqxim.so

###########

%package -n %{libtqt3}-mt-devel
Summary:	TQt development files (Threaded)
Group:		Development/Libraries/X11
Provides:	trinity-tqt3-devel = %{version}-%{release}
Provides:	libtqt3-mt-devel = %{version}-%{release}
Requires:	%{libtqt3}-mt = %{version}-%{release}

Requires: glibc-devel
Requires: fontconfig-devel
Requires: freetype-devel
Requires: %{libjpeg}-devel
Requires: %{libpng}-devel
Requires: zlib-devel

%{?glib2_devel:Requires: %{glib2_devel}}
%{?uuid_devel:Requires: %{uuid_devel}}
%{?xi_devel:Requires: %{xi_devel}}
%{?xrender_devel:Requires: %{xrender_devel}}
%{?xrandr_devel:Requires: %{xrandr_devel}}
%{?xcursor_devel:Requires: %{xcursor_devel}}
%{?xinerama_devel:Requires: %{xinerama_devel}}
%{?xft_devel:Requires: %{xft_devel}}
%{?xext_devel:Requires: %{xext_devel}}
%{?x11_devel:Requires: %{x11_devel}}
%{?sm_devel:Requires: %{sm_devel}}
%{?ice_devel:Requires: %{ice_devel}}
%{?libaudio_devel:Requires: %{libaudio_devel}}

%description -n %{libtqt3}-mt-devel
TQt is a C++ class library optimized for graphical user interface
development. This package contains the libtqt-mt.so symlink, necessary
for building threaded TQt applications as well as the libtqui.so symlink
and the necessary header files for libtqui.so. (See README.Debian and
the TQt Documentation for instructions on libtqui.so)

WARNING: If you plan to build some older TQt3 applications, you will
most probably have to install the tqt3-compat-headers package. It
contains all the headers which are not part of the official TQt3 API
anymore but which are still used by some programs. So if you encounter
problems with missing header files, please install this package first
before you send a bugreport.

%post -n %{libtqt3}-mt-devel
/sbin/ldconfig || :

%postun -n %{libtqt3}-mt-devel
/sbin/ldconfig || :

%files -n %{libtqt3}-mt-devel
%defattr(-,root,root,-)
%{_libdir}/libtqt-mt.la
%{_libdir}/libtqt-mt.so
%{_libdir}/libtqt-mt.prl
%{_libdir}/libtqui.so
%{_libdir}/libtqui.prl
%{_libdir}/pkgconfig/tqt-mt.pc
%dir %{_includedir}/tqt3
%{_includedir}/tqt3/ntqgl.h
%{_includedir}/tqt3/ntqglcolormap.h
%{_includedir}/tqt3/ntqwidgetfactory.h
%{_includedir}/tqt3/actioninterface.h
%{_includedir}/tqt3/arghintwidget.h
%{_includedir}/tqt3/browser.h
%{_includedir}/tqt3/cindent.h
%{_includedir}/tqt3/classbrowserinterface.h
%{_includedir}/tqt3/completion.h
%{_includedir}/tqt3/conf.h
%{_includedir}/tqt3/designerinterface.h
%{_includedir}/tqt3/editor.h
%{_includedir}/tqt3/editorinterface.h
%{_includedir}/tqt3/filterinterface.h
%{_includedir}/tqt3/interpreterinterface.h
%{_includedir}/tqt3/languageinterface.h
%{_includedir}/tqt3/markerwidget.h
%{_includedir}/tqt3/ntqabstractlayout.h
%{_includedir}/tqt3/ntqaccel.h
%{_includedir}/tqt3/ntqaccessible.h
%{_includedir}/tqt3/ntqaction.h
%{_includedir}/tqt3/ntqapplication.h
%{_includedir}/tqt3/ntqasciicache.h
%{_includedir}/tqt3/ntqasciidict.h
%{_includedir}/tqt3/ntqasyncimageio.h
%{_includedir}/tqt3/ntqasyncio.h
%{_includedir}/tqt3/ntqbig5codec.h
%{_includedir}/tqt3/ntqbitarray.h
%{_includedir}/tqt3/ntqbitmap.h
%{_includedir}/tqt3/ntqbrush.h
%{_includedir}/tqt3/ntqbuffer.h
%{_includedir}/tqt3/ntqbutton.h
%{_includedir}/tqt3/ntqbuttongroup.h
%{_includedir}/tqt3/ntqcache.h
%{_includedir}/tqt3/ntqcanvas.h
%{_includedir}/tqt3/ntqcdestyle.h
%{_includedir}/tqt3/ntqcheckbox.h
%{_includedir}/tqt3/ntqcleanuphandler.h
%{_includedir}/tqt3/ntqclipboard.h
%{_includedir}/tqt3/ntqcolor.h
%{_includedir}/tqt3/ntqcolordialog.h
%{_includedir}/tqt3/ntqcombobox.h
%{_includedir}/tqt3/ntqcommonstyle.h
%{_includedir}/tqt3/ntqcompactstyle.h
%{_includedir}/tqt3/ntqconfig.h
%{_includedir}/tqt3/ntqconnection.h
%{_includedir}/tqt3/ntqcstring.h
%{_includedir}/tqt3/ntqcursor.h
%{_includedir}/tqt3/ntqdatabrowser.h
%{_includedir}/tqt3/ntqdatastream.h
%{_includedir}/tqt3/ntqdatatable.h
%{_includedir}/tqt3/ntqdataview.h
%{_includedir}/tqt3/ntqdatetime.h
%{_includedir}/tqt3/ntqdatetimeedit.h
%{_includedir}/tqt3/ntqdeepcopy.h
%{_includedir}/tqt3/ntqdesktopwidget.h
%{_includedir}/tqt3/ntqdial.h
%{_includedir}/tqt3/ntqdialog.h
%{_includedir}/tqt3/ntqdict.h
%{_includedir}/tqt3/ntqdir.h
%{_includedir}/tqt3/ntqdns.h
%{_includedir}/tqt3/ntqdockarea.h
%{_includedir}/tqt3/ntqdockwindow.h
%{_includedir}/tqt3/ntqdom.h
%{_includedir}/tqt3/ntqdragobject.h
%{_includedir}/tqt3/ntqdrawutil.h
%{_includedir}/tqt3/ntqdropsite.h
%{_includedir}/tqt3/ntqeditorfactory.h
%{_includedir}/tqt3/ntqerrormessage.h
%{_includedir}/tqt3/ntqeucjpcodec.h
%{_includedir}/tqt3/ntqeuckrcodec.h
%{_includedir}/tqt3/ntqevent.h
%{_includedir}/tqt3/ntqeventloop.h
%{_includedir}/tqt3/ntqfeatures.h
%{_includedir}/tqt3/ntqfile.h
%{_includedir}/tqt3/ntqfiledialog.h
%{_includedir}/tqt3/ntqfileinfo.h
%{_includedir}/tqt3/ntqfocusdata.h
%{_includedir}/tqt3/ntqfont.h
%{_includedir}/tqt3/ntqfontdatabase.h
%{_includedir}/tqt3/ntqfontdialog.h
%{_includedir}/tqt3/ntqfontinfo.h
%{_includedir}/tqt3/ntqfontmetrics.h
%{_includedir}/tqt3/ntqframe.h
%{_includedir}/tqt3/ntqftp.h
%{_includedir}/tqt3/ntqgarray.h
%{_includedir}/tqt3/ntqgb18030codec.h
%{_includedir}/tqt3/ntqgbkcodec.h
%{_includedir}/tqt3/ntqgcache.h
%{_includedir}/tqt3/ntqgdict.h
%{_includedir}/tqt3/ntqgeneric.h
%{_includedir}/tqt3/ntqgif.h
%{_includedir}/tqt3/ntqglist.h
%{_includedir}/tqt3/ntqglobal.h
%{_includedir}/tqt3/ntqgplugin.h
%{_includedir}/tqt3/ntqgrid.h
%{_includedir}/tqt3/ntqgridview.h
%{_includedir}/tqt3/ntqgroupbox.h
%{_includedir}/tqt3/ntqguardedptr.h
%{_includedir}/tqt3/ntqgvector.h
%{_includedir}/tqt3/ntqhbox.h
%{_includedir}/tqt3/ntqhbuttongroup.h
%{_includedir}/tqt3/ntqheader.h
%{_includedir}/tqt3/ntqhgroupbox.h
%{_includedir}/tqt3/ntqhostaddress.h
%{_includedir}/tqt3/ntqhttp.h
%{_includedir}/tqt3/ntqiconset.h
%{_includedir}/tqt3/ntqiconview.h
%{_includedir}/tqt3/ntqimage.h
%{_includedir}/tqt3/ntqimageformatplugin.h
%{_includedir}/tqt3/ntqinputcontext.h
%{_includedir}/tqt3/ntqinputcontextfactory.h
%{_includedir}/tqt3/ntqinputcontextplugin.h
%{_includedir}/tqt3/ntqinputdialog.h
%{_includedir}/tqt3/ntqintcache.h
%{_includedir}/tqt3/ntqintdict.h
%{_includedir}/tqt3/ntqinterlacestyle.h
%{_includedir}/tqt3/ntqiodevice.h
%{_includedir}/tqt3/ntqjiscodec.h
%{_includedir}/tqt3/ntqjpegio.h
%{_includedir}/tqt3/ntqjpunicode.h
%{_includedir}/tqt3/ntqkeycode.h
%{_includedir}/tqt3/ntqkeysequence.h
%{_includedir}/tqt3/ntqlabel.h
%{_includedir}/tqt3/ntqlayout.h
%{_includedir}/tqt3/ntqlcdnumber.h
%{_includedir}/tqt3/ntqlibrary.h
%{_includedir}/tqt3/ntqlineedit.h
%{_includedir}/tqt3/ntqlistbox.h
%{_includedir}/tqt3/ntqlistview.h
%{_includedir}/tqt3/ntqlocale.h
%{_includedir}/tqt3/ntqlocalfs.h
%{_includedir}/tqt3/ntqmainwindow.h
%{_includedir}/tqt3/ntqmap.h
%{_includedir}/tqt3/ntqmemarray.h
%{_includedir}/tqt3/ntqmenubar.h
%{_includedir}/tqt3/ntqmenudata.h
%{_includedir}/tqt3/ntqmessagebox.h
%{_includedir}/tqt3/ntqmetaobject.h
%{_includedir}/tqt3/ntqmime.h
%{_includedir}/tqt3/ntqmngio.h
%{_includedir}/tqt3/ntqmodules.h
%{_includedir}/tqt3/ntqmotifplusstyle.h
%{_includedir}/tqt3/ntqmotifstyle.h
%{_includedir}/tqt3/ntqmovie.h
%{_includedir}/tqt3/ntqmultilineedit.h
%{_includedir}/tqt3/ntqmutex.h
%{_includedir}/tqt3/ntqnamespace.h
%{_includedir}/tqt3/ntqnetwork.h
%{_includedir}/tqt3/ntqnetworkprotocol.h
%{_includedir}/tqt3/ntqnp.h
%{_includedir}/tqt3/ntqobject.h
%{_includedir}/tqt3/ntqobjectcleanuphandler.h
%{_includedir}/tqt3/ntqobjectdefs.h
%{_includedir}/tqt3/ntqobjectdict.h
%{_includedir}/tqt3/ntqobjectlist.h
%{_includedir}/tqt3/ntqpaintdevice.h
%{_includedir}/tqt3/ntqpaintdevicemetrics.h
%{_includedir}/tqt3/ntqpainter.h
%{_includedir}/tqt3/ntqpair.h
%{_includedir}/tqt3/ntqpalette.h
%{_includedir}/tqt3/ntqpen.h
%{_includedir}/tqt3/ntqpicture.h
%{_includedir}/tqt3/ntqpixmap.h
%{_includedir}/tqt3/ntqpixmapcache.h
%{_includedir}/tqt3/ntqplatinumstyle.h
%{_includedir}/tqt3/ntqpngio.h
%{_includedir}/tqt3/ntqpoint.h
%{_includedir}/tqt3/ntqpointarray.h
%{_includedir}/tqt3/ntqpolygonscanner.h
%{_includedir}/tqt3/ntqpopupmenu.h
%{_includedir}/tqt3/ntqprintdialog.h
%{_includedir}/tqt3/ntqprinter.h
%{_includedir}/tqt3/ntqprocess.h
%{_includedir}/tqt3/ntqprogressbar.h
%{_includedir}/tqt3/ntqprogressdialog.h
%{_includedir}/tqt3/ntqptrcollection.h
%{_includedir}/tqt3/ntqptrdict.h
%{_includedir}/tqt3/ntqptrlist.h
%{_includedir}/tqt3/ntqptrqueue.h
%{_includedir}/tqt3/ntqptrstack.h
%{_includedir}/tqt3/ntqptrvector.h
%{_includedir}/tqt3/ntqpushbutton.h
%{_includedir}/tqt3/ntqradiobutton.h
%{_includedir}/tqt3/ntqrangecontrol.h
%{_includedir}/tqt3/ntqrect.h
%{_includedir}/tqt3/ntqregexp.h
%{_includedir}/tqt3/ntqregion.h
%{_includedir}/tqt3/ntqrtlcodec.h
%{_includedir}/tqt3/ntqscrollbar.h
%{_includedir}/tqt3/ntqscrollview.h
%{_includedir}/tqt3/ntqsemaphore.h
%{_includedir}/tqt3/ntqsemimodal.h
%{_includedir}/tqt3/ntqserversocket.h
%{_includedir}/tqt3/ntqsession.h
%{_includedir}/tqt3/ntqsessionmanager.h
%{_includedir}/tqt3/ntqsettings.h
%{_includedir}/tqt3/ntqsgistyle.h
%{_includedir}/tqt3/ntqshared.h
%{_includedir}/tqt3/ntqsignal.h
%{_includedir}/tqt3/ntqsignalmapper.h
%{_includedir}/tqt3/ntqsignalslotimp.h
%{_includedir}/tqt3/ntqsimplerichtext.h
%{_includedir}/tqt3/ntqsize.h
%{_includedir}/tqt3/ntqsizegrip.h
%{_includedir}/tqt3/ntqsizepolicy.h
%{_includedir}/tqt3/ntqsjiscodec.h
%{_includedir}/tqt3/ntqslider.h
%{_includedir}/tqt3/ntqsocket.h
%{_includedir}/tqt3/ntqsocketdevice.h
%{_includedir}/tqt3/ntqsocketnotifier.h
%{_includedir}/tqt3/ntqsortedlist.h
%{_includedir}/tqt3/ntqsound.h
%{_includedir}/tqt3/ntqspinbox.h
%{_includedir}/tqt3/ntqsplashscreen.h
%{_includedir}/tqt3/ntqsplitter.h
%{_includedir}/tqt3/ntqsql.h
%{_includedir}/tqt3/ntqsqlcursor.h
%{_includedir}/tqt3/ntqsqldatabase.h
%{_includedir}/tqt3/ntqsqldriver.h
%{_includedir}/tqt3/ntqsqldriverplugin.h
%{_includedir}/tqt3/ntqsqleditorfactory.h
%{_includedir}/tqt3/ntqsqlerror.h
%{_includedir}/tqt3/ntqsqlfield.h
%{_includedir}/tqt3/ntqsqlform.h
%{_includedir}/tqt3/ntqsqlindex.h
%{_includedir}/tqt3/ntqsqlpropertymap.h
%{_includedir}/tqt3/ntqsqlquery.h
%{_includedir}/tqt3/ntqsqlrecord.h
%{_includedir}/tqt3/ntqsqlresult.h
%{_includedir}/tqt3/ntqsqlselectcursor.h
%{_includedir}/tqt3/ntqstatusbar.h
%{_includedir}/tqt3/ntqstring.h
%{_includedir}/tqt3/ntqstringlist.h
%{_includedir}/tqt3/ntqstrlist.h
%{_includedir}/tqt3/ntqstrvec.h
%{_includedir}/tqt3/ntqstyle.h
%{_includedir}/tqt3/ntqstylefactory.h
%{_includedir}/tqt3/ntqstyleplugin.h
%{_includedir}/tqt3/ntqstylesheet.h
%{_includedir}/tqt3/ntqsyntaxhighlighter.h
%{_includedir}/tqt3/ntqt.h
%{_includedir}/tqt3/ntqtabbar.h
%{_includedir}/tqt3/ntqtabdialog.h
%{_includedir}/tqt3/ntqtable.h
%{_includedir}/tqt3/ntqtabwidget.h
%{_includedir}/tqt3/ntqtextbrowser.h
%{_includedir}/tqt3/ntqtextcodec.h
%{_includedir}/tqt3/ntqtextcodecfactory.h
%{_includedir}/tqt3/ntqtextcodecplugin.h
%{_includedir}/tqt3/ntqtextedit.h
%{_includedir}/tqt3/ntqtextstream.h
%{_includedir}/tqt3/ntqtextview.h
%{_includedir}/tqt3/ntqthread.h
%{_includedir}/tqt3/ntqthreadstorage.h
%{_includedir}/tqt3/ntqtimer.h
%{_includedir}/tqt3/ntqtl.h
%{_includedir}/tqt3/ntqtoolbar.h
%{_includedir}/tqt3/ntqtoolbox.h
%{_includedir}/tqt3/ntqtoolbutton.h
%{_includedir}/tqt3/ntqtooltip.h
%{_includedir}/tqt3/ntqtranslator.h
%{_includedir}/tqt3/ntqtsciicodec.h
%{_includedir}/tqt3/ntqurl.h
%{_includedir}/tqt3/ntqurlinfo.h
%{_includedir}/tqt3/ntqurloperator.h
%{_includedir}/tqt3/ntqutfcodec.h
%{_includedir}/tqt3/ntquuid.h
%{_includedir}/tqt3/ntqvalidator.h
%{_includedir}/tqt3/ntqvaluelist.h
%{_includedir}/tqt3/ntqvaluestack.h
%{_includedir}/tqt3/ntqvaluevector.h
%{_includedir}/tqt3/ntqvariant.h
%{_includedir}/tqt3/ntqvbox.h
%{_includedir}/tqt3/ntqvbuttongroup.h
%{_includedir}/tqt3/ntqvfbhdr.h
%{_includedir}/tqt3/ntqvgroupbox.h
%{_includedir}/tqt3/ntqwaitcondition.h
%{_includedir}/tqt3/ntqwhatsthis.h
%{_includedir}/tqt3/ntqwidget.h
%{_includedir}/tqt3/ntqwidgetintdict.h
%{_includedir}/tqt3/ntqwidgetlist.h
%{_includedir}/tqt3/ntqwidgetplugin.h
%{_includedir}/tqt3/ntqwidgetstack.h
%{_includedir}/tqt3/ntqwindowdefs.h
%{_includedir}/tqt3/ntqwindowsstyle.h
%{_includedir}/tqt3/ntqwinexport.h
%{_includedir}/tqt3/ntqwizard.h
%{_includedir}/tqt3/ntqwmatrix.h
%{_includedir}/tqt3/ntqworkspace.h
%{_includedir}/tqt3/ntqxml.h
%{_includedir}/tqt3/paragdata.h
%{_includedir}/tqt3/parenmatcher.h
%{_includedir}/tqt3/preferenceinterface.h
%{_includedir}/tqt3/preferences.h
%{_includedir}/tqt3/preferences.ui.h
%{_includedir}/tqt3/projectsettingsiface.h
%{_includedir}/tqt3/qconfig-dist.h
%{_includedir}/tqt3/qconfig-large.h
%{_includedir}/tqt3/qconfig-medium.h
%{_includedir}/tqt3/qconfig-minimal.h
%{_includedir}/tqt3/qconfig-small.h
%{_includedir}/tqt3/qsql_ibase.h
%{_includedir}/tqt3/qsql_mysql.h
%{_includedir}/tqt3/qsql_odbc.h
%{_includedir}/tqt3/qsql_psql.h
%{_includedir}/tqt3/qsql_sqlite.h
%{_includedir}/tqt3/qsql_sqlite3.h
%{_includedir}/tqt3/qsqlcachedresult.h
%{_includedir}/tqt3/qt_pch.h
%{_includedir}/tqt3/qwindow.h
%{_includedir}/tqt3/sourcetemplateiface.h
%{_includedir}/tqt3/templatewizardiface.h
%{_includedir}/tqt3/viewmanager.h
%{_includedir}/tqt3/widgetinterface.h

%dir %{_includedir}/tqt3/private/
%{_includedir}/tqt3/private/*.h

##########

%package -n %{libtqt3}-mt-mysql
Summary:	MySQL database driver for TQt3 (Threaded)
Group:		System/GUI/Other
Provides:	libtqt3-mt-mysql = %{version}-%{release}
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n %{libtqt3}-mt-mysql
This package contains the threaded MySQL plugin for TQt3. Install it if
you intend to use or write TQt programs that are to access a MySQL DB.

%files -n %{libtqt3}-mt-mysql
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/sqldrivers/libqsqlmysql.so

##########

%package -n %{libtqt3}-mt-odbc
Summary:	ODBC database driver for TQt3 (Threaded)
Group:		System/GUI/Other
Provides:	libtqt3-mt-odbc = %{version}-%{release}
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n %{libtqt3}-mt-odbc
This package contains the threaded ODBC plugin for TQt3. Install it if
you intend to use or write TQt programs that are to access an ODBC DB.

%files -n %{libtqt3}-mt-odbc
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/sqldrivers/libqsqlodbc.so

##########

%package -n %{libtqt3}-mt-psql
Summary:	PostgreSQL database driver for TQt3 (Threaded)
Group:		System/GUI/Other
Provides:	libtqt3-mt-psql = %{version}-%{release}
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n %{libtqt3}-mt-psql
This package contains the threaded PostgreSQL plugin for TQt3.
Install it if you intend to use or write TQt programs that are
to access a PostgreSQL DB.

%files -n %{libtqt3}-mt-psql
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/sqldrivers/libqsqlpsql.so

##########

%if 0%{?with_ibase}
%package -n %{libtqt3}-mt-ibase
Summary:	InterBase/FireBird database driver for TQt3 (Threaded)
Group:		System/GUI/Other
Provides:	libtqt3-mt-ibase = %{version}-%{release}
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n %{libtqt3}-mt-ibase
This package contains the threaded InterBase/FireBird plugin
for TQt3. Install it if you intend to use or write TQt programs
that are to access an InterBase/FireBird DB.

%files -n %{libtqt3}-mt-ibase
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/sqldrivers/libqsqlibase.so
%endif

##########

%package -n %{libtqt3}-mt-sqlite
Summary:	SQLite database driver for TQt3 (Threaded)
Group:		System/GUI/Other
Provides:	libtqt3-mt-sqlite = %{version}-%{release}
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n %{libtqt3}-mt-sqlite
This package contains the threaded SQLite plugin for TQt3. Install
it if you intend to use or write TQt programs that are to access an
SQLite DB.

%files -n %{libtqt3}-mt-sqlite
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/sqldrivers/libqsqlite.so

##########

%package -n %{libtqt3}-mt-sqlite3
Summary:	SQLite3 database driver for TQt3 (Threaded)
Group:		System/GUI/Other
Provides:	libtqt3-mt-sqlite3 = %{version}-%{release}
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n %{libtqt3}-mt-sqlite3
This package contains the threaded SQLite3 plugin for TQt3. Install
it if you intend to use or write TQt programs that are to access an
SQLite3 DB.

%files -n %{libtqt3}-mt-sqlite3
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/sqldrivers/libqsqlite3.so

###########

%package -n tqt3-compat-headers
Summary:	TQt 1.x and 2.x compatibility includes
Group:		Development/Libraries/X11
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n tqt3-compat-headers
This package contains header files that are intended for build
compatibility for applications that build with TQt3 but still use
deprecated includes. It is meant as an intermediate solution and
these header files are not part of the official TQt3 API.
All sourcecode that is still using the headers of this package is
subject to be changed to use the new header files which are in
libtqt3-headers.

%files -n tqt3-compat-headers
%defattr(-,root,root,-)
%{_includedir}/tqt3/ntqapp.h
%{_includedir}/tqt3/ntqarray.h
%{_includedir}/tqt3/ntqbitarry.h
%{_includedir}/tqt3/ntqbttngrp.h
%{_includedir}/tqt3/ntqchkbox.h
%{_includedir}/tqt3/ntqclipbrd.h
%{_includedir}/tqt3/ntqcollect.h
%{_includedir}/tqt3/ntqcollection.h
%{_includedir}/tqt3/ntqcombo.h
%{_includedir}/tqt3/ntqconnect.h
%{_includedir}/tqt3/ntqdatetm.h
%{_includedir}/tqt3/ntqdrawutl.h
%{_includedir}/tqt3/ntqdstream.h
%{_includedir}/tqt3/ntqfiledef.h
%{_includedir}/tqt3/ntqfiledlg.h
%{_includedir}/tqt3/ntqfileinf.h
%{_includedir}/tqt3/ntqfontinf.h
%{_includedir}/tqt3/ntqfontmet.h
%{_includedir}/tqt3/ntqgrpbox.h
%{_includedir}/tqt3/ntqintcach.h
%{_includedir}/tqt3/ntqiodev.h
%{_includedir}/tqt3/ntqlcdnum.h
%{_includedir}/tqt3/ntqlined.h
%{_includedir}/tqt3/ntqmenudta.h
%{_includedir}/tqt3/ntqmetaobj.h
%{_includedir}/tqt3/ntqmlined.h
%{_includedir}/tqt3/ntqmsgbox.h
%{_includedir}/tqt3/ntqmultilinedit.h
%{_includedir}/tqt3/ntqobjcoll.h
%{_includedir}/tqt3/ntqobjdefs.h
%{_includedir}/tqt3/ntqpdevmet.h
%{_includedir}/tqt3/ntqpmcache.h
%{_includedir}/tqt3/ntqpntarry.h
%{_includedir}/tqt3/ntqpopmenu.h
%{_includedir}/tqt3/ntqprndlg.h
%{_includedir}/tqt3/ntqprogbar.h
%{_includedir}/tqt3/ntqprogdlg.h
%{_includedir}/tqt3/ntqpsprn.h
%{_includedir}/tqt3/ntqpushbt.h
%{_includedir}/tqt3/ntqqueue.h
%{_includedir}/tqt3/ntqradiobt.h
%{_includedir}/tqt3/ntqrangect.h
%{_includedir}/tqt3/ntqscrbar.h
%{_includedir}/tqt3/ntqsocknot.h
%{_includedir}/tqt3/ntqtabdlg.h
%{_includedir}/tqt3/ntqtstream.h
%{_includedir}/tqt3/ntqwidcoll.h
%{_includedir}/tqt3/ntqwindefs.h

###########

%package -n tqt3-dev-tools
Summary:	TQt3 development tools
Group:		Development/Libraries/X11
Requires:	%{libtqt3}-mt-devel = %{version}-%{release}
Requires:	tqt3-dev-tools-devel = %{version}-%{release}

%description -n tqt3-dev-tools
This package contains all tools that are necessary to build programs
that are written using TQt3. These are: qmake, uic and moc.
For TQt3 development, you most likely want to install this package.

%files -n tqt3-dev-tools
%defattr(-,root,root,-)
%{_datadir}/tqt3/doc/html/qmake*html
%{_datadir}/tqt3/doc/html/qmake*dcf
%{_bindir}/tqmake
%{_bindir}/tqlupdate
%{_bindir}/tqlrelease
%{_bindir}/tquic
%{_bindir}/tqmoc
%{_bindir}/tqembed
%{_mandir}/man1/*.1*

##########

%package -n tqt3-dev-tools-devel
Summary:	TQt3 development tools
Group:		Development/Libraries/X11

%description -n tqt3-dev-tools-devel
This package contains all tools that are necessary to build programs
that are written using TQt3.

%files -n tqt3-dev-tools-devel
%defattr(-,root,root,-)
%dir %{_datadir}/tqt3/mkspecs/
%{_datadir}/tqt3/mkspecs/*

##########

%package -n tqt3-designer
Summary:	TQt3 Designer
Group:		System/GUI/Other
Requires:	%{libtqt3}-mt = %{version}-%{release}
Requires:	tqt3-doc = %{version}-%{release}

%description -n tqt3-designer
The TQt Designer is a GUI design program that interactively lets you
construct user interfaces for the TQt library. Additionally it lets you
create whole project and works together with the database drivers
provided by TQt to create applications with easy database access through
TQt. The resulting user interface files can then be converted to
C++ classes using the uic commandline utility which is usually done
automatically for the developer with a project management with qmake
or automake.

%files -n tqt3-designer
%defattr(-,root,root,-)
%{_bindir}/tqdesigner
%{_bindir}/tqtcreatecw
%{_bindir}/tqtconv2ui
%{_datadir}/tqt3/doc/html/designer*html
%{_datadir}/tqt3/doc/html/designer*dcf
%{_datadir}/tqt3/doc/html/designer*jpg
%dir %{_datadir}/tqt3/templates/
%{_datadir}/tqt3/templates/*
%{_libdir}/tqt3/plugins/designer/libcppeditor.so
%{_libdir}/tqt3/plugins/designer/libdlgplugin.so
%{_libdir}/tqt3/plugins/designer/libgladeplugin.so
%{_libdir}/tqt3/plugins/designer/libkdevdlgplugin.so
%{_libdir}/tqt3/plugins/designer/librcplugin.so
%{_libdir}/tqt3/plugins/designer/libwizards.so
%dir %{_datadir}/tqt3/tools/tqtconv2ui
%{_datadir}/tqt3/tools/tqtconv2ui/main.cpp
%{_datadir}/tqt3/tools/tqtconv2ui/tqtconv2ui.pro
%dir %{_datadir}/tqt3/tools/tqtcreatecw
%{_datadir}/tqt3/tools/tqtcreatecw/README
%{_datadir}/tqt3/tools/tqtcreatecw/main.cpp
%{_datadir}/tqt3/tools/tqtcreatecw/tqtcreatecw.pro
%{_datadir}/applications/tqdesigner.desktop
%{_datadir}/pixmaps/tqdesigner.png

###########

%package -n tqt3-apps-devel
Summary:	TQt3 Developer applications development files
Group:		Development/Libraries/X11
Requires:	%{libtqt3}-mt-devel = %{version}-%{release}
Requires:	tqt3-apps-libs = %{version}-%{release}

%description -n tqt3-apps-devel
This package is intended for developers who want to develop applications
using the additional static libraries that ship with the applications
included with TQt; the TQt Designer and the TQt Assistant.
It allows integrating additional enhancements into the TQt Designer
respectively faciliate the TQt Assistant from within your TQt application
to interactively call the Assistant for displaying online help that the
developer includes with his application.

%post -n tqt3-apps-devel
/sbin/ldconfig || :

%postun -n tqt3-apps-devel
/sbin/ldconfig || :

%files -n tqt3-apps-devel
%defattr(-,root,root,-)
%{_libdir}/libtqtdesignercore.prl
%{_libdir}/libtqtdesignercore.so
%{_libdir}/libtqteditor.prl
%{_libdir}/libtqteditor.so
%{_libdir}/libtqassistantclient.prl
%{_libdir}/libtqassistantclient.so
%{_includedir}/tqt3/ntqassistantclient.h

###########

%package -n tqt3-apps-libs
Summary:	TQt3 Developer applications libraries
Group:		Development/Libraries/X11
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n tqt3-apps-libs
This package is intended for developers who want to develop applications
using the additional static libraries that ship with the applications
included with TQt; the TQt Designer and the TQt Assistant.
It allows integrating additional enhancements into the TQt Designer
respectively faciliate the TQt Assistant from within your TQt application
to interactively call the Assistant for displaying online help that the
developer includes with his application.

%post -n tqt3-apps-libs
/sbin/ldconfig || :

%postun -n tqt3-apps-libs
/sbin/ldconfig || :

%files -n tqt3-apps-libs
%defattr(-,root,root,-)
%{_libdir}/libtqtdesignercore.so.1
%{_libdir}/libtqtdesignercore.so.1.0
%{_libdir}/libtqtdesignercore.so.1.0.0
%{_libdir}/libtqteditor.so.1
%{_libdir}/libtqteditor.so.1.0
%{_libdir}/libtqteditor.so.1.0.0
%{_libdir}/libtqassistantclient.so.1
%{_libdir}/libtqassistantclient.so.1.0
%{_libdir}/libtqassistantclient.so.1.0.0

##########

%package -n tqt3-linguist
Summary:	The TQt3 Linguist
Group:		System/GUI/Other
Requires:	%{libtqt3}-mt = %{version}-%{release}
Requires:	tqt3-doc = %{version}-%{release}

%description -n tqt3-linguist
This package contains the TQt3 Linguist which provides translators a
tool perfect for translating any TQt-based application into other
languages and can be used and installed independently of any TQt
development files by the translator.

%files -n tqt3-linguist
%defattr(-,root,root,-)
%{_bindir}/tqlinguist
%dir %{_datadir}/tqt3/phrasebooks/
%{_datadir}/tqt3/phrasebooks/*
%{_datadir}/tqt3/doc/html/linguist*html
%{_datadir}/tqt3/doc/html/linguist*dcf
%dir %{_docdir}/tqt3-linguist
%{_docdir}/tqt3-linguist/qt_untranslated.ts
%{_datadir}/applications/tqlinguist.desktop
%{_datadir}/pixmaps/tqlinguist.png

##########

%package -n tqt3-assistant
Summary:	The TQt3 assistant application
Group:		System/GUI/Other
Requires:	%{libtqt3}-mt = %{version}-%{release}
Requires:	tqt3-doc = %{version}-%{release}

%description -n tqt3-assistant
This package contains the TQt3 Assistant, an easy to use frontend for
the complete TQt3 documentation and serves as an online help viewer for
any TQt program that wants to give the usesr access to online help.
Within the TQt tools it is used as the help viewer for the online help
for the TQt3 Designer and Linguist as well as qmake and the TQt 3 API
documentation.

Developers of TQt Application who want to faciliate the TQt Assistant for online
help display should refer to the README.Debian file for libtqt3-mt-devel and
the package tqt3-apps-devel.

%files -n tqt3-assistant
%defattr(-,root,root,-)
%{_bindir}/tqassistant
%{_datadir}/tqt3/doc/html/assistant*html
%{_datadir}/tqt3/doc/html/assistant*dcf
%{_datadir}/applications/tqassistant.desktop
%{_datadir}/pixmaps/tqassistant.png

##########

%package -n tqt3-qtconfig
Summary:	The TQt3 Configuration Application
Group:		Development/Libraries/X11
Requires:	%{libtqt3}-mt = %{version}-%{release}
Requires:	tqt3-doc = %{version}-%{release}

%description -n tqt3-qtconfig
The TQt Configuration program allows endusers to configure the look
and behavior of any TQt3 application. It is mostly only necessary
on systems which don't run TDE because the Trinity control center already
covers this configuration automatically for the users TQt3 applications
according to his desktop settings in TDE. However, if you need to run
CJK-fonts or other non-latin scripts, you will most likely want to
install this package.

%files -n tqt3-qtconfig
%defattr(-,root,root,-)
%{_bindir}/tqtconfig
%{_datadir}/applications/tqtconfig.desktop
%{_datadir}/pixmaps/tqtconfig.png

###########

%package -n tqt3-dev-tools-embedded
Summary:	Tools to develop embedded TQt applications
Group:		System/GUI/Other
Requires:	%{libtqt3}-mt-devel = %{version}-%{release}

%description -n tqt3-dev-tools-embedded
This package contains applications only suitable for developing
applications with TQt Embedded and/or Qtopia. It provides the QVFB
program for simulating an embedded device desktop as well as maketqpf
for converting fonts to embedded fonts suitable for being utilized
by TQt Embedded applications.

%files -n tqt3-dev-tools-embedded
%defattr(-,root,root,-)
%{_bindir}/maketqpf
%{_bindir}/tqvfb
%dir %{_sysconfdir}/tqt3/tqvfb
%config %{_sysconfdir}/tqt3/tqvfb/pda.skin
%dir %{_datadir}/tqvfb
%{_datadir}/tqvfb/pda_down.png
%{_datadir}/tqvfb/pda_up.png

###########

%package -n tqt3-dev-tools-compat
Summary:	Conversion utilities for TQt3 development
Group:		System/GUI/Other
Requires:	%{libtqt3}-mt-devel = %{version}-%{release}

%description -n tqt3-dev-tools-compat
This package contains some older TQt tools (namely tqtrename140,
tqm2ts, tqtmergetr, tqtfindtr and msg2tqm). These tools are needed only by
application developers who need to migrate any TQt application written
for TQt 1.x or 2.x over to TQt 3.x. The purpose of the tools are to
help fixing the changes with include file renaming as well as migrating
the message file format of TQt 2 translation files or any gettext-based
translation system to the TQt 3 system.

%files -n tqt3-dev-tools-compat
%defattr(-,root,root,-)
%{_bindir}/tqtrename140
%{_bindir}/tqm2ts
%{_bindir}/tqtmergetr
%{_bindir}/tqtfindtr
%{_bindir}/msg2tqm

##########

%package -n tqt3-i18n
Summary:	Translation (i18n) files for TQt3 library
Group:		System/GUI/Other
Requires:	%{libtqt3}-mt = %{version}-%{release}

%description -n tqt3-i18n
This package contains the internationalization files for the TQt library.
TQt applications that are internationalized will need to depend on this package
for full internationalization support of the application towards the end user.

%files -n tqt3-i18n
%defattr(-,root,root,-)
%dir %{_datadir}/tqt3/translations/
%{_datadir}/tqt3/translations/assistant_de.qm
%{_datadir}/tqt3/translations/assistant_fr.qm
%{_datadir}/tqt3/translations/designer_de.qm
%{_datadir}/tqt3/translations/designer_fr.qm
%{_datadir}/tqt3/translations/linguist_de.qm
%{_datadir}/tqt3/translations/linguist_fr.qm
%{_datadir}/tqt3/translations/qt_ar.qm
%{_datadir}/tqt3/translations/qt_ca.qm
%{_datadir}/tqt3/translations/qt_cs.qm
%{_datadir}/tqt3/translations/qt_de.qm
%{_datadir}/tqt3/translations/qt_es.qm
%{_datadir}/tqt3/translations/qt_fr.qm
%{_datadir}/tqt3/translations/qt_he.qm
%{_datadir}/tqt3/translations/qt_it.qm
%{_datadir}/tqt3/translations/qt_ja.qm
%{_datadir}/tqt3/translations/qt_nb.qm
%{_datadir}/tqt3/translations/qt_pt.qm
%{_datadir}/tqt3/translations/qt_pt-br.qm
%{_datadir}/tqt3/translations/qt_ru.qm
%{_datadir}/tqt3/translations/qt_sk.qm
%{_datadir}/tqt3/translations/qt_tr.qm
%{_datadir}/tqt3/translations/qt_zh-cn.qm
%{_datadir}/tqt3/translations/qt_zh-tw.qm

##########

%package -n tqt3-doc
Summary:	TQt3 API documentation
Group:		System/GUI/Other

%description -n tqt3-doc
This package contains the complete API documentation for TQt3.
Examples to coding are in tqt3-examples. The documentation is provided
in HTML and manpage format; the HTML version can be viewed in conjunction
with the TQt Assistant.

%files -n tqt3-doc
%defattr(-,root,root,-)
%exclude %{_datadir}/tqt3/doc/html/qmake*html
%exclude %{_datadir}/tqt3/doc/html/qmake*dcf
%exclude %{_datadir}/tqt3/doc/html/designer*html
%exclude %{_datadir}/tqt3/doc/html/designer*dcf
%exclude %{_datadir}/tqt3/doc/html/designer*jpg
%exclude %{_datadir}/tqt3/doc/html/linguist*html
%exclude %{_datadir}/tqt3/doc/html/linguist*dcf
%exclude %{_datadir}/tqt3/doc/html/assistant*html
%exclude %{_datadir}/tqt3/doc/html/assistant*dcf
%{_datadir}/tqt3/doc/html/*

##########

%package -n tqt3-examples
summary:	Examples for TQt3
Group:		System/GUI/Other

%description -n tqt3-examples
These are examples provided with TQt3. They may be especially useful for
you if you are learning to program in TQt as they cover tquite a lot of
things that are possible with TQt3.

%files -n tqt3-examples
%defattr(-,root,root,-)
%dir %{_docdir}/tqt3-examples/
%{_docdir}/tqt3-examples/build-examples
%{_docdir}/tqt3-examples/tqt3-examples.tar.gz

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%if 0%{?suse_version}
echo "suse_version = %{?suse_version}"
echo "sle_version = %{?sle_version}"
%endif

%if 0%{?rhel} == 5
%__sed -i "src/sql/drivers/mysql/qsql_mysql.cpp" -e "s|bool reconnect = 0;|my_bool reconnect = 0;|g"
%endif

# fix variables in 'qmake.conf'
%__sed -i mkspecs/*/qmake.conf \
  -e "s|^QMAKE_INCDIR_TQT.*|QMAKE_INCDIR_TQT		= %{_includedir}/tqt3|" \
  -e "s|\$(QTDIR)|/usr|g" \
  -e "s|-lqt|-ltqt|g" \
  -e "s|^QMAKE_CFLAGS		=.*|QMAKE_CFLAGS		= ${distrib_cflags} -pipe -fvisibility=hidden -fvisibility-inlines-hidden|" \
  -e "s|^QMAKE_INCDIR		=.*|QMAKE_INCDIR		= %{_includedir}|" \
  -e "s|^QMAKE_LIBDIR		=.*|QMAKE_LIBDIR		= %{_libdir}|" \
  -e "s|^QMAKE_RPATH		= .*|QMAKE_RPATH		=|" \
  -e "s|^QMAKE_STRIP             =.*|QMAKE_STRIP             =|" \
  -e "s|^QMAKE_STRIPFLAGS_LIB 	+=.*|QMAKE_STRIPFLAGS_LIB 	+=|" \
  -e "s|^QMAKE_MOC		=.*|QMAKE_MOC		= %{_bindir}/tqmoc|" \
  -e "s|^QMAKE_UIC		=.*|QMAKE_UIC		= %{_bindir}/tquic|" \
  -e "s|^QMAKE_INCDIR_TQT		=.*|QMAKE_INCDIR_TQT		= %{_includedir}/tqt3|" \
  -e "s|^QMAKE_LIBDIR_TQT		=.*|QMAKE_LIBDIR_TQT		= %{_libdir}|" \


%build
unset QTDIR QTINC QTLIB
export QTDIR=$(pwd)
export PATH=${QTDIR}/bin:${PATH}
export MANPATH=${QTDIR}/doc/man:${MANPATH}
export LD_LIBRARY_PATH="${QTDIR}/lib"

# Checks for supplementary include dir
INCDIRS=""
for d in \
	%{_includedir}/fontconfig \
	%{_includedir}/pgsql \
	%{_includedir}/pgsql/server \
	%{_includedir}/postgresql/server \
	%{_includedir}/Xft2 \
	%{_includedir}/Xft2/X11/Xft \
	%{_includedir}/mysql \
	%{_includedir}/libpng15 \
	%{_includedir}/libpng16 \
	%{_includedir}/tirpc \
; do
	if [ -d "${d}" ]; then
		INCDIRS="${INCDIRS} -I${d}"
	fi
done

# Checks for supplementary library dirs
LIBDIRS=""
for d in \
	%{_libdir}/libglvnd \
	%{_libdir}/mysql \
	%{_libdir}/pgsql \
; do
	if [ -d "${d}" ]; then
		LIBDIRS="${LIBDIRS} -L${d}"
	fi
done

# build shared, threaded (default) libraries
echo yes | ./configure \
		${INCDIRS} \
		${LIBDIRS} \
		-L%{_libdir} \
		-prefix		"%{_prefix}" \
		-libdir		"%{_libdir}" \
		-sysconfdir	"%{_sysconfdir}/tqt3" \
		-datadir	"%{_datadir}/tqt3" \
		-headerdir	"%{_includedir}/tqt3" \
		-docdir		"%{_datadir}/tqt3/doc" \
		-plugindir	"%{_libdir}/tqt3/plugins" \
		-translationdir	"%{_datadir}/tqt3/translations" \
		-sysshare "%{_datadir}" \
		\
		-thread \
		-shared \
		-fast \
		-no-exceptions \
%if "%{?c_compiler}" == "clang"
		-platform linux-clang \
%else
%if "%{_lib}" == "lib64"
		-platform linux-g++-64 \
%else
		-platform linux-g++ \
%endif
%endif
		\
		%{?with_nis:-nis} %{?!with_nis:-no-nis}		\
		-no-pch				\
		-cups				\
		-stl				\
		-ipv6				\
		\
		-sm				\
		-xshape				\
		-xinerama			\
		-xcursor			\
		-xrandr				\
		-xrender			\
		-xft				\
		-tablet				\
		-xkb				\
		\
		-system-zlib			\
		-system-libpng			\
		-system-libmng			\
		-system-libjpeg			\
		%{?with_nas:-system-nas-sound} %{?!with_nas:-no-nas-sound}		\
		\
		-enable-opengl			\
		-dlopen-opengl			\
		\
		-qt-gif				\
		-qt-imgfmt-mng \
		-qt-imgfmt-png			\
		-qt-imgfmt-jpeg			\
		-plugin-imgfmt-mng		\
		\
		-plugin-sql-odbc		\
		-plugin-sql-psql		\
		-plugin-sql-mysql		\
		%{?with_ibase:-plugin-sql-ibase}		\
		-plugin-sql-sqlite		\
		-plugin-sql-sqlite3		\
		\
		-lfontconfig			\
		-inputmethod			\
		%{?with_glibmainloop:-glibmainloop} \
		-debug \
		-v

# proceed
%__make %{?_smp_mflags} sub-src || %__make sub-src
%__make %{?_smp_mflags} sub-plugins || %__make sub-plugins
%__make %{?_smp_mflags} sub-tools

# build tqtconv2ui
%__make -C tools/designer/tools/tqtconv2ui

# build tqvfb
%__make -C tools/tqvfb

# fix .prl files
%__sed -i lib/*.prl -e "s|${QTDIR}|%{_datadir}/tqt3|g"


%install
%__rm -rf %{buildroot}
export QTDIR=$(pwd)
export PATH="${QTDIR}/bin:${PATH}"
export LD_LIBRARY_PATH=${QTDIR}/lib

# Installs 'libtqt-mt.so.3' library
%__make -C src INSTALL_ROOT="%{?buildroot}" install_target

# Installs all the remaining
%__make INSTALL_ROOT=%{?buildroot} install
%__make INSTALL_ROOT=%{?buildroot} plugins-install

%__install -m755 "bin/tqtrename140" "%{?buildroot}%{_bindir}"
%__install -m755 "bin/tqtfindtr" "%{?buildroot}%{_bindir}"

# install tqtconv2ui
%__install -m755 "bin/tqtconv2ui" "%{?buildroot}%{_bindir}/tqtconv2ui"

# install tqvfb
%__install -m755 -D "tools/tqvfb/tqvfb" "%{?buildroot}%{_bindir}/tqvfb"
%__install -m644 -D "tools/tqvfb/pda.skin" "%{?buildroot}%{_sysconfdir}/tqt3/tqvfb/pda.skin"
%__install -m644 -D "tools/tqvfb/pda_down.png" "%{?buildroot}%{_datadir}/tqvfb/pda_down.png"
%__install -m644 -D "tools/tqvfb/pda_up.png" "%{?buildroot}%{_datadir}/tqvfb/pda_up.png"

## create tqt3-apps-dev-package
cp tools/designer/interfaces/*.h "%{?buildroot}%{?_includedir}/tqt3/"
cp tools/designer/editor/*.h "%{?buildroot}%{?_includedir}/tqt3/"

# language file for linguist
%__install -D -m644 "translations/template.ts" "%{?buildroot}%{?_docdir}/tqt3-linguist/qt_untranslated.ts"

# fix that stupid friggin professional file
perl -pi -e 's{\$$\$$QT_SOURCE_TREE}{$(QTDIR)}' "src/qt_professional.pri"

## i18n files for designer, linguist and assistant
for i in designer/designer assistant linguist/linguist; do
  pushd "tools/${i}"
  tqlrelease "${i##*/}.pro"
  for j in ${i##*/}_*.qm; do
    install -m644 "${j}" "%{?buildroot}%{_datadir}/tqt3/translations/"
  done
  popd
done

%if 0%{?suse_version}
%suse_update_desktop_file tqassistant Documentation
%suse_update_desktop_file tqdesigner GUIDesigner
%suse_update_desktop_file tqlinguist Translation
%suse_update_desktop_file tqtconfig Utility
%endif

# Install applications icons
#__install -m644 -D "tools/assistant/images/appicon.png" "%{?buildroot}%{_datadir}/icons/hicolor/32x32/apps/tqassistant.png"
#__install -m644 -D "tools/designer/designer/images/designer_appicon.png" "%{?buildroot}%{_datadir}/icons/hicolor/32x32/apps/tqdesigner.png"
#__install -m644 -D "tools/linguist/linguist/images/appicon.png" "%{?buildroot}%{_datadir}/icons/hicolor/32x32/apps/tqlinguist.png"
#__install -m644 -D "tools/qtconfig/images/appicon.png" "%{?buildroot}%{_datadir}/icons/hicolor/32x32/apps/tqtconfig.png"

# install the man pages
%__install -d "%{?buildroot}%{_mandir}/man1"
%__install -m644 "doc/man/man1/"*"embed.1" "%{?buildroot}%{_mandir}/man1/"
%__install -m644 "doc/man/man1/"*"lrelease.1" "%{?buildroot}%{_mandir}/man1/"
%__install -m644 "doc/man/man1/"*"lupdate.1" "%{?buildroot}%{_mandir}/man1/"
%__install -m644 "doc/man/man1/"*"moc.1" "%{?buildroot}%{_mandir}/man1/"
%__install -m644 "doc/man/man1/"*"uic.1" "%{?buildroot}%{_mandir}/man1/"

# Install source for the designer tools, such as tqtcreatecw.
cp -ra tools/designer/tools %{?buildroot}%{_datadir}/tqt3/tools
rm -f %{?buildroot}%{_datadir}/tqt3/tools/tqtcreatecw/tqtcreatecw
rm -rf %{?buildroot}%{_datadir}/tqt3/tools/tqtcreatecw/.moc
rm -rf %{?buildroot}%{_datadir}/tqt3/tools/tqtcreatecw/.obj
rm -f %{?buildroot}%{_datadir}/tqt3/tools/tqtcreatecw/Makefile
rm -f %{?buildroot}%{_datadir}/tqt3/tools/tqtconv2ui/tqtconv2ui
rm -rf %{?buildroot}%{_datadir}/tqt3/tools/tqtconv2ui/.moc
rm -rf %{?buildroot}%{_datadir}/tqt3/tools/tqtconv2ui/.obj
rm -f %{?buildroot}%{_datadir}/tqt3/tools/tqtconv2ui/Makefile

# create examples package
%__install -d tqt3-examples
cp -ax examples tqt3-examples/
cp -ax tutorial tqt3-examples/
mkdir -p tqt3-examples/tools/designer
cp -ax tools/designer/examples tqt3-examples/tools/designer/
mkdir -p tqt3-examples/tools/linguist
cp -ax tools/linguist/tutorial tqt3-examples/tools/linguist/
find tqt3-examples -name "tt1" -print | xargs rm -rf
find tqt3-examples -name "tt2" -print | xargs rm -rf
find tqt3-examples -name "tt3" -print | xargs rm -rf
find tqt3-examples -name ".moc" | xargs rm -rf
find tqt3-examples -name ".obj" | xargs rm -rf
find tqt3-examples -name "Makefile" | xargs rm -rf
install -D -m 755 %{SOURCE1} %{?buildroot}%{_docdir}/tqt3-examples/build-examples
tar cvvfz tqt3-examples.tar.gz tqt3-examples/
install -D -m644 "tqt3-examples.tar.gz" "%{?buildroot}%{_docdir}/tqt3-examples/tqt3-examples.tar.gz"

# Fix wrong permissions
chmod 644 "%{?buildroot}%{_datadir}/tqt3/mkspecs/"*/*


%clean
%__rm -rf %{buildroot}


%changelog
