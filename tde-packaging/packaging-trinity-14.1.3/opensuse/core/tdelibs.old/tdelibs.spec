#
# spec file for package tdelibs
#
# Copyright (c) 2011 the Trinity Project (opensuse).
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
  
# Please submit bugfixes or comments via http://bugs.trinitydesktop.org/
#

# norootforbuild


Name:           tdelibs
BuildRequires:  OpenEXR-devel arts arts-devel aspell-devel cups-devel fam-devel flac-devel krb5-devel
BuildRequires:  libart_lgpl-devel libidn-devel libsndfile libtiff-devel
BuildRequires:  libxslt-devel openldap2-devel pcre-devel libtqt4-devel sgml-skel
BuildRequires:  db-devel libacl-devel libattr-devel unsermake update-desktop-files utempter
BuildRequires:  unzip
BuildRequires:  avahi-compat-mDNSResponder-devel fdupes libbz2-devel libjasper-devel
BuildRequires:  libdrm-devel tde-filesystem cmake
URL:            http://www.trinitydesktop.org/
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Group:          System/GUI/TDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Trinity Base Libraries
Version:        R13.99
Release:        1
Provides:       kups keramik tdelibs-cups tdelibs-33addons tdepim-networkstatus
Provides:       kdelibs3_base = 3.3
Requires:       libtqt4 >= %( echo `rpm -q --queryformat '%{VERSION}' libtqt4`)
Requires:       openssl tdelibs-default-style
Requires:       hicolor-icon-theme
Recommends:     ispell enscript
Requires:       sudo
Source0:        %{name}-%{version}.tar.bz2
Source3:        baselibs.conf
Source4:        api_docu_description
Source6:        tderc
# svn export svn://anonsvn.kde.org/home/kde/branches/KDE/3.5/kde-common/admin
Source8:        admin.tar.bz2
Source9:        cr16-filesys-file_broken.png
Source10:       kdemm-20050330.tar.bz2
Source11:       10888-bt.tar.gz
Source12:       mimetype-icons.tar.bz2
Source14:       vnd.openxmlformats-officedocument.wordprocessingml.document.desktop
Source15:       vnd.openxmlformats-officedocument.presentationml.presentation.desktop
Source16:       vnd.openxmlformats-officedocument.spreadsheetml.sheet.desktop

%description
This package contains tdelibs, one of the basic packages of the Trinity
Desktop Environment. It contains the necessary libraries for the Trinity
desktop.

This package is absolutely necessary for using TDE.

%package arts
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Summary:        TDE aRts support
Group:          System/GUI/TDE
Provides:       tdelibs:/opt/tde/bin/artsmessage
Requires:       arts >= %( echo `rpm -q --queryformat '%{VERSION}' arts`)
Recommends:     tdemultimedia-arts

%description arts
This package contains bindings and gui elements for using aRts sound
daemon.

%package default-style
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Summary:        The default TDE style
Group:          System/GUI/TDE
Provides:       tdelibs:%{_tde_libdir}/libtdefx.so.4

%description default-style
This package contains the Plastik widget style and libkdefx. It only
depends on TQt, not the KDE libraries.

%package doc
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Summary:        Documentation for TDE Base Libraries
Group:          System/GUI/TDE
Provides:       tdelibs:/opt/tde/share/apps/ksgmltools2
Provides:       tdelibs_doc
Requires:       sgml-skel libxml2
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         sed grep awk

%description doc
This package contains the core environment and templates for the Trinity
help system.

%package devel
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
# usefiles /opt/tde/bin/dcopidl /opt/tde/bin/dcopidl2cpp /opt/tde/bin/kdb2html /opt/tde/bin/preparetips 
Requires:       libtqt4-devel libvorbis-devel tdelibs = %version autoconf automake libxslt-devel libxml2-devel libart_lgpl-devel libjpeg-devel tde-filesystem
# next line from tde-devel-packages macro
Requires:       tdelibs-doc libtiff-devel openssl-devel update-desktop-files
Requires:       libdrm-devel dbus-1-tqt-devel
Requires:       libattr-devel libacl-devel
Requires:       tdelibs-arts
Summary:        Trinity Base Package: Build Environment
Group:          System/GUI/TDE
Requires:       fam-devel pcre-devel libidn-devel arts-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
  echo %suse_version
