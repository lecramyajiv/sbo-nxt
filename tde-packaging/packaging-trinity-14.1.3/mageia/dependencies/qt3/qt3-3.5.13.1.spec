%define Werror_cflags %nil

# QTDIR is always /usr/lib/qt3, whether that's a lib64 architecture or
# not (sublibdirs are correctly qualified in the latter case however).
%define qtdir	%{_prefix}/lib/qt3
%define libqt3name	%mklibname qt 3

%define libqassistantname %mklibname qassistantclient 1
%define libdesignercore %mklibname designercore 1
%define libeditor %mklibname editor 1

%define nameqt	qt-x11-free

%define buildSQL 1
%{?_without_SQL: %{expand4 %%global buildSQL 0}}

%define buildDebug 0
%{?_with_debug: %{expand: %%global buildDebug 1}}

%define buildStatic 1
%{?_without_static: %{expand: %%global buildStatic 0}}

%define buildImmodule 1
%{?_without_immodule: %{expand: %%global buildImmodule 0}}

%define plugindir  %_libdir/qt3/plugins

Name: qt3
Version: 3.3.8.d
Release: %mkrel 3
License: GPLv3+ and QPL
Summary: Qt3 Sources
Group: System/Libraries
URL: http://www.trolltech.com
Source0: qt3-3.5.13.1.tar.gz
Source1: qt3.macros
Source2: qt3-assistant.desktop
Source3: qt3-designer.desktop
Source4: qt3-linguist.desktop
Source5: qt3-designer-sh
Source6: qt3-assistant-sh
Source7: qt3-uic-sh
Source8: qt3-README-Mageia
Source9: 90qtrc-jp
Patch1: qt-3.1.1-fix-xft2-compile.patch
Patch2: qt-3.2.3-fix-cupslib.patch
Patch4: qt-x11-free-3.3.5-no-rpath.patch
Patch5: qt-3.3.2-fix-configure.patch
Patch8: qt-3.3.5-lib64-plugins.patch
Patch10: qt-3.3.3-fix-accessible.patch
Patch12: fix-key-release-event-with-imm.diff
Patch13: qt-x11-free-3.3.6-lib64.patch
Patch14: qt-x11-free-3.3.4-linux32.patch
Patch15: qt-visibility.patch
Patch16: qt-x11-free-3.3.5-makelibshared.patch
Patch24: qt-x11-free-3.3.5-qtranslator-crash.patch
Patch28: qt-x11-immodule-nodebug.diff
Patch29: fix-x11-immodule.diff
Patch30: fix-im-crash-on-exit.diff
Patch31: workaround-for-xlib-xim-bug.diff
Patch56: qt3-3.3.6-fix-xorg7.0.patch
Patch58: qt-3.3.6-fix-qfile-message-error.patch
Patch59: qt-3.3.6-fix-qfile-message-error2.patch
Patch63: qt-x11-free-3.3.8-qmo35263.patch
Patch64: qt-x11-free-3.3.8b-unixodb-64.patch
Patch65: qt-x11-free-3.3.8b-cstddef.patch
#-------------- KDE qt-copy patches ( added the relevant ones )
Patch102: 0017-qiconview-ctrl_rubber.patch 
Patch104: 0035-qvaluelist-streaming-operator.patch 
Patch115: 0078-argb-visual-hack.patch 

# TDE 3.5.13 patches
Patch300: qt3-3.3.8.d-updates_zh-tw_translations.patch



Buildroot: %_tmppath/%name-%version-%release-root
%if %buildSQL
BuildRequires: mysql-devel 
BuildRequires: unixODBC-devel 
BuildRequires: libpq-devel
%endif
BuildRequires: freetype2-devel
BuildRequires: mesaglu-devel
BuildRequires: libsm-devel
BuildRequires: libice-devel
BuildRequires: libx11-devel
BuildRequires: libxcursor-devel
BuildRequires: libxext-devel
BuildRequires: libxft-devel
BuildRequires: libxinerama-devel
BuildRequires: libxmu-devel
BuildRequires: libxrandr-devel
BuildRequires: libxrender-devel
BuildRequires: fontconfig-devel
BuildRequires: bzip2-devel
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
%if 0%{pclinuxos}
BuildRequires: libpng-devel
%else
BuildRequires: pkgconfig(libpng15)
%endif
BuildRequires: zlib-devel 
BuildRequires: nas-devel
BuildRequires: libiodbc-devel
%if "%{_lib}" != "lib"
BuildRequires: linux32
%endif
BuildRequires: postgresql-devel

