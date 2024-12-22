#
# spec file for package tdesdk (version R14)
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
%define tde_pkg tdesdk
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


Name:			trinity-%{tde_pkg}
Summary:		The Trinity Software Development Kit (SDK)
Group:			Development/Tools/Other
Version:		%{tde_version}
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:		GPL-2.0+
%else
License:		GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-perl-dcop >= %{tde_version}
BuildRequires:	trinity-tdepim-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# PCRE support
BuildRequires:	pcre-devel

# for kbugbuster/libkcal
BuildRequires:	desktop-file-utils

# DB5 support
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 33
BuildRequires:	libdb-devel

# DB4 support
%else
%if 0%{?mgaversion} || 0%{?mdkversion}
#BuildRequires:	%{_lib}db4.8-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	db4-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libdb-4_8-devel
%endif
%endif

# kbabel,  F-7+: flex >= 2.5.33-9
BuildRequires:	flex
%if 0%{?mdkversion} && 0%{?pclinuxos} == 0
BuildRequires:	flex-devel
%endif
# umbrello
BuildRequires:	libxml2-devel
BuildRequires:	subversion-devel
BuildRequires:	neon-devel

# XSLT support
%if 0%{?mdkver}
BuildRequires:	%{_lib}xslt-devel
%else
BuildRequires:	libxslt-devel
%endif

# PERL support
BuildRequires:	perl
%if 0%{?fedora} >= 19
BuildRequires:	perl-podlators
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# PYTHON support
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 30 || 0%{?mgaversion} >= 8
%define python python3
%else
%define python python
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
BuildRequires:	%{_lib}binutils-devel
%endif
%if 0%{?fedora} >= 6 || 0%{?rhel} >= 5 || 0%{?suse_version}
BuildRequires:	binutils-devel
%endif
%if 0%{?fedora} >= 6 || 0%{?rhel} >= 5 || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif

# KIOSLAVE
# Does not build on RHEL4
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion}
%define build_kioslave 1
%endif

