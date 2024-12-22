#
# spec file for package qt3-devel-doc
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           qt3-devel-doc
BuildRequires:  cups-devel freeglut-devel freetype2-devel gcc-c++ pkgconfig qt3-devel update-desktop-files
%if %suse_version < 1130
BuildRequires:  libpng-devel
%else
BuildRequires:  libpng14-devel
%endif
Url:            http://www.trolltech.com/
License:        GPL, QPL
AutoReqProv:    on
Summary:        Documentation for the Qt 3 Development Kit
Group:          Documentation/HTML
Version:        3.4.0
Release:        1
PreReq:         /bin/grep
BuildArch:      noarch 
Provides:       qt3-devel-tutorial
Obsoletes:      qt3-devel-tutorial
Requires:       qt3-devel
# COMMON-BEGIN
# COMMON-BEGIN
Source0:        qt3-%{version}.tar.bz2
Source1:        build_script.sh
Source2:        qtconfig3.desktop
Source3:        qtrc
Source4:        assistant3.png
Source6:        assistant3.desktop
Source7:        designer.desktop
Source8:        designer.png
Source9:        linguist.desktop
Source5:        linguist.png
Source10:       qt3.sh
Source11:       qt3.csh
# Translations did not change
Source12:       qt3-3.3.8b-translations.tar.bz2
Source102:      baselibs.conf
Source200:      attributes
Source201:      update_spec.pl
Patch1:         aliasing.diff
Patch2:         head.diff
Patch4:         qt3-never-strip.diff
Patch5:         external-libs.diff
Patch12:        qtrc-path.diff
Patch14:        lib64-plugin-support.diff
Patch15:        pluginmanager-fix.diff
Patch18:        no-rpath.dif
Patch19:        shut-up.diff
Patch23:        fix-accessible.diff
Patch31:        limit-image-size.diff
Patch35:        qt-transparency.patch
Patch37:        0055-qtextedit_zoom.patch
Patch39:        fix-qtranslator-crash.diff
Patch54:        kmenu-search-fix.diff
Patch113:       fix-assistant-path.patch
Patch117:       qtimer-debug.diff
Patch127:       mng-reading-fix.patch
Patch134:       fix-xinput-clash.diff
Patch135:       parseFontName.diff
Patch136:       qt3-no-date.diff
Patch139:       gcc46.diff
Patch140:       revert-iodbc-to-uodbc.diff

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

%define build_sub_dirs src plugins/src tools/designer/uilib/ tools/designer/uic tools/qtconfig tools/assistant/lib tools/assistant tutorial

%prep
%setup -q
%patch1
%patch2
%patch4
%patch5
%patch12
if [ "%_lib" = "lib64" ]; then
%patch14
fi
%patch15
%patch18
%patch19
%patch23
%patch31
%patch35
%patch37
%patch39
%patch54
%patch113
%patch117
ln -sf $PWD/src/inputmethod/qinputcontextfactory.h include/
ln -sf $PWD/src/inputmethod/qinputcontextplugin.h  include/
ln -sf $PWD/src/kernel/qinputcontext.h       include/
ln -sf $PWD/src/kernel/qinputcontextinterface_p.h include/private/
ln -sf $PWD/src/kernel/qximinputcontext_p.h       include/private/
%patch127
%patch134
%patch135
%patch136
%patch139
%patch140
cd translations
tar xvjf %SOURCE12
cd ..
# COMMON-END
# COMMON-END

%description
This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

%build
export VERSION=%suse_version
source %SOURCE1 %{version}
export WLIB=%_lib
export QTDIR=`pwd`
if [ %_lib == "lib64" ]; then
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DUSE_LIB64_PATHES"
fi
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
#
# call build from build_script.rpmrc for threaded Qt library
# only really needed tools will be builded here, all extra tools will be
# builded in qt3.spec
#
call_configure -thread -shared -no-sql-mysql -no-sql-psql -no-sql-odbc -no-sql-sqlite $OPTIONS
cd src
make %{?jobs:-j%jobs}
cd ..

%install
export VERSION=%suse_version
export WLIB=%_lib
export QTDIR=`pwd`
source %SOURCE1 %{version}
cd src
make INSTALL_ROOT=$RPM_BUILD_ROOT install_htmldocs
cd ..
#
# install menu entries
#
%suse_update_desktop_file -i -u qtconfig3 Qt Utility DesktopSettings
%suse_update_desktop_file -i assistant3 Qt Development Documentation

install -d -m 0755 ${RPM_BUILD_ROOT}/%{_defaultdocdir}/qt3/
ln -sf /usr/lib/qt3/doc/html ${RPM_BUILD_ROOT}/%{_defaultdocdir}/qt3/
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
install -m 0644 %SOURCE4 $RPM_BUILD_ROOT/usr/share/pixmaps/

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%dir /usr/lib/qt3/doc
%doc /usr/lib/qt3/doc/html
%{_docdir}/qt3/html
/usr/share/applications/qtconfig3.desktop
/usr/share/applications/assistant3.desktop
/usr/share/pixmaps/assistant3.png

%changelog