%setup -q
tar xfvj %SOURCE10
rm -rf admin
bunzip2 -cd %{SOURCE8} | tar xfv - --exclude=.cvsignore --exclude=CVS

tar xfvj %SOURCE12
#
# define KDE version exactly
#
myrelease=$(echo %release | cut -d. -f-1)
sed 's,#define KDE_VERSION_STRING "\(.*\)",#define KDE_VERSION_STRING "\1 \\"release '$myrelease'\\"",' kdecore/kdeversion.h > kdecore/kdeversion.h_ && mv kdecore/kdeversion.h_ kdecore/kdeversion.h
#
# create build enviroment
# 
#UNSERMAKE=yes make -f admin/Makefile.common cvs

%build
export PATH=$PWD/admin/:$PATH
FINAL="--enable-final"
CFLAGS="$CFLAGS -fno-strict-aliasing"
CXXFLAGS="$CXXFLAGS -fno-strict-aliasing"

# common_options and do_make have been obsoleted by tde-filesystem

  export path_sudo=/usr/bin/sudo
  #
  # define the distribution exactly
  #
  test -e /.buildenv && . /.buildenv
%if %is_plus
  # supplementary package
  DISTRI="openSUSE $BUILD_DISTRIBUTION_VERSION UNSUPPORTED"
%else
  # official build on released and maintained products
  DISTRI="openSUSE $BUILD_DISTRIBUTION_VERSION"
%endif
  sed 's,#define KDE_VERSION_STRING "\(.*\)",#define KDE_VERSION_STRING "\1 '"$ADD_VERSION"'",' kdecore/kdeversion.h > kdecore/kdeversion.h_ && mv kdecore/kdeversion.h_ kdecore/kdeversion.h
  # find MIT kerberos
  export PATH=/usr/lib/mit/bin:$PATH
  # fast-malloc is not needed anymore

EXTRA_FLAGS="-DCMAKE_SKIP_RPATH=OFF -DKDE_MALLOC_FULL=OFF -DKDE_MALLOC=OFF -DSSL_INSTALL_DIR=/usr/ssl -DPCSC_INSTALL_DIR=/usr -DENABLE_DNOFIFY=ON"

# -DKDE_DISTRIBUTION=\"$DISTRI\"

#	%if %is_plus
#	-DENABLE_DNOFIFY=ON \
#	%endif

%cmake_tde -d build -- $EXTRA_FLAGS

%make_tde -d build

#
xmlcatbin=/usr/bin/xmlcatalog
# CATALOG=docbook-simple.xml
# $xmlcatbin --noout --create $CATALOG
# $xmlcatbin --noout --add "public" \
#   "-//OASIS//DTD Simplified DocBook XML V1.0//EN" \
#   "file://%{xml_mod_dtd_dir}/sdocbook.dtd" $CATALOG
# $xmlcatbin --noout --add "system" \
#   "http://www.oasis-open.org/docbook/xml/simple/1.0/sdocbook.dtd" \
#   "file://%{xml_mod_dtd_dir}/sdocbook.dtd" $CATALOG
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=%{_tde_prefix}/share/apps/ksgmltools2/customization/catalog.xml
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
# $xmlcatbin --noout --add "delegateSystem" \
#   "http://www.oasis-open.org/docbook/xml/simple/" \
#   "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//KDE//DTD DocBook XML V4.2" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//KDE//ELEMENTS" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//KDE//ENTITIES" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
  %makeinstall_tde -d build
  mkdir -p $RPM_BUILD_ROOT/%{_tde_configkcfgdir}
  install -D %SOURCE9 $RPM_BUILD_ROOT/%{_tde_icondir}/crystalsvg/16x16/filesystems/file_broken.png
  mv $RPM_BUILD_ROOT/etc/xdg/menus/applications.menu \
     $RPM_BUILD_ROOT/etc/xdg/menus/applications.menu.kde
  #
  # lib64 compatibility symlink
  #
%ifarch x86_64 ppc64 s390x mips64 sparc64
    mkdir -p $RPM_BUILD_ROOT/%{_tde_prefix}/lib/kde3/
    ln -sf ../../lib64/kde3/plugins \
         $RPM_BUILD_ROOT/%{_tde_prefix}/lib/kde3/plugins-lib64
