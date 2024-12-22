#
# spec file for package tdebase (version 3.5.13)
#
# copyright (c) 2011 the Trinity Project
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
# Please submit bugfixes or comments to http://bugs.trinitydesktop.org/

# norootforbuild

Name:           tdebase
BuildRequires:  OpenEXR-devel cups-devel db-devel doxygen graphviz tdelibs-devel krb5-devel libsmbclient-devel mDNSResponder-devel openldap2 openldap2-devel openmotif openmotif-devel openslp-devel openssh pam-devel pcsc-lite-devel qt3-devel-doc samba-client utempter xorg-x11
BuildRequires:  libtqt4-devel tde-filesystem cmake xorg-x11-libfontenc-devel
BuildRequires:  liblazy-devel 
BuildRequires:  libusb-compat-devel
BuildRequires:  fdupes libbz2-devel
BuildRequires:  libsensors4-devel
%define qt_path    /usr/lib/qt3
%define kde_path   %{_tde_prefix}
Provides:       windowmanager kfontinst kdebase3-konqueror kdebase3-khotkeys
Obsoletes:      kfontinst kdebase3-konqueror kdebase3-khotkeys
Requires:       tdelibs >= %( echo `rpm -q --queryformat '%{VERSION}' tdelibs`)
Requires:       xorg-x11 misc-console-font
Recommends:     tdelibs_doc
Recommends:     gdb
PreReq:         fileshareset
%define	fileshare_prefix	%{_prefix}
PreReq:         /bin/sh fileutils permissions
License:        GPLv2+
Group:          System/GUI/TDE
Summary:        The Trinity Desktop Core Components
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            http://www.trinitydesktop.org/
Version:        3.5.13
Release:        1
Requires:       %{name}-runtime == %{version}
Source0:        tdebase-%{version}.tar.bz2
Source1:        baselibs.conf
Source3:        startkde.suse.sh
Source4:        tdebase.fillup
Source6:        ksysguardd.init
# we append this file for older dist verions
Source8:        mp3-info.tar.bz2
Source9:        wizard_small.png
# kicker gets messed up, if it got deinstalled
Source11:       kickerrc
# from HEAD/3.2:
Source12:       console8x16.pcf.gz
Source13:       fileshareset2.tar.bz2
Source914:      kdm-pam-np-legacy
Source15:       ksysguardd.reg
Source16:       stopkde.suse.sh
Source17:       zh_TW.flag.png
Source18:       fileshareset.8.gz
Source19:       kcheckpass.8.gz
Source20:       kickoff-data.tar.bz2
Source21:       kcheckpass-pam-11.1
Source921:      kcheckpass-pam-11.0
Source9921:     kcheckpass-pam-legacy
Source22:       bnc.desktop
Source23:       sourceforge.desktop
Source24:       devmon-automounter.sh
Patch0:         3_5_BRANCH.diff
Patch3:         startkde.diff
Patch5:         media-iPod.diff
Patch6:         ksysguardd-openslp.diff
Patch7:         fix-kio-smb-auth.diff
Patch8:         konsole_keytab.diff
Patch10:        kdesud-security.diff
Patch11:        clock-applet-style.diff
Patch12:        dont-always-start-kaccess.diff
Patch14:        autorun.patch
Patch15:        artwork.diff
# TODO
Patch16:        kfontinst.diff
Patch17:        nsplugin-Preference.diff
Patch20:        ksplashml.patch
Patch21:        media_suse.diff
Patch22:        libkonq-kdemm.diff
Patch39:        kdesktop_icons.diff
Patch40:        suse_default_move.diff
Patch44:        clock-suse-integrate.diff
Patch45:        klipperrc.diff
Patch46:        lock-xvkbd.diff
Patch51:        kcontrol.diff
Patch60:        short-menus.diff
# from http://fred.hexbox.de/kde_patches/kmenu-search-fs20050503.diff 
Patch61:        kmenu-search-fs20050503-fixed.diff
Patch62:        fix-kcontrol-yast.diff
Patch63:        quick_browser_menu.diff
Patch64:        default_fonts.diff
#kdm
Patch69:        kdm-cope-with-new-grub.diff
Patch70:        kdm-aliasing.diff
Patch71:        kdm-mark_autologin.diff
Patch72:        kdm-all-users-nopass.diff
Patch74:        kdm-sysconfig-values.diff
# svn diff $BASE/branches/KDE/3.5/kdebase/kdm@599257 $BASE/branches/work/coolos_kdm | sed -e "s,^+++ ,+++ kdm/,"
Patch75:        kdm-make_it_cool.diff
Patch76:        kdm-admin-mode.diff
Patch77:        kdm-suspend-hal.diff
Patch78:        kdm-relaxed-auth.diff
Patch79:        kdm-wordbreak.diff
Patch80:        non-fast-malloc.diff
Patch81:        ksmserver-defaulttohalt.diff
Patch82:        fix-lockup-from-gnome-apps.diff
Patch83:        ksmserver-suspend.diff
Patch84:        default-kdeprintfax.diff
Patch85:        ksmserver-tooltips.diff
Patch88:        hide-only-showin-entries.diff
Patch92:        kcminit-ignore-arts.diff
Patch94:        mach_blass.diff
Patch96:        khelpcenter-gnome-support.patch
Patch996:       khelpcenter-gnome-support-legacy.patch
Patch98:        workaround-pdf-on64bit-nsplugin-bug.diff
Patch99:        xcursor.diff
Patch100:       ksysguard-slp-ratelimit.diff
Patch104:       locale-dont-show-flag.diff
Patch105:       kscreensaver-random-NG.diff
Patch111:       fix_default_theme_reset.diff
Patch114:       improve-panelservicemenu-geticonset.diff
Patch116:       teach-minicli-lock.diff
Patch117:       access.diff
Patch120:       kmenu-search-slowdown-fix.diff
Patch123:       less_verbal_kdesu.patch
Patch125:       kicker-defaults.diff
Patch126:       kdebase_khc_rellinks.diff
Patch127:       khelpcenter-use-suseconfig-indexer.diff
Patch131:       background_default.diff
Patch141:       khelpcenter-use-susehelp.diff
Patch144:       make-wallpapers-hideable.diff
Patch145:       kdebase_networkstatus_branch.diff
Patch149:       kdeeject.diff
Patch155:       use-full-hinting-by-default.diff
Patch156:       kcmshell_use_kde-sound.diff
Patch157:       kcmsamba_log.diff
Patch160:       khelpcenter-localindices.patch
Patch161:       applet-lock-logout.diff
# svn diff $BASE/branches/KDE/3.5/kdebase/kicker@849788 $BASE/branches/work/suse_kickoff_qstyle/kicker | clean_patch
Patch162:       kickoff.diff
Patch1629:      kickoff-beagle.diff
# svn diff $BASE/branches/KDE/3.5/kdebase/kcontrol/kicker@755866 $BASE/branches/work/suse_kickoff_qstyle/kcontrol/kicker
Patch158:       kickoff-kcm.diff
# svn diff -r 551296:HEAD khelpcenter
Patch159:       khelpcenter-beagle.diff
Patch163:       xinerama.patch
Patch165:       optional-compmgr.diff
Patch166:       lowdiskspace.patch
Patch167:       ksmserver-timed.diff
Patch169:       systray_order.diff
Patch170:       khotkeys-multimedia-action.diff
Patch171:       khotkeys-multimedia-action2.diff
Patch172:       select-wm-gui.diff
Patch173:       suspend-unmount.diff
Patch174:       ksmserver-kdeinit.diff
Patch177:       kio-media-errorhandling.diff
Patch179:       restore-description-parens.diff
Patch180:       kompmgr_use_defaults.diff
Patch189:       runupdater.patch
Patch190:       kcontrol-energy.diff
Patch195:       ioslaveinfo-icon.diff
Patch197:       rotate-wacom-pointers.diff
Patch198:       konsole-schema-update.diff
Patch199:       media-cryptosupport.diff
Patch200:       kdm-use-rpmoptflags.diff
Patch203:       show-konqueror-in-menu.diff
Patch204:       fix-desktop-icons.diff
Patch205:       kcmkdm-default-grub.diff
Patch206:       simplify-randr-settings.diff
Patch207:       spellcheck-default-utf8.diff
Patch208:       kdm-audit-log.diff
Patch209:       kwinbindings.diff
Patch211:       konq-combo-editor.diff
Patch212:       minicli-combo-editor.diff
Patch214:       kdm-color-scheme.diff
Patch215:       kdm-consolekit.diff
Patch216:       krandr-0.5.2.1.diff.bz2
Patch217:       kickoff-install-software.diff
Patch218:       kdm-align-userlist-labels.diff
Patch219:       kxkb-include-latin-layout.diff
Patch220:       mediamanager-mount-point-utf8.diff
Patch222:       khelpcenter-delayed-indexcheck.cpp
Patch225:       system-folder_man.diff
Patch227:       arts-start-on-demand.diff
Patch228:       media-teardown_crypto.diff
Patch229:       beagle-0.3.diff
Patch230:       remove-beagle-stuff.diff
Patch231:       kde3-session.diff
Patch232:       kde3-session-restore.diff
Patch233:       uninit.diff
Patch234:       kpamgreeter.diff
Patch235:       use-pam-before-classic.diff
Patch236:       kdesu-remember-keep-password.diff
Patch237:       suspend-kpowersave.diff
Patch238:       knetattach-show.diff
Patch239:       gcc44.diff
Patch240:       bnc584223.diff
Patch241:       openssl1.patch
Patch242:       nsplugin-init-gtk.diff
Patch243:       taskbar.patch
Patch244:       mtab-reenable.patch

