#
# spec file for package tdewebdev (version R14)
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
%define tde_pkg tdewebdev
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
Summary:	Web development applications
Group:		Applications/Editors
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:	http://download.sourceforge.net/quanta/css.tar.bz2
Source2:	http://download.sourceforge.net/quanta/html.tar.bz2
Source3:	http://download.sourceforge.net/quanta/php_manual_en_20030401.tar.bz2
Source4:	http://download.sourceforge.net/quanta/javascript.tar.bz2

Source10:		%{name}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdesdk-devel >= %{tde_version}

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# XSLT support
%if 0%{?mdkver}
BuildRequires:	%{_lib}xslt-devel
%else
BuildRequires:	libxslt-devel
%endif

%if 0%{?rhel} == 4
# a bogus dep in libexslt.la file from EL-4 (WONTFIX bug http://bugzilla.redhat.com/142241)
BuildRequires:	libgcrypt-devel
%endif

# PERL support
BuildRequires:	perl

# KXSLDBG requires libxml2
#if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || ( 0%{?fedora} > 0 && %{?fedora} <= 17 ) || 0%{?suse_version}
%define build_kxsldbg 1
BuildRequires:	libxml2-devel
#endif

# ICU support
%if 0%{?mdkver}
BuildRequires:	%{_lib}icu-devel
%else
BuildRequires:	libicu-devel
%endif

# Readline support
BuildRequires:	readline-devel

%define build_tdefilereplace 0

Obsoletes:	trinity-kdewebdev-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewebdev-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdewebdev < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewebdev = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: trinity-quanta = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-quanta-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kimagemapeditor = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klinkstatus = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kommander = %{?epoch:%{epoch}:}%{version}-%{release}
%{?build_kxsldbg:Requires: trinity-kxsldbg = %{?epoch:%{epoch}:}%{version}-%{release}}

%description
Web development applications, including:
* kimagemapeditor: HTML image map editor
* klinkstatus: link checker
* kommander: visual dialog building tool
* quanta+: web development
%{?build_kxsldbg:* kxsldbg: xslt Debugger}

%files
%defattr(-,root,root,-)

##########

%package -n trinity-quanta
Summary:	web development environment for TDE [Trinity]
Group:		Applications/Development
Requires:	trinity-tdefilereplace
Requires:	trinity-klinkstatus = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kommander = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-quanta-data = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	trinity-kimagemapeditor = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	trinity-kxsldbg = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	tidy

%description -n trinity-quanta
Quanta Plus is a web development environment for working with HTML
and associated languages. It strives to be neutral and transparent
to all markup languages, while supporting popular web-based scripting
languages, CSS and other emerging W3C recommendations.

Quanta Plus supports many external components, debuggers and other tools
for web development, several of which are shipped with the TDE web
development module.