%endif
  #
  # add missing directories
  #
  for i in Applications Development Editors Edutainment Games Graphics Internet Multimedia Office Settings System Toys Utilities WordProcessing; do
    install -d -m 0755 $RPM_BUILD_ROOT/%{_tde_appsdir}/$i
  done
  rm -f locale.list
  for i in $(find /usr/share/locale -mindepth 1 -maxdepth 1 -type d | sed 's:/usr/share/locale/::'); do
    install -d -m 755 $RPM_BUILD_ROOT/%{_tde_locale}/$i
    install -d -m 755 $RPM_BUILD_ROOT/%{_tde_locale}/$i/LC_MESSAGES
    install -d -m 755 $RPM_BUILD_ROOT/%{_tde_htmldir}/$i
    echo "%lang($i) %doc %{_tde_locale}/$i" >> locale.list
  done
  %suse_update_desktop_file kresources X-KDE-settings-desktop
  # unlike with other modules, tde_post_install shouldn't
  # be put at the end of %install
  %tde_post_install
  # now create a filesystem layer
  for theme in hicolor locolor; do
    for j in actions apps filesystems mimetypes; do
      for i in 16 22 32 48 64 128; do
        install -d -m 0755 $RPM_BUILD_ROOT/%{_tde_icondir}/${theme}/${i}x${i}/${j}
      done
      install -d -m 0755 $RPM_BUILD_ROOT/%{_tde_icondir}/${theme}/scalable/${j}
    done
  done
  install -d -m 0755 $RPM_BUILD_ROOT/etc/%{_tde_libdir}
  install -d -m 0755 $RPM_BUILD_ROOT/etc/%{_tde_configdir}
  install -d -m 0755 $RPM_BUILD_ROOT/%{_tde_datadir}/kdelibs/
  install -m 0644 %SOURCE6 $RPM_BUILD_ROOT/etc/
  rm -f $RPM_BUILD_ROOT/%{_tde_libdir}/libkdeinit_*.la
  #
  # add additional icon path (not needed anymore? we use cmake)
  #
  #mkdir -p ${RPM_BUILD_ROOT}/%{_tde_datadir}/kdelibs
  #rm -f admin/*.orig
  #cp -a admin ${RPM_BUILD_ROOT}/%{_tde_datadir}/kdelibs/
  # This is not needed on SUSE Linux! - Marcus Meissner <meissner@suse.de>
  rm $RPM_BUILD_ROOT/%{_tde_bindir}/kgrantpty
  #
  # our version is in kdebase3
  #
  rm -f $RPM_BUILD_ROOT/%{_tde_bindir}/fileshare*
  #
  # no sources for man pages
  #
  rm -f $RPM_BUILD_ROOT/%{_tde_htmldir}/en/kdelibs/man-*
  # 
  # install BitTorrent icons
  #
  tar xfvz %SOURCE11
  for i in 16x16 22x22 32x32 48x48 64x64 128x128 ; do
      install -m 0644 bt/$i/mimetypes/bt.png \
              $RPM_BUILD_ROOT/%{_tde_icondir}/crystalsvg/$i/mimetypes/torrent.png
  done
  #cp CATALOG.%{name} catalog.xml ${RPM_BUILD_ROOT}/%{_tde_datadir}/ksgmltools2/customization/
  cp catalog.xml ${RPM_BUILD_ROOT}/%{_tde_datadir}/ksgmltools2/customization/
  mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/xml
  cp %{FOR_ROOT_CAT} ${RPM_BUILD_ROOT}%{_sysconfdir}/xml