%description
This package contains tdebase, one of the basic packages of the Trinity Desktop Environment. It contains, among others, kwin (the window
manager), Konqueror (the Web browser), and KControl (the
configuration program)

This package is needed if you want to use the Trinity Desktop. It is not
needed if you only want to start some Trinity applications.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package -n misc-console-font
License:        GPLv2+
Group:          System/GUI/TDE
Summary:        A font for terminal usage

%description -n misc-console-font
This package contains the Misc Console font as shipped with KDE.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package runtime
License:        GPLv2+
Summary:        Runtime Dependencies of Trinity Applications
Group:          System/GUI/TDE
Provides:       kio_fish
Obsoletes:      kio_fish
Provides:       tdebase:%{_tde_libdir}/libkonq.so.4

%description runtime
This package contains runtime dependencies of Trinity applications like
KIO-slaves.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package workspace
License:        GPLv2+
Summary:        Workspace Components of Trinity Desktop
Group:          System/GUI/TDE
Requires:       %{name} == %{version}
Provides:       tdebase:%{_tde_bindir}/kicker
Recommends:     %{name}-ksysguardd == %{version}

%description workspace
This package contains the wrkspace components of kdebase3 like
kdesktop, kicker and kwin.


Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package apps
License:        GPLv2+
Summary:        Trinity's Major Applications
Group:          System/GUI/TDE
Requires:       %{name} == %{version}
Provides:       %{name}:%{_tde_bindir}/konsole

%description apps
This package contains the major applications kdebase3 like
Kate, Konqueror and KWrite.


Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package devel
License:        GPLv2+
Requires:       tdelibs-devel %{name} = %{version} %{name}-apps = %{version} %{name}-runtime = %{version} %{name}-workspace = %{version}
Summary:        Trinity Base, Build Environment
Group:          System/GUI/TDE

%description devel
This package contains the development files for the Trinity Desktop Environent Base Package, including runtime, workspace, and core applications.

It is not needed if you do not want to compile high level KDE
applications.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package kdm
License:        GPLv2+
# usesubdirs kdm
Summary:        The Trinity login and display manager
Provides:       tdebase:%{_tde_bindir}/kdm
Requires:       xorg-x11
Requires:       %{name}-runtime >= %version
Group:          System/GUI/TDE
PreReq:         %fillup_prereq /bin/grep

%description kdm
This package contains kdm, the login and session manager for Trinity.

Note that the RC symlink for Trinity's KDM is /usr/sbin/tdm.

Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package samba
License:        GPLv2+
# usesubdirs kioslave/smb kcontrol/samba
Summary:        Trinity's Windows Connection Module
Group:          System/GUI/TDE

%description samba
This package provides the "smb://" protocol, to connect to and from
Windows and Samba shares.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package extra
License:        GPLv2+
# usesubdirs kpersonalizer kcontrol/thememgr
Summary:        Trinity's Extra Applications
Group:          System/GUI/TDE

%description extra
This package contains applications which are usually not needed on
SUSE.

- kpersonalizer - sets different settings

- khotkeys aRts support - for voice triggered shortcuts



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package nsplugin
License:        GPLv2+
%ifarch x86_64
Requires:       nspluginwrapper
%endif
Supplements:    tdebase >= %version
Requires:       tdebase = %version
Summary:        Netscape plugin support for Konqueror
Group:          System/GUI/TDE

%description nsplugin
This package contains support for Netscape plug-ins in konqueror. You
have to enable JavaScript for this.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>


%package ksysguardd
License:        GPLv2+
PreReq:         %insserv_prereq %fillup_prereq aaa_base
Summary:        Trinity's ksysguard daemon
Group:          System/GUI/TDE

%description ksysguardd
This package contains the ksysguard daemon. It is needed for ksysguard.

This package can be installed on servers without any other Trinity
packages to guard the system from remote computers.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>


%package session
License:        GPLv2+
Summary:        The Trinity Session
Group:          System/GUI/TDE
Provides:       tdebase:/usr/bin/tde
Requires:       kdebase3-workspace

%description session
This package contains the startup scripts necessary to start a Trinity
session from the login screen.



Authors:
--------
    Timothy Pearson <kb9vqf@pearsoncomputing.net>
    The KDE Team <kde@kde.org>

%package -n fileshareset
License:        GPLv2+
Summary:        Set and list fileshares
Group:          System/Management
Version:        2.0
Release:        579

%description -n fileshareset
This package contains the the fieshareset utility to allow users to
add or remove file shares.  It's also possible to list currently shared
locations. /etc/security/fileshare.conf is the main configuration file.



Authors:
--------
    Uwe Gansert <uwe.gansert at SuSE dot de>

%prep
%setup -q -b 8 -b 13 -n tdebase-%{version}
%patch0
%patch3
%patch5
# causes hangs (bnc#158239)
#%patch6
#%patch100
%patch7
%patch8
%patch10
%patch11
%patch12
%patch14
# do we really still need it ?
#%patch16
%patch15
%patch17
%patch20
%patch21
%patch85
%patch39
%patch40
%patch44
%patch45
%patch46
%patch51
%patch63
%patch60
%patch64
%patch94
%patch98
# all the kdm changes
%patch75
%patch70
%patch71
%patch72
%patch74
%patch76
%patch78
%patch79
# default-to-halt
%patch81
%patch82
%patch83
%patch77
%patch200
%patch215
%patch84
%patch61
%patch120
%patch22
%patch92
%patch88
%patch96
# xcursor
%patch99
%patch62
%patch69
%patch104
%patch105
%patch111
%patch114
%patch116
%patch117
%patch123
%patch126
%patch131
%patch141 -p1
%patch127
%patch144
%patch145
%patch149
%patch155
%patch156
%patch157
%patch160
%patch161
pushd kicker
%patch162
pushd ../kcontrol/kicker
%patch158
popd
popd
%patch165
%patch166
%patch167
tar xvfj %SOURCE20
%patch163
%patch125
%patch169
%patch170
%patch171
%patch172
%patch173
%patch174
%patch177
%patch179
%patch180
%patch189
%patch190
%patch195
%patch198
%patch199
%patch203
%patch204
%patch205
%patch207
%patch208
%patch209
%patch211
%patch212
%patch214
pushd kcontrol
%patch216
popd
%patch217
%patch218
%patch219
%patch220
%patch222
%patch225
%patch197
%patch206
%patch227
%patch228
%patch231
%patch232
%patch233
%patch234
%patch235
%patch236
%patch237
%patch238
%patch239
%patch240 -p1
%patch241 -p0
%patch242 -p0
%patch243
%patch244 -p1

rm -rf kappfinder
rm pics/crystalsvg/cr??-*emacs.png
cp %SOURCE17 l10n/tw/flag.png
cd ../fileshareset2
aclocal
autoconf
automake -a -c 
cd ../%{name}-%{version}
update_admin

%build

%cmake_tde -d build -- -DCMAKE_SKIP_RPATH=OFF \
  -DWITH_HAL=OFF \
  -DWITH_LDAP=ON \
  -DWITH_ARTS=ON \
  -DWITH_SAMBA=ON \
  -DWITH_SASL=ON \
  -DWITH_LIBUSB=ON \
  -DWITH_PAM=ON \
  -DBUILD_ALL=ON

%make_tde -d build

cd ../fileshareset2
  ./configure --prefix=%{fileshare_prefix}
  make %{?_smp_mflags}

%install
# relabel smb icon
grep -v ^Icon= kioslave/smb/smb-network.desktop | grep -v ^Name > w
mv w kioslave/smb/smb-network.desktop
echo "Icon=samba" >> kioslave/smb/smb-network.desktop
echo "Name=SMB Shares" >> kioslave/smb/smb-network.desktop
# install
%makeinstall_tde -d build
rm $RPM_BUILD_ROOT/%{_tde_appsdir}/System/kmenuedit.desktop
rm $RPM_BUILD_ROOT/%{_tde_appsdir}/System/kpersonalizer.desktop
rm $RPM_BUILD_ROOT/%{_tde_appsdir}/Utilities/kpager.desktop
rm $RPM_BUILD_ROOT/%{_tde_appsdir}/Internet/keditbookmarks.desktop
rm $RPM_BUILD_ROOT/%{_tde_appsdir}/Toys/ktip.desktop
install -m 0644 %SOURCE12 $RPM_BUILD_ROOT/%{_tde_sharedir}/fonts/
install -D -m 0644 %SOURCE21 $RPM_BUILD_ROOT/etc/pam.d/kcheckpass
install -m 0644 %SOURCE22 $RPM_BUILD_ROOT/%{_tde_servicesdir}/searchproviders/
install -m 0644 %SOURCE23 $RPM_BUILD_ROOT/%{_tde_servicesdir}/searchproviders/
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir} \
         ${RPM_BUILD_ROOT}/%{_sbindir} \
         ${RPM_BUILD_ROOT}/var/run/xdmctl
