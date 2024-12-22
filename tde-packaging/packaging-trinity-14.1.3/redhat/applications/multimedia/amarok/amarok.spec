#
# spec file for package amarok (version R14)
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
%define tde_pkg amarok
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
Version:	1.4.10
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Media player for TDE
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/
#Url:		http://amarok.kde.org

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
BuildRequires:	trinity-konqueror-devel >= %{tde_version}

BuildRequires:	trinity-filesystem >= %{tde_version}
Requires:		trinity-filesystem >= %{tde_version}

BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	gettext

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# ALSA supportl
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}asound-devel
%else
BuildRequires: alsa-lib-devel
%endif

# ESOUND support
#BuildRequires:	esound-devel

# PCRE support
BuildRequires:	pcre-devel

# LIBTOOL
BuildRequires:	libtool
%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires:	libtool-ltdl-devel
%endif

%if 0%{?fedora} >= 37
BuildRequires:	libusb1-devel
BuildRequires:	libusb-compat-0.1-devel
%else
BuildRequires:	libusb-devel
%endif
BuildRequires:	mysql-devel
BuildRequires:	taglib-devel

# SDL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}SDL-devel
%else
BuildRequires:	SDL-devel
%endif

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

# not used anymore, in favor of libvisual ? -- Rex
#{?fedora:BuildRequires:  xmms-devel}

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# DBUS support
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%else
BuildRequires:	dbus-devel
%endif

# DBUS-(T)QT support
%if 0%{?rhel} == 4
BuildRequires:	dbus-qt
%else
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63
%endif

# DAAP support
%define with_daap 0

# IFP support
#  IFP package is broken under PCLinuxOS.
%if 0%{?pclinuxos} == 0
%if ( 0%{?fedora} && 0%{?fedora} <= 40 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_ifp 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ifp-devel
%else
BuildRequires:	libifp-devel
%endif
%endif
%endif

# KARMA support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos} == 0 && 0%{?mdkver} < 5000000
%define with_karma 1
BuildRequires:	libkarma-devel
BuildRequires:	karma-sharp
%endif
%endif

# GPOD (ipod) support
%if 0%{?rhel} == 6 || 0%{?rhel} == 7 || 0%{?rhel} == 8 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_gpod 1
BuildRequires:	libgpod-devel >= 0.4.2
%endif

# MTP players
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_mtp 1
%if 0%{?mdkver}
BuildRequires:	%{_lib}mtp-devel
%else
BuildRequires:	libmtp-devel
%endif
%endif

# Creative Nomad Jukebox
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} >= 1220
%define with_njb 1
%if 0%{?mdkver}
BuildRequires:	%{_lib}njb-devel
%else
BuildRequires:	libmtp-devel
%endif
%endif

# VISUAL support
%if 0%{?rhel} >= 4 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_libvisual 1
%if 0%{?mdkver}
BuildRequires:	%{_lib}visual-devel
%else
BuildRequires:	libvisual-devel
%endif
%endif

# MUSICBRAINZ support
%if 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version}
%if 0%{?fedora} >= 24
BuildRequires:	libmusicbrainz5-devel
%else
%if 0%{?mgaversion} >= 9
BuildRequires:	%{_lib}musicbrainz5-devel
%else
BuildRequires:	libmusicbrainz-devel
%endif
%endif
%endif

# TUNEPIMP support
%if 0%{?pclinuxos}
BuildRequires:	libofa-devel
%endif
%if 0%{?mgaversion} && 0%{?mgaversion} <= 2
BuildRequires:	libtunepimp-devel
%endif
%if 0%{?suse_version} && 0%{?suse_version} != 1330 && 0%{?suse_version} < 1500
BuildRequires:	libtunepimp-devel
%endif
%if 0%{?fedora} && 0%{?fedora} <= 23
BuildRequires:	libtunepimp-devel
%endif

# INOTIFY support
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_inotify 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}inotifytools-devel
%endif
%endif

# XINE support
%if 0%{?fedora} && 0%{?fedora} <= 31
%define with_xine 1
BuildRequires: xine-lib-devel
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
#define with_xine 1
BuildRequires: xine-lib-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define with_xine 1
%if 0%{?mdkver} >= 5000000
BuildRequires: %{_lib}xine-devel
%else
BuildRequires: %{_lib}xine1.2-devel
%endif
%endif
%if 0%{?sle_version} && 0%{?sle_version} <= 150000
%define with_xine 1
BuildRequires: libxine-devel
%endif

# YAUAP support
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_yauap 1
%endif