#  rm -f $RPM_BUILD_ROOT/%{_tde_libdir}/libkdefakes.la
#  rm -f $RPM_BUILD_ROOT/%{_tde_libdir}/libkjava.la
rm -f $RPM_BUILD_ROOT/%{_tde_icondir}/hicolor/index.theme
  # .desktop files in kdeaccessibility3 require the kttsd icon
  for i in {16x16,22x22,32x32,48x48,64x64,128x128,scalable}; do mv $RPM_BUILD_ROOT/%{_tde_icondir}/crystalsvg/$i/apps/kttsd.* $RPM_BUILD_ROOT/%{_tde_icondir}/hicolor/$i/apps/;done
  install -m 0644 %SOURCE14 $RPM_BUILD_ROOT/%{_tde_mimedir}/application/
  install -m 0644 %SOURCE15 $RPM_BUILD_ROOT/%{_tde_mimedir}/application/
  install -m 0644 %SOURCE16 $RPM_BUILD_ROOT/%{_tde_mimedir}/application/
  # fix bnc#396153
  for i in 16x16 22x22 32x32 48x48 64x64 128x128; do
    ln -s %{_tde_icondir}/crystalsvg/$i/filesystems/network.png $RPM_BUILD_ROOT/%{_tde_icondir}/crystalsvg/$i/filesystems/preferences-system-network.png
    ln -s %{_tde_icondir}/crystalsvg/$i/filesystems/desktop.png $RPM_BUILD_ROOT/%{_tde_icondir}/crystalsvg/$i/filesystems/preferences-desktop.png
  done
  chmod a-x $RPM_BUILD_ROOT/%{_tde_icondir}/crystalsvg/16x16/filesystems/file_broken.png
  %fdupes -s $RPM_BUILD_ROOT
  mkdir -p $RPM_BUILD_ROOT/etc/%{_tde_applicationsdir}
  touch $RPM_BUILD_ROOT/etc/%{_tde_applicationsdir}/mimeinfo.cache
  mkdir -p $RPM_BUILD_ROOT/%{_tde_applicationsdir}
  touch $RPM_BUILD_ROOT/%{_tde_applicationsdir}/mimeinfo.cache
# Create /etc/ld.so.conf.d/kdelibs3.conf 
mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
cat > $RPM_BUILD_ROOT/etc/ld.so.conf.d/tdelibs.conf <<EOF
%ifarch s390x sparc64 x86_64 ppc64
/opt/tde/lib64
%endif
/opt/tde/lib
EOF

# Fix Kspell symlink
rm -fv $RPM_BUILD_ROOT/opt/tde/share/doc/kde/HTML/en/kspell/common
ln -sfv /opt/tde/share/doc/kde/HTML/en/common $RPM_BUILD_ROOT/opt/tde/share/doc/kde/HTML/en/kspell/common

# move cmake to %{_datadir}
mkdir -pv %{buildroot}/%{_datadir}/cmake
mv -v %{buildroot}/%{_tde_sharedir}/cmake/tdelibs.cmake %{buildroot}/%{_datadir}/cmake

%post
/sbin/ldconfig
%run_permissions

%postun
  rm -f usr/share/doc/KDE3-API/index.html
/sbin/ldconfig

%post arts
/sbin/ldconfig

%postun arts
/sbin/ldconfig

%post default-style
/sbin/ldconfig

%postun default-style
/sbin/ldconfig

%post doc
  if [ -x %{regcat} ]; then
    %{regcat} -a %{_tde_datadir}/ksgmltools2/customization/CATALOG.%{name} >/dev/null 2>&1
  fi
  if [ -x /usr/bin/edit-xml-catalog ]; then
    edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
      --add /etc/xml/%{FOR_ROOT_CAT}
  fi

%postun doc
  if [ "$1" = "0" -a -x %{regcat} ]; then
    %{regcat} -r %{_tde_datadir}/ksgmltools2/customization/CATALOG.%{name} >/dev/null 2>&1
  fi
  # remove entries only on removal of file
  if [ ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} -a -x /usr/bin/edit-xml-catalog ] ; then
    edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
      --del %{name}-%{version}
  fi
  exit 0

%clean
  rm -rf ${RPM_BUILD_ROOT}