%description
Qt is a complete and well-designed multi-platform object-oriented framework for
developing graphical user interface (GUI) applications using C++. Qt has
seamless integration with OpenGL/Mesa 3D libraries.

#--------------------------------------------------------------------

%package -n %libqt3name
Summary: Qt3 - Shared libraries
Group: System/Libraries
Requires: %{name}-common = %version
Provides:	qt3 = %{version}-%{release}

%description -n %libqt3name
Qt is a complete and well-designed multi-platform object-oriented framework for
developing graphical user interface (GUI) applications using C++. Qt has
seamless integration with OpenGL/Mesa 3D libraries.

This package contains shared libraries. 

%postun -n %libqt3name 
if [ "$1" = "0" ]; then
   rm -f /etc/ld.so.conf.new
   grep -v -e "^%qtdir/%_lib$" /etc/ld.so.conf > /etc/ld.so.conf.new
   mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi

%files -n %libqt3name
%defattr(-,root,root,-)
%dir %qtdir/
%_libdir/libqt-mt.so.3
%_libdir/libqt-mt.so.3.3
%_libdir/libqt-mt.so.3.3.8
%_libdir/libqt-mt.la
%_libdir/libqui.so.1
%_libdir/libqui.so.1.0
%_libdir/libqui.so.1.0.0
%_libdir/*.prl

%dir %{plugindir}/styles/
%{plugindir}/styles/*style.so

%if %{buildImmodule}
%dir %{plugindir}/inputmethods/
%{plugindir}/inputmethods/*.so
%endif

#--------------------------------------------------------------------

%package -n %libqt3name-devel
Summary: Qt3 - Files needed to build Qt3 based applications
Group: Development/KDE and Qt
Requires: %libqt3name = %version-%release
Requires: %{libeditor} = %version-%release
Requires: %{libqassistantname} = %version-%release
Requires: %{libdesignercore} = %version-%release
Provides: libqt-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: libqt3-pch-headers < 3.3.5

%description -n %libqt3name-devel
The qt3-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt meta
object compiler.

%post -n %libqt3name-devel
update-alternatives --install %_bindir/qmake qmake %qtdir/bin/qmake 10

%postun -n %libqt3name-devel
if ! [ -e %qtdir/bin/qmake ]; then
  update-alternatives --remove qmake %qtdir/bin/qmake
fi

%files -n %libqt3name-devel
%defattr(-,root,root,-)
%doc %_mandir/man1/*
%doc %_mandir/man3/*
%_bindir/designer-qt3
%_libdir/*.so
%_sysconfdir/rpm/macros.d/*
%_libdir/pkgconfig/*.pc
%_datadir/applications/*
%dir %qtdir/
%dir %qtdir/bin
%qtdir/bin/designer 
%qtdir/bin/lrelease  
%qtdir/bin/moc    
%qtdir/bin/%multiarch_platform/qmake
%qtdir/bin/qmake
%qtdir/bin/uic
%qtdir/bin/lupdate   
%qtdir/bin/qm2ts  
%dir %qtdir/include/%multiarch_platform
%qtdir/include/%multiarch_platform/*.h
%dir %qtdir/include/
%qtdir/include/*
%dir %qtdir/templates/
%qtdir/templates/*.ui
%dir %{plugindir}/designer
%{plugindir}/designer/*
%dir %qtdir/mkspecs/
%qtdir/mkspecs/*
%dir %qtdir/src/
%qtdir/src/*
%{qtdir}/bin/createcw
%{qtdir}/bin/makeqpf
%{qtdir}/bin/mergetr
%{qtdir}/bin/msg2qm
%{qtdir}/bin/qembed
%dir %qtdir/bin/%multiarch_platform

#--------------------------------------------------------------------
%if %{buildStatic}

%package -n %libqt3name-static-devel
Summary: Qt3 - Static files needed to build Qt3 based applications
Group: Development/KDE and Qt
Requires: %libqt3name-devel = %version-%release
Provides: libqt-static-devel = %{version}-%{release}
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %libqt3name-static-devel
This package contains:
  - files needed to build static Qt based applications

%files -n %libqt3name-static-devel
%defattr(-,root,root,-)
%_libdir/*.a

%endif

#--------------------------------------------------------------------

%package common
Summary:	Config, language file for Qt
Group:      Development/KDE and Qt
Requires:   %libqt3name = %version
Obsoletes:	libqt3-common < %{version}-%{release}
Provides:	libqt3-common = %{version}-%{release}
# Laurent : allow to install package which use this provides (commercial packages which want to install under distro and used this provides
Provides:	qt = %{version}-%{release}
Provides:	qt3 = %{version}-%{release}

%description common
This package contains all config file and language file

%post common
update-alternatives --install %_bindir/qtconfig qtconfig %qtdir/bin/qtconfig 10

%postun common
if ! [ -e %qtdir/bin/qtconfig ]; then
  update-alternatives --remove qtconfig %qtdir/bin/qtconfig 
fi

%files common
%defattr(-,root,root,-)
%dir %{plugindir}
%if %buildSQL
%dir %{plugindir}/sqldrivers
%endif
%dir %qtdir/phrasebooks/
%qtdir/phrasebooks/*.qph
%dir %qtdir/
%dir %qtdir/bin
%qtdir/bin/qtconfig
%_sysconfdir/profile.d/*.csh
%_sysconfdir/profile.d/*.sh
%config(noreplace) %_sysconfdir/qtrc
%config(noreplace) %_sysconfdir/kstylerc
%dir %qtdir/translations/
%qtdir/translations/*.qm
%_sysconfdir/X11/xinit.d/*

#--------------------------------------------------------------------

%if %buildSQL
%package -n %libqt3name-mysql
Summary: 	MySQL plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-MySQL = %{version}-%{release}

%description -n %libqt3name-mysql
This package contain the MySQL plugin for Qt.

%files -n %libqt3name-mysql
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlmysql.so


%package -n %libqt3name-psql
Summary: 	PostgresSQL plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-PostgreSQL = %{version}-%{release}

%description -n %libqt3name-psql
This package contain the PostgresSQL plugin for Qt.


%files -n %libqt3name-psql
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlpsql.so

%package -n %libqt3name-odbc
Summary: 	ODBC plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-ODBC = %{version}-%{release}

%description -n %libqt3name-odbc
This package contain the ODBC plugin for Qt.


%files -n %libqt3name-odbc
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlodbc.so


%package -n %libqt3name-sqlite
Summary: 	Sqlite 2 plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-Sqlite = %{version}-%{release}

%description -n %libqt3name-sqlite
This package contain the Sqlite 2 plugin for Qt.

%files -n %libqt3name-sqlite
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlite.so

%endif

#--------------------------------------------------------------------

%package -n %libqassistantname
Summary: Qt3 - Shared libraries
Group: System/Libraries

%description -n %libqassistantname
Qt3 - Shared libraries

%files -n %libqassistantname
%defattr(-,root,root)
%_libdir/libqassistantclient.so.*

#--------------------------------------------------------------------

%package assistant
Summary: Qt assistant
Group: Development/KDE and Qt

%description assistant
This package contain Qt assistant

%files assistant
%defattr(-,root,root)
%_bindir/assistant-qt3
%qtdir/bin/assistant  

#--------------------------------------------------------------------

%package linguist
Summary: Qt linguist
Group: Development/KDE and Qt

%description linguist
This package contain Qt linguist

%files linguist
%defattr(-,root,root)
%qtdir/bin/linguist       

#--------------------------------------------------------------------

%package -n %libdesignercore
Summary: Qt3 - Shared libraries
Group: System/Libraries

%description -n %libdesignercore
Qt3 - Shared libraries

%files -n %libdesignercore
%defattr(-,root,root)
%_libdir/libdesignercore.so.*

#--------------------------------------------------------------------

%package -n %libeditor
Summary: Qt3 - Shared libraries
Group: System/Libraries

%description -n %libeditor
Qt3 - Shared libraries

%files -n %libeditor
%defattr(-,root,root)
%_libdir/libeditor.so.*

#--------------------------------------------------------------------

%package example
Summary:    Qt examples
Group:      Development/KDE and Qt
Obsoletes:  libqt3-example
Provides:   libqt3-example
BuildArch: noarch

%description example
This package contain Qt example.

%files example
%defattr(-,root,root)
%dir %_docdir/%name/examples
%doc %_docdir/%name/examples/*

#--------------------------------------------------------------------

%package tutorial
Summary:    Qt tutorials
Group:      Development/KDE and Qt
BuildArch: noarch

%description tutorial
This package contain Qt tutorial.

%files tutorial
%defattr(-,root,root)
%dir %_docdir/%name/tutorial
%doc %_docdir/%name/tutorial/*

#--------------------------------------------------------------------

%package doc
Summary: Qt documentation
Group: Development/KDE and Qt
Conflicts:libqt3-devel <= 3.3.4-13mdk
BuildArch: noarch

%description doc
This package contain Qt documentation

%post doc
# Remove old qt3 doc directories
find %_docdir -maxdepth 1 -type d -name qt-3.\* -exec rm -rf {} \;

%files doc
%dir %_docdir/%name
%doc %_docdir/%name/FAQ
%doc %_docdir/%name/LICENSE*
%doc %_docdir/%name/README*
%dir %_docdir/%name/doc/
%dir %_docdir/%name/doc/html/
%doc %_docdir/%name/doc/html/*
%dir %qtdir/doc/
%qtdir/doc/html

#--------------------------------------------------------------------

%if 0%{?pclinuxos}
%debug_package
%endif

%prep
%setup -q -n qt3-3.5.13.1

%patch1 -p1 -b .fix_xft_compile
%patch2 -p1 -b .fix_cups_lib
%patch4 -p0 
%patch5 -p1 -b .fix_configure_space
%patch13 -p1 -b .lib64
%patch14 -p1 -b .linux32
%patch10 -p1 -b .fix_accessible
%patch15 -p1 -b .fix_qt_export
%patch16 -p1 -b .sharedlibs
%patch24 -p0 -b .qtranslator
%patch56 -p1 -b .fix_xorg_7.0
%patch58 -p1 -b .fix_qfile_message_error
%patch59 -p1 -b .fix_qfile_message_error
%patch63 -p0 -b .fix_bug_35263
%if "%_lib" == "lib64"
%patch64 -p0 -b .fix_unixodbc
%endif
%patch65 -p1 -b .gcc46
# KDE qt-copy patches
%patch102 -p0 -b .qt-copy
%patch104 -p0 -b .qt-copy
%patch115 -p0 -b .qt-copy

# TDE 3.5.13 patches
%patch300 -p1


# (Anssi 01/2008)
# Hack to disable stripping, a better fix for configure script welcome:
mkdir -p stripbin
echo "#!/bin/true" > stripbin/strip
chmod +x stripbin/strip

sed -e "s|^QMAKE_STRIP.*=.*|QMAKE_STRIP =|" -i mkspecs/linux-g++*/qmake.conf
sed -e "s|^QMAKE_CFLAGS\t.*$|QMAKE_CFLAGS = %{optflags}  -DPIC -fPIC|" \
        -e "s|^QMAKE_LFLAGS\t.*=.*$|QMAKE_LFLAGS = %{ldflags} |" \
        -e "s|^QMAKE_LFLAGS_PLUGIN\t.*\+= |QMAKE_LFLAGS_PLUGIN = %(echo %ldflags|sed -e 's#-Wl,--no-undefined##') |" \
        -i mkspecs/linux-g++*/qmake.conf