Obsoletes:		trinity-kdesdk < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdesdk = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdesdk-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdesdk-libs = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: trinity-cervisia = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kapptemplate = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kbabel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kbugbuster = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdecachegrind = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdecachegrind-converters = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-misc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-scripts = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmtrace = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kompare = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kspy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kuiviewer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libcvsservice0 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-poxml = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-umbrello = %{?epoch:%{epoch}:}%{version}-%{release}
%{?build_kioslave:Requires: %{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: trinity-tdeunittest = %{?epoch:%{epoch}:}%{version}-%{release}


%description
A collection of applications and tools used by developers, including:
* cervisia: a CVS frontend
* kbabel: PO file management
* kbugbuster: a tool to manage the TDE bug report system
* tdecachegrind: a browser for data produced by profiling tools (e.g. cachegrind)
* kompare: diff tool
* kuiviewer: displays designer's UI files
* umbrello: UML modeller and UML diagram tool

%files
%defattr(-,root,root,-)

##########

%package -n trinity-cervisia
Summary:	A graphical CVS front end for Trinity
Group:		Development/Tools/Version Control

%description -n trinity-cervisia
Cervisia is a TDE-based graphical front end for the CVS client.

As well as providing both common and advanced CVS operations, it offers
a variety of methods for graphically viewing information about the CVS
repository, your own sandbox and the relationships between different
versions of files.  A Changelog editor is also included and is coupled
with the commit dialog.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-cervisia
%defattr(-,root,root,-)
%{tde_bindir}/cervisia
%{tde_libdir}/libtdeinit_cervisia.la
%{tde_libdir}/libtdeinit_cervisia.so
%{tde_tdelibdir}/cervisia.la
%{tde_tdelibdir}/cervisia.so
%{tde_tdelibdir}/libcervisiapart.la
%{tde_tdelibdir}/libcervisiapart.so
%{tde_tdeappdir}/cervisia.desktop
%{tde_datadir}/apps/cervisia/
%{tde_datadir}/apps/cervisiapart/
%{tde_datadir}/apps/tdeconf_update/cervisia.upd
%{tde_datadir}/apps/tdeconf_update/cervisia-change_repos_list.pl
%{tde_datadir}/apps/tdeconf_update/cervisia-normalize_cvsroot.pl
%{tde_datadir}/apps/tdeconf_update/move_repositories.pl
%{tde_datadir}/apps/tdeconf_update/change_colors.pl
%{tde_datadir}/config.kcfg/cervisiapart.kcfg
%{tde_datadir}/icons/hicolor/*/apps/cervisia.png
%{tde_datadir}/icons/crystalsvg/*/actions/vcs_*.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/vcs_*.svgz
%{tde_mandir}/man1/cervisia.1*
%{tde_tdedocdir}/HTML/en/cervisia/

##########

%package -n trinity-kapptemplate
Summary:	Creates a framework to develop a Trinity application
Group:		Development/Languages/Other

%description -n trinity-kapptemplate
KAppTemplate is a shell script that will create the necessary
framework to develop various TDE applications.  It takes care of the
autoconf/automake code as well as providing a skeleton and example of
what the code typically looks like.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kapptemplate
%defattr(-,root,root,-)
%{tde_bindir}/kapptemplate
%{tde_datadir}/apps/kapptemplate/
%{tde_mandir}/man1/kapptemplate.1*

%pre -n trinity-kapptemplate
if [ -d "%{tde_bindir}/kapptemplate" ]; then
  rm -rf "%{tde_bindir}/kapptemplate"
fi

##########

%package -n trinity-kbabel
Summary:	PO-file editing suite for Trinity
Group:		Development/Languages/Other

%description -n trinity-kbabel
This is a suite of programs for editing gettext message files (PO-files).
It is designed to help you translate fast and consistently.

This suite includes KBabel, CatalogManager and KBabelDict.  KBabel is an
advanced and easy to use PO-file editor with full navigational and editing
capabilities, syntax checking and statistics.  CatalogManager is a multi
functional catalog manager which allows you to keep track of many
PO-files at once.  KBabelDict is a dictionary to assist with searching
for common translations.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kbabel
%defattr(-,root,root,-)
%{tde_bindir}/catalogmanager
%{tde_bindir}/kbabel
%{tde_bindir}/kbabeldict
%{tde_libdir}/libkbabelcommon.so.*
%{tde_libdir}/libkbabeldictplugin.so.*
%{tde_tdelibdir}/tdefile_po.la
%{tde_tdelibdir}/tdefile_po.so
%{tde_tdelibdir}/pothumbnail.la
%{tde_tdelibdir}/pothumbnail.so
%{tde_tdelibdir}/kbabel_accelstool.la
%{tde_tdelibdir}/kbabel_accelstool.so
%{tde_tdelibdir}/kbabel_argstool.la
%{tde_tdelibdir}/kbabel_argstool.so
%{tde_tdelibdir}/kbabel_contexttool.la
%{tde_tdelibdir}/kbabel_contexttool.so
%{tde_tdelibdir}/kbabel_equationstool.la
%{tde_tdelibdir}/kbabel_equationstool.so
%{tde_tdelibdir}/kbabel_gettextexport.la
%{tde_tdelibdir}/kbabel_gettextexport.so
%{tde_tdelibdir}/kbabel_gettextimport.la
%{tde_tdelibdir}/kbabel_gettextimport.so
%{tde_tdelibdir}/kbabel_lengthtool.la
%{tde_tdelibdir}/kbabel_lengthtool.so
%{tde_tdelibdir}/kbabel_linguistexport.la
%{tde_tdelibdir}/kbabel_linguistexport.so
%{tde_tdelibdir}/kbabel_linguistimport.la
%{tde_tdelibdir}/kbabel_linguistimport.so
%{tde_tdelibdir}/kbabel_nottranslatedtool.la
%{tde_tdelibdir}/kbabel_nottranslatedtool.so
%{tde_tdelibdir}/kbabel_pluraltool.la
%{tde_tdelibdir}/kbabel_pluraltool.so
%{tde_tdelibdir}/kbabel_punctuationtool.la
%{tde_tdelibdir}/kbabel_punctuationtool.so
%{tde_tdelibdir}/kbabel_regexptool.la
%{tde_tdelibdir}/kbabel_regexptool.so
%{tde_tdelibdir}/kbabel_setfuzzytool.la
%{tde_tdelibdir}/kbabel_setfuzzytool.so
%{tde_tdelibdir}/kbabel_whitespacetool.la
%{tde_tdelibdir}/kbabel_whitespacetool.so
%{tde_tdelibdir}/kbabel_xliffexport.la
%{tde_tdelibdir}/kbabel_xliffexport.so
%{tde_tdelibdir}/kbabel_xliffimport.la
%{tde_tdelibdir}/kbabel_xliffimport.so
%{tde_tdelibdir}/kbabel_xmltool.la
%{tde_tdelibdir}/kbabel_xmltool.so
%{tde_tdelibdir}/kbabeldict_dbsearchengine.la
%{tde_tdelibdir}/kbabeldict_dbsearchengine.so
%{tde_tdelibdir}/kbabeldict_poauxiliary.la
%{tde_tdelibdir}/kbabeldict_poauxiliary.so
%{tde_tdelibdir}/kbabeldict_pocompendium.la
%{tde_tdelibdir}/kbabeldict_pocompendium.so
%{tde_tdelibdir}/kbabeldict_tmxcompendium.la
%{tde_tdelibdir}/kbabeldict_tmxcompendium.so
%{tde_tdeappdir}/catalogmanager.desktop
%{tde_tdeappdir}/kbabel.desktop
%{tde_tdeappdir}/kbabeldict.desktop
%{tde_datadir}/apps/catalogmanager/
%{tde_datadir}/apps/kbabel/
%{tde_datadir}/apps/tdeconf_update/kbabel-difftoproject.upd
%{tde_datadir}/apps/tdeconf_update/kbabel-project.upd
%{tde_datadir}/apps/tdeconf_update/kbabel-projectrename.upd
%{tde_datadir}/config.kcfg/kbabel.kcfg
%{tde_datadir}/config.kcfg/kbprojectsettings.kcfg
%{tde_tdedocdir}/HTML/en/kbabel/
%{tde_datadir}/icons/hicolor/*/apps/catalogmanager.png
%{tde_datadir}/icons/hicolor/*/apps/kbabel.png
%{tde_datadir}/icons/hicolor/*/apps/kbabeldict.png
%{tde_datadir}/icons/locolor/*/apps/catalogmanager.png
%{tde_datadir}/icons/locolor/*/apps/kbabel.png
%{tde_datadir}/icons/locolor/*/apps/kbabeldict.png
%{tde_datadir}/services/dbsearchengine.desktop
%{tde_datadir}/services/tdefile_po.desktop
%{tde_datadir}/services/pothumbnail.desktop
%{tde_datadir}/services/kbabel_accelstool.desktop
%{tde_datadir}/services/kbabel_argstool.desktop
%{tde_datadir}/services/kbabel_contexttool.desktop
%{tde_datadir}/services/kbabel_equationstool.desktop
%{tde_datadir}/services/kbabel_gettext_export.desktop
%{tde_datadir}/services/kbabel_gettext_import.desktop
%{tde_datadir}/services/kbabel_lengthtool.desktop
%{tde_datadir}/services/kbabel_linguist_export.desktop
%{tde_datadir}/services/kbabel_linguist_import.desktop
%{tde_datadir}/services/kbabel_nottranslatedtool.desktop
%{tde_datadir}/services/kbabel_pluralformstool.desktop
%{tde_datadir}/services/kbabel_punctuationtool.desktop
%{tde_datadir}/services/kbabel_regexptool.desktop
%{tde_datadir}/services/kbabel_setfuzzytool.desktop
%{tde_datadir}/services/kbabel_whitespacetool.desktop
%{tde_datadir}/services/kbabel_xliff_export.desktop
%{tde_datadir}/services/kbabel_xliff_import.desktop
%{tde_datadir}/services/kbabel_xmltool.desktop
%{tde_datadir}/services/pocompendium.desktop
%{tde_datadir}/services/poauxiliary.desktop
%{tde_datadir}/services/tmxcompendium.desktop
%{tde_datadir}/servicetypes/kbabel_tool.desktop
%{tde_datadir}/servicetypes/kbabel_validator.desktop
%{tde_datadir}/servicetypes/kbabeldict_module.desktop
%{tde_datadir}/servicetypes/kbabelfilter.desktop
%{tde_mandir}/man1/catalogmanager.1*
%{tde_mandir}/man1/kbabel.1*
%{tde_mandir}/man1/kbabeldict.1*

##########

%package -n trinity-kbabel-devel
Summary:	PO-file editing suite for Trinity (development files)
Group:		Development/Libraries/Other
Requires:	trinity-kbabel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kbabel-devel
This is a suite of programs for editing gettext message files (PO-files).
It is designed to help you translate fast and consistently.

This suite includes KBabel, CatalogManager and KBabelDict.  KBabel is an
advanced and easy to use PO-file editor with full navigational and editing
capabilities, syntax checking and statistics.  CatalogManager is a multi
functional catalog manager which allows you to keep track of many
PO-files at once.  KBabelDict is a dictionary to assist with searching
for common translations.

This package contains the KBabel development files.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kbabel-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kbabel/
%{tde_libdir}/libkbabelcommon.la
%{tde_libdir}/libkbabelcommon.so
%{tde_libdir}/libkbabeldictplugin.la
%{tde_libdir}/libkbabeldictplugin.so

##########

%package -n trinity-kbugbuster
Summary:	A front end for the Trinity bug tracking system
Group:		Development/Languages/Other
Requires:	trinity-libkcal >= %{tde_version}

%description -n trinity-kbugbuster
KBugBuster is a GUI front end for the TDE bug tracking system.
It allows the user to view and manipulate bug reports and provides a
variety of options for searching through reports.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kbugbuster
%defattr(-,root,root,-)
%{tde_bindir}/kbugbuster
%{tde_tdelibdir}/kcal_bugzilla.la
%{tde_tdelibdir}/kcal_bugzilla.so
%{tde_tdeappdir}/kbugbuster.desktop
%{tde_datadir}/apps/kbugbuster/
%{tde_datadir}/icons/hicolor/*/apps/kbugbuster.png
%{tde_datadir}/icons/locolor/*/apps/kbugbuster.png
%{tde_datadir}/services/tderesources/kcal/bugzilla.desktop
%{tde_tdedocdir}/HTML/en/kbugbuster/
%{tde_mandir}/man1/kbugbuster.1*

##########

%package -n trinity-tdecachegrind
Summary:	Visualisation tool for valgrind profiling output
Group:		Development/Languages/Other

%description -n trinity-tdecachegrind
tdecachegrind is a visualisation tool for the profiling data generated
by calltree, a profiling skin for valgrind.  Applications can be
profiled using calltree without being recompiled, and shared libraries
and plugin architectures are supported.

For visualising the output from other profiling tools, several converters
can be found in the tdecachegrind-converters package.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-tdecachegrind
%defattr(-,root,root,-)
%{tde_bindir}/tdecachegrind
%{tde_tdeappdir}/tdecachegrind.desktop
%{tde_datadir}/apps/tdecachegrind/
%{tde_datadir}/icons/locolor/*/apps/tdecachegrind.png
%{tde_datadir}/icons/hicolor/*/apps/tdecachegrind.png
%{tde_datadir}/mimelnk/application/x-tdecachegrind.desktop
%{tde_tdedocdir}/HTML/en/tdecachegrind/
%{tde_mandir}/man1/tdecachegrind.1*

##########

%package -n trinity-tdecachegrind-converters
Summary:	Format converters for tdecachegrind profiling visualisation tool
Group:		Development/Languages/Other
Requires:	%{python}
%if 0%{?suse_version} || 0%{?rhel} == 4
Requires:	php
%else
Requires:	php-cli
%endif

%description -n trinity-tdecachegrind-converters
This is a collection of scripts for converting the output from
different profiling tools into a format that tdecachegrind can use.

tdecachegrind is a visualisation tool for the profiling data generated
by calltree, a profiling skin for valgrind.  Applications can be
profiled using calltree without being recompiled, and shared libraries
and plugin architectures are supported.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-tdecachegrind-converters
%defattr(-,root,root,-)
%{tde_bindir}/dprof2calltree
%{tde_bindir}/hotshot2calltree
%{tde_bindir}/memprof2calltree
%{tde_bindir}/op2calltree
%{tde_bindir}/pprof2calltree
%{tde_mandir}/man1/dprof2calltree.1*
%{tde_mandir}/man1/hotshot2calltree.1*
%{tde_mandir}/man1/memprof2calltree.1*
%{tde_mandir}/man1/op2calltree.1*
%{tde_mandir}/man1/pprof2calltree.1*

##########

%package kfile-plugins
Summary:	Trinity file dialog plugins for software development files
Group:		Development/Languages/Other

%description kfile-plugins
This is a collection of plugins for the TDE file dialog.  These plugins
extend the file dialog to offer advanced meta-information for source files,
patch files and Qt Linguist data.

This package is part of Trinity, and a component of the TDE SDK module.

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/tdefile_cpp.so
%{tde_tdelibdir}/tdefile_cpp.la
%{tde_tdelibdir}/tdefile_diff.so
%{tde_tdelibdir}/tdefile_diff.la
%{tde_tdelibdir}/tdefile_ts.so
%{tde_tdelibdir}/tdefile_ts.la
%{tde_datadir}/services/tdefile_cpp.desktop
%{tde_datadir}/services/tdefile_diff.desktop
%{tde_datadir}/services/tdefile_h.desktop
%{tde_datadir}/services/tdefile_ts.desktop

##########

%package misc
Summary:	Various goodies from the Trinity Software Development Kit
Group:		Development/Languages/Other

%description misc
This package contains miscellaneous goodies provided with the official
TDE release to assist with TDE software development.

Included are:
- headers to assist with profiling TDE code;
- a widget style for checking conformity with the TDE/Qt style guide;
- palettes that match the KDE standard colour palette;
- a TDE address book plugin that reads the list of TDE CVS accounts.

This package is part of Trinity, and a component of the TDE SDK module.

%files misc
%defattr(-,root,root,-)
%{tde_tdelibdir}/tdeabcformat_kdeaccounts.la
%{tde_tdelibdir}/tdeabcformat_kdeaccounts.so
%{tde_tdelibdir}/plugins/styles/scheck.so
%{tde_tdelibdir}/plugins/styles/scheck.la
%{tde_datadir}/apps/tdeabc/formats/kdeaccountsplugin.desktop
%{tde_datadir}/apps/tdestyle/themes/scheck.themerc
%{tde_datadir}/kdepalettes/

%{tde_libdir}/libkstartperf.so.*
%{tde_libdir}/libkstartperf.la
%{tde_bindir}/kstartperf

##########

%package scripts
Summary:	a set of useful development scripts for Trinity
Group:		Development/Languages/Other
Requires:	%{python}

%description scripts
This package contains a number of scripts which can be used to help in
developing TDE-based applications.  Many of these scripts however are
not specific to TDE, and in particular there are several general-use
scripts to help users in working with SVN and CVS repositories.

In addition to these scripts, this package provides:
- gdb macros for Qt/TDE programming;
- vim and emacs helper files for Qt/TDE programming;
- bash and zsh completion controls for TDE apps;
- valgrind error suppressions for TDE apps.

This package is part of Trinity, and a component of the TDE SDK module.

%files scripts
%defattr(-,root,root,-)
%{tde_bindir}/adddebug
%{tde_bindir}/build-progress.sh
%{tde_bindir}/cheatmake
%{tde_bindir}/create_cvsignore
%{tde_bindir}/create_makefile
%{tde_bindir}/create_makefiles
%{tde_bindir}/cvs-clean
%{tde_bindir}/cvs2dist
%{tde_bindir}/cvsbackport
%{tde_bindir}/cvsblame
%{tde_bindir}/cvscheck
%{tde_bindir}/cvsforwardport
%{tde_bindir}/cvslastchange
%{tde_bindir}/cvslastlog
%{tde_bindir}/cvsrevertlast
%{tde_bindir}/cvsversion
%{tde_bindir}/cxxmetric
%{tde_bindir}/extend_dmalloc
%{tde_bindir}/extractattr
%{tde_bindir}/extractrc
%{tde_bindir}/findmissingcrystal
%{tde_bindir}/fixkdeincludes
%{tde_bindir}/fixuifiles
%{tde_bindir}/includemocs
%{tde_bindir}/kde-build
%{tde_bindir}/kdedoc
%{tde_bindir}/tdekillall
%{tde_bindir}/kdelnk2desktop.py*
%{tde_bindir}/kdemangen.pl
%{tde_bindir}/makeobj
%{tde_bindir}/noncvslist
%{tde_bindir}/package_crystalsvg
%{tde_bindir}/png2mng.pl
%{tde_bindir}/pruneemptydirs
%{tde_bindir}/qtdoc
%{tde_bindir}/zonetab2pot.py*
%{tde_bindir}/svn2dist
%{tde_bindir}/svnrevertlast
%{tde_bindir}/svnforwardport
%{tde_bindir}/nonsvnlist
%{tde_bindir}/tdesvn-build
%{tde_bindir}/svnlastlog
%{tde_bindir}/svnversions
%{tde_bindir}/create_svnignore
%{tde_bindir}/svnlastchange
%{tde_bindir}/colorsvn
%{tde_bindir}/svnaddcurrentdir
%{tde_bindir}/svnbackport
%{tde_bindir}/svngettags
%{tde_bindir}/svnchangesince
%{tde_bindir}/svn-clean
%{tde_datadir}/apps/katepart/syntax/tdesvn-buildrc.xml
%{tde_mandir}/man1/adddebug.1*
%{tde_mandir}/man1/build-progress.sh.1*
%{tde_mandir}/man1/cheatmake.1*
%{tde_mandir}/man1/create_cvsignore.1*
%{tde_mandir}/man1/create_makefile.1*
%{tde_mandir}/man1/create_makefiles.1*
%{tde_mandir}/man1/cvsblame.1*
%{tde_mandir}/man1/cvscheck.1*
%{tde_mandir}/man1/cvs-clean.1*
%{tde_mandir}/man1/cvs2dist.1*
%{tde_mandir}/man1/cvsaskpass.1*
%{tde_mandir}/man1/cvsbackport.1*
%{tde_mandir}/man1/cvsforwardport.1*
%{tde_mandir}/man1/cvslastchange.1*
%{tde_mandir}/man1/cvslastlog.1*
%{tde_mandir}/man1/cvsrevertlast.1*
%{tde_mandir}/man1/cvsservice.1*
%{tde_mandir}/man1/cvsversion.1*
%{tde_mandir}/man1/cxxmetric.1*
%{tde_mandir}/man1/extend_dmalloc.1*
%{tde_mandir}/man1/extractattr.1*
%{tde_mandir}/man1/extractrc.1*
%{tde_mandir}/man1/findmissingcrystal.1*
%{tde_mandir}/man1/fixkdeincludes.1*
%{tde_mandir}/man1/fixuifiles.1*
%{tde_mandir}/man1/includemocs.1*
%{tde_mandir}/man1/kde-build.1*
%{tde_mandir}/man1/kdedoc.1*
%{tde_mandir}/man1/kdelnk2desktop.py.1*
%{tde_mandir}/man1/kdemangen.pl.1*
%{tde_mandir}/man1/licensecheck.1*
%{tde_mandir}/man1/noncvslist.1*
%{tde_mandir}/man1/makeobj.1*
%{tde_mandir}/man1/package_crystalsvg.1*
%{tde_mandir}/man1/png2mng.pl.1
%{tde_mandir}/man1/pruneemptydirs.1
%{tde_mandir}/man1/qtdoc.1*
%{tde_mandir}/man1/tdekillall.1*
%{tde_mandir}/man1/tdesvn-build.1*
%{tde_mandir}/man1/zonetab2pot.py.1*
%{tde_tdedocdir}/HTML/en/tdesvn-build/
#scripts/kde-devel-gdb /opt/trinity/share/tdesdk-scripts
#scripts/kde-devel-vim.vim /opt/trinity/share/tdesdk-scripts
#scripts/kde-emacs/*.el /opt/trinity/share/emacs/site-lisp/tdesdk-scripts
#scripts/kde.supp /opt/trinity/lib/valgrind
#scripts/completions /opt/trinity/share/tdesdk-scripts

#debian/desktop-i18n/createdesktop.pl /opt/trinity/lib/kubuntu-desktop-i18n/
#debian/desktop-i18n/findfiles /opt/trinity/lib/kubuntu-desktop-i18n/
#debian/desktop-i18n/msgsplit /opt/trinity/lib/kubuntu-desktop-i18n/

%if "%{?tde_prefix}" != "/usr"
%{tde_bindir}/licensecheck
%else
%exclude %{tde_bindir}/licensecheck
%endif

##########

%package -n trinity-kmtrace
Summary:	A Trinity memory leak tracer
Group:		Development/Languages/Other
Requires:	less

%description -n trinity-kmtrace
KMtrace is a TDE tool to assist with malloc debugging using glibc's
"mtrace" functionality.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kmtrace
%defattr(-,root,root,-)
%{tde_bindir}/demangle
%{tde_bindir}/kminspector
%{tde_bindir}/kmmatch
%{tde_bindir}/kmtrace
%dir %{tde_libdir}/kmtrace
%{tde_libdir}/kmtrace/libktrace.la
%{tde_libdir}/kmtrace/libktrace.so
%{tde_datadir}/apps/kmtrace/
%{tde_mandir}/man1/demangle.1*
%{tde_mandir}/man1/kminspector.1*
%{tde_mandir}/man1/kmmatch.1*
%{tde_mandir}/man1/kmtrace.1*

##########

%package -n trinity-kompare
Summary:	A Trinity GUI for viewing differences between files
Group:		Development/Languages/Other

%description -n trinity-kompare
Kompare is a graphical user interface for viewing the differences between
files.  It can compare two documents, create a diff file, display a diff
file and/or blend a diff file back into the original documents.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kompare
%defattr(-,root,root,-)
%{tde_bindir}/kompare
%{tde_libdir}/libkompareinterface.la
%{tde_libdir}/libkompareinterface.so.*
%{tde_tdelibdir}/libkomparenavtreepart.la
%{tde_tdelibdir}/libkomparenavtreepart.so
%{tde_tdelibdir}/libkomparepart.la
%{tde_tdelibdir}/libkomparepart.so
%{tde_tdeappdir}/kompare.desktop
%{tde_datadir}/apps/kompare/
%{tde_datadir}/services/komparenavtreepart.desktop
%{tde_datadir}/services/komparepart.desktop
%{tde_datadir}/servicetypes/komparenavigationpart.desktop
%{tde_datadir}/servicetypes/kompareviewpart.desktop
%{tde_datadir}/icons/hicolor/*/apps/kompare.png
%{tde_datadir}/icons/hicolor/scalable/apps/kompare.svgz
%{tde_tdedocdir}/HTML/en/kompare/
%{tde_mandir}/man1/kompare.1*

##########

%package -n trinity-kspy
Summary:	Examines the internal state of a Qt/TDE app
Group:		Development/Languages/Other
Requires:	trinity-tdelibs-devel

%description -n trinity-kspy
KSpy is a tiny library which can be used to graphically display
the QObjects in use by a Qt/TDE app.  In addition to the object tree,
you can also view the properties, signals and slots of any QObject.

Basically it provides much the same info as QObject::dumpObjectTree() and
QObject::dumpObjectInfo(), but in a much more convenient form.  KSpy has
minimal overhead for the application, because the kspy library is
loaded dynamically using KLibLoader.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kspy
%defattr(-,root,root,-)
%{tde_libdir}/libkspy.la
%{tde_libdir}/libkspy.so.*
%{tde_mandir}/man1/testkspy.1*

##########

%package -n trinity-kuiviewer
Summary:	Viewer for Qt Designer user interface files
Group:		Development/Languages/Other

%description -n trinity-kuiviewer
KUIViewer is a utility to display and test the user interface (.ui) files
generated by Qt Designer.  The interfaces can be displayed in a variety of
different widget styles.

The Qt Designer itself is in the package qt3-designer.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kuiviewer
%defattr(-,root,root,-)
%{tde_bindir}/kuiviewer
%{tde_tdelibdir}/libkuiviewerpart.so
%{tde_tdelibdir}/libkuiviewerpart.la
%{tde_tdelibdir}/quithumbnail.so
%{tde_tdelibdir}/quithumbnail.la
%{tde_tdeappdir}/kuiviewer.desktop
%{tde_datadir}/apps/kuiviewer/
%{tde_datadir}/apps/kuiviewerpart/
%{tde_datadir}/icons/hicolor/*/apps/kuiviewer.png
%{tde_datadir}/icons/locolor/*/apps/kuiviewer.png
%{tde_datadir}/services/designerthumbnail.desktop
%{tde_datadir}/services/kuiviewer_part.desktop
%{tde_tdedocdir}/HTML/en/kuiviewer/
%{tde_mandir}/man1/kuiviewer.1*

##########

%package -n trinity-libcvsservice0
Summary:	DCOP service for accessing CVS repositories
Group:		Development/Languages/Other
Requires:	cvs

%description -n trinity-libcvsservice0
This library provides a DCOP service for accessing and working with
remote CVS repositories.  Applications may link with this library to
access the DCOP service directly from C++.  Alternatively, scripts may
access the service using the standard "dcop" command-line tool.

DCOP is the Desktop Communication Protocol used throughout TDE.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-libcvsservice0
%defattr(-,root,root,-)
%{tde_bindir}/cvsaskpass
%{tde_bindir}/cvsservice
%{tde_libdir}/libcvsservice.so.*
%{tde_libdir}/libtdeinit_cvsaskpass.so
%{tde_libdir}/libtdeinit_cvsservice.so
%{tde_tdelibdir}/cvsaskpass.la
%{tde_tdelibdir}/cvsaskpass.so
%{tde_tdelibdir}/cvsservice.la
%{tde_tdelibdir}/cvsservice.so
%{tde_datadir}/services/cvsservice.desktop

##########

%package -n trinity-libcvsservice-devel
Summary:	Development files for CVS DCOP service
Group:		Development/Libraries/Other
Requires:	trinity-libcvsservice0 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libcvsservice-devel
The library libcvsservice provides a DCOP service for accessing and
working with remote CVS repositories.  Applications may link with this
library to access the DCOP service directly from C++.  Alternatively,
scripts may access the service using the standard "dcop" command-line
tool.

Development files for libcvsservice are included in this package.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-libcvsservice-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/cvsjob_stub.h
%{tde_tdeincludedir}/cvsservice_stub.h
%{tde_tdeincludedir}/repository_stub.h
%{tde_libdir}/libcvsservice.la
%{tde_libdir}/libcvsservice.so
%{tde_libdir}/libtdeinit_cvsaskpass.la
%{tde_libdir}/libtdeinit_cvsservice.la
%{tde_datadir}/cmake/cervisia.cmake

##########

%package -n trinity-poxml
Summary:	Tools for using PO-files to translate DocBook XML files
Group:		Development/Languages/Other

%description -n trinity-poxml
This is a collection of tools that facilitate translating DocBook XML
files using gettext message files (PO-files).

Also included are some miscellaneous command-line utilities for
manipulating DocBook XML files, PO-files and PO-template files.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-poxml
%defattr(-,root,root,-)
%{tde_bindir}/po2xml
%{tde_bindir}/split2po
%{tde_bindir}/swappo
%{tde_bindir}/transxx
%{tde_bindir}/xml2pot
%{tde_mandir}/man1/po2xml.1*
%{tde_mandir}/man1/split2po.1*
%{tde_mandir}/man1/swappo.1*
%{tde_mandir}/man1/transxx.1*
%{tde_mandir}/man1/xml2pot.1*

##########

%package -n trinity-umbrello
Summary:	UML modelling tool and code generator
Group:		Development/Languages/Other

%description -n trinity-umbrello
Umbrello UML Modeller is a Unified Modelling Language editor for TDE.
With UML you can create diagrams of software and other systems in an
industry standard format.  Umbrello can also generate code from your
UML diagrams in a number of programming languages.

The program supports class diagrams, sequence diagrams, collaboration
diagrams, use case diagrams, state diagrams, activity diagrams, component
diagrams and deployment diagrams.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-umbrello
%defattr(-,root,root,-)
%{tde_bindir}/umbodoc
%{tde_bindir}/umbrello
%{tde_tdeappdir}/umbrello.desktop
%{tde_datadir}/apps/umbrello/
%{tde_datadir}/icons/crystalsvg/*/actions/umbrello_*.png
%{tde_datadir}/icons/crystalsvg/*/mimetypes/umbrellofile.png
%{tde_datadir}/icons/crystalsvg/scalable/mimetypes/umbrellofile.svgz
%{tde_datadir}/icons/hicolor/*/apps/umbrello.png
%{tde_datadir}/icons/hicolor/scalable/apps/umbrello.svgz
%{tde_datadir}/icons/hicolor/*/mimetypes/umbrellofile.png
%{tde_datadir}/mimelnk/application/x-umbrello.desktop
%{tde_tdedocdir}/HTML/en/umbrello/
%{tde_mandir}/man1/umbrello.1*

##########

%if 0%{?build_kioslave}

%package tdeio-plugins
Summary:	Subversion ioslave for Trinity
Group:		Development/Languages/Other
Requires:	subversion

Obsoletes:	trinity-tdesdk-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdesdk-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This package provides easy access to remote SVN repositories from within
Konqueror, and TDE generally, by browsing them as if they were a
filesystem, using URLs like svn://hostname/path, or svn+ssh://, etc.

This package is part of Trinity, and a component of the TDE SDK module.

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_bindir}/tdeio_svn_helper
%{tde_tdelibdir}/kded_ksvnd.la
%{tde_tdelibdir}/kded_ksvnd.so
%{tde_tdelibdir}/tdeio_svn.la
%{tde_tdelibdir}/tdeio_svn.so
%{tde_datadir}/apps/konqueror/servicemenus/subversion_toplevel.desktop
%{tde_datadir}/apps/konqueror/servicemenus/subversion.desktop
%{tde_datadir}/services/kded/ksvnd.desktop
%{tde_datadir}/services/svn+file.protocol_tdesdk
%{tde_datadir}/services/svn+http.protocol_tdesdk
%{tde_datadir}/services/svn+https.protocol_tdesdk
%{tde_datadir}/services/svn+ssh.protocol_tdesdk
%{tde_datadir}/services/svn.protocol_tdesdk
%{tde_datadir}/icons/crystalsvg/*/actions/svn_switch.png
%{tde_datadir}/icons/crystalsvg/*/actions/svn_merge.png
%{tde_datadir}/icons/crystalsvg/*/actions/svn_branch.png
%{tde_datadir}/icons/crystalsvg/*/actions/svn_remove.png
%{tde_datadir}/icons/crystalsvg/*/actions/svn_add.png
%{tde_datadir}/icons/crystalsvg/*/actions/svn_status.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/svn_add.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/svn_status.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/svn_remove.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/svn_switch.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/svn_branch.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/svn_merge.svgz

%post tdeio-plugins
for proto in svn+file svn+http svn+https svn+ssh svn; do
  update-alternatives --install \
    %{tde_datadir}/services/${proto}.protocol \
    ${proto}.protocol \
    %{tde_datadir}/services/${proto}.protocol_tdesdk \
    10
done

%preun tdeio-plugins
if [ $1 -eq 0 ]; then
  for proto in svn+file svn+http svn+https svn+ssh svn; do
    update-alternatives --remove \
      ${proto}.protocol \
      %{tde_datadir}/services/${proto}.protocol_tdesdk || :
  done
fi

%endif

##########

%package -n trinity-tdeunittest
Summary:	Unit testing library for Trinity
Group:		Development/Languages/Other

Obsoletes:	trinity-kunittest < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kunittest = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdeunittest
tdeunittest is a small library that facilitates the writing of tests for
TDE developers. There are two ways to use the tdeunittest library. One is
to create dynamically loadable modules and use the tdeunittestmodrunner or
tdeunittestguimodrunner programs to run the tests. The other is to use the
libraries to create your own testing application.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-tdeunittest
%defattr(-,root,root,-)
%{tde_bindir}/tdeunittest
%{tde_bindir}/tdeunittest_debughelper
%{tde_bindir}/tdeunittestmod
%{tde_bindir}/tdeunittestguimodrunner
%{tde_libdir}/libtdeunittestgui.la
%{tde_libdir}/libtdeunittestgui.so.*

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries/Other

Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kbabel-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-misc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kspy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmtrace = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdeunittest = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libcvsservice-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kompare = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdesdk-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdesdk-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development files for tdesdk.

%files devel
%defattr(-,root,root,-)
# misc
%{tde_tdeincludedir}/kprofilemethod.h
%{tde_libdir}/libkstartperf.so
# kspy
%{tde_tdeincludedir}/kspy.h
%{tde_libdir}/libkspy.so
# kmtrace
%{tde_libdir}/kmtrace/libktrace_s.a
%{tde_tdeincludedir}/ktrace.h
# tdeunittest
%{tde_libdir}/libtdeunittestgui.so
%{tde_tdeincludedir}/tdeunittest/runnergui.h
# kompare
%{tde_libdir}/libkompareinterface.so

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8 || 0%{?mgaversion} >= 8
# Fix shebangs
sed -i "scripts/kdelnk2desktop.py" \
       "scripts/zonetab2pot.py" \
       "tdecachegrind/converters/hotshot2calltree" \
       "umbrello/umbrello/headings/heading.py" \
    -e "s|env python|env %{python}|"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# FIXME PCLinuxOS: '/usr/bin/ld: cannot find -ltdeabc'
%if 0%{?pclinuxos}
export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -L%{tde_libdir}"
%endif

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DMAN_INSTALL_DIR=%{tde_mandir} \
  -DPKGCONFIG_INSTALL_DIR=%{tde_tdelibdir}/pkgconfig \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DWITH_DBSEARCHENGINE=ON \
  -DWITH_KCAL=ON \
  -DBUILD_ALL=ON \
  %{!?build_kioslave:-DBUILD_KIOSLAVE=OFF} \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot} 

%__make install DESTDIR=%{?buildroot} -C build


# Installs kdepalettes
%__install -D -m 644 kdepalettes/kde_xpaintrc %{?buildroot}%{tde_datadir}/kdepalettes/kde_xpaintrc
%__install -D -m 644 kdepalettes/KDE_Gimp %{?buildroot}%{tde_datadir}/kdepalettes/KDE_Gimp
%__install -D -m 644 kdepalettes/README %{?buildroot}%{tde_datadir}/kdepalettes/README

# Installs SVN protocols as alternatives
%if 0%{?build_kioslave}
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+file.protocol %{?buildroot}%{tde_datadir}/services/svn+file.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+http.protocol %{?buildroot}%{tde_datadir}/services/svn+http.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+https.protocol %{?buildroot}%{tde_datadir}/services/svn+https.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_datadir}/services/svn.protocol %{?buildroot}%{tde_datadir}/services/svn.protocol_tdesdk
%endif

# Removes useless stuff
%__rm -f %{?buildroot}%{tde_datadir}/apps/kapptemplate/admin/debianrules

# Fix permissions
chmod 644 %{?buildroot}%{tde_datadir}/apps/kapptemplate/admin/Doxyfile.global

# Make kapptemplate archive
pushd  %{?buildroot}%{tde_datadir}/apps/kapptemplate
mkdir kapptemplate
mv admin appframework bin existing include kapp kpartapp kpartplugin kapptemplate/
tar cfz kapptemplate.tar.gz kapptemplate
rm -rf kapptemplate
popd

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file    kuiviewer      Development GUIDesigner
%suse_update_desktop_file    umbrello       Development Design
%suse_update_desktop_file    kbugbuster     Development Debugger
%suse_update_desktop_file -u catalogmanager Development Translation
%suse_update_desktop_file    kbabel         Development Translation
%suse_update_desktop_file -u kbabeldict     Development Translation
%suse_update_desktop_file    cervisia       Development RevisionControl
%suse_update_desktop_file    kompare        Development RevisionControl
%suse_update_desktop_file    tdecachegrind  Development Profiling
%endif

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"


%clean
%__rm -rf %{buildroot}


%changelog