# AKODE support
%define with_akode 0
%if 0 && 0%{?with_akode}
BuildRequires:	trinity-akode-devel
%endif

# ruby
BuildRequires:	ruby
BuildRequires:	ruby-devel
%if 0%{?fedora} >= 19
BuildRequires:	rubypick
%endif

# PYTHON support
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

# To open the selected browser, works with Patch2
Requires:		xdg-utils
Requires(post): xdg-utils
Requires(postun): xdg-utils


%description
Amarok is a multimedia player with:
 - fresh playlist concept, very fast to use, with drag and drop
 - plays all formats supported by the various engines
 - audio effects, like reverb and compressor
 - compatible with the .m3u and .pls formats for playlists
 - nice GUI, integrates into the TDE look, but with a unique touch

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog README.md
%{tde_bindir}/amarok
%{tde_bindir}/amarokapp
%{tde_bindir}/amarokcollectionscanner
%{tde_bindir}/amarok_proxy.rb
%{tde_datadir}/apps/amarok/
%{tde_datadir}/icons/crystalsvg/*/actions/covermanager.png
%{tde_datadir}/icons/crystalsvg/*/actions/dynamic.png
%{tde_datadir}/icons/crystalsvg/*/actions/equalizer.png
%{tde_datadir}/icons/crystalsvg/*/actions/mini_dock.png
%{tde_datadir}/icons/crystalsvg/*/actions/player_playlist_2.png
%{tde_datadir}/icons/crystalsvg/*/actions/podcast.png
%{tde_datadir}/icons/crystalsvg/*/actions/podcast_new.png
%{tde_datadir}/icons/crystalsvg/*/actions/random.png
%{tde_datadir}/icons/crystalsvg/*/actions/repeat_playlist.png
%{tde_datadir}/icons/crystalsvg/*/actions/repeat_track.png
%{tde_datadir}/icons/crystalsvg/*/actions/visualizations.png
%{tde_datadir}/icons/crystalsvg/*/actions/wiki.png
%{tde_datadir}/icons/crystalsvg/*/actions/amarok_podcast.png
%{tde_datadir}/icons/crystalsvg/*/actions/amarok_podcast_new.png
%{tde_datadir}/icons/crystalsvg/*/actions/amazon_locale.png
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_tdeappdir}/*.desktop
%{tde_datadir}/servicetypes/*.desktop
%{tde_datadir}/apps/profiles/amarok.profile.xml
%config(noreplace) %{tde_confdir}/amarokrc
%{tde_datadir}/config.kcfg/*.kcfg
%{tde_datadir}/services/amarokitpc.protocol
%{tde_datadir}/services/amaroklastfm.protocol
%{tde_datadir}/services/amarokpcast.protocol
%{tde_mandir}/man1/amarok.1*
%{tde_mandir}/man1/amarokapp.1*
%{tde_mandir}/man1/amarokcollectionscanner.1*
# -libs ?  -- Rex
%{tde_libdir}/libamarok.so.0
%{tde_libdir}/libamarok.so.0.0.0
# DAAP
%if 0%{?with_daap}
%{tde_bindir}/amarok_daapserver.rb
%{tde_tdelibdir}/libamarok_daap-mediadevice.*
%{tde_datadir}/services/amarok_daap-mediadevice.desktop
%endif
# Mass-storage
%{tde_datadir}/services/amarok_massstorage-device.desktop
%{tde_tdelibdir}/libamarok_massstorage-device.*
# NFS
%{tde_datadir}/services/amarok_nfs-device.desktop
%{tde_tdelibdir}/libamarok_nfs-device.*
# SMB
%{tde_datadir}/services/amarok_smb-device.desktop
%{tde_tdelibdir}/libamarok_smb-device.*
# IPod
%if 0%{?with_gpod}
%{tde_datadir}/services/amarok_ipod-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ipod-mediadevice.*
%endif
# VFAT
%{tde_datadir}/services/amarok_generic-mediadevice.desktop
%{tde_tdelibdir}/libamarok_generic-mediadevice.*
# iRiver
%if 0%{?with_ifp}
%{tde_datadir}/services/amarok_ifp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ifp-mediadevice.*
%endif
# Creative Zen
%if 0%{?with_njb}
%{tde_datadir}/services/amarok_njb-mediadevice.desktop
%{tde_tdelibdir}/libamarok_njb-mediadevice.*
%endif
# MTP players
%if 0%{?with_mtp}
%{tde_datadir}/services/amarok_mtp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_mtp-mediadevice.*
%endif
# Rio Karma
%if 0%{?with_karma}
%{tde_datadir}/services/amarok_riokarma-mediadevice.desktop
%{tde_tdelibdir}/libamarok_riokarma-mediadevice.*
%endif
# Void engine (noop)
%{tde_datadir}/services/amarok_void-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_void-engine_plugin.*
# Xine engine
%if 0%{?with_xine}
%{tde_datadir}/services/amarok_xine-engine.desktop
%{tde_tdelibdir}/libamarok_xine-engine.*
%endif
## Gstreamer engine
#{tde_datadir}/services/amarok_gst10engine_plugin.desktop
#{tde_tdelibdir}/libamarok_gst10engine_plugin.*
# YAUAP
%if 0%{?with_yauap}
%{tde_datadir}/services/amarok_yauap-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_yauap-engine_plugin.*
%endif
# AKODE
%if 0 && 0%{?with_akode}
%{tde_datadir}/services/amarok_aKode-engine.desktop
%{tde_tdelibdir}/libamarok_aKode-engine.*
%endif

##########

%package konqueror
Summary:		Amarok konqueror (service menus, sidebar) support
Group:			Applications/Multimedia

Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-konqueror

%description konqueror
%{summary}.

%files konqueror
%defattr(-,root,root,-)
%{tde_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_tdelibdir}/konqsidebar_universalamarok.*
%{tde_datadir}/apps/konqsidebartng/*/amarok_konquisidebar.desktop