%build
export QTDIR=$(/bin/pwd)
export PATH=$(pwd)/stripbin:$QTDIR/bin:$PATH
export MANPATH=$QTDIR/doc/man:$MANPATH
export LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH

%if %{buildImmodule}
sh ./make-symlinks.sh
%endif

# Default platform (take care to lib64 arches)
PLATFORM=linux-g++
%if "%_lib" == "lib64"
PLATFORM=linux-g++-64
%endif
echo "#define QT_MITSHM" >> mkspecs/${PLATFORM}/qplatformdefs.h

function main_configure {
echo "yes" | ./configure \
	-I/usr/include/postgresql/server/ \
	-I/usr/include/fontconfig \
	-I/usr/include/Xft2 \
	-I/usr/include/Xft2/X11/Xft \
	-I/usr/include/mysql/ \
	-I/usr/include/libpng15 \
	-prefix %qtdir/ \
	-libdir %_libdir \
	-plugindir %{plugindir} \
	-sysconfdir %_sysconfdir \
	-docdir %_docdir/%name/doc/ \
   %if %{buildDebug}
   -debug \
   %else
	-release \
   %endif
	-qt-gif \
	-system-zlib \
	-no-exceptions \
	-platform $PLATFORM \
	-enable-tools \
	-enable-kernel \
	-enable-widgets \
	-enable-dialogs \
	-enable-iconview \
	-enable-workspace \
	-enable-network \
	-enable-canvas \
	-enable-table \
	-enable-xml \
	-enable-input \
	-enable-opengl \
	-dlopen-opengl \
	%if %buildSQL		
		-enable-sql \
		-plugin-sql-mysql \
		-plugin-sql-odbc \
		-plugin-sql-psql \
		-plugin-sql-sqlite \
	%endif
	-plugin-style-cde \
	-plugin-style-compact \
	-plugin-style-motif \
	-plugin-style-sgi \
	-plugin-style-platinum \
	-plugin-style-motifplus \
	-thread \
	-stl \
	-qt-imgfmt-png \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng  \
	-system-libpng \
	-system-libjpeg \
	-system-libmng \
	-sm \
	-xkb \
	-xinerama \
	-xrender \
	-xrandr \
	-xcursor \
	-xft \
	-nis \
	-no-tablet \
	-v \
	-xkb \
	$*
}