Quanta Plus is not in any way affiliated with any commercial versions
of Quanta. The primary coders from the original team left the GPL'd
version to produce a commercial product.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-quanta
%defattr(-,root,root,-)
%{tde_bindir}/quanta
%{tde_tdelibdir}/quantadebuggerdbgp.la
%{tde_tdelibdir}/quantadebuggerdbgp.so
%{tde_tdelibdir}/quantadebuggergubed.la
%{tde_tdelibdir}/quantadebuggergubed.so
%{tde_tdeappdir}/quanta.desktop
%{tde_datadir}/apps/kafkapart
%{tde_datadir}/icons/hicolor/*/apps/quanta.png
%{tde_datadir}/mimelnk/application/x-webprj.desktop
%{tde_datadir}/services/quantadebuggerdbgp.desktop
%{tde_datadir}/services/quantadebuggergubed.desktop
%{tde_datadir}/services/quanta_preview_config.desktop
%{tde_datadir}/servicetypes/quantadebugger.desktop
%{tde_tdedocdir}/HTML/en/quanta/
%{tde_mandir}/man1/quanta.1*

##########

%package -n trinity-quanta-data
Summary:	data files for Quanta Plus web development environment [Trinity]
Group:		Applications/Development

%description -n trinity-quanta-data
This package contains architecture-independent data files for Quanta
Plus, a web development environment for working with HTML and associated
languages.

See the quanta package for further information.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-quanta-data
%defattr(-,root,root,-)
%{tde_datadir}/apps/quanta/

##########

%package -n trinity-kimagemapeditor
Summary:	HTML image map editor for TDE
Group:		Applications/Development

%description -n trinity-kimagemapeditor
KImageMapEditor is a tool that allows you to edit image maps in HTML
files. As well as providing a standalone application, KImageMapEditor
makes itself available as a KPart for embedding into larger applications.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-kimagemapeditor
%defattr(-,root,root,-)
%{tde_bindir}/kimagemapeditor
%{tde_tdelibdir}/libkimagemapeditor.la
%{tde_tdelibdir}/libkimagemapeditor.so
%{tde_tdeappdir}/kimagemapeditor.desktop
%{tde_datadir}/apps/kimagemapeditor/
%{tde_datadir}/icons/hicolor/*/apps/kimagemapeditor.png
%{tde_datadir}/icons/locolor/*/apps/kimagemapeditor.png
%{tde_datadir}/services/kimagemapeditorpart.desktop
%{tde_tdedocdir}/HTML/en/kimagemapeditor/
%{tde_mandir}/man1/kimagemapeditor.1*

##########

%package -n trinity-klinkstatus
Summary:	web link validity checker for TDE
Group:		Applications/Development

%description -n trinity-klinkstatus
KLinkStatus is TDE's web link validity checker. It allows you to
search internal and external links throughout your web site. Simply
point it to a single page and choose the depth to search.

You can also check local files, or files over ftp:, fish: or any other
KIO protocols. For performance, links can be checked simultaneously.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-klinkstatus
%defattr(-,root,root,-)
%{tde_bindir}/klinkstatus
%{tde_tdelibdir}/libklinkstatuspart.la
%{tde_tdelibdir}/libklinkstatuspart.so
%{tde_tdeappdir}/klinkstatus.desktop
%{tde_datadir}/apps/klinkstatus/
%{tde_datadir}/apps/klinkstatuspart/
%{tde_datadir}/config.kcfg/klinkstatus.kcfg
%{tde_datadir}/icons/hicolor/*/apps/klinkstatus.png
%{tde_datadir}/services/klinkstatus_part.desktop
%{tde_tdedocdir}/HTML/en/klinkstatus/
%{tde_mandir}/man1/klinkstatus.1*

##########

%package -n trinity-kommander
Summary:	visual dialog builder and executor tool [Trinity]
Group:		Applications/Development
Requires:	gettext

%description -n trinity-kommander
Kommander is a visual dialog building tool whose primary objective is
to create as much functionality as possible without using any scripting
language.

More specifically, Kommander is a set of tools that allow you to create
dynamic GUI dialogs that generate, based on their state, a piece of
text. The piece of text can be a command line to a program, any piece
of code, business documents that contain a lot of repetitious or
templated text and so on.

The resulting generated text can then be executed as a command line
program (hence the name "Kommander"), written to a file, passed to a
script for extended processing, and literally anything else you can
think of. And you aren't required to write a single line of code!

