#
# spec file for package tdeaccessibility (version R14)
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
%define tde_pkg tdeaccessibility
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


Name:			trinity-tdeaccessibility
Summary:		Trinity Desktop Environment - Accessibility
Version:		%{tde_version}
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdemultimedia-devel >= %{tde_version}

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# AUDIOFILE support
BuildRequires:	audiofile-devel

# AKODE support
%define with_akode 1
BuildRequires: trinity-akode-devel

# MAD support
%ifarch %{ix86} x86_64
%define with_libmad 1
%{?with_libmad:BuildRequires: libakode_mpeg_decoder}
%endif

# ALSA support
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}asound-devel
%else
BuildRequires: alsa-lib-devel
%endif

# GLIB2 support
BuildRequires:	glib2-devel

# JPEG support
%if 0%{?mdkver}
%define libjpeg %{_lib}jpeg
%else
%define libjpeg libjpeg
%endif
BuildRequires: %{libjpeg}-devel

# XCB support
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?pclinuxos}
BuildRequires:	libxcb-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos} == 0
BuildRequires:	%{_lib}xcb-devel
%endif
%endif

# XAU support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xau-devel
%else
BuildRequires:	%{_lib}xau%{?mgaversion:6}-devel
%endif
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXau-devel
%endif

Obsoletes:		trinity-kdeaccessibility < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdeaccessibility = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdeaccessibility-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdeaccessibility-libs = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: trinity-tde-icons-mono = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kbstate = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmag = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmousetool = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmouth = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksayit = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kttsd = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kttsd-contrib-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Included with this package are:
* kmag, a screen magnifier,
* kmousetool, a program for people whom it hurts to click the mouse,
* kmouth, program that allows people who have lost their voice
  to let their computer speak for them.

%files

##########

%package -n trinity-tde-icons-mono
Summary:	A monochromatic icons theme for TDE
Group:		System/GUI/Other

Obsoletes:	trinity-kde-icons-mono < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kde-icons-mono = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tde-icons-mono
A monochromatic icon theme for TDE, designed for accessibility purposes.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-tde-icons-mono
%defattr(-,root,root,-)
%{tde_datadir}/icons/mono/

##########

%package -n trinity-kbstate
Summary:	A keyboard status applet for TDE
Group:		System/GUI/Other

%description -n trinity-kbstate
A panel applet that displays the keyboard status.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kbstate
%defattr(-,root,root,-)
%{tde_tdelibdir}/kbstate_panelapplet.la
%{tde_tdelibdir}/kbstate_panelapplet.so
%{tde_datadir}/apps/kbstateapplet/
%{tde_datadir}/apps/kicker/applets/kbstateapplet.desktop

##########

%package -n trinity-kmag
Summary:	A screen magnifier for TDE
Group:		System/GUI/Other

%description -n trinity-kmag
TDE's screen magnifier tool.

You can use KMagnifier to magnify a part of the screen just as you would use 
a lens to magnify a newspaper fine-print or a photograph.  This application is
useful for a variety of people: from researchers to artists to web-designers to
people with low vision.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kmag
%defattr(-,root,root,-)
%{tde_bindir}/kmag
%{tde_tdeappdir}/kmag.desktop
%{tde_datadir}/apps/kmag/
%{tde_datadir}/icons/hicolor/*/apps/kmag.png
%{tde_datadir}/icons/locolor/*/apps/kmag.png
%{tde_tdedocdir}/HTML/en/kmag/
%{tde_mandir}/man1/kmag.1*

##########

%package -n trinity-kmousetool
Summary:	TDE mouse manipulation tool for the disabled
Group:		System/GUI/Other

%description -n trinity-kmousetool
KMouseTool clicks the mouse whenever the mouse cursor pauses briefly. It was
designed to help those with repetitive strain injuries, for whom pressing
buttons hurts.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kmousetool
%defattr(-,root,root,-)
%{tde_bindir}/kmousetool
%{tde_tdeappdir}/kmousetool.desktop
%{tde_datadir}/apps/kmousetool/
%{tde_datadir}/icons/hicolor/*/apps/kmousetool.png
%{tde_tdedocdir}/HTML/en/kmousetool/
%{tde_mandir}/man1/kmousetool.1*

##########

%package -n trinity-kmouth
Summary:	A type-and-say KDE frontend for speech synthesizers
Group:		System/GUI/Other

%description -n trinity-kmouth
KDE's type-and-say frontend for speech synthesizers.

It includes a history of spoken sentences from which the user can select
sentences to be re-spoken.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kmouth
%defattr(-,root,root,-)
%config(noreplace) %{tde_confdir}/kmouthrc
%{tde_bindir}/kmouth
%{tde_tdeappdir}/kmouth.desktop
%{tde_datadir}/apps/kmouth/
%{tde_datadir}/icons/hicolor/*/actions/speak.png
%{tde_datadir}/icons/hicolor/*/actions/nospeak.png
%{tde_datadir}/icons/hicolor/*/apps/kmouth.png
%{tde_datadir}/icons/locolor/*/actions/speak.png
%{tde_datadir}/icons/locolor/*/apps/kmouth.png
%{tde_tdedocdir}/HTML/en/kmouth/
%{tde_mandir}/man1/kmouth.1*