ln -fs %{_tde_bindir}/startkde $RPM_BUILD_ROOT/usr/bin/tde
ln -fs %{_tde_bindir}/startkde $RPM_BUILD_ROOT/usr/bin/starttde
ln -sf rcxdm ${RPM_BUILD_ROOT}/usr/sbin/rctdm
mv ${RPM_BUILD_ROOT}/%{_tde_bindir}/ksysguardd ${RPM_BUILD_ROOT}/%{_bindir}/ksysguardd
ln -sf %{_bindir}/ksysguardd ${RPM_BUILD_ROOT}/%{_tde_bindir}/ksysguardd
install -d ${RPM_BUILD_ROOT}/%{_tde_prefix}/env
install -D -m 0755 %SOURCE16 ${RPM_BUILD_ROOT}/%{_tde_prefix}/shutdown/stopkde.suse.sh
mkdir -p "${RPM_BUILD_ROOT}"/etc/security/
echo "RESTRICT=yes" > "${RPM_BUILD_ROOT}"/etc/security/fileshare.conf
#
# install pixmaps and configuration
#
mkdir -p $RPM_BUILD_ROOT/var/adm/fillup-templates
mkdir -p $RPM_BUILD_ROOT/etc/init.d/
install -m 0644 %SOURCE9 ${RPM_BUILD_ROOT}/%{_tde_datadir}/kdewizard/pics/wizard_small.png
install -m 0744 %SOURCE6 $RPM_BUILD_ROOT/etc/init.d/ksysguardd
mkdir -p $RPM_BUILD_ROOT/%{_tde_datadir}/kdm/faces/
ln -s ../pics/users/root1.png $RPM_BUILD_ROOT/%{_tde_datadir}/kdm/faces/root.face.icon
ln -s ../pics/users/default2.png $RPM_BUILD_ROOT/%{_tde_datadir}/kdm/faces/.default.face.icon
ln -sf /etc/init.d/ksysguardd  $RPM_BUILD_ROOT/%{_sbindir}/rcksysguardd
install -D -m 644 %SOURCE15 $RPM_BUILD_ROOT/etc/slp.reg.d/ksysguardd.reg
# even if we use smbro
install -D -m 644 kioslave/smb/smb-network.desktop $RPM_BUILD_ROOT/{%{_tde_datadir}/konqueror/dirtree/remote/smb-network.desktop
#
# install kde session file
#
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/xsessions/
mv $RPM_BUILD_ROOT/%{_tde_datadir}/kdm/sessions/tde.desktop $RPM_BUILD_ROOT/usr/share/xsessions/
# for those we have a package for remove the backup and rely on the package
for wm in gnome xfce4 xfce wmaker blackbox fvwm95 fvwm icewm enlightenment; do
  rm -f $RPM_BUILD_ROOT/%{_tde_datadir}/kdm/sessions/$wm.desktop
done
%suse_update_desktop_file $RPM_BUILD_ROOT/usr/share/xsessions/tde.desktop
#
# delete unwanted/double files
#
rm $RPM_BUILD_ROOT/%{_tde_datadir}/kdesktop/DesktopLinks/Home.desktop
rm $RPM_BUILD_ROOT/%{_tde_datadir}/kdesktop/DesktopLinks/System.desktop
rm $RPM_BUILD_ROOT/%{_tde_iconsdir}/*/*/apps/kvirc.*
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv $RPM_BUILD_ROOT/%{_tde_wallpapersdir} $RPM_BUILD_ROOT/%{_datadir}
cd ../fileshareset2/src
rm -f $RPM_BUILD_ROOT/%{_tde_bindir}/fileshare{set,list}
make DESTDIR=$RPM_BUILD_ROOT install
chmod 0755 $RPM_BUILD_ROOT/%{fileshare_prefix}/bin/fileshareset
cd ..
FILLUP_DIR=$RPM_BUILD_ROOT/var/adm/fillup-templates
install -m 644 -D  %SOURCE4 $FILLUP_DIR/sysconfig.windowmanager-tdebase
mkdir -p $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps/

for i in {16,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/mimetypes/misc.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmcomponentchooser.png;done

for i in {16,22,32,48,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/launch.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmperformance.png;done

cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/16x16/actions/services.png $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/16x16/apps/kcmkded.png

for i in {16,22,32,48}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/exit.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmsmserver.png;done

for i in {16,22,32}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/spellcheck.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmspellchecking.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/filesystems/desktop.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmdesktopbehavior.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/filesystems/desktop.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmdesktop.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/apps/kmenu.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmtaskbar.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/mimetypes/colorscm.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmcolors.png;done

for i in {16,22,32,48,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/launch.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmlaunch.png;done

for i in {16,22,32}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/filter.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmkhtml_filter.png;done

for i in {16,22,32}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/run.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmcgi.png;done

for i in {16,22}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/history.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmhistory.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/filesystems/network.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmnetpref.png;done

for i in {16,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/devices/blockdevice.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmkdnssd.png;done

for i in {16,22,32,48,64}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/devices/joystick.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmjoystick.png;done

for i in {16,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/devices/mouse.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmmouse.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/devices/system.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmmedia.png;done

for i in {16,22,32}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/actions/encrypted.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmcrypto.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/filesystems/trashcan_empty.png  $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmprivacy.png;done

for i in {16,22,32,48,64,128}; do cp %{buildroot}/%{_tde_iconsdir}/crystalsvg/"$i"x"$i"/filesystems/network.png $RPM_BUILD_ROOT/%{_tde_iconsdir}/hicolor/"$i"x"$i"/apps/kcmnic.png;done
#
# solve file conflicts with theme packages ...
#
mv $RPM_BUILD_ROOT/%{_tde_datadir}/ksplash/pics $RPM_BUILD_ROOT/%{_tde_datadir}/ksplash/pics-default
ln -s pics-default $RPM_BUILD_ROOT/%{_tde_datadir}/ksplash/pics
chmod 0755 $RPM_BUILD_ROOT/%{fileshare_prefix}/bin/fileshareset
%suse_update_desktop_file kate             TextEditor
%suse_update_desktop_file kwrite        TextEditor
%suse_update_desktop_file Help             Documentation Viewer
%suse_update_desktop_file Home             System FileManager core
%suse_update_desktop_file KControl         X-SuSE-core
%suse_update_desktop_file konqbrowser      WebBrowser
%suse_update_desktop_file Kfind            System Filesystem core
%suse_update_desktop_file kinfocenter      System Monitor
%suse_update_desktop_file kmenuedit        Core-Configuration
%suse_update_desktop_file konsole          TerminalEmulator
%suse_update_desktop_file konsolesu        TerminalEmulator
%suse_update_desktop_file ksysguard        System Monitor
%suse_update_desktop_file -r klipper          System TrayIcon
%suse_update_desktop_file kpager           Utility  DesktopUtility
%suse_update_desktop_file -u ktip          System Utility
%suse_update_desktop_file konqfilemgr      System FileManager
%suse_update_desktop_file konquerorsu      System FileManager
%suse_update_desktop_file kdeprintfax      PrintingUtility
%suse_update_desktop_file kjobviewer       PrintingUtility
%suse_update_desktop_file kpersonalizer    DesktopUtility
%suse_update_desktop_file kcmkicker        X-KDE-settings-desktop
%suse_update_desktop_file knetattach       System Network
%suse_update_desktop_file -r kfontview     Graphics Viewer
%suse_update_desktop_file -r krandrtray    Applet X-KDE-settings-desktop
%suse_update_desktop_file $RPM_BUILD_ROOT/%{_tde_datadir}/remoteview/smb-network.desktop
for i in $RPM_BUILD_ROOT/%{_tde_appsdir}/System/ScreenSavers/*.desktop ; do
  sed -e '/^\[Desktop Entry\]/a\
Categories=Screensaver;' $i > ${i}_
  mv ${i}_ $i
  %suse_update_desktop_file "$i"
done
install -d $RPM_BUILD_ROOT/%{_tde_appsdir}/apps
ln -sf %{_tde_appsdir}/System/ScreenSavers $RPM_BUILD_ROOT/%{_tde_appsdir}/apps/ScreenSavers

for i in $RPM_BUILD_ROOT/%{_tde_applicationsdir}/kde/*.desktop \
	 $RPM_BUILD_ROOT/%{_tde_datadir}/konqueror/servicemenus/*.desktop \
	 $RPM_BUILD_ROOT/%{_tde_datadir}/kicker/*/*.desktop \
	 $RPM_BUILD_ROOT/%{_tde_datadir}/kicker/*/*/*.desktop \
         $RPM_BUILD_ROOT/%{_tde_datadir}/kicker/*/*/*.desktop \
         $RPM_BUILD_ROOT/%{_datadir}/wallpapers/*.desktop \
	 $RPM_BUILD_ROOT/%{_tde_datadir}/konqsidebartng/virtual_folders/services/*.desktop; do
  [ "`sed -n '/^\[Desktop Entry\]/,/^\[/ s,NoDisplay=\(.*\),\1,p' "$i"`" = "true" ] && continue
  [ "`sed -n '/^\[Desktop Entry\]/,/^\[/ s,Hidden=\(.*\),\1,p' "$i"`" = "true" ] && continue
  grep -q X-SuSE-translate "$i" && continue
  %suse_update_desktop_file "$i"
done
rm -f $RPM_BUILD_ROOT/%{_tde_configdir}/kdm/README
rm -f $RPM_BUILD_ROOT/%{_tde_datadir}/kdm/sessions/icewm.desktop
#
# gimp 2.0 does have a different named icon
#
for i in $RPM_BUILD_ROOT/%{_tde_iconsdir}/*/*/apps/gimp.png; do
  ln "$i" "${i%/*}/wilber-icon.png"
done
mkdir -p -m 755 $RPM_BUILD_ROOT/%_mandir/man8
cp %SOURCE18 $RPM_BUILD_ROOT/%_mandir/man8
cp %SOURCE19 $RPM_BUILD_ROOT/%_mandir/man8
# don't conflict with man pages from KDE4 packages
rm $RPM_BUILD_ROOT/%_mandir/man1/kate.*
rm $RPM_BUILD_ROOT/%_mandir/man1/kdesu.*
rm $RPM_BUILD_ROOT/%_mandir/man1/kbookmarkmerger.*
rm $RPM_BUILD_ROOT/%_mandir/man1/kfind.*
%tde_post_install
%fdupes $RPM_BUILD_ROOT/%{_tde_sharedir}
# move konqueror.desktop back to old position (#281572)
mv $RPM_BUILD_ROOT/%{_tde_applicationsdir}/kde/konqueror.desktop $RPM_BUILD_ROOT/%{_tde_appsdir}/konqueror.desktop

# while this script uses udisks, it's better to be fully integrated
# into Trinity.
#%if 0%{?with_hal} == 0
#cp -f %{SOURCE24} $RPM_BUILD_ROOT/opt/kde3/bin
#chmod +x $RPM_BUILD_ROOT/opt/kde3/bin/devmon-automounter.sh
#sed -i 5i\ '/opt/kde3/bin/devmon-automounter.sh &' $RPM_BUILD_ROOT/opt/kde3/bin/startkde
#%endif

%pre
# we have this as link
if test -e opt/tde/share/apps/ksplash/pics -a ! -L opt/tde/share/apps/ksplash/pics ;
 then
  if test -e opt/tde/share/apps/ksplash/pics-default; then
     rm -rf opt/tde/share/apps/ksplash/pics
  else
     mv opt/tde/share/apps/ksplash/pics opt/tde/share/apps/ksplash/pics-default
  fi
fi
kdmrc=/opt/tde/share/config/kdm/kdmrc
# if the /opt/tde one is obviously wrong and we have one in /etc we move that one over to 
# avoid confusion on update what's the right kdmrc
if test -f $kdmrc && grep -q "Session=/opt/tde/share/config/kdm/Xsession" $kdmrc && test -f /etc$kdmrc; then
   mv /etc$kdmrc $kdmrc
fi

%post
/sbin/ldconfig
%run_permissions

%post kdm
%{fillup_only -an windowmanager-tdebase}
/opt/tde/bin/genkdmconf
if test -f /etc/sysconfig/displaymanager ; then
  . /etc/sysconfig/displaymanager
fi
%{fillup_only -n displaymanager -s tdebase-SuSE}
%{remove_and_set -n displaymanager KDM_SHUTDOWN}
if test -n "$KDM_SHUTDOWN" -a "$KDM_SHUTDOWN" != "no"; then
  if test "$KDM_SHUTDOWN" = "local" ; then
    KDM_SHUTDOWN=all
  fi
  case "$KDM_SHUTDOWN" in
  "auto" | "none" | "root")
    sed -i -e "s/^DISPLAYMANAGER_SHUTDOWN=.*/DISPLAYMANAGER_SHUTDOWN=\"$KDM_SHUTDOWN\"/" /etc/sysconfig/displaymanager
    ;;
  esac
fi

%post -n fileshareset
%run_permissions

%postun kdm
%insserv_cleanup

%postun
%insserv_cleanup
/sbin/ldconfig

%post runtime -p /sbin/ldconfig

%postun runtime -p /sbin/ldconfig

%post workspace -p /sbin/ldconfig

%postun workspace -p /sbin/ldconfig

%post apps -p /sbin/ldconfig

%postun apps -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n misc-console-font
%defattr(-,root,root)
%doc COPYING
%{_tde_sharedir}/fonts/console8x16.pcf.gz

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README README.pam ../lame.spec ../README.mp3
%exclude %{_tde_sharedir}/fonts/console8x16.pcf.gz
%dir %{_tde_iconsdir}/hicolor/*
%dir %{_tde_libdir}/kconf_update_bin
%dir %{_tde_datadir}/plugin
%dir %{_tde_appsdir}
%dir %{_tde_appsdir}/Settings
%dir %{_tde_appsdir}/Settings/WebBrowsing
%dir %{_tde_appsdir}/System/ScreenSavers
%dir %{_tde_appsdir}/apps
%{_tde_appsdir}/apps/ScreenSavers
/etc/xdg/menus/*.menu
/etc/xdg/menus/applications-merged
%verify(not mode) %attr(2755,root,nogroup) %{_tde_bindir}/kdesud
%verify(not mode) %attr(0755,root,man) %{_tde_bindir}/khc_indexbuilder
%{_tde_prefix}/env
%{_tde_bindir}/arts-start
%{_tde_bindir}/drkonqi
%{_tde_bindir}/kaccess
%{_tde_bindir}/kblankscrn.kss
%{_tde_bindir}/kbookmarkmerger
%{_tde_bindir}/kcminit
%{_tde_bindir}/kcminit_startup
%{_tde_modulesdir}/kcminit_startup.*
%{_tde_bindir}/kcontrol*
%{_tde_bindir}/kdeinstallktheme
%{_tde_bindir}/kdepasswd
%{_tde_bindir}/kdcop
%{_tde_bindir}/kdebugdialog
%{_tde_bindir}/kdeeject
%{_tde_bindir}/kdeprintfax
%{_tde_bindir}/keditfiletype
%{_tde_bindir}/khelpcenter
%{_tde_bindir}/kjobviewer
%{_tde_bindir}/kcheckrunning
%{_tde_bindir}/kpm
%{_tde_bindir}/krandom.kss
%{_tde_bindir}/krdb
%{_tde_bindir}/kxkb
%{_tde_bindir}/kdialog
%{_tde_bindir}/klocaldomainurifilterhelper
%{_tde_bindir}/kio_media_mounthelper
%{_tde_bindir}/knetattach
%{_tde_bindir}/ktrash
%{_tde_bindir}/khc_docbookdig.pl
%{_tde_bindir}/khc_mansearch.pl
%{_tde_bindir}/khc_htdig.pl
%{_tde_bindir}/khc_htsearch.pl
%{_tde_bindir}/kapplymousetheme
%{_tde_bindir}/kio_system_documenthelper
%{_tde_bindir}/runupdater
%{_tde_bindir}/kstart                      
%{_tde_bindir}/ksystraycmd
%{_tde_modulesdir}/cursorthumbnail.*
%{_tde_modulesdir}/htmlthumbnail.*
%{_tde_modulesdir}/imagethumbnail.*
%{_tde_modulesdir}/kcm_a*
%{_tde_modulesdir}/kcm_bell*
%{_tde_modulesdir}/kcm_keyboard*
%{_tde_modulesdir}/kcm_c*
%{_tde_modulesdir}/kcm_d*
%{_tde_modulesdir}/kcm_e*
%{_tde_modulesdir}/kcm_f*
%{_tde_modulesdir}/kcm_h*
%{_tde_modulesdir}/kcm_i*
%{_tde_modulesdir}/kcm_l*
%{_tde_modulesdir}/kcm_nic.*
%{_tde_modulesdir}/kcm_p*
%{_tde_modulesdir}/kcm_smserver.*
%{_tde_modulesdir}/kcm_spellchecking.*
%{_tde_modulesdir}/kcm_style.*
%{_tde_modulesdir}/kcm_usb.*
%{_tde_modulesdir}/khelpcenter.*
%{_tde_modulesdir}/kcm_xinerama.*
%{_tde_modulesdir}/kxkb.*
%{_tde_modulesdir}/djvuthumbnail.*
%{_tde_modulesdir}/kaccess.*
%{_tde_modulesdir}/kcminit.*
%{_tde_modulesdir}/kcm_nsplugins.*
%{_tde_modulesdir}/kcontrol.*
%{_tde_modulesdir}/keditbookmarks.*
%{_tde_modulesdir}/kfmclient.*
%{_tde_modulesdir}/kjobviewer.*
%{_tde_modulesdir}/kprinter.*
%{_tde_modulesdir}/libkdeprint_part.*
%{_tde_modulesdir}/libkshorturifilter.*
%{_tde_modulesdir}/libkuri*
%{_tde_modulesdir}/libkonsolepart.*
%{_tde_modulesdir}/textthumbnail.*
%{_tde_modulesdir}/kcm_joystick.*
%{_tde_modulesdir}/kcm_useraccount.*
%{_tde_modulesdir}/kcontroledit.*
%{_tde_modulesdir}/kded_kwrited.*
%{_tde_modulesdir}/kstyle_keramik_config.*
%{_tde_modulesdir}/libkmanpart.*
%{_tde_modulesdir}/liblocaldomainurifilter.*
%{_tde_modulesdir}/runupdater.*
%{_tde_libdir}/libkdeinit_runupdater.so
%{_tde_libdir}/libkdeinit_kaccess.so
%{_tde_libdir}/libkdeinit_kcminit.so
%{_tde_libdir}/libkdeinit_kcminit_startup.so
%{_tde_libdir}/libkdeinit_kcontrol.so
%{_tde_libdir}/libkdeinit_kcontroledit.so
%{_tde_libdir}/libkdeinit_keditbookmarks.so
%{_tde_libdir}/libkdeinit_kfmclient.so
%{_tde_libdir}/libkdeinit_khelpcenter.so
%{_tde_libdir}/libkdeinit_kjobviewer.so
%{_tde_libdir}/libkdeinit_kxkb.so
%{_tde_modulesdir}/libnsplugin.*
%{_tde_modulesdir}/kded_remotedirnotify.*
%{_tde_modulesdir}/kded_systemdirnotify.*
%{_tde_modulesdir}/libkhtmlkttsdplugin.*
%{_tde_modulesdir}/kcm_media.la
%{_tde_modulesdir}/kcm_media.so
%{_tde_modulesdir}/kded_homedirnotify.la
%{_tde_modulesdir}/kded_homedirnotify.so
%{_tde_modulesdir}/kded_medianotifier.la
%{_tde_modulesdir}/kded_medianotifier.so
%{_tde_modulesdir}/kcm_kded.*
%{_tde_modulesdir}/kcm_kdnssd.*
%{_tde_modulesdir}/kcm_keyboard.*
%{_tde_modulesdir}/kcm_keys.*
%{_tde_modulesdir}/kcm_kio.*
%{_tde_modulesdir}/kcm_knotify.*
%{_tde_modulesdir}/kcm_konq.*
%{_tde_modulesdir}/kcm_konqhtml.*
%{_tde_modulesdir}/kcm_kthememanager.*
%{_tde_modulesdir}/kcm_kurifilt.*
%{_tde_applicationsdir}/kde/khtml_filter.desktop
%{_tde_applicationsdir}/kde/media.desktop
%{_tde_applicationsdir}/kde/joystick.desktop
%{_tde_applicationsdir}/kde/kcm_useraccount.desktop
%{_tde_applicationsdir}/kde/kdepasswd.desktop
%{_tde_applicationsdir}/kde/kthememanager.desktop
%{_tde_applicationsdir}/kde/Help.desktop
%{_tde_applicationsdir}/kde/KControl.desktop
%{_tde_applicationsdir}/kde/arts.desktop
%{_tde_applicationsdir}/kde/bell.desktop
%{_tde_applicationsdir}/kde/cache.desktop
%{_tde_applicationsdir}/kde/colors.desktop
%{_tde_applicationsdir}/kde/componentchooser.desktop
%{_tde_applicationsdir}/kde/cookies.desktop
%{_tde_applicationsdir}/kde/crypto.desktop
%{_tde_applicationsdir}/kde/display.desktop
%{_tde_applicationsdir}/kde/dma.desktop
%{_tde_applicationsdir}/kde/ebrowsing.desktop
%{_tde_applicationsdir}/kde/filebrowser.desktop
%{_tde_applicationsdir}/kde/filetypes.desktop
%{_tde_applicationsdir}/kde/fonts.desktop
%{_tde_applicationsdir}/kde/clock.desktop
%{_tde_applicationsdir}/kde/icons.desktop
%{_tde_applicationsdir}/kde/interrupts.desktop
%{_tde_applicationsdir}/kde/installktheme.desktop
%{_tde_applicationsdir}/kde/ioports.desktop
%{_tde_applicationsdir}/kde/ioslaveinfo.desktop
%{_tde_applicationsdir}/kde/kcmaccess.desktop
%{_tde_applicationsdir}/kde/kcmcgi.desktop
%{_tde_applicationsdir}/kde/kcmcss.desktop
%{_tde_applicationsdir}/kde/kcmhistory.desktop
%{_tde_applicationsdir}/kde/kcmkded.desktop
%{_tde_applicationsdir}/kde/kcmlaunch.desktop
%{_tde_applicationsdir}/kde/kcm_kdnssd.desktop
%{_tde_applicationsdir}/kde/kcmnotify.desktop
%{_tde_applicationsdir}/kde/kcmperformance.desktop
%{_tde_applicationsdir}/kde/kcmusb.desktop
%{_tde_applicationsdir}/kde/kdeprintfax.desktop
%{_tde_applicationsdir}/kde/keyboard.desktop
%{_tde_applicationsdir}/kde/keyboard_layout.desktop
%{_tde_applicationsdir}/kde/keys.desktop
%{_tde_applicationsdir}/kde/kfmclient.desktop
%{_tde_applicationsdir}/kde/kfmclient_dir.desktop
%{_tde_applicationsdir}/kde/kfmclient_html.desktop
%{_tde_applicationsdir}/kde/kfmclient_war.desktop
%{_tde_applicationsdir}/kde/khtml_behavior.desktop
%{_tde_applicationsdir}/kde/khtml_fonts.desktop
%{_tde_applicationsdir}/kde/khtml_java_js.desktop
%{_tde_applicationsdir}/kde/khtml_plugins.desktop
%{_tde_applicationsdir}/kde/kjobviewer.desktop
%{_tde_applicationsdir}/kde/lanbrowser.desktop
%{_tde_applicationsdir}/kde/language.desktop
%{_tde_applicationsdir}/kde/memory.desktop
%{_tde_applicationsdir}/kde/mouse.desktop
%{_tde_applicationsdir}/kde/netpref.desktop
%{_tde_applicationsdir}/kde/nic.desktop
%{_tde_applicationsdir}/kde/partitions.desktop
%{_tde_applicationsdir}/kde/pci.desktop
%{_tde_applicationsdir}/kde/printers.desktop
%{_tde_applicationsdir}/kde/privacy.desktop
%{_tde_applicationsdir}/kde/processor.desktop
%{_tde_applicationsdir}/kde/proxy.desktop
%{_tde_applicationsdir}/kde/scsi.desktop
%{_tde_applicationsdir}/kde/smbstatus.desktop
%{_tde_applicationsdir}/kde/sound.desktop
%{_tde_applicationsdir}/kde/spellchecking.desktop
%{_tde_applicationsdir}/kde/style.desktop
%{_tde_applicationsdir}/kde/useragent.desktop
%{_tde_applicationsdir}/kde/xserver.desktop
%{_tde_applicationsdir}/kde/cdinfo.desktop
%{_tde_appsdir}/.hidden
%{_tde_appsdir}/Settings/Information
%{_tde_appsdir}/Settings/LookNFeel
%{_tde_appsdir}/Settings/WebBrowsing/khtml_appearance.desktop
%{_tde_appsdir}/Settings/WebBrowsing/smb.desktop
%{_tde_datadir}/drkonqi
%{_tde_datadir}/kc*
%{_tde_datadir}/kdcop
%{_tde_datadir}/kdeprint*
%{_tde_datadir}/kdewizard
%{_tde_datadir}/kdisplay
%{_tde_datadir}/khelpcenter/searchhandlers/docbook.desktop
%{_tde_datadir}/khelpcenter
%{_tde_datadir}/kio*
%{_tde_datadir}/kjobviewer
%{_tde_datadir}/konsole
%{_tde_datadir}/khtml/kpartplugins
%{_tde_datadir}/kthememanager
%{_tde_datadir}/remoteview
%{_tde_datadir}/systemview
%{_tde_datadir}/kaccess
%{_tde_configdir}.kcfg/klaunch.kcfg
%{_tde_configdir}.kcfg/khelpcenter.kcfg
%{_tde_configdir}.kcfg/keditbookmarks.kcfg
%{_tde_configdir}.kcfg/launcherapplet.kcfg
%{_tde_configdir}.kcfg/mediamanagersettings.kcfg
%{_tde_mimedir}/inode/system_directory.desktop
%{_tde_servicesdir}/kded/remotedirnotify.desktop
%{_tde_servicesdir}/kded/systemdirnotify.desktop
%config(noreplace) %{_tde_configdir}/kshorturifilterrc
%config(noreplace) %{_tde_configdir}/kxkb_groups
%{_tde_sharedir}/desktop-directories
%exclude %{_tde_htmldir}/en/kioslave
%dir %{_tde_sharedir}/fonts
%dir %{_tde_sharedir}/fonts/override
%verify(not md5 size mtime) %{_tde_sharedir}/fonts/override/fonts.dir
%dir %{_tde_iconsdir}/*/*/*
%{_tde_configdir}.kcfg/kcm_useraccount.kcfg
%{_tde_configdir}.kcfg/kcm_useraccount_pass.kcfg
%exclude %{_tde_iconsdir}/*/*/*/style.*
%exclude %{_tde_iconsdir}/*/*/*/looknfeel.*
%exclude %{_tde_iconsdir}/*/*/*/energy.*
%exclude %{_tde_iconsdir}/*/*/*/date.*
%exclude %{_tde_iconsdir}/*/*/*/filetypes.*
%exclude %{_tde_iconsdir}/*/*/*/personal.*
%{_tde_iconsdir}/*/*/*/a*.*
%{_tde_iconsdir}/*/*/*/b*.*
%{_tde_iconsdir}/*/*/*/c*.*
%{_tde_iconsdir}/*/*/*/d*.*
%{_tde_iconsdir}/*/*/*/f*.*
%{_tde_iconsdir}/*/*/*/g*.*
%{_tde_iconsdir}/*/*/*/help_index.*
%{_tde_iconsdir}/*/*/*/icons.*
%{_tde_iconsdir}/*/*/*/input_devices_settings.*
%{_tde_iconsdir}/*/*/*/kcmx.*
%{_tde_iconsdir}/*/*/*/kcmdf.*
%{_tde_iconsdir}/*/*/*/kbinaryclock.*
%{_tde_iconsdir}/*/*/apps/kcmcgi.*
%{_tde_iconsdir}/*/*/apps/kcmcolors.*
%{_tde_iconsdir}/*/*/apps/kcmcomponentchooser.*
%{_tde_iconsdir}/*/*/apps/kcmcrypto.*
%{_tde_iconsdir}/*/*/apps/kcmhistory.*
%{_tde_iconsdir}/*/*/apps/kcmjoystick.*
%{_tde_iconsdir}/*/*/apps/kcmkded.*
%{_tde_iconsdir}/*/*/apps/kcmkdnssd.*
%{_tde_iconsdir}/*/*/apps/kcmkhtml_filter.*
%{_tde_iconsdir}/*/*/apps/kcmlaunch.*
%{_tde_iconsdir}/*/*/apps/kcmmedia.*
%{_tde_iconsdir}/*/*/apps/kcmmouse.*
%{_tde_iconsdir}/*/*/apps/kcmnetpref.*
%{_tde_iconsdir}/*/*/apps/kcmnic.*
%{_tde_iconsdir}/*/*/apps/kcmperformance.*
%{_tde_iconsdir}/*/*/apps/kcmprivacy.*
%{_tde_iconsdir}/*/*/apps/kcmspellchecking.*
%{_tde_iconsdir}/*/*/*/ieee1394.*
%{_tde_iconsdir}/*/*/*/kdeprintfax.*
%{_tde_iconsdir}/*/*/*/kdisknav.*
%{_tde_iconsdir}/*/*/*/knetattach.*
%{_tde_iconsdir}/*/*/*/key_bindings.*
%{_tde_iconsdir}/*/*/*/keyboard_layout.*
%{_tde_iconsdir}/*/*/*/kfm_home.*
%{_tde_iconsdir}/*/*/*/khelpcenter.*
%{_tde_iconsdir}/*/*/*/kjobviewer.*
%{_tde_iconsdir}/*/*/*/konsole.*
%{_tde_iconsdir}/*/*/*/l*.*
%{_tde_iconsdir}/*/*/*/m*.*
%{_tde_iconsdir}/*/*/*/ne*.*
%{_tde_iconsdir}/*/*/*/opera.*
%{_tde_iconsdir}/*/*/*/r*.*
%{_tde_iconsdir}/*/*/*/s*.*
%{_tde_iconsdir}/*/*/*/usb.*
%{_tde_iconsdir}/*/*/*/vnc.*
%{_tde_iconsdir}/*/*/*/w*.*
%{_tde_iconsdir}/*/*/*/e*.*
%{_tde_iconsdir}/*/*/*/kcmdevices.*
%{_tde_iconsdir}/*/*/*/kcmdrkonqi.*
%{_tde_iconsdir}/*/*/*/kcmmemory.*
%{_tde_iconsdir}/*/*/*/kcmmidi.*
%{_tde_iconsdir}/*/*/*/kcmpartitions.*
%{_tde_iconsdir}/*/*/*/kcmpci.*
%{_tde_iconsdir}/*/*/*/kcmprocessor.*
%{_tde_iconsdir}/*/*/*/kcmscsi.*
%{_tde_iconsdir}/*/*/*/kthememgr.*
%{_tde_iconsdir}/*/*/*/kcontrol.*
%{_tde_iconsdir}/*/*/*/kxkb.*
%{_tde_iconsdir}/*/*/*/p*.*
%{_tde_iconsdir}/*/*/*/t*.*
%{_tde_iconsdir}/*/*/*/qtella.*
%{_tde_iconsdir}/*/*/*/x*.*
# these have no PNG
%{_tde_iconsdir}/*/scalable/apps/hardware.svgz
%{_tde_iconsdir}/*/scalable/apps/kate2.svgz
%{_tde_iconsdir}/*/scalable/apps/kwrite2.svgz
%{_tde_iconsdir}/*/scalable/apps/openoffice.svgz
%{_tde_iconsdir}/*/scalable/apps/quicktime.svgz
%{_tde_sharedir}/locale
%{_tde_mimedir}/application/x-konsole.desktop
%{_tde_mimedir}/application/x-ktheme.desktop
%{_tde_mimedir}/application/x-smb-server.desktop
%{_tde_mimedir}/print
%{_tde_servicesdir}/textthumbnail.desktop
%{_tde_servicesdir}/htmlthumbnail.desktop
%{_tde_servicesdir}/ka*.desktop
%{_tde_servicesdir}/kdeprint_part.desktop
%{_tde_servicesdir}/konsolepart.desktop
%{_tde_servicesdir}/konsole-script.desktop
%{_tde_servicesdir}/kshorturifilter.desktop
%{_tde_servicesdir}/ku*.desktop
%{_tde_servicesdir}/searchproviders
%{_tde_servicesdir}/useragentstrings
%{_tde_servicesdir}/imagethumbnail.desktop
%{_tde_servicesdir}/kxkb.desktop
%{_tde_servicesdir}/kmanpart.desktop
%{_tde_servicesdir}/localdomainurifilter.desktop
%{_tde_servicesdir}/kwrited.desktop
%{_tde_servicesdir}/djvuthumbnail.desktop
%{_tde_servicesdir}/kded/kwrited.desktop
%{_tde_servicetypesdir}/terminalemulator.desktop
%{_tde_servicetypesdir}/kateplugin.desktop
%{_tde_servicetypesdir}/findpart.desktop
%{_tde_servicetypesdir}/searchprovider.desktop
%{_tde_servicetypesdir}/thumbcreator.desktop
%{_tde_servicetypesdir}/uasprovider.desktop
%exclude %{_tde_sounddir}/KDE_Close_Window*
%exclude %{_tde_sounddir}/KDE_Dialog*
%exclude %{_tde_sounddir}/KDE_Desktop*
%exclude %{_tde_sounddir}/KDE_Logout*
%exclude %{_tde_sounddir}/KDE_Startup*
%exclude %{_tde_sounddir}/KDE_Window*
%{_tde_sounddir}
%{_tde_sharedir}/templates
%{_tde_servicesdir}/khelpcenter.desktop
%{_tde_bindir}/keditbookmarks
%{_tde_bindir}/kfm*
%{_tde_datadir}/kbookmark
%{_tde_datadir}/keditbookmarks
%{_tde_iconsdir}/*/*/*/keditbookmarks.*
%{_tde_iconsdir}/*/*/*/kfm.*
%{_tde_iconsdir}/*/*/*/konqueror.*
%{_tde_servicesdir}/konq*
%{_tde_servicetypesdir}/konq*
%{_tde_servicesdir}/cursorthumbnail.desktop
%{_tde_modulesdir}/kcm_randr.*
%{_tde_bindir}/krandrtray
%{_tde_applicationsdir}/kde/krandrtray.desktop
%{_tde_modulesdir}/kded_mediamanager.*
%{_tde_modulesdir}/kfile_media.*
%{_tde_modulesdir}/kfile_trash.*
%{_tde_applicationsdir}/kde/devices.desktop
%{_tde_applicationsdir}/kde/knetattach.desktop
%{_tde_applicationsdir}/kde/opengl.desktop
%{_tde_iconsdir}/*/*/*/kcmopengl.*
%{_tde_mimedir}/media
%{_tde_servicesdir}/kded/mediamanager.desktop
%{_tde_servicesdir}/kded/homedirnotify.desktop
%{_tde_servicesdir}/kded/medianotifier.desktop
%{_tde_servicesdir}/kfile_media.desktop
%{_tde_servicesdir}/kfile_trash.desktop
%{_tde_servicesdir}/kfile_trash_system.desktop
%{_tde_mimedir}/fonts/package.desktop
%{_tde_modulesdir}/exrthumbnail.*
%{_tde_servicesdir}/exrthumbnail.desktop
%dir %{_tde_mimedir}/fonts
%{_tde_bindir}/kfontinst
%{_tde_modulesdir}/fontthumbnail.*
%{_tde_modulesdir}/kfile_font.*
%{_tde_modulesdir}/libkfontviewpart.*
%dir %{_tde_datadir}/kfontview
%{_tde_datadir}/kfontview/kfontviewpart.rc
%{_tde_applicationsdir}/kde/kcmfontinst.desktop
%{_tde_mimedir}/fonts/folder.desktop
%{_tde_mimedir}/fonts/system-folder.desktop
%{_tde_servicesdir}/fontthumbnail.desktop
%{_tde_servicesdir}/kfile_font.desktop
%{_tde_servicesdir}/kfontviewpart.desktop
%_mandir/man1/*
%{_mandir}/man8/kcheckpass.8.gz
%doc %lang(en) %{_tde_htmldir}/en/kcontrol
%doc %lang(en) %{_tde_htmldir}/en/kdcop
%doc %lang(en) %{_tde_htmldir}/en/kdebugdialog
%doc %lang(en) %{_tde_htmldir}/en/kdeprint
%doc %lang(en) %{_tde_htmldir}/en/kdesu
%exclude %{_tde_htmldir}/en/khelpcenter/userguide
%exclude %{_tde_htmldir}/en/khelpcenter/visualdict
%doc %lang(en) %{_tde_htmldir}/en/khelpcenter
%doc %lang(en) %{_tde_htmldir}/en/knetattach
%{_tde_applicationsdir}/kde/desktoppath.desktop

%files samba
%defattr(-,root,root)
%{_tde_modulesdir}/kcm_samba.*
%{_tde_modulesdir}/kio_smb.*
%{_tde_servicesdir}/smb.protocol
%dir %{_tde_datadir}/konqueror/dirtree
%dir %{_tde_datadir}/konqueror/dirtree/remote
%{_tde_datadir}/konqueror/dirtree/remote/smb-network.desktop
%{_tde_mimedir}/application/x-smb-workgroup.desktop

%files kdm
%defattr(-,root,root)
%dir %{_tde_docdir}/kdm
%{_tde_bindir}/genkdmconf
%{_tde_bindir}/kdm*
%{_tde_bindir}/krootimage
%{_tde_datadir}/kdm
%{_tde_modulesdir}/kgreet_pam.*
%doc %{_tde_docdir}/kdm/README
%dir %{_tde_configdir}/kdm
%config(noreplace) %{_tde_configdir}/kdm/kdmrc
%config(noreplace) %{_tde_configdir}/kdm/backgroundrc
%ghost /var/run/xdmctl
# kdm has not been renamed.
%{_sbindir}/rckdm
%{_tde_applicationsdir}/kde/kdm.desktop
%{_tde_iconsdir}/*/*/*/kdmconfig.*
%{_tde_modulesdir}/kcm_kdm.*
%doc %lang(en) %{_tde_htmldir}/en/kdm

%files session
%defattr(-,root,root)
/usr/bin/tde
/usr/bin/starttde
/usr/share/xsessions/kde.desktop

%files extra
%defattr(-,root,root)
%{_tde_bindir}/kpersonalizer
%{_tde_applicationsdir}/kde/kpersonalizer.desktop
%{_tde_datadir}/kpersonalizer
%{_tde_iconsdir}/*/*/*/kpersonalizer.*
%{_tde_bindir}/kfontview
%{_tde_applicationsdir}/kde/kfontview.desktop
%{_tde_datadir}/kfontview/kfontviewui.rc
%{_tde_modulesdir}/khotkeys_arts.*

%files nsplugin
%defattr(-,root,root)
%{_tde_bindir}/nsplugin*
%{_tde_datadir}/plugin/nspluginpart.rc
%dir %{_tde_appsdir}/Settings/WebBrowsing
%{_tde_appsdir}/Settings/WebBrowsing/nsplugin.desktop

%files devel
%defattr(-,root,root)
%{_tde_includedir}/*
%{_tde_libdir}/libkonq.so
%{_tde_libdir}/libkdecorations.so
%{_tde_libdir}/libkonqsidebarplugin.so
%{_tde_libdir}/libkickermain.so
%{_tde_libdir}/libtask*.so
%{_tde_libdir}/libksgrd.so
%{_tde_libdir}/libkickoffsearch_interfaces.so
%{_tde_libdir}/libkickoffsearch_interfaces.la
%{_tde_libdir}/libksplashthemes.so
%{_tde_libdir}/libkateinterfaces.so
%{_tde_libdir}/libkateutils.so
%{_tde_libdir}/libkhotkeys_shared.so
%{_tde_libdir}/libkateinterfaces.la
%{_tde_libdir}/libkateutils.la
%{_tde_libdir}/libkdecorations.la
%{_tde_libdir}/libkfontinst.la
%{_tde_libdir}/libkfontinst.so
%{_tde_libdir}/libkhotkeys_shared.la
%{_tde_libdir}/libkickermain.la
%{_tde_libdir}/libkonq.la
%{_tde_libdir}/libkonqsidebarplugin.la
%{_tde_libdir}/libksgrd.la
%{_tde_libdir}/libksplashthemes.la
%{_tde_libdir}/libtaskbar.la
%{_tde_libdir}/libtaskmanager.la
%{_tde_libdir}/libkasbar.so
%{_tde_libdir}/libkasbar.la

%files ksysguardd
%defattr(-,root,root)
%dir /etc/slp.reg.d
%{_bindir}/ksysguardd
%{_tde_bindir}/ksysguardd
%config(noreplace) /etc/ksysguarddrc
/etc/init.d/ksysguardd
%{_sbindir}/rcksysguardd
%config(noreplace) /etc/slp.reg.d/*

%files -n fileshareset
%defattr(-,root,root)
%config(noreplace) /etc/security/fileshare.conf
%{_bindir}/filesharelist
%verify(not mode) %{_bindir}/fileshareset
%{_mandir}/man8/fileshareset.8.gz

%files apps
%defattr(-,root,root)
%{_tde_bindir}/konsole*
%{_tde_modulesdir}/konsole.*
%{_tde_modulesdir}/kcm_konsole.*
%{_tde_libdir}/libkdeinit_konsole.so
%{_tde_applicationsdir}/kde/konsole.desktop
%{_tde_applicationsdir}/kde/konsolesu.desktop
%doc %lang(en) %{_tde_htmldir}/en/konsole
%{_tde_applicationsdir}/kde/Home.desktop
%{_tde_libdir}/libkdeinit_konqueror.so
%{_tde_datadir}/konqueror/konq-simplebrowser.rc
%{_tde_applicationsdir}/kde/konquerorsu.desktop
%{_tde_appsdir}/konqueror.desktop
%doc %lang(en) %{_tde_htmldir}/en/konqueror
%{_tde_configdir}.kcfg/konqueror.kcfg
%{_tde_bindir}/konqueror
%{_tde_modulesdir}/konq*.so
%{_tde_modulesdir}/konq*.la
%dir %{_tde_datadir}/konqueror
%{_tde_datadir}/konqueror/tiles
%{_tde_datadir}/konqueror/about
%{_tde_datadir}/konqueror/icons
%{_tde_datadir}/konqueror/konqueror.rc
%{_tde_datadir}/konqueror/p*
%{_tde_datadir}/konqueror/servicemenus
%{_tde_modulesdir}/konqueror.*
%{_tde_datadir}/konqiconview
%{_tde_datadir}/konqlistview
%{_tde_datadir}/konqsidebartng
%{_tde_modulesdir}/kded_konqy_preloader.*
%{_tde_servicesdir}/kded/konqy_preloader.desktop
%{_tde_applicationsdir}/kde/konqbrowser.desktop
%{_tde_applicationsdir}/kde/konqfilemgr.desktop
%{_tde_configdir}.kcfg/konq_listview.kcfg
%config(noreplace) %{_tde_configdir}/konqsidebartng.rc
%{_tde_bindir}/kfind
%{_tde_modulesdir}/libkfindpart.*
%{_tde_applicationsdir}/kde/Kfind.desktop
%{_tde_datadir}/kfindpart
%{_tde_iconsdir}/*/*/*/kfind.*
%{_tde_servicesdir}/kfindpart.desktop
%doc %lang(en) %{_tde_htmldir}/en/kfind
%{_tde_bindir}/kwrite
%{_tde_modulesdir}/kwrite.*
%{_tde_libdir}/libkdeinit_kwrite.so
%{_tde_applicationsdir}/kde/kwrite.desktop
%{_tde_datadir}/kwrite
%{_tde_iconsdir}/*/*/*/kwrite.*
%doc %lang(en) %{_tde_htmldir}/en/kwrite
%{_tde_bindir}/kate
%{_tde_modulesdir}/kate.*
%{_tde_libdir}/libkateinterfaces.so.*
%{_tde_libdir}/libkateutils.so.*
%{_tde_libdir}/libkdeinit_kate.so
%{_tde_applicationsdir}/kde/kate.desktop
%{_tde_datadir}/kate
%{_tde_configdir}/katerc
%{_tde_iconsdir}/*/*/*/kate.*
%doc %lang(en) %{_tde_htmldir}/en/kate

%files workspace
%defattr(-,root,root)
%exclude %{_datadir}/default_blue.*
%doc %lang(en) %{_tde_htmldir}/en/kicker
%{_datadir}/wallpapers
%{_tde_bindir}/startkde
%{_tde_bindir}/kdesktop
%{_tde_bindir}/kdesktop_lock
%{_tde_bindir}/ksmserver
%{_tde_libdir}/libkdeinit_ksmserver.so
%{_tde_bindir}/ksplash                     
%{_tde_bindir}/ksplashsimple
%{_tde_modulesdir}/kdesktop.*
%{_tde_datadir}/kdesktop
%{_tde_configdir}.kcfg/kdesktop.kcfg
%config(noreplace) %{_tde_configdir}/kdesktop_custom_menu*
%{_tde_bindir}/kicker
%{_tde_modulesdir}/kicker*
%{_tde_modulesdir}/kcm_kicker*
%{_tde_libdir}/libkickermain.so.*
%{_tde_applicationsdir}/kde/kcmkicker.desktop
%{_tde_datadir}/kicker
%{_tde_configdir}.kcfg/kickerSettings.kcfg
%{_tde_iconsdir}/*/*/*/kcmkicker.*
%{_tde_iconsdir}/*/*/*/kicker.*
%{_tde_libdir}/kconf_update_bin/kicker-3.4-reverseLayout
%{_tde_bindir}/kwin
%{_tde_bindir}/kwin_killer_helper
%{_tde_bindir}/kwin_rules_dialog
%{_tde_modulesdir}/kwin_*
%{_tde_datadir}/kwin
%{_tde_modulesdir}/kwin.*
%{_tde_modulesdir}/kwin3_*
%{_tde_libdir}/kconf_update_bin/kwin_update_default_rules
%{_tde_libdir}/kconf_update_bin/kwin_update_window_settings
%{_tde_applicationsdir}/kde/kwinrules.desktop
%{_tde_applicationsdir}/kde/kwindecoration.desktop
%{_tde_applicationsdir}/kde/kwinoptions.desktop
%{_tde_configdir}.kcfg/kwin.kcfg
%{_tde_iconsdir}/*/*/*/kwin.*
/var/adm/fillup-templates/sysconfig.windowmanager-kdebase3
%{_tde_datadir}/ksplash
%{_tde_servicesdir}/ksplash.desktop
%{_tde_servicesdir}/ksplashdefault.desktop
%{_tde_servicesdir}/ksplashredmond.desktop
%{_tde_servicesdir}/ksplashstandard.desktop
%{_tde_servicetypesdir}/ksplashplugins.desktop
%{_tde_iconsdir}/*/*/*/ksplash.*
%{_tde_modulesdir}/ksplash*
%{_tde_libdir}/libksplashthemes.so.*
%{_tde_iconsdir}/*/*/apps/kcmsmserver.*
%{_tde_applicationsdir}/kde/kcmsmserver.desktop
%{_tde_modulesdir}/ksmserver.*
%{_tde_datadir}/ksmserver
%{_tde_modulesdir}/clock_panelapplet.*
%{_tde_modulesdir}/dockbar_panelextension.*
%{_tde_modulesdir}/kasbar_panelextension.*
%{_tde_modulesdir}/menu_panelapplet.*
%{_tde_modulesdir}/klipper_panelapplet.*
%{_tde_modulesdir}/launcher_panelapplet.*
%{_tde_modulesdir}/lockout_panelapplet.*
%{_tde_modulesdir}/minipager_panelapplet.*
%{_tde_modulesdir}/naughty_panelapplet.*
%{_tde_modulesdir}/run_panelapplet.*
%{_tde_modulesdir}/sidebar_panelextension.*
%{_tde_applicationsdir}/kde/panel.desktop
%{_tde_applicationsdir}/kde/panel_appearance.desktop
%{_tde_modulesdir}/media_panelapplet.*
%{_tde_modulesdir}/kcm_taskbar.*
%{_tde_applicationsdir}/kde/kcmtaskbar.desktop
%{_tde_configdir}.kcfg/taskbar.kcfg
%{_tde_iconsdir}/*/*/apps/kcmtaskbar.*
%{_tde_modulesdir}/kcm_screensaver.*
%{_tde_applicationsdir}/kde/screensaver.desktop
%{_tde_appsdir}/System/ScreenSavers/KBlankscreen.desktop
%{_tde_appsdir}/System/ScreenSavers/KRandom.desktop
%{_tde_bindir}/kwebdesktop
%{_tde_configdir}.kcfg/kwebdesktop.kcfg
%{_tde_applicationsdir}/kde/background.desktop
%{_tde_modulesdir}/kcm_background*
%{_tde_bindir}/default_desktop_aligning
%{_tde_applicationsdir}/kde/desktop.desktop
%{_tde_applicationsdir}/kde/desktopbehavior.desktop
%{_tde_applicationsdir}/kde/ksplashthememgr.desktop
%{_tde_iconsdir}/*/*/apps/kcmdesktop.*
%{_tde_iconsdir}/*/*/apps/kcmdesktopbehavior.*
%{_tde_modulesdir}/kcm_ksplashthemes.*
%{_tde_modulesdir}/kcm_kwindecoration.*
%{_tde_modulesdir}/kcm_kwinoptions.*
%{_tde_modulesdir}/kcm_kwinrules.*
%doc %lang(en) %{_tde_htmldir}/en/ksplashml
%{_tde_prefix}/shutdown
%{_tde_libdir}/libkickoffsearch_interfaces.so.*
%{_tde_servicetypesdir}/kickoffsearchplugin.desktop
%{_tde_sharedir}/autostart/*
%{_tde_datadir}/naughtyapplet
%{_tde_libdir}/libtask*.so.*
%{_tde_bindir}/extensionproxy
%{_tde_bindir}/appletproxy
%{_tde_modulesdir}/appletproxy.*
%{_tde_modulesdir}/extensionproxy.*
%{_tde_modulesdir}/taskbar*
%{_tde_modulesdir}/trash_panelapplet*
%{_tde_modulesdir}/sys*
%{_tde_datadir}/clockapplet
%{_tde_bindir}/kasbar
%{_tde_libdir}/libkasbar.so.*
%{_tde_libdir}/libkdeinit_kicker.so
%{_tde_libdir}/libkdeinit_appletproxy.so
%{_tde_libdir}/libkdeinit_extensionproxy.so
%{_tde_libdir}/libkdeinit_kdesktop.so
%{_tde_libdir}/libkdeinit_kwin.so
%{_tde_libdir}/libkdeinit_kwin_rules_dialog.so
%{_tde_bindir}/ktip
%{_tde_sharedir}/appl*/*/ktip.desktop
%{_tde_iconsdir}/*/*/*/ktip.*
%{_tde_bindir}/kpager
%{_tde_sharedir}/appl*/*/kpager.desktop
%{_tde_iconsdir}/*/*/*/kpager.*
%doc %lang(en) %{_tde_htmldir}/en/kpager
%{_tde_bindir}/klipper
%{_tde_modulesdir}/klipper.*
%{_tde_libdir}/libkdeinit_klipper.so
%{_tde_applicationsdir}/kde/klipper.desktop
%config(noreplace) %{_tde_configdir}/klipperrc
%{_tde_iconsdir}/*/*/*/klipper.*
%doc %lang(en) %{_tde_htmldir}/en/klipper
%{_tde_applicationsdir}/kde/kmenuedit.desktop
%{_tde_datadir}/kmenuedit
%{_tde_iconsdir}/*/*/*/kmenuedit.*
%doc %lang(en) %{_tde_htmldir}/en/kmenuedit
%{_tde_bindir}/kmenuedit
%{_tde_modulesdir}/kmenuedit.*
%{_tde_libdir}/libkdeinit_kmenuedit.so
%{_tde_bindir}/kinfocenter
%{_tde_applicationsdir}/kde/kinfocenter.desktop
%{_tde_datadir}/kinfocenter
%doc %lang(en) %{_tde_htmldir}/en/kinfocenter
%doc %lang(en) %{_tde_htmldir}/en/khelpcenter/userguide
%doc %lang(en) %{_tde_htmldir}/en/khelpcenter/visualdict
%{_tde_sounddir}/KDE_Close_Window*
%{_tde_sounddir}/KDE_Dialog*
%{_tde_sounddir}/KDE_Desktop*
%{_tde_sounddir}/KDE_Logout*
%{_tde_sounddir}/KDE_Startup*
%{_tde_sounddir}/KDE_Window*
%{_tde_libdir}/libkdeinit_khotkeys.so
%{_tde_modulesdir}/kcm_khotkeys.*
%{_tde_modulesdir}/kcm_khotkeys_init.*
%{_tde_iconsdir}/*/*/*/khotkeys.*
%{_tde_bindir}/khotkeys
%{_tde_libdir}/kconf_update_bin/khotkeys_update
%{_tde_modulesdir}/khotkeys.*
%{_tde_modulesdir}/kded_khotkeys.*
%{_tde_libdir}/libkhotkeys_shared.so.*
%{_tde_applicationsdir}/kde/khotkeys.desktop
%{_tde_datadir}/khotkeys
%{_tde_servicesdir}/kded/khotkeys.desktop
%{_tde_bindir}/ksysguard
%{_tde_applicationsdir}/kde/ksysguard.desktop
%{_tde_datadir}/ksysguard
%{_tde_iconsdir}/*/*/*/ksysguard.*
%{_tde_mimedir}/application/x-ksysguard.desktop
%doc %lang(en) %{_tde_htmldir}/en/ksysguard
%doc %lang(en) %{_tde_htmldir}/en/kxkb
%{_tde_libdir}/libksgrd.so.*
%{_tde_bindir}/kompmgr
%doc %lang(en) %{_tde_htmldir}/en/kompmgr

%files runtime
%defattr(-,root,root)
%doc %lang(en) %{_tde_htmldir}/en/kioslave
%exclude %{_tde_modulesdir}/kio_smb.*
%exclude %{_tde_servicesdir}/smb.protocol
%{_tde_bindir}/kde3
%{_tde_bindir}/kreadconfig
%{_tde_bindir}/kwriteconfig
%{_tde_bindir}/kprinter
%{_tde_libdir}/libkdeinit_kprinter.so
%{_tde_bindir}/kdesu
%{_tde_modulesdir}/kio_*
%{_tde_libdir}/libkfontinst.so.*
%{_tde_servicesdir}/*.protocol
%{_tde_libdir}/libkonq.so.*
%{_tde_libdir}/libkonqsidebarplugin.so.*
%{_tde_modulesdir}/kded_favicons.*
%{_tde_servicesdir}/kded/favicons.desktop
%{_tde_libdir}/libkdecorations.so.*
%{_tde_modulesdir}/kgreet_winbind.*
%{_tde_modulesdir}/kgreet_classic.*
%config /etc/pam.d/kcheckpass
%verify(not mode) %attr(4755,root,shadow) %{_tde_bindir}/kcheckpass
%{_tde_iconsdir}/*/*/*/knotify.*
%{_tde_iconsdir}/*/*/*/kscreensaver.*
%{_tde_iconsdir}/*/*/*/style.*
%{_tde_iconsdir}/*/*/*/looknfeel.*
%{_tde_iconsdir}/*/*/*/iconthemes.*
%{_tde_iconsdir}/*/*/*/keyboard.*
%{_tde_iconsdir}/*/*/*/kcmsound.*
%{_tde_iconsdir}/*/*/*/energy.*
%{_tde_iconsdir}/*/*/*/kcmkwm.*
%{_tde_iconsdir}/*/*/*/hwinfo.*
%{_tde_iconsdir}/*/*/*/date.*
%{_tde_iconsdir}/*/*/*/filetypes.*
%{_tde_iconsdir}/*/*/*/kcmsystem.*
%{_tde_iconsdir}/*/*/*/personal.*

%changelog