##########

%if 0%{?with_libvisual}

%package visualisation
Summary:		Visualisation plugins for Amarok
Group:			Applications/Multimedia
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# No plugins by default, we need libvisual-plugins
#Requires:   libvisual-plugins

%description visualisation
Amarok can use visualisation plugins from different origins.
Right now, only xmms is supported, which means that you can
use any of xmms' visualisation plugins with Amarok.

%files visualisation
%defattr(-,root,root,-)
%{tde_bindir}/amarok_libvisual
%{tde_mandir}/man1/amarok_libvisual.1*

%endif

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Fix some Ruby stuff
if ! ruby -rrbconfig -e "puts Config.expand( Config::MAKEFILE_CONFIG['MAJOR'] )" &>/dev/null; then
  %__sed -i "amarok/src/mediadevice/daap/ConfigureChecks.cmake" \
         -e "s|Config::|RbConfig::|g" \
         -e "s|Config\.|RbConfig\.|g"
fi

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?mgaversion} >= 8
%__sed -i "amarok/src/scripts/common/Publisher.py" \
          "amarok/src/scripts/common/Zeroconf.py" \
          "amarok/src/scripts/playlist2html/Playlist.py" \
          "amarok/src/scripts/playlist2html/playlist2html.py" \
          "amarok/src/scripts/playlist2html/PlaylistServer.py" \
          "amarok/src/scripts/webcontrol/Playlist.py" \
          "amarok/src/scripts/webcontrol/RequestHandler.py" \
          "amarok/src/scripts/webcontrol/WebControl.py" \
  -e "s|/usr/bin/env python|/usr/bin/env %{python}|"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

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
  %{?with_libvisual:-DWITH_LIBVISUAL=ON} \
  -DWITH_KONQSIDEBAR=ON \
  %{?with_xine:-DWITH_XINE=ON} %{?!with_xine:-DWITH_XINE=OFF}\
  %{?with_yauap:-DWITH_YAUAP=ON} \
  -DWITH_AKODE=OFF \
  %{?with_gpod:-DWITH_IPOD=ON} \
  %{?with_ifp:-DWITH_IFP=ON} \
  %{?with_njb:-DWITH_NJB=ON} \
  %{?with_mtp:-DWITH_MTP=ON} \
  %{?with_karma:-DWITH_RIOKARMA=ON} \
  %{!?with_daap:-DWITH_DAAP=OFF} \
  %{?with_inotify:-DWITH_INOTIFY=ON} \
  -DWITH_SYSTEM_SQLITE=ON \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -fr $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT -C build


# unpackaged files
%__rm -f $RPM_BUILD_ROOT%{tde_libdir}/lib*.la
# Removes '.so' to avoid automatic -devel dependency
%__rm -f $RPM_BUILD_ROOT%{tde_libdir}/libamarok.so

# Locales
%find_lang %{tde_pkg}

# HTML
for lang_dir in $RPM_BUILD_ROOT%{tde_tdedocdir}/HTML/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    [ "$lang" == "en" ] && d=en/amarok || d=$lang
    echo "%lang($lang) %doc %{tde_tdedocdir}/HTML/$d" >> amarok.lang
  fi
done



%clean
%__rm -fr $RPM_BUILD_ROOT


%changelog
