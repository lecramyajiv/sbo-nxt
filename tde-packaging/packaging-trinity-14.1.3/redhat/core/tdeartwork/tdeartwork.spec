#
# spec file for package tdeartwork (version R14)
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
%define tde_pkg tdeartwork
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_sbindir %{tde_prefix}/sbin
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Summary:	Additional artwork (themes, sound themes, ...) for TDE
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Group:		System/GUI/Other
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

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

Obsoletes:	trinity-kdeartwork < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeartwork = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	fdupes

BuildRequires:	gettext
BuildRequires:	libidn-devel

# ESOUND support
#BuildRequires:	esound-devel

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
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

# LIBART support
%define with_libart 1
BuildRequires:	libart_lgpl-devel

# XSCREENSAVER support
#  RHEL 4: disabled
#  RHEL 6: available in EPEL
#  RHEL 7: available in NUX
#  RHEL 8: available in EPEL
#  RHEL 9: available in EPEL
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version}
%define with_xscreensaver 1

%if 0%{?fedora} || 0%{?rhel} >= 5
BuildRequires:	libXScrnSaver-devel
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
BuildRequires:	xscreensaver-extras
%if 0%{?fedora}
BuildRequires:	xscreensaver-extras-base
%endif
BuildRequires:	xscreensaver-gl-base
BuildRequires:	xscreensaver-gl-extras
%endif

%if 0%{?suse_version}
BuildRequires:	libXScrnSaver-devel
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-data
BuildRequires:	xscreensaver-data-extra
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xscrnsaver-devel
%else
BuildRequires:	%{_lib}xscrnsaver%{?mgaversion:1}-devel
%endif
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
%if 0%{?pclinuxos} == 0
BuildRequires:	xscreensaver-extrusion
%endif
BuildRequires:	xscreensaver-gl
%endif

# Opensuse <= 13.10 does not provide 'webcollage' screensaver
%if 0%{?suse_version} == 0 || 0%{?suse_version} >= 1320
%define with_webcollage 1
%endif

%endif

# JACK support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define with_jack 1
%if 0%{?mgaversion} || 0%{?mdkversion}
%define jack_devel %{_lib}jack-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
%define jack_devel jack-audio-connection-kit-devel
%endif
%if 0%{?suse_version}
%define jack_devel libjack-devel
%endif
BuildRequires:	%{jack_devel}
%endif

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


# Metapackage
Requires: %{name}-emoticons = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-misc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-style = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-theme-icon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-theme-window = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdewallpapers = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdescreensaver = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?with_xscreensaver}
Requires: trinity-tdescreensaver-xsavers = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdescreensaver-xsavers-extra = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?with_webcollage}
Requires: trinity-tdescreensaver-xsavers-webcollage = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif


%description
TDE (the Trinity Desktop Environment) is a powerful Open Source graphical
desktop environment for Unix workstations. It combines ease of use,
contemporary functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This metapackage includes a collection of artistic extras (themes, widget
styles, screen savers, wallpaper, icons, emoticons and so on) provided
with the official release of TDE.


%files

##########

%package emoticons
Summary:	Emoticon collections for tDE chat clients
Group:		System/GUI/Other

%description emoticons
This package contains several collections of emoticons used by official
and unofficial TDE chat clients, such as Kopete and Konversation.

This package is part of TDE, and a component of the TDE artwork module.

%files emoticons
%defattr(-,root,root,-)
%{tde_datadir}/emoticons/

##########

%package misc
Summary:	Various multimedia goodies released with TDE
Group:		System/GUI/Other

%description misc
This package contains miscellaneous multimedia goodies for TDE.
Included are additional TDE sounds and kworldclock themes.

This package is part of Trinity, and a component of the TDE artwork module.

%files misc
%defattr(-,root,root,-)
%{tde_datadir}/apps/kworldclock/
%{tde_datadir}/sounds/KDE_Logout_new.wav
%{tde_datadir}/sounds/KDE_Startup_new.wav

##########

%package style
Summary:	Widget styles released with Trinity
Group:		System/GUI/Other