%files default-style
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.BSD COPYING.LIB NAMING README 
%{_tde_libdir}/libtdefx.so.*
%{_tde_libdir}/trinity/plugins/styles/plastik.*

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.BSD COPYING.LIB NAMING README 
/etc/ld.so.conf.d/tdelibs.conf
%dir /etc/%{_tde_prefix}
%dir %{_tde_prefix}
%dir %{_tde_bindir}
%dir %{_tde_includedir}
%dir %{_tde_sharedir}
%dir %{_tde_configkcfgdir}
%{_tde_bindir}/checkXML
%{_tde_bindir}/dcop
%{_tde_bindir}/dcopclient
%{_tde_bindir}/dcopfind
%{_tde_bindir}/dcopobject
%{_tde_bindir}/dcopref
%{_tde_bindir}/dcops*
%{_tde_bindir}/dcopquit
%{_tde_bindir}/imagetops
%{_tde_bindir}/ka*
%{_tde_bindir}/kbuildsycoca
%{_tde_bindir}/kco*
%{_tde_bindir}/kcmshell
%{_tde_bindir}/kded
%{_tde_bindir}/kdetcompmgr
%{_tde_bindir}/networkstatustestservice
%{_tde_bindir}/tdeinit*
%{_tde_bindir}/start_tdeinit
%{_tde_bindir}/start_tdeinit_wrapper
%{_tde_bindir}/tde-config
%{_tde_bindir}/kde-menu
%{_tde_bindir}/tdesu_stub
%{_tde_bindir}/kdontchangethehostname
%{_tde_bindir}/kfile
%{_tde_bindir}/ki*
%{_tde_bindir}/kfmexec
%{_tde_bindir}/klauncher
%{_tde_bindir}/kmailservice
%{_tde_bindir}/ktradertest
%{_tde_bindir}/kstartupconfig
%{_tde_bindir}/kdostartupconfig
%verify(not mode) %{_tde_bindir}/kpac_dhcp_helper
%{_tde_bindir}/ksendbugmail
%{_tde_bindir}/kshell
%{_tde_bindir}/ktelnetservice
%{_tde_bindir}/kwrapper
%{_tde_bindir}/lnusertemp
%{_tde_bindir}/make_driver_db_lpr
%{_tde_bindir}/khotnewstuff
%{_tde_bindir}/makekdewidgets
%dir %{_tde_libdir}
%dir %{_tde_libdir}/trinity
%{_tde_libdir}/trinity/dcopserver.*
%{_tde_libdir}/trinity/kaddprinterwizard.*
%{_tde_libdir}/trinity/kbuildsycoca.*
%{_tde_libdir}/trinity/kcmshell.*
%{_tde_libdir}/trinity/kcm_kresources.*
%{_tde_libdir}/trinity/kconf_update.*
%{_tde_libdir}/trinity/kcookiejar.*
%{_tde_libdir}/trinity/kded.*
%{_tde_libdir}/trinity/kded_proxyscout.*
%{_tde_libdir}/trinity/kfileaudiopreview.*
%{_tde_libdir}/trinity/klauncher.*
%{_tde_libdir}/trinity/knotify.*
%{_tde_libdir}/trinity/kabc*
%{_tde_libdir}/trinity/kbzip2filter.*
%{_tde_libdir}/trinity/kded_k*
%{_tde_libdir}/trinity/tdeprint_ext.*
%{_tde_libdir}/trinity/tdeprint_lp*
%{_tde_libdir}/trinity/tdeprint_rlpr.*
%{_tde_libdir}/trinity/tdeprint_tool_escputil.*
%{_tde_libdir}/trinity/kgzipfilter.*
%{_tde_libdir}/trinity/khtmlimagepart.*
%{_tde_libdir}/trinity/ki*
%{_tde_libdir}/trinity/kjavaappletviewer.*
%{_tde_libdir}/trinity/ktexteditor_*
%{_tde_libdir}/trinity/libk*
%{_tde_libdir}/trinity/kspell_*
%{_tde_libdir}/trinity/kstyle_plastik_config.*
%{_tde_libdir}/trinity/kstyle_highcontrast_config.*
%{_tde_libdir}/trinity/libshellscript.*
# unsure
%{_tde_libdir}/trinity/kded_tdeprintd.*
%{_tde_libdir}/trinity/libtdeprint_management_module.*
# end unsure
%exclude %{_tde_libdir}/trinity/plugins/styles/plastik.*
%{_tde_libdir}/trinity/plugins
%{_tde_libdir}/libDCOP.so.*
%exclude %{_tde_libdir}/libtdefx.so.*
%{_tde_libdir}/libk*.so.*
%{_tde_libdir}/libvcard.so.*
%{_tde_libdir}/libtdecore.so.*
%{_tde_libdir}/libtdefakes.so.*
%{_tde_libdir}/libtdeinit*.so
%{_tde_libdir}/libtdeprint.so.*
%{_tde_libdir}/libtdeprint_management.so.*
%{_tde_libdir}/libtdesasl.so.*
%{_tde_libdir}/libtdesu.so.*
%{_tde_libdir}/libtdeui.so.*
%{_tde_libdir}/libnetworkstatus.so.*
%{_tde_libdir}/libconnectionmanager.so.*
%{_tde_libdir}/trinity/kded_networkstatus.*
%{_tde_appsdir}
%dir %{_tde_datadir}
%{_tde_datadir}/LICENSES
%{_tde_datadir}/ka*
%{_tde_datadir}/kc*
%dir %{_tde_datadir}/tdeprint
%{_tde_datadir}/tdeprint/apsdriver*
%{_tde_datadir}/tdeprint/filters
%{_tde_datadir}/tdeprint/icons
%{_tde_datadir}/tdeprint/lprngtooldriver1
%{_tde_datadir}/tdeprint/pics
%dir %{_tde_datadir}/tdeprint/plugins
%{_tde_datadir}/tdeprint/plugins/ext.print
%{_tde_datadir}/tdeprint/plugins/lp*.print
%{_tde_datadir}/tdeprint/plugins/rlpr.print
%{_tde_datadir}/tdeprint/s*
%{_tde_datadir}/tdeprint/t*
%{_tde_datadir}/tdeui
%{_tde_datadir}/kdewidgets
%{_tde_datadir}/khtml
%{_tde_datadir}/kio_uiserver
%{_tde_datadir}/kjava
%{_tde_datadir}/knotify
%{_tde_datadir}/kssl
%{_tde_datadir}/kstyle
%{_tde_datadir}/ktexteditor_*
%{_tde_datadir}/proxyscout
%{_tde_datadir}/knewstuff
%{_tde_sharedir}/autostart
%{_tde_configdir}
%{_tde_sharedir}/emoticons
%{_tde_icondir}
%{_tde_locale}
%{_tde_mimedir}
%{_tde_sharedir}/service*
%config /etc/tderc
%{_tde_applicationsdir}
%{_tde_bindir}/cupsd*
%{_tde_bindir}/make_driver_db_cups
%{_tde_libdir}/trinity/tdeprint_cups.*
%{_tde_libdir}/trinity/cupsdconf.*
%{_tde_datadir}/tdeprint/cups*
%{_tde_datadir}/tdeprint/kde_logo.png
%{_tde_datadir}/tdeprint/plugins/cups.print
%{_tde_datadir}/tdeprint/preview*
%ifarch x86_64 ppc64 s390x mips64 sparc64
%dir %{_tde_prefix}/lib
%dir %{_tde_prefix}/lib/trinity
%{_tde_prefix}/lib/trinity/plugins-lib64
%endif
/etc/xdg/menus
%dir /etc/%{_tde_prefix}
%dir /etc/%{_tde_sharedir}
%dir /etc/%{_tde_applicationsdir}
%ghost /etc/%{_tde_applicationsdir}/mimeinfo.cache
%dir %{_tde_prefix}
%dir %{_tde_sharedir}
%dir %{_tde_applicationsdir}
%ghost %{_tde_applicationsdir}/mimeinfo.cache
%dir %{_tde_datadir}/konqueror
%dir %{_tde_datadir}/konqueror/servicemenus
%{_tde_datadir}/konqueror/servicemenus/isoservice.desktop