As well as building dialogs, Kommander may be expanded to create full
mainwindow applications.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-kommander
%defattr(-,root,root,-)
%{tde_bindir}/kmdr-editor
%{tde_bindir}/kmdr-executor
%{tde_bindir}/kmdr-plugins
%{tde_libdir}/libkommanderplugin.so.*
%{tde_libdir}/libkommanderwidgets.la
%{tde_libdir}/libkommanderwidget.so.*
%{tde_libdir}/libkommanderwidgets.so.*
%{tde_tdeappdir}/kmdr-editor.desktop
%{tde_datadir}/applnk/.hidden/kmdr-executor.desktop
%{tde_datadir}/apps/katepart/syntax/kommander.xml
%{tde_tdedocdir}/HTML/en/kommander/
%{tde_datadir}/icons/crystalsvg/*/apps/kommander.png
%{tde_datadir}/icons/hicolor/*/apps/kommander.png
%{tde_datadir}/mimelnk/application/x-kommander.desktop
%{tde_tdelibdir}/libkommander_part.so
%{tde_tdelibdir}/libkommander_part.la
%{tde_datadir}/apps/kommander/
%{tde_datadir}/apps/kmdr-editor/
%{tde_datadir}/apps/katepart/syntax/kommander-new.xml
%{tde_datadir}/apps/tdevappwizard/
%{tde_datadir}/services/kommander_part.desktop
%{tde_mandir}/man1/extractkmdr.1*
%{tde_mandir}/man1/kmdr-editor.1*
%{tde_mandir}/man1/kmdr-executor.1*
%{tde_mandir}/man1/kmdr-plugins.1*
%{tde_mandir}/man1/kmdr2po.1*

##########

%package -n trinity-kommander-devel
Summary:	development files for Kommander [Trinity]
Group:		Development/Libraries
Requires:	trinity-kommander = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kommander-devel
This package contains the headers and other development files for
building plugins or otherwise extending Kommander.

Kommander is a visual dialog building tool whose primary objective is
to create as much functionality as possible without using any scripting
language.

See the kommander package for further information.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-kommander-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkommanderplugin.la
%{tde_libdir}/libkommanderplugin.so
%{tde_libdir}/libkommanderwidget.la
%{tde_libdir}/libkommanderwidget.so
%{tde_libdir}/libkommanderwidgets.so
%{tde_tdeincludedir}/kommander*
%{tde_tdeincludedir}/specials.h

##########

%if 0%{?build_kxsldbg}

%package -n trinity-kxsldbg
Summary:	graphical XSLT debugger for TDE [Trinity]
Group:		Applications/Development

%description -n trinity-kxsldbg
KXSLDbg is a debugger for XSLT scripts. It includes a graphical user
interface as well as a text-based debugger. KXSLDbg can be run as a
standalone application or as an embedded TDE part.

XSLT is an XML language for defining transformations of XML files from
XML to some other arbitrary format, such as XML, HTML, plain text, etc.,
using standard XSLT stylesheets.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-kxsldbg
%defattr(-,root,root,-)
%{tde_bindir}/kxsldbg
%{tde_bindir}/xsldbg
%{tde_tdelibdir}/libkxsldbgpart.la
%{tde_tdelibdir}/libkxsldbgpart.so
%{tde_tdeappdir}/kxsldbg.desktop
%{tde_datadir}/applnk/.hidden/xsldbg.desktop
%{tde_datadir}/apps/kxsldbg/
%{tde_datadir}/apps/kxsldbgpart/
%{tde_tdedocdir}/HTML/en/kxsldbg/
%{tde_tdedocdir}/HTML/en/xsldbg/
%{tde_datadir}/icons/hicolor/*/actions/1downarrow.png
%{tde_datadir}/icons/hicolor/*/actions/configure.png
%{tde_datadir}/icons/hicolor/*/actions/system-log-out.png
%{tde_datadir}/icons/hicolor/*/actions/system-run.png
%{tde_datadir}/icons/hicolor/*/actions/hash.png
%{tde_datadir}/icons/hicolor/*/actions/mark.png
%{tde_datadir}/icons/hicolor/*/actions/next.png
%{tde_datadir}/icons/hicolor/*/actions/step.png
%{tde_datadir}/icons/hicolor/*/actions/xsldbg_*.png
%{tde_datadir}/icons/hicolor/*/apps/kxsldbg.png
%{tde_datadir}/icons/locolor/*/apps/kxsldbg.png
%{tde_datadir}/services/kxsldbg_part.desktop
%{tde_mandir}/man1/kxsldbg.1*

%endif

##########

%if 0%{?build_tdefilereplace}

%package -n trinity-tdefilereplace
Summary:	Batch search-and-replace component for TDE
Group:		Applications/Utilities

Obsoletes:	trinity-kfilereplace < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kfilereplace = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdefilereplace
TDEFileReplace is an embedded component for TDE that acts as a batch
search-and-replace tool. It allows you to replace one expression with
another in many files at once.

Note that at the moment TDEFileReplace does not come as a standalone
application.

This package is part of Trinity, as a component of the TDE utilities module.

%files -n trinity-tdefilereplace
%defattr(-,root,root,-)
%{tde_bindir}/tdefilereplace
%{tde_tdelibdir}/libtdefilereplacepart.la
%{tde_tdelibdir}/libtdefilereplacepart.so
%{tde_tdeappdir}/tdefilereplace.desktop
%{tde_datadir}/apps/tdefilereplace/
%{tde_datadir}/apps/tdefilereplacepart/
%{tde_tdedocdir}/HTML/en/tdefilereplace/
%{tde_datadir}/icons/hicolor/*/apps/tdefilereplace.png
%{tde_datadir}/services/tdefilereplacepart.desktop
%{tde_mandir}/man1/tdefilereplace.1*