%description style
This package contains additional widget styles for Trinity. Widget styles
can be used to customise the look and feel of interface components such
as buttons, scrollbars and so on.  They can be applied using the style
manager in the Trinity Control Center.

This package is part of Trinity, and a component of the TDE artwork module.

%files style
%defattr(-,root,root,-)
%{tde_tdelibdir}/plugins/styles/
%{tde_tdelibdir}/tdestyle_phase_config.la
%{tde_tdelibdir}/tdestyle_phase_config.so
%{tde_datadir}/apps/tdestyle/

##########

%package theme-icon
Summary:	Icon themes released with Trinity
Group:		System/GUI/Other

Obsoletes:	trinity-kdeartwork-icons < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeartwork-icons = %{?epoch:%{epoch}:}%{version}-%{release}

%description theme-icon
This package contains additional icon themes for Trinity. Icon themes can be
used to customise the appearance of standard icons throughout TDE. They
can be applied using the icon manager in the Trinity Control Centre.

This package is part of Trinity, and a component of the TDE artwork module.

%files theme-icon
%defattr(-,root,root,-)
%{tde_datadir}/icons/ikons/
%{tde_datadir}/icons/kdeclassic/
%{tde_datadir}/icons/kids/
%{tde_datadir}/icons/slick/
%{tde_datadir}/icons/locolor/index.theme
%{tde_datadir}/icons/locolor/*/*/*.png

##########

%package theme-window
Summary:	Window decoration themes released with Trinity
Group:		System/GUI/Other

%description theme-window
This package contains additional window decoration themes for Trinity. Window
decoration themes can be used to customise the look of window borders and
buttons, and can be applied using the window decoration manager in the Trinity
Control Center.

This package is part of Trinity, and a component of the TDE artwork module.

%files theme-window
%defattr(-,root,root,-)
%{tde_tdelibdir}/twin*
%{tde_datadir}/apps/twin/

##########