%if %{buildStatic}

main_configure -static 
pushd src
	%make && make INSTALL_ROOT=%{buildroot} install_target
popd
mkdir -p safelib
mv -f lib/libqt-mt.a safelib
%endif

# Build shared
main_configure -shared 
%make symlinks src-qmake src-moc sub-src sub-tools

%install
export QTDIR=$(/bin/pwd)
export PATH=$(pwd)/stripbin:$QTDIR/bin:$PATH
export MANPATH=$QTDIR/doc/man:$MANPATH
export LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH
rm -fr %buildroot

make install INSTALL_ROOT=%buildroot/

rm -rf %buildroot/%qtdir/bin/qmake
install -m 0755  qmake/qmake %buildroot/%qtdir/bin/

# David - 3.0.0-0.11mdk - Install a README for Mandriva Linux
install -m 0644 %SOURCE8 %buildroot/%_docdir/%name/README.Mandriva_Linux
perl -pi -e "s|QtVersion|%version|" %buildroot/%_docdir/%name/README.Mandriva_Linux
perl -pi -e "s|PackageVersion|%version-%release|" %buildroot/%_docdir/%name/README.Mandriva_Linux

# David - 3.0.0-0.11mdk - Install missing documentation
install -d -m 0755 %buildroot/%_docdir/%name/
install -m 0644 FAQ       %buildroot/%_docdir/%name/
install -m 0644 LICENSE*  %buildroot/%_docdir/%name/
install -m 0644 README    %buildroot/%_docdir/%name/
install -m 0644 README-QT.TXT %buildroot/%_docdir/%name/

