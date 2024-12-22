#
# spec file for package trinity-filesystem (version R14)
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
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define _docdir %{tde_docdir}
%define tde_docdir %{tde_datadir}/doc
%define tde_mandir %{tde_datadir}/man
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_includedir %{tde_prefix}/include
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-filesystem
Version:	%{tde_version}
Release:	1%{?dist}
Summary:	Trinity Directory Layout
Group:		System/Fhs
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch


%description
This package installs the Trinity directory structure.


%files
%defattr(-,root,root,-)
%dir %{tde_prefix}

%dir %{tde_bindir}

%dir %{tde_datadir}
%dir %{tde_confdir}/magic

%dir %{tde_docdir}
%dir %{tde_tdedocdir}
%dir %{tde_tdedocdir}/HTML
%dir %{tde_tdedocdir}/HTML/*
%dir %{tde_tdedocdir}/HTML/*/common

%dir %{tde_includedir}
%dir %{tde_tdeincludedir}

%dir %{tde_libdir}
%dir %{tde_libdir}/java
%dir %{tde_libdir}/jni
%dir %{tde_libdir}/pkgconfig
%dir %{tde_tdelibdir}

%dir %{tde_datadir}/applications
%dir %{tde_datadir}/applications/tde
%dir %{tde_datadir}/applnk
%dir %{tde_datadir}/applnk/.hidden
%dir %{tde_datadir}/applnk/*
%dir %{tde_datadir}/applnk/*/*
%dir %{tde_datadir}/apps
%dir %{tde_datadir}/apps/*
%dir %{tde_datadir}/apps/*/*
%dir %{tde_datadir}/cmake
%dir %{tde_datadir}/config.kcfg
%dir %{tde_datadir}/autostart
%dir %{tde_datadir}/emoticons
%dir %{tde_datadir}/icons
%dir %{tde_datadir}/icons/crystalsvg
%dir %{tde_datadir}/icons/crystalsvg/*
%dir %{tde_datadir}/icons/crystalsvg/*/*
%dir %{tde_datadir}/icons/hicolor
%dir %{tde_datadir}/icons/hicolor/*
%dir %{tde_datadir}/icons/hicolor/*/*
%dir %{tde_datadir}/icons/locolor
%dir %{tde_datadir}/icons/locolor/*
%dir %{tde_datadir}/icons/locolor/*/*
%dir %{tde_datadir}/locale
%dir %{tde_datadir}/locale/*
%dir %{tde_datadir}/locale/*/*
%dir %{tde_datadir}/man
%dir %{tde_datadir}/man/*
%dir %{tde_datadir}/mime
%dir %{tde_datadir}/mime/*
%dir %{tde_datadir}/mimelnk
%dir %{tde_datadir}/mimelnk/*
%dir %{tde_datadir}/services
%dir %{tde_datadir}/services/*
%dir %{tde_datadir}/servicetypes
%dir %{tde_datadir}/tdestyle
%dir %{tde_datadir}/tdestyle/*
%dir %{tde_datadir}/X11
%dir %{tde_datadir}/X11/xkb
%dir %{tde_datadir}/X11/xkb/symbols

%dir %{tde_datadir}/wallpapers


%dir %{_sysconfdir}/trinity
%dir %{_sysconfdir}/xdg/menus

##########

%prep

%build

%install
%__install -d -m 755 %{?buildroot}%{tde_prefix}

%__install -d -m 755 %{?buildroot}%{tde_bindir}

%__install -d -m 755 %{?buildroot}%{tde_datadir}
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applications
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applications/tde
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/.hidden
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Applications
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Development
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Edutainment
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Edutainment/Languages
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Edutainment/Mathematics
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Edutainment/Miscellaneous
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Edutainment/Science
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Edutainment/Tools
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Games
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Games/Board
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Graphics
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Internet
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Multimedia
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Office
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Settings
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Settings/LookNFeel
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Settings/WebBrowsing
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/System
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/System/ScreenSavers
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Toys
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk/Utilities
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/plugin
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/profiles
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/remotes
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/remoteview
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/tdedisplay
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/tdedisplay/color-schemes
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/videothumbnail
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps/zeroconf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/autostart
%__install -d -m 755 %{?buildroot}%{tde_datadir}/cmake
%__install -d -m 755 %{?buildroot}%{tde_confdir}
%__install -d -m 755 %{?buildroot}%{tde_confdir}/magic
%__install -d -m 755 %{?buildroot}%{tde_datadir}/config.kcfg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/emoticons
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man1
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man2
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man3
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man4
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man5
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man6
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man7
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man8
%__install -d -m 755 %{?buildroot}%{tde_datadir}/man/man9
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mime
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mime/packages
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/all
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/application
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/audio
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/fonts
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/image
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/interface
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/inode
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/media
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/message
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/model
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/multipart
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/print
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/text
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/uri
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk/video
%__install -d -m 755 %{?buildroot}%{tde_datadir}/services
%__install -d -m 755 %{?buildroot}%{tde_datadir}/services/tdeconfiguredialog
%__install -d -m 755 %{?buildroot}%{tde_datadir}/servicetypes
%__install -d -m 755 %{?buildroot}%{tde_datadir}/tdestyle
%__install -d -m 755 %{?buildroot}%{tde_datadir}/tdestyle/themes
%__install -d -m 755 %{?buildroot}%{tde_datadir}/X11/xkb/symbols

%__install -d -m 755 %{?buildroot}%{tde_datadir}/wallpapers

# Create icons directories
%__install -d -m 755 %{?buildroot}%{tde_datadir}/icons
for t in crystalsvg hicolor locolor ; do
  %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}"
  %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/scalable"
  for i in {16,22,32,48,64,128,256} ; do
    %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/${i}x${i}"
  done

  # Create subdirectories
  for r in actions apps categories devices mimetypes places ; do
    %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/scalable/${r}"
    for i in {16,22,32,48,64,128} ; do
      %__install -d -m 755 "%{?buildroot}%{tde_datadir}/icons/${t}/${i}x${i}/${r}"
    done
  done
done

%__install -d -m 755 %{?buildroot}%{tde_docdir}
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}

# HTML directories
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/ca/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/cs/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/da/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/de/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/en/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/en_GB/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/es/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/et/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/fi/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/fr/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/gl/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/he/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/hu/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/it/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/ja/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/nl/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/pl/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/pt_BR/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/pt/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/ro/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/ru/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/sk/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/sl/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/sr/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/sr@Latn/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/sv/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/tr/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/uk/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/zh_CN/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/zh_Hans/common
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/zh_TW/common

%__install -d -m 755 %{?buildroot}%{tde_includedir}
%__install -d -m 755 %{?buildroot}%{tde_tdeincludedir}

%__install -d -m 755 %{?buildroot}%{tde_libdir}
%__install -d -m 755 %{?buildroot}%{tde_libdir}/java
%__install -d -m 755 %{?buildroot}%{tde_libdir}/jni
%__install -d -m 755 %{?buildroot}%{tde_libdir}/pkgconfig
%__install -d -m 755 %{?buildroot}%{tde_tdelibdir}

%__install -d -m 755 %{?buildroot}%{_sysconfdir}/trinity
%__install -d -m 755 %{?buildroot}%{_sysconfdir}/xdg/menus

# Locales directories
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/en_US
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/C
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ad
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ae
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/af
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ag
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ai
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/al
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/am
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/an
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ao
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ar
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/as
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/at
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/au
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/aw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ax
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/az
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ba
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/be
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/br
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/braille
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bs
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/by
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/bz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ca
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ch
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ci
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ck
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/co
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cx
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/cz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/de
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/do
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/dz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ec
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ee
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/eg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/eh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/eo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/er
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/es
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/et
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/fr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ga
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ge
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gq
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/gy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ht
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/hu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/id
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ie
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/il
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/in
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/iq
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ir
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/is
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/it
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/jm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/jo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/jp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/jv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ke
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ki
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/km
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ky
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/kz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/la
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/li
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ls
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/lv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ly
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ma
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/md
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/me
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ml
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mo
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mq
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ms
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mx
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/my
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/mz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/na
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ne
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ng
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ni
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/no
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/np
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/nz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/om
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pa
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pe
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ph
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pl
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ps
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/pw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/py
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/qa
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ro
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/rs
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ru
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/rw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sa
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sb
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sd
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/se
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sh
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/si
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/so
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/st
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/sz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/td
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/th
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tj
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/to
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tp
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tr
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tt
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tv
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tw
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/tz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ua
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ug
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/us
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/uy
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/uz
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/va
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vc
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ve
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vi
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vn
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/vu
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/wf
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ws
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/ye
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/za
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/zm
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/l10n/zw

# Directories for LC_MESSAGES (from *-i18n packages)
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/af/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ar/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/az/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/be/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/bg/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/bn/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/br/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/bs/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ca/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ca@valencia/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/cs/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/csb/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/cy/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/da/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/de/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/du/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ee/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/el/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/en/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/en_GB/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/en_US/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/eo/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/es/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/es_AR/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/et/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/eu/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/fa/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/fi/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/fo/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/fr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/fy/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ga/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/gl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/gu/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/he/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/hi/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/hr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/hu/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/id/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/is/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/it/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ja/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ka/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/kk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/km/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ko/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ku/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/lo/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/lt/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/lv/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/mk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/mr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ms/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/mt/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/nb/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/nds/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ne/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/nl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/nn/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/nso/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/pa/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/pl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/pl_PL/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/pl-utf/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/pt/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/pt_PT/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/pt_BR/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ro/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ru/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/rw/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/se/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/si/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sl_SI/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sq/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sr@latin/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sr@Latn/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ss/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/sv/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ta/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/tg/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/th/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/tr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ug/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/uk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/uk@cyrillic/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/uz/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/uz@cyrillic/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ve/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/ven/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/vi/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/wa/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/xh/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/xx/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/zh_CN.GB2312/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/zh_CN/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/zh_Hans/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/zh_TW.Big5/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/zh_TW/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale/zu/LC_MESSAGES/

%post
%if 0%{?suse_version}
# Add setuid files in '/etc/permissions.local'
for b in kcheckpass kgrantpty kpac_dhcp_helper kppp start_tdeinit tdmtsak tdekbdledsync ; do
  if ! grep -q "^%{tde_bindir}/${b}" "/etc/permissions.local"; then
    echo "%{tde_bindir}/${b}          root:root       4711" >>/etc/permissions.local
  fi
done
for b in fileshareset ; do
  if ! grep -q "^%{_bindir}/${b}" "/etc/permissions.local"; then
    echo "%{_bindir}/${b}          root:root       4711" >>/etc/permissions.local
  fi
done
%endif


%changelog