%package -n trinity-tdewallpapers
Summary:	Wallpapers released with Trinity
Group:		System/GUI/Other
Obsoletes:	trinity-kdewallpapers < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewallpapers = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdewallpapers
This package contains additional wallpapers for Trinity. Wallpapers can be
applied using the background manager in the Trinity Control Center.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdewallpapers
%defattr(-,root,root,-)
%{tde_datadir}/wallpapers/*

##########

%package -n trinity-tdescreensaver
Summary:	Additional screen savers released with Trinity
Group:		System/GUI/Other

Obsoletes:	trinity-kscreensaver < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kscreensaver = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdescreensaver
This package contains the screen savers for Trinity. They can be tested and
selected within the Appearance and Themes section of the Trinity Control
Center.

The hooks for the standard xscreensavers are no longer part of this
package. To select and/or configure the standard xscreensavers through
the Trinity Control Center, install the separate package tdescreensaver-xsavers.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdescreensaver
%defattr(-,root,root,-)
%{tde_bindir}/kslideshow.kss
%{tde_bindir}/kpolygon.kss
%{tde_bindir}/krotation.kss
%{tde_bindir}/ksolarwinds.kss
%{tde_bindir}/klorenz.kss
%{tde_bindir}/kvm.kss
%{tde_bindir}/kflux.kss
%{tde_bindir}/kscience.kss
%{tde_bindir}/kbanner.kss
%{tde_bindir}/kclock.kss
%{tde_bindir}/kfiresaver.kss
%{tde_bindir}/keuphoria.kss
%{tde_bindir}/kfountain.kss
%{tde_bindir}/kgravity.kss
%{tde_bindir}/tdepartsaver.kss
%{tde_bindir}/kpendulum.kss
%{tde_bindir}/kblob.kss
%{tde_bindir}/klines.kss
%{tde_bindir}/kwave.kss
%{tde_bindir}/tdeasciiquarium.kss
%{tde_datadir}/applnk/System/ScreenSavers/KBanner.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KBlob.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KClock.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KEuphoria.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KFiresaver.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KFlux.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KFountain.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KGravity.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KLines-saver.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KLorenz.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KPendulum.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KPolygon.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KRotation.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KScience.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KSlideshow.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KSolarWinds.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KVm.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KWave.desktop
%{tde_datadir}/applnk/System/ScreenSavers/tdepartsaver.desktop
%{tde_datadir}/apps/kfiresaver/
%{tde_datadir}/apps/tdescreensaver/
%{tde_mandir}/man1/kbanner.kss.1*
%{tde_mandir}/man1/kblob.kss.1*
%{tde_mandir}/man1/kclock.kss.1*
%{tde_mandir}/man1/keuphoria.kss.1
%{tde_mandir}/man1/kfiresaver.kss.1
%{tde_mandir}/man1/kflux.kss.1
%{tde_mandir}/man1/kfountain.kss.1
%{tde_mandir}/man1/kgravity.kss.1
%{tde_mandir}/man1/klines.kss.1
%{tde_mandir}/man1/klorenz.kss.1
%{tde_mandir}/man1/kpendulum.kss.1
%{tde_mandir}/man1/kpolygon.kss.1
%{tde_mandir}/man1/krotation.kss.1
%{tde_mandir}/man1/kscience.kss.1
%{tde_mandir}/man1/kslideshow.kss.1
%{tde_mandir}/man1/ksolarwinds.kss.1
%{tde_mandir}/man1/kvm.kss.1
%{tde_mandir}/man1/kwave.kss.1
%{tde_mandir}/man1/tdeasciiquarium.kss.1
%{tde_mandir}/man1/tdepartsaver.kss.1

%if 0%{?with_xscreensaver}
%{tde_bindir}/kspace.kss
%{tde_bindir}/kswarm.kss
%{tde_datadir}/applnk/System/ScreenSavers/KSpace.desktop
%{tde_datadir}/applnk/System/ScreenSavers/KSwarm.desktop
%{tde_mandir}/man1/kspace.kss.1
%{tde_mandir}/man1/kswarm.kss.1
%endif

##########

%if 0%{?with_xscreensaver}

%package -n trinity-tdescreensaver-xsavers
Summary:	Trinity hooks for standard xscreensavers
Group:		System/GUI/Other
Requires:	trinity-tdebase-bin >= %{tde_version}
Requires:	xscreensaver

Obsoletes:	trinity-kscreensaver-xsavers < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kscreensaver-xsavers = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdescreensaver-xsavers
This package allows a smooth integration of the standard xscreensavers
into Trinity. With this package installed you can select and/or configure
the standard xscreensavers through the Appearances and Themes section of
the Trinity Control Centre.

Note that this package does not actually contain any screensavers itself.
For the additional screensavers shipped with Trinity, see the separate package
tdescreensaver-trinity. This package does depend on the xscreensaver package, and
recommend the xscreensaver-gl package, as well as contain the necessary
files to integrate these packages into Trinity.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdescreensaver-xsavers
%defattr(-,root,root,-)
%{tde_bindir}/xscreensaver-getimage-file
%{tde_bindir}/xscreensaver-getimage
%{tde_bindir}/kxsconfig
%{tde_bindir}/kxsrun
%{tde_datadir}/applnk/System/ScreenSavers/antinspect.desktop
%{tde_datadir}/applnk/System/ScreenSavers/antspotlight.desktop
%{tde_datadir}/applnk/System/ScreenSavers/atunnel.desktop
%{tde_datadir}/applnk/System/ScreenSavers/blinkbox.desktop
%{tde_datadir}/applnk/System/ScreenSavers/braid.desktop
%{tde_datadir}/applnk/System/ScreenSavers/bubble3d.desktop
%{tde_datadir}/applnk/System/ScreenSavers/circuit.desktop
%{tde_datadir}/applnk/System/ScreenSavers/cubestorm.desktop
%{tde_datadir}/applnk/System/ScreenSavers/deco.desktop
%{tde_datadir}/applnk/System/ScreenSavers/distort.desktop
%{tde_datadir}/applnk/System/ScreenSavers/endgame.desktop
%{tde_datadir}/applnk/System/ScreenSavers/engine.desktop
%{tde_datadir}/applnk/System/ScreenSavers/fiberlamp.desktop
%{tde_datadir}/applnk/System/ScreenSavers/flipflop.desktop
%{tde_datadir}/applnk/System/ScreenSavers/flipscreen3d.desktop
%{tde_datadir}/applnk/System/ScreenSavers/flyingtoasters.desktop
%{tde_datadir}/applnk/System/ScreenSavers/fuzzyflakes.desktop
%{tde_datadir}/applnk/System/ScreenSavers/galaxy.desktop
%{tde_datadir}/applnk/System/ScreenSavers/gears.desktop
%{tde_datadir}/applnk/System/ScreenSavers/gflux.desktop
%{tde_datadir}/applnk/System/ScreenSavers/glblur.desktop
%{tde_datadir}/applnk/System/ScreenSavers/gleidescope.desktop
%{tde_datadir}/applnk/System/ScreenSavers/glknots.desktop
%{tde_datadir}/applnk/System/ScreenSavers/glslideshow.desktop
%{tde_datadir}/applnk/System/ScreenSavers/glsnake.desktop
%{tde_datadir}/applnk/System/ScreenSavers/gltext.desktop
%{tde_datadir}/applnk/System/ScreenSavers/hypertorus.desktop
%{tde_datadir}/applnk/System/ScreenSavers/jigglypuff.desktop
%{tde_datadir}/applnk/System/ScreenSavers/lavalite.desktop
%{tde_datadir}/applnk/System/ScreenSavers/metaballs.desktop
%{tde_datadir}/applnk/System/ScreenSavers/mirrorblob.desktop
%{tde_datadir}/applnk/System/ScreenSavers/moebius.desktop
%{tde_datadir}/applnk/System/ScreenSavers/molecule.desktop
%{tde_datadir}/applnk/System/ScreenSavers/morph3d.desktop
%{tde_datadir}/applnk/System/ScreenSavers/penrose.desktop
%{tde_datadir}/applnk/System/ScreenSavers/pipes.desktop
%{tde_datadir}/applnk/System/ScreenSavers/polyhedra.desktop
%{tde_datadir}/applnk/System/ScreenSavers/polytopes.desktop
%{tde_datadir}/applnk/System/ScreenSavers/popsquares.desktop
%{tde_datadir}/applnk/System/ScreenSavers/pulsar.desktop
%{tde_datadir}/applnk/System/ScreenSavers/queens.desktop
%{tde_datadir}/applnk/System/ScreenSavers/ripples.desktop
%{tde_datadir}/applnk/System/ScreenSavers/shadebobs.desktop
%{tde_datadir}/applnk/System/ScreenSavers/sierpinski3d.desktop
%{tde_datadir}/applnk/System/ScreenSavers/slidescreen.desktop
%{tde_datadir}/applnk/System/ScreenSavers/sonar.desktop
%{tde_datadir}/applnk/System/ScreenSavers/spheremonics.desktop
%{tde_datadir}/applnk/System/ScreenSavers/stonerview.desktop
%{tde_datadir}/applnk/System/ScreenSavers/superquadrics.desktop
%{tde_datadir}/applnk/System/ScreenSavers/swirl.desktop
%{tde_datadir}/applnk/System/ScreenSavers/xlyap.desktop
%{tde_datadir}/applnk/System/ScreenSavers/m6502.desktop
%{tde_datadir}/applnk/System/ScreenSavers/glschool.desktop
%{tde_datadir}/applnk/System/ScreenSavers/moebiusgears.desktop
%{tde_datadir}/applnk/System/ScreenSavers/glcells.desktop
%{tde_datadir}/applnk/System/ScreenSavers/abstractile.desktop
%{tde_datadir}/applnk/System/ScreenSavers/lockward.desktop
%{tde_datadir}/applnk/System/ScreenSavers/cwaves.desktop
%{tde_datadir}/applnk/System/ScreenSavers/topblock.desktop
%{tde_datadir}/applnk/System/ScreenSavers/voronoi.desktop
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%{tde_datadir}/applnk/System/ScreenSavers/cubicgrid.desktop
%{tde_datadir}/applnk/System/ScreenSavers/hypnowheel.desktop
%{tde_datadir}/applnk/System/ScreenSavers/lcdscrub.desktop
%{tde_datadir}/applnk/System/ScreenSavers/photopile.desktop
%{tde_datadir}/applnk/System/ScreenSavers/skytentacles.desktop
%endif
%if 0%{?rhel} == 5
%{tde_datadir}/applnk/System/ScreenSavers/bubbles.desktop
%{tde_datadir}/applnk/System/ScreenSavers/critical.desktop
%{tde_datadir}/applnk/System/ScreenSavers/flag.desktop
%{tde_datadir}/applnk/System/ScreenSavers/forest.desktop
%{tde_datadir}/applnk/System/ScreenSavers/glforestfire.desktop
%{tde_datadir}/applnk/System/ScreenSavers/hyperball.desktop
%{tde_datadir}/applnk/System/ScreenSavers/hypercube.desktop
%{tde_datadir}/applnk/System/ScreenSavers/juggle.desktop
%{tde_datadir}/applnk/System/ScreenSavers/laser.desktop
%{tde_datadir}/applnk/System/ScreenSavers/lightning.desktop
%{tde_datadir}/applnk/System/ScreenSavers/lisa.desktop
%{tde_datadir}/applnk/System/ScreenSavers/lissie.desktop
%{tde_datadir}/applnk/System/ScreenSavers/lmorph.desktop
%{tde_datadir}/applnk/System/ScreenSavers/mismunch.desktop
%{tde_datadir}/applnk/System/ScreenSavers/rotor.desktop
%{tde_datadir}/applnk/System/ScreenSavers/sphere.desktop
%{tde_datadir}/applnk/System/ScreenSavers/spiral.desktop
%{tde_datadir}/applnk/System/ScreenSavers/t3d.desktop
%{tde_datadir}/applnk/System/ScreenSavers/vines.desktop
%{tde_datadir}/applnk/System/ScreenSavers/whirlygig.desktop
%{tde_datadir}/applnk/System/ScreenSavers/worm.desktop
%endif
%{tde_mandir}/man1/kxsconfig.1
%{tde_mandir}/man1/kxsrun.1

%endif

##########

%if 0%{?with_webcollage}

%package -n trinity-tdescreensaver-xsavers-webcollage
Summary:	Webcollage screensaver Trinity hook
Group:		System/GUI/Other
Requires:	trinity-tdescreensaver-xsavers-extra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	netpbm

Obsoletes:	trinity-kscreensaver-xsavers-webcollage < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kscreensaver-xsavers-webcollage = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdescreensaver-xsavers-webcollage
This package give access to the webcollage screensaver through the Trinity
screensaver configuration.

This screensaver downloads random pictures from the internet and creates
a collage as screensaver.

IMPORTANT NOTICE: The internet contains all kinds of pictures, some of which
you might find inappropriate and offensive.
You are specially discouraged to install this package if you are using 
your computer in a working environment or in an environment with children.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdescreensaver-xsavers-webcollage
%defattr(-,root,root,-)
%{tde_datadir}/applnk/System/ScreenSavers/webcollage.desktop

%endif

##########

%package -n trinity-tdescreensaver-xsavers-extra
Summary:	Trinity hooks for standard xscreensavers
Group:		System/GUI/Other
Requires:	trinity-tdescreensaver-xsavers = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kscreensaver-xsavers-extra < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kscreensaver-xsavers-extra = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdescreensaver-xsavers-extra
This package allows a smooth integration of the universe xscreensavers
into Trinity. With this package installed you can select and/or configure
the universe xscreensavers through the Appearances and Themes section of
the Trinity Control Centre.

Note that this package does not actually contain any screensavers itself.
For the additional screensavers shipped with TDE, see the separate package
tdescreensaver.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdescreensaver-xsavers-extra
%defattr(-,root,root,-)
%exclude %{tde_datadir}/applnk/System/ScreenSavers/webcollage.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/antinspect.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/antspotlight.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/atunnel.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/blinkbox.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/braid.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/bubble3d.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/circuit.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/cubestorm.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/deco.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/distort.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/endgame.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/engine.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/fiberlamp.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/flipflop.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/flipscreen3d.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/flyingtoasters.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/fuzzyflakes.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/galaxy.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/gears.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/gflux.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/glblur.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/gleidescope.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/glknots.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/glslideshow.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/glsnake.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/gltext.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/hypertorus.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/jigglypuff.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/lavalite.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/metaballs.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/mirrorblob.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/moebius.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/molecule.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/morph3d.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/penrose.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/pipes.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/polyhedra.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/polytopes.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/popsquares.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/pulsar.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/queens.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/ripples.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/shadebobs.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/sierpinski3d.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/slidescreen.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/sonar.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/spheremonics.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/stonerview.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/superquadrics.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/swirl.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/xlyap.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/m6502.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/glschool.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/moebiusgears.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/glcells.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/abstractile.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/lockward.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/cwaves.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/topblock.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/voronoi.desktop
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%exclude %{tde_datadir}/applnk/System/ScreenSavers/cubicgrid.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/hypnowheel.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/lcdscrub.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/photopile.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/skytentacles.desktop
%endif
%if 0%{?rhel} == 5
%exclude %{tde_datadir}/applnk/System/ScreenSavers/bubbles.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/critical.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/flag.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/forest.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/glforestfire.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/hyperball.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/hypercube.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/juggle.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/laser.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/lightning.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/lisa.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/lissie.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/lmorph.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/mismunch.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/rotor.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/sphere.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/spiral.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/t3d.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/vines.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/whirlygig.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/worm.desktop
%endif

%exclude %{tde_datadir}/applnk/System/ScreenSavers/KBanner.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KBlob.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KClock.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KEuphoria.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KFiresaver.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KFlux.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KFountain.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KGravity.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KLines-saver.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KLorenz.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KPendulum.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KPolygon.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KRotation.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KScience.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KSlideshow.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KSolarWinds.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KVm.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KWave.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/tdepartsaver.desktop

%exclude %{tde_datadir}/applnk/System/ScreenSavers/KSpace.desktop
%exclude %{tde_datadir}/applnk/System/ScreenSavers/KSwarm.desktop

%{tde_datadir}/applnk/System/ScreenSavers/*.desktop

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

# http://www.trinitydesktop.org/wiki/bin/view/Developers/HowToBuild
# NOTE: Before building tdeartwork, install any and all xhack screensavers that might be uses, then:
cd tdescreensaver/kxsconfig/
./update_hacks.sh


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
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  %{!?with_xscreensaver:-DWITH_XSCREENSAVER=OFF} \
  %{!?with_libart:-DWITH_LIBART=OFF} \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_ARTS=ON \
  -DWITH_LIBART=ON \
  -DWITH_OPENGL=ON \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf "%{buildroot}"
%__make install -C build DESTDIR="%{buildroot}"

# Should not be here if xscreensaver is disabled
%if 0%{?with_xscreensaver} == 0
%__rm -f "%{?buildroot}%{tde_bindir}/xscreensaver-getimage"
%__rm -f "%{?buildroot}%{tde_bindir}/xscreensaver-getimage-file"
%endif

# Duplicate with trinity-kbabel (from tdesdk)
%__rm -f "%{?buildroot}%{tde_datadir}/icons/locolor/16x16/apps/kbabel.png"
%__rm -f "%{?buildroot}%{tde_datadir}/icons/locolor/32x32/apps/kbabel.png"

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"

# Fix invalid permissions
%if 0%{?with_xscreensaver}
chmod +x "%{?buildroot}%{tde_bindir}/xscreensaver-getimage"
chmod +x "%{?buildroot}%{tde_bindir}/xscreensaver-getimage-file"
%endif


%clean
%__rm -rf %{buildroot}


%changelog