%endif

##########

%package devel
Group: Development/Libraries
Summary:	Header files and documentation for %{name} 

Obsoletes:	trinity-kdewebdev-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewebdev-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	trinity-tdelibs-devel >= %{tde_version}
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kommander-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%files devel

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}} -a 1 -a 2 -a 3 -a 4

%if 0%{?build_kxsldbg} == 0
%__rm -rf kxsldbg/ doc/kxsldbg/ doc/xsldbg/
%endif


%build
unset QTDIR QTLIB QTINC
export PATH="%{tde_bindir}:${PATH}"

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
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DDOC_INSTALL_DIR="%{tde_docdir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_QUANTA_CVSSERVICE=OFF \
  \
  -DBUILD_ALL=ON \
  \
  ..

# Strange cmake behaviour under rhel6
%if 0%{?rhel} == 6
grep -rl "CXX_FLAGS.*\"-O2" | while read file; do
  sed -i "${file}" -e "s|\"||g"
done
%endif

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build


## package separately?  Why doesn't upstream include this? -- Rex
# install docs
for i in css html javascript ; do
   pushd $i
   ./install.sh <<EOF
%{buildroot}%{tde_datadir}/apps/quanta/doc
EOF
   popd
   rm -rf $i
done
cp -a php php.docrc %{buildroot}%{tde_datadir}/apps/quanta/doc/

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r klinkstatus      Office WebDevelopment
%if 0%{?build_kxsldbg}
%suse_update_desktop_file -r kxsldbg          Office WebDevelopment
%endif
%suse_update_desktop_file -r kimagemapeditor  Office WebDevelopment
%suse_update_desktop_file    kmdr-editor      Development GUIDesigner
%suse_update_desktop_file    kmdr-executor    Development GUIDesigner
%suse_update_desktop_file -r quanta           Office WebDevelopment
%if 0%{?build_tdefilereplace}
%suse_update_desktop_file -r tdefilereplace   System      FileManager
%endif
%endif

# Adds missing icons in 'hicolor' theme
%__mkdir_p %{buildroot}%{tde_datadir}/icons/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps/
pushd %{buildroot}%{tde_datadir}/icons
for i in {16,22,32,64,128}; do %__cp crystalsvg/"$i"x"$i"/apps/kommander.png  hicolor/"$i"x"$i"/apps/kommander.png  ;done
popd

# Unwanted icon
%__rm -f "%{buildroot}%{tde_datadir}/icons/crystalsvg/16x16/actions/bug.png"


%clean
%__rm -rf %{buildroot}


%changelog