%files arts
%defattr(-,root,root)
%{_tde_bindir}/artsmessage
%{_tde_libdir}/libartskde.so.*

%files doc
%defattr(-,root,root)
%doc %{_tde_docdir}
%{_tde_bindir}/meinproc
%{_tde_datadir}/ksgmltools2
%config %{_sysconfdir}/xml/%{FOR_ROOT_CAT}

%files devel
%defattr(-,root,root)
%dir %{_tde_datadir}/kdelibs
%{_tde_bindir}/dcopidl*
%{_tde_bindir}/kmimelist
%{_tde_bindir}/preparetips
%{_tde_bindir}/kunittestmodrunner
#%{_tde_bindir}/MISC
%{_tde_includedir}/*
%{_tde_datadir}/dcopidlng
%{_tde_libdir}/libartskde.la
%{_tde_libdir}/libkunittest.la
%{_tde_libdir}/libkunittest.so
%{_tde_libdir}/libartskde.so
%{_tde_libdir}/libDCOP.so
%{_tde_libdir}/libvcard.so
%{_tde_libdir}/libvcard.la
%{_tde_libdir}/libDCOP.la
%{_tde_libdir}/lib*.a
%{_tde_libdir}/libkabc_dir.la
%{_tde_libdir}/libkabc_dir.so
%{_tde_libdir}/libkabc_file.la
%{_tde_libdir}/libkabc_file.so
%{_tde_libdir}/libkabc.la
%{_tde_libdir}/libkabc_ldapkio.la
%{_tde_libdir}/libkabc_ldapkio.so
%{_tde_libdir}/libkabc_net.la
%{_tde_libdir}/libkabc_net.so
%{_tde_libdir}/libkabc.so
%{_tde_libdir}/libkatepartinterfaces.la
%{_tde_libdir}/libkatepartinterfaces.so
%{_tde_libdir}/libtdecore.la
%{_tde_libdir}/libtdecore.so
%{_tde_libdir}/libtdefakes.la
%{_tde_libdir}/libtdefakes.so
%{_tde_libdir}/libtdefx.la
%{_tde_libdir}/libtdefx.so
%{_tde_libdir}/libtdeinit*.la
%{_tde_libdir}/libtdeprint.la
%{_tde_libdir}/libtdeprint_management.la
%{_tde_libdir}/libtdeprint_management.so
%{_tde_libdir}/libtdeprint.so
%{_tde_libdir}/libtdesasl.la
%{_tde_libdir}/libtdesasl.so
%{_tde_libdir}/libtdesu.la
%{_tde_libdir}/libtdesu.so
%{_tde_libdir}/libtdeui.la
%{_tde_libdir}/libtdeui.so
%{_tde_libdir}/libkdnssd.la
%{_tde_libdir}/libkdnssd.so
%{_tde_libdir}/libkglib.la
%{_tde_libdir}/libkglib.so
%{_tde_libdir}/libkhtml.la
%{_tde_libdir}/libkhtml.so
%{_tde_libdir}/libkimproxy.la
%{_tde_libdir}/libkimproxy.so
%{_tde_libdir}/libkio.la
%{_tde_libdir}/libkio.so
%{_tde_libdir}/libkjava.la
%{_tde_libdir}/libkjava.so
%{_tde_libdir}/libkjs.la
%{_tde_libdir}/libkjs.so
%{_tde_libdir}/libkmdi2.la
%{_tde_libdir}/libkmdi2.so
%{_tde_libdir}/libkmdi.la
%{_tde_libdir}/libkmdi.so
%{_tde_libdir}/libkmediaplayer.la
%{_tde_libdir}/libkmediaplayer.so
%{_tde_libdir}/libkmid.la
%{_tde_libdir}/libkmid.so
%{_tde_libdir}/libknewstuff.la
%{_tde_libdir}/libknewstuff.so
%{_tde_libdir}/libkntlm.la
%{_tde_libdir}/libkntlm.so
%{_tde_libdir}/libkparts.la
%{_tde_libdir}/libkparts.so
%{_tde_libdir}/libkrandr.la
%{_tde_libdir}/libkrandr.so
%{_tde_libdir}/libkresources.la
%{_tde_libdir}/libkresources.so
%{_tde_libdir}/libkrsync.la
%{_tde_libdir}/libkrsync.so
%{_tde_libdir}/libkscreensaver.la
%{_tde_libdir}/libkscreensaver.so
%{_tde_libdir}/libkscript.la
%{_tde_libdir}/libkscript.so
%{_tde_libdir}/libkspell2.la
%{_tde_libdir}/libkspell2.so
%{_tde_libdir}/libkspell.la
%{_tde_libdir}/libkspell.so
%{_tde_libdir}/libktexteditor.la
%{_tde_libdir}/libktexteditor.so
%{_tde_libdir}/libkutils.la
%{_tde_libdir}/libkutils.so
%{_tde_libdir}/libkwalletbackend.la
%{_tde_libdir}/libkwalletbackend.so
%{_tde_libdir}/libkwalletclient.la
%{_tde_libdir}/libkwalletclient.so
%{_tde_libdir}/libnetworkstatus.la
%{_tde_libdir}/libnetworkstatus.so
%{_tde_libdir}/libconnectionmanager.la
%{_tde_libdir}/libconnectionmanager.so
%{_datadir}/cmake/tdelibs.cmake

%changelog