# David - 3.0.0-0.11mdk - Install man pages
install -d -m 0755 %buildroot/%_mandir/man1/
for i in doc/man/man1/* ; do
		if [ ! -d $i ] ; then
		   install -m 0644 $i %buildroot/%_mandir/man1/
		fi
done
#
install -d -m 0755 %buildroot/%_mandir/man3/
for i in doc/man/man3/* ; do
	    if [ ! -d $i ] ; then
   			install -m 0644 $i %buildroot/%_mandir/man3/
	    fi
done

install -d -m 0755 %buildroot/%_bindir/
install -m 0755 bin/moc %buildroot/%qtdir/bin/moc

# David - 3.0.1-2mdk - Install .pri files needed to build examples and tutorials
install -d -m 0755 %buildroot/%qtdir/src/
for i in src/*.pri; do
   install -m 0644 $i %buildroot/%qtdir/src/
done


cp -ar examples/ %buildroot/%_docdir/%name
cp -ar tutorial/ %buildroot/%_docdir/%name

# Fix include directory for examples ( based on David Faure changes )
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../include|%qtdir/include|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../include|%qtdir/include|"

# Fix lib directory for examples
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../../lib/libqt-mt.prl|%_libdir/libqt-mt.prl|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../lib/libqt-mt.prl|%_libdir/libqt-mt.prl|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../lib/libqt-mt.prl|%_libdir/libqt-mt.prl|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../src/qt_professional.pri|%qtdir/src/qt_professional.pri|"

# Set RPM_BUILD_DIR to QTDIR
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|%_builddir/qt-%version|%qtdir|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|%_builddir/qt-x11-free-%version/mkspecs/|%qtdir/mkspecs/|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|%_builddir/qt-x11-free-%version/|%qtdir/|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../lib/libqassistantclient.prl|%_libdir/libqassistantclient.prl|"

# Remove .obj .moc directories
for name in `find %buildroot/%_docdir/%name/{examples,tutorial} -type d -name .obj`; do
   rm -rf $name
done
for name in `find %buildroot/%_docdir/%name/{examples,tutorial} -type d -name .moc`; do
   rm -rf $name
done

install -m 0755 %SOURCE5 %buildroot/%_bindir/designer-qt3
install -m 0755 %SOURCE6 %buildroot/%_bindir/assistant-qt3

cd %buildroot/%qtdir/
install -d -m 0755 doc
ln -s %_docdir/%name/doc/html/ doc/html
cd -

install -d -m 0755 %buildroot/%_sysconfdir/profile.d/
cat >> %buildroot/%_sysconfdir/profile.d/qt3.csh << EOF
if (! \$?QTDIR ) then
    setenv QTDIR "%qtdir"
endif
if (! \$?QTINC ) then
    setenv QTINC "%qtdir/include"
endif
if (! \$?QTLIB ) then
    setenv QTLIB "%_libdir"
endif
if (! \$?QT_XFT ) then
    setenv QT_XFT 0
endif
EOF

cat > %buildroot/%_sysconfdir/profile.d/qt3.sh << EOF
#! /bin/bash
[ -z "\$QTDIR" ] && QTDIR="%qtdir"
[ -z "\$QTINC" ] && QTINC="%qtdir/include"
[ -z "\$QTLIB" ] && QTLIB="%_libdir"
[ -z "\$QT_XFT" ] && QT_XFT=0

if ! echo \${PATH} | /bin/grep -q \$QTDIR/bin ; then
   PATH=\$QTDIR/bin:\${PATH}
fi

export PATH QTDIR QTINC QTLIB QT_XFT
EOF

# Generate default qtrc
install -d -m 0755 %buildroot/%_sysconfdir/
cat >> %buildroot/%_sysconfdir/qtrc << EOF
[3.3]
libraryPath=%{plugindir}

[General]
enableXft=true
font=Sans,10,-1,5,0,0,0,0,0,0
style=plastik
useXft=true
EOF

cat >> %buildroot/%_sysconfdir/kstylerc << EOF
[Settings]
MenuDropShadow=true
MenuOpacity=0.9
MenuTransparencyEngine=Disabled
SemiTransparentRubberband=true
EOF


install -d -m 0755 %buildroot/%_datadir/applications
install -m 0644 %SOURCE2 %buildroot/%_datadir/applications/qt3-assistant.desktop
install -m 0644 %SOURCE3 %buildroot/%_datadir/applications/qt3-designer.desktop
install -m 0644 %SOURCE4 %buildroot/%_datadir/applications/qt3-linguist.desktop

# Multiarch fixes
%multiarch_binaries %buildroot%qtdir/bin/qmake

%multiarch_includes %buildroot%qtdir/include/qconfig.h

%if %{buildStatic}
# Static install
install -d -m 0755 %buildroot/%_libdir/ 
install -m644 safelib/*  %{buildroot}/%_libdir/
%endif

# Removing invalid symlink. They really should not be here
# Old symlink if was set in right place, would create a cyclic symlynk
cd %buildroot/%qtdir/mkspecs/
if [ -h default ]; then
   rm -f default/linux*
fi
# provide default64 for multiarch devel
%if "%_lib" == "lib64"
ln -sf linux-g++-64 default64
%endif
cd -

# Install rpm macros
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/rpm/macros.d

mkdir -p %buildroot/%_sysconfdir/X11/xinit.d/
install -m 0755 %SOURCE9 %buildroot/%_sysconfdir/X11/xinit.d/

# Fix all buildroot paths

%clean
rm -fr %buildroot





%changelog
* Sat Sep 29 2012 Francois Andriot <francois.andriot@free.fr> 3.3.8.d-3
- Initial release for TDE 3.5.13.1

* Mon Aug 27 2012 Francois Andriot <francois.andriot@free.fr> 3.3.8.d-2
- Rebuild with libpng 1.5
- Updates zh_TW translations

* Sat Jul 27 2012 Francois Andriot <francois.andriot@free.fr> 3.3.8.d-1
- Initial build for MGA2