##########

%package -n trinity-ksayit
Summary:	A frontend for the TDE Text-to-Speech system
Group:		System/GUI/Other

%description -n trinity-ksayit
Text-to-speech front-end to kttsd.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-ksayit
%defattr(-,root,root,-)
%{tde_bindir}/ksayit
%{tde_tdelibdir}/libFreeverb_plugin.la
%{tde_tdelibdir}/libFreeverb_plugin.so
%{tde_libdir}/libKTTSD_Lib.so.*
%{tde_tdeappdir}/ksayit.desktop
%{tde_datadir}/apps/ksayit/
%{tde_datadir}/icons/hicolor/*/apps/ksayit.png
%{tde_datadir}/icons/hicolor/32x32/apps/ksayit_clipempty.png
%{tde_datadir}/icons/hicolor/32x32/apps/ksayit_talking.png
%{tde_datadir}/services/ksayit_libFreeverb.desktop
%{tde_datadir}/servicetypes/ksayit_libFreeverb_service.desktop
%{tde_tdedocdir}/HTML/en/ksayit/
%{tde_mandir}/man1/ksayit.1*

##########

%package -n trinity-kttsd
Summary:	A Text-to-Speech system for TDE
Group:		System/GUI/Other

%description -n trinity-kttsd
The KDE Text-to-Speech system is a plugin based service that allows any KDE
(or non-KDE) application to speak using the DCOP interface.

ksayit and kmouth are useful front-ends for this capability, while one of
festival, flite, and epos are essential back-ends.

This package is part of Trinity, as a component of the TDE accessibility module.

Homepage: http://accessibility.kde.org/developer/kttsd

%files -n trinity-kttsd
%defattr(-,root,root,-)
%{tde_bindir}/kttsd
%{tde_bindir}/kttsmgr
%{tde_tdelibdir}/kcm_kttsd.la
%{tde_tdelibdir}/kcm_kttsd.so
%{tde_tdelibdir}/tdetexteditor_kttsd.la
%{tde_tdelibdir}/tdetexteditor_kttsd.so
%if 0%{?with_akode}
%{tde_tdelibdir}/libkttsd_akodeplugin.la
%{tde_tdelibdir}/libkttsd_akodeplugin.so
%endif
%{tde_tdelibdir}/libkttsd_alsaplugin.la
%{tde_tdelibdir}/libkttsd_alsaplugin.so
%{tde_tdelibdir}/libkttsd_artsplugin.la
%{tde_tdelibdir}/libkttsd_artsplugin.so
%{tde_tdelibdir}/libkttsd_commandplugin.la
%{tde_tdelibdir}/libkttsd_commandplugin.so
%{tde_tdelibdir}/libkttsd_eposplugin.la
%{tde_tdelibdir}/libkttsd_eposplugin.so
%{tde_tdelibdir}/libkttsd_festivalintplugin.la
%{tde_tdelibdir}/libkttsd_festivalintplugin.so
%{tde_tdelibdir}/libkttsd_fliteplugin.la
%{tde_tdelibdir}/libkttsd_fliteplugin.so
%{tde_tdelibdir}/libkttsd_sbdplugin.la
%{tde_tdelibdir}/libkttsd_sbdplugin.so
%{tde_tdelibdir}/libkttsd_stringreplacerplugin.la
%{tde_tdelibdir}/libkttsd_stringreplacerplugin.so
%{tde_tdelibdir}/libkttsd_talkerchooserplugin.la
%{tde_tdelibdir}/libkttsd_talkerchooserplugin.so
%{tde_tdelibdir}/libkttsd_xmltransformerplugin.la
%{tde_tdelibdir}/libkttsd_xmltransformerplugin.so
%{tde_tdelibdir}/libkttsjobmgrpart.la
%{tde_tdelibdir}/libkttsjobmgrpart.so
%{tde_libdir}/libkttsd.so.*
%{tde_tdeappdir}/kcmkttsd.desktop
%{tde_tdeappdir}/kttsmgr.desktop
%{tde_datadir}/apps/tdetexteditor_kttsd/
%exclude %{tde_datadir}/apps/kttsd/hadifix/xslt/SSMLtoTxt2pho.xsl
%{tde_datadir}/apps/kttsd/
%{tde_datadir}/icons/hicolor/16x16/actions/female.png
%{tde_datadir}/icons/hicolor/16x16/actions/male.png
%{tde_datadir}/icons/hicolor/*/apps/kttsd.png
%{tde_datadir}/icons/hicolor/*/apps/kcmkttsd.png
%{tde_datadir}/services/tdetexteditor_kttsd.desktop
%{tde_datadir}/services/kttsd.desktop
%if 0%{?with_akode}
%{tde_datadir}/services/kttsd_akodeplugin.desktop
%endif
%{tde_datadir}/services/kttsd_alsaplugin.desktop
%{tde_datadir}/services/kttsd_artsplugin.desktop
%{tde_datadir}/services/kttsd_commandplugin.desktop
%{tde_datadir}/services/kttsd_eposplugin.desktop
%{tde_datadir}/services/kttsd_festivalintplugin.desktop
%{tde_datadir}/services/kttsd_fliteplugin.desktop
%{tde_datadir}/services/kttsd_sbdplugin.desktop
%{tde_datadir}/services/kttsd_stringreplacerplugin.desktop
%{tde_datadir}/services/kttsd_talkerchooserplugin.desktop
%{tde_datadir}/services/kttsd_xmltransformerplugin.desktop
%{tde_datadir}/services/kttsjobmgr.desktop
%{tde_datadir}/servicetypes/kttsd_audioplugin.desktop
%{tde_datadir}/servicetypes/kttsd_filterplugin.desktop
%{tde_datadir}/servicetypes/kttsd_synthplugin.desktop
%{tde_tdedocdir}/HTML/en/kttsd/
%{tde_mandir}/man1/kttsd.1*
%{tde_mandir}/man1/kttsmgr.1*

##########

%package -n trinity-kttsd-contrib-plugins
Summary:	The TDE Text-to-Speech system
Group:		System/GUI/Other
Requires:	trinity-kttsd = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kttsd-contrib-plugins
kttsd synthetizer plugins that depends on non-free software :
* FreeTTS plugin.
* Hadifix (mbrola/txt2pho) plugin.
Those plugins will require manual installation of third party,
non free software to work.

This package is part of Trinity, as a component of the TDE accessibility module.

%files -n trinity-kttsd-contrib-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/libkttsd_freettsplugin.la
%{tde_tdelibdir}/libkttsd_freettsplugin.so
%{tde_tdelibdir}/libkttsd_hadifixplugin.la
%{tde_tdelibdir}/libkttsd_hadifixplugin.so
%{tde_datadir}/apps/kttsd/hadifix/xslt/SSMLtoTxt2pho.xsl
%{tde_datadir}/services/kttsd_freettsplugin.desktop
%{tde_datadir}/services/kttsd_hadifixplugin.desktop

##########

%package devel
Summary:	Development files for tdeaccessibility
Group:		Development/Libraries/X11
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdelibs-devel >= %{version}
Requires:	%{libjpeg}-devel
Requires:	libpng-devel

Obsoletes:		trinity-kdeaccessibility-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdeaccessibility-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development file for TDE accessibility 
programs.

%files devel
%defattr(-,root,root,-)
%{tde_libdir}/libkttsd.la
%{tde_libdir}/libkttsd.so
%{tde_libdir}/libKTTSD_Lib.la
%{tde_libdir}/libKTTSD_Lib.so
%{tde_tdeincludedir}/ksayit_fxplugin.h

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

# Update icons for some control center modules
%__sed -i "kttsd/kcmkttsmgr/kcmkttsd.desktop" -e "s|^Icon=.*|Icon=kcmkttsd|"


%build
unset QTDIR QTLIB QTINC
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

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
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INCLUDE_PATH="%{tde_tdeincludedir}" \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DDOC_INSTALL_DIR="%{tde_docdir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  \
  -DBUILD_ALL=ON \
  \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Adds missing icons in 'hicolor' theme
# These icons are copied from 'crystalsvg' theme, provided by 'tdelibs'.
%__mkdir_p "%{?buildroot}%{tde_datadir}/icons/hicolor/"{16x16,22x22,32x32,48x48,64x64,128x128}"/apps/"
pushd "%{?buildroot}%{tde_datadir}/icons"
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/apps/kttsd.png  hicolor/"$i"x"$i"/apps/kttsd.png    ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/apps/kttsd.png  hicolor/"$i"x"$i"/apps/kcmkttsd.png ;done
popd

# Avoid conflict with tdelibs
%__rm -f %{?buildroot}%{tde_datadir}/icons/crystalsvg/*/apps/kttsd.png
%__rm -f %{?buildroot}%{tde_datadir}/icons/crystalsvg/scalable/apps/kttsd.svgz

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r kmag         Utility Accessibility
%suse_update_desktop_file    kmousetool   Utility Accessibility
%suse_update_desktop_file    kmouth       Utility Accessibility
%suse_update_desktop_file    kttsmgr      Utility Accessibility
%suse_update_desktop_file    ksayit       Utility Accessibility
%suse_update_desktop_file    kcmkttsd     Utility Accessibility
%endif

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"


%clean
%__rm -rf %{buildroot}


%changelog
