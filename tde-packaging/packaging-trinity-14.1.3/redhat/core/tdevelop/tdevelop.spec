#
# spec file for package tdevelop (version R14)
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
%define tde_pkg tdevelop
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Summary:	Integrated Development Environment for C++/C
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Group:		Development/Tools
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
Source1:	%{name}-rpmlintrc

Requires:	%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	tqt3-apps-devel >= 3.5.0
BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdesdk-devel >= %{tde_version}

Obsoletes:	trinity-kdevelop < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdevelop = %{?epoch:%{epoch}:}%{version}-%{release}

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	fdupes
BuildRequires:	desktop-file-utils
BuildRequires:	make

Requires:	make
Requires:	perl
Requires:	tqt3-designer >= 3.5.0
Requires:	libtqt3-mt-devel >= 3.5.0
Requires:	gettext
Requires:	ctags


# LIBIDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# PCRE support
BuildRequires:	pcre-devel

# DB5 support
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 33
BuildRequires:	libdb-devel

%else
# DB4 support
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

# FLEX support
BuildRequires:	flex
Requires: flex >= 2.5.4

# SVN support
BuildRequires:	subversion-devel

# NEON support
BuildRequires:	neon-devel

# OPENLDAP support
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
%if 0%{?mdkver} >= 5000000
BuildRequires:	lib64ldap-devel
%else
BuildRequires:	openldap-devel
%endif
%endif
%if 0%{?suse_version}
BuildRequires:	openldap2-devel
%endif
%if 0%{?rhel} == 5
BuildRequires:	openldap24-libs-devel
%endif

# LIBACL support
%if 0%{?suse_version} || 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
# ACL support
%if 0%{?mdkver} >= 5000000
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# PYTHON support
%global python python3
%global __python %__python3


%description
The TDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to programs
like gdb, the C/C++ compiler, and make. TDevelop manages or provides:

All development tools needed for C++ programming like Compiler,
Linker, automake and autoconf; KAppWizard, which generates complete,
ready-to-go sample applications; Classgenerator, for creating new
classes and integrating them into the current project; File management
for sources, headers, documentation etc. to be included in the
project; The creation of User-Handbooks written with SGML and the
automatic generation of HTML-output with the KDE look and feel;
Automatic HTML-based API-documentation for your project's classes with
cross-references to the used libraries; Internationalization support
for your application, allowing translators to easily add their target
language to a project;

tdevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%files
%defattr(-,root,root,-)
%{tde_bindir}/kdevassistant
%{tde_bindir}/kdevdesigner
%{tde_bindir}/tdevelop
%{tde_bindir}/tdevelop-htdig
%{tde_bindir}/kdevprj2kdevelop
%{tde_bindir}/kdevprofileeditor
%{tde_libdir}/tdeconf_update_bin/kdev-gen-settings-tdeconf_update
%config(noreplace) %{tde_confdir}/kdevassistantrc
%config(noreplace) %{tde_confdir}/tdeveloprc
%{tde_tdeappdir}/kdevassistant.desktop
%{tde_tdeappdir}/kdevdesigner.desktop
%{tde_tdeappdir}/tdevelop.desktop
%{tde_tdeappdir}/tdevelop_c_cpp.desktop
%{tde_tdeappdir}/tdevelop_kde_cpp.desktop
%{tde_tdeappdir}/tdevelop_ruby.desktop
%{tde_tdeappdir}/tdevelop_scripting.desktop
%{tde_tdelibdir}/tdeio_chm.la
%{tde_tdelibdir}/tdeio_chm.so
%{tde_tdelibdir}/tdeio_csharpdoc.la
%{tde_tdelibdir}/tdeio_csharpdoc.so
%{tde_tdelibdir}/tdeio_perldoc.la
%{tde_tdelibdir}/tdeio_perldoc.so
%{tde_tdelibdir}/tdeio_pydoc.la
%{tde_tdelibdir}/tdeio_pydoc.so
%{tde_tdelibdir}/libdocchmplugin.la
%{tde_tdelibdir}/libdocchmplugin.so
%{tde_tdelibdir}/libdoccustomplugin.la
%{tde_tdelibdir}/libdoccustomplugin.so
%{tde_tdelibdir}/libdocdevhelpplugin.la
%{tde_tdelibdir}/libdocdevhelpplugin.so
%{tde_tdelibdir}/libdocdoxygenplugin.la
%{tde_tdelibdir}/libdocdoxygenplugin.so
%{tde_tdelibdir}/libdockdevtocplugin.la
%{tde_tdelibdir}/libdockdevtocplugin.so
%{tde_tdelibdir}/libdocqtplugin.la
%{tde_tdelibdir}/libdocqtplugin.so
%{tde_tdelibdir}/libkchmpart.la
%{tde_tdelibdir}/libkchmpart.so
%{tde_tdelibdir}/libkdevabbrev.la
%{tde_tdelibdir}/libkdevabbrev.so
%{tde_tdelibdir}/libkdevadaproject.la
%{tde_tdelibdir}/libkdevadaproject.so
%{tde_tdelibdir}/libkdevadasupport.la
%{tde_tdelibdir}/libkdevadasupport.so
%{tde_tdelibdir}/libkdevantproject.la
%{tde_tdelibdir}/libkdevantproject.so
%{tde_tdelibdir}/libkdevappview.la
%{tde_tdelibdir}/libkdevappview.so
%{tde_tdelibdir}/libkdevappwizard.la
%{tde_tdelibdir}/libkdevappwizard.so
%{tde_tdelibdir}/libkdevastyle.la
%{tde_tdelibdir}/libkdevastyle.so
%{tde_tdelibdir}/libkdevautoproject.la
%{tde_tdelibdir}/libkdevautoproject.so
%{tde_tdelibdir}/libkdevbashsupport.la
%{tde_tdelibdir}/libkdevbashsupport.so
%{tde_tdelibdir}/libkdevbookmarks.la
%{tde_tdelibdir}/libkdevbookmarks.so
%{tde_tdelibdir}/libkdevclassview.la
%{tde_tdelibdir}/libkdevclassview.so
%{tde_tdelibdir}/libkdevcppsupport.la
%{tde_tdelibdir}/libkdevcppsupport.so
%{tde_tdelibdir}/libkdevcsharpsupport.la
%{tde_tdelibdir}/libkdevcsharpsupport.so
%{tde_tdelibdir}/libkdevctags2.la
%{tde_tdelibdir}/libkdevctags2.so
%{tde_tdelibdir}/libkdevcustompcsimporter.la
%{tde_tdelibdir}/libkdevcustompcsimporter.so
%{tde_tdelibdir}/libkdevcustomproject.la
%{tde_tdelibdir}/libkdevcustomproject.so
%{tde_tdelibdir}/libkdevdccoptions.la
%{tde_tdelibdir}/libkdevdccoptions.so
%{tde_tdelibdir}/libkdevdebugger.la
%{tde_tdelibdir}/libkdevdebugger.so
%{tde_tdelibdir}/libkdevdesignerpart.la
%{tde_tdelibdir}/libkdevdesignerpart.so
%{tde_tdelibdir}/libkdevdiff.la
%{tde_tdelibdir}/libkdevdiff.so
%{tde_tdelibdir}/libkdevdistpart.la
%{tde_tdelibdir}/libkdevdistpart.so
%{tde_tdelibdir}/libkdevdocumentation.la
%{tde_tdelibdir}/libkdevdocumentation.so
%{tde_tdelibdir}/libkdevdoxygen.la
%{tde_tdelibdir}/libkdevdoxygen.so
%{tde_tdelibdir}/libkdeveditorchooser.la
%{tde_tdelibdir}/libkdeveditorchooser.so
%{tde_tdelibdir}/libkdevfilecreate.la
%{tde_tdelibdir}/libkdevfilecreate.so
%{tde_tdelibdir}/libkdevfilegroups.la
%{tde_tdelibdir}/libkdevfilegroups.so
%{tde_tdelibdir}/libkdevfilelist.la
%{tde_tdelibdir}/libkdevfilelist.so
%{tde_tdelibdir}/libkdevfileselector.la
%{tde_tdelibdir}/libkdevfileselector.so
%{tde_tdelibdir}/libkdevfileview.la
%{tde_tdelibdir}/libkdevfileview.so
%{tde_tdelibdir}/libkdevfilter.la
%{tde_tdelibdir}/libkdevfilter.so
%{tde_tdelibdir}/libkdevfortransupport.la
%{tde_tdelibdir}/libkdevfortransupport.so
%{tde_tdelibdir}/libkdevfpcoptions.la
%{tde_tdelibdir}/libkdevfpcoptions.so
%{tde_tdelibdir}/libkdevfullscreen.la
%{tde_tdelibdir}/libkdevfullscreen.so
%{tde_tdelibdir}/libkdevgccoptions.la
%{tde_tdelibdir}/libkdevgccoptions.so
%{tde_tdelibdir}/libkdevgrepview.la
%{tde_tdelibdir}/libkdevgrepview.so
%{tde_tdelibdir}/libkdevjavasupport.la
%{tde_tdelibdir}/libkdevjavasupport.so
%{tde_tdelibdir}/libkdevtdelibsimporter.la
%{tde_tdelibdir}/libkdevtdelibsimporter.so
%{tde_tdelibdir}/libkdevkonsoleview.la
%{tde_tdelibdir}/libkdevkonsoleview.so
%{tde_tdelibdir}/libkdevmakeview.la
%{tde_tdelibdir}/libkdevmakeview.so
%{tde_tdelibdir}/libkdevopenwith.la
%{tde_tdelibdir}/libkdevopenwith.so
%{tde_tdelibdir}/libkdevpartexplorer.la
%{tde_tdelibdir}/libkdevpartexplorer.so
%{tde_tdelibdir}/libkdevpascalproject.la
%{tde_tdelibdir}/libkdevpascalproject.so
%{tde_tdelibdir}/libkdevpascalsupport.la
%{tde_tdelibdir}/libkdevpascalsupport.so
%{tde_tdelibdir}/libkdevperlsupport.la
%{tde_tdelibdir}/libkdevperlsupport.so
%{tde_tdelibdir}/libkdevpgioptions.la
%{tde_tdelibdir}/libkdevpgioptions.so
%{tde_tdelibdir}/libkdevphpsupport.la
%{tde_tdelibdir}/libkdevphpsupport.so
%{tde_tdelibdir}/libkdevpythonsupport.la
%{tde_tdelibdir}/libkdevpythonsupport.so
%{tde_tdelibdir}/libkdevqtimporter.la
%{tde_tdelibdir}/libkdevqtimporter.so
%{tde_tdelibdir}/libkdevquickopen.la
%{tde_tdelibdir}/libkdevquickopen.so
%{tde_tdelibdir}/libkdevrbdebugger.la
%{tde_tdelibdir}/libkdevrbdebugger.so
%{tde_tdelibdir}/libkdevregexptest.la
%{tde_tdelibdir}/libkdevregexptest.so
%{tde_tdelibdir}/libkdevreplace.la
%{tde_tdelibdir}/libkdevreplace.so
%{tde_tdelibdir}/libkdevrubysupport.la
%{tde_tdelibdir}/libkdevrubysupport.so
%{tde_tdelibdir}/libkdevscripting.la
%{tde_tdelibdir}/libkdevscripting.so
%{tde_tdelibdir}/libkdevscriptproject.la
%{tde_tdelibdir}/libkdevscriptproject.so
%{tde_tdelibdir}/libkdevsnippet.la
%{tde_tdelibdir}/libkdevsnippet.so
%{tde_tdelibdir}/libkdevsqlsupport.la
%{tde_tdelibdir}/libkdevsqlsupport.so
%{tde_tdelibdir}/libkdevtexttools.la
%{tde_tdelibdir}/libkdevtexttools.so
%{tde_tdelibdir}/libkdevtipofday.la
%{tde_tdelibdir}/libkdevtipofday.so
%{tde_tdelibdir}/libkdevtools.la
%{tde_tdelibdir}/libkdevtools.so
%{tde_tdelibdir}/libkdevtrollproject.la
%{tde_tdelibdir}/libkdevtrollproject.so
%{tde_tdelibdir}/libkdevuichooser.la
%{tde_tdelibdir}/libkdevuichooser.so
%{tde_tdelibdir}/libkdevvalgrind.la
%{tde_tdelibdir}/libkdevvalgrind.so
%{tde_tdelibdir}/libkdevvcsmanager.la
%{tde_tdelibdir}/libkdevvcsmanager.so
%{tde_datadir}/apps/tdeconf_update/
%{tde_datadir}/apps/kdevabbrev/
%{tde_datadir}/apps/kdevadaproject/
%{tde_datadir}/apps/kdevadasupport/
%{tde_datadir}/apps/kdevantproject/
%{tde_datadir}/apps/kdevappoutputview/
%{tde_datadir}/apps/kdevappwizard/
%{tde_datadir}/apps/kdevassistant/
%{tde_datadir}/apps/kdevastyle/
%{tde_datadir}/apps/kdevautoproject/
%{tde_datadir}/apps/kdevbashsupport/
%{tde_datadir}/apps/kdevclassview/
%{tde_datadir}/apps/kdevcppsupport/
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_add.png
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_delete.png
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_delete_all.png
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_edit.png
%{tde_datadir}/icons/hicolor/*/actions/ktip.png
%{tde_datadir}/icons/hicolor/*/apps/kdevassistant.png
%{tde_datadir}/icons/hicolor/*/apps/kdevdesigner.png
%{tde_datadir}/icons/hicolor/*/apps/tdevelop.png
%{tde_datadir}/icons/locolor/*/actions/tdevelop_tip.png
%{tde_datadir}/mimelnk/application/x-tdevelop.desktop
%{tde_datadir}/services/chm.protocol
%{tde_datadir}/services/csharpdoc.protocol
%{tde_datadir}/services/docchmplugin.desktop
%{tde_datadir}/services/doccustomplugin.desktop
%{tde_datadir}/services/docdevhelpplugin.desktop
%{tde_datadir}/services/docdoxygenplugin.desktop
%{tde_datadir}/services/dockdevtocplugin.desktop
%{tde_datadir}/services/docqtplugin.desktop
%{tde_datadir}/services/kchmpart.desktop
%{tde_datadir}/services/kdevabbrev.desktop
%{tde_datadir}/services/kdevadaproject.desktop
%{tde_datadir}/services/kdevadasupport.desktop
%{tde_datadir}/services/kdevantproject.desktop
%{tde_datadir}/services/kdevappoutputview.desktop
%{tde_datadir}/services/kdevappwizard.desktop
%{tde_datadir}/services/kdevastyle.desktop
%{tde_datadir}/services/kdevautoproject.desktop
%{tde_datadir}/services/kdevbashsupport.desktop
%{tde_datadir}/services/kdevbookmarks.desktop
%{tde_datadir}/services/kdevclassview.desktop
%{tde_datadir}/services/kdevcppsupport.desktop
%{tde_datadir}/services/kdevcsharpsupport.desktop
%{tde_datadir}/services/kdevcsupport.desktop
%{tde_datadir}/services/kdevctags2.desktop
%{tde_datadir}/services/kdevcustomproject.desktop
%{tde_datadir}/services/kdevdccoptions.desktop
%{tde_datadir}/services/kdevdebugger.desktop
%{tde_datadir}/services/kdevdesigner_part.desktop
%{tde_datadir}/services/kdevdiff.desktop
%{tde_datadir}/services/kdevdistpart.desktop
%{tde_datadir}/services/kdevdocumentation.desktop
%{tde_datadir}/services/kdevdoxygen.desktop
%{tde_datadir}/services/kdeveditorchooser.desktop
%{tde_datadir}/services/kdevfilecreate.desktop
%{tde_datadir}/services/kdevfilegroups.desktop
%{tde_datadir}/services/kdevfilelist.desktop
%{tde_datadir}/services/kdevfileselector.desktop
%{tde_datadir}/services/kdevfileview.desktop
%{tde_datadir}/services/kdevfilter.desktop
%{tde_datadir}/services/kdevfortransupport.desktop
%{tde_datadir}/services/kdevfpcoptions.desktop
%{tde_datadir}/services/kdevfullscreen.desktop
%{tde_datadir}/services/kdevg77options.desktop
%{tde_datadir}/services/kdevgccoptions.desktop
%{tde_datadir}/services/kdevgppoptions.desktop
%{tde_datadir}/services/kdevgrepview.desktop
%{tde_datadir}/services/kdevjavasupport.desktop
%{tde_datadir}/services/kdevtdeautoproject.desktop
%{tde_datadir}/services/kdevtdelibsimporter.desktop
%{tde_datadir}/services/kdevkonsoleview.desktop
%{tde_datadir}/services/kdevmakeview.desktop
%{tde_datadir}/services/kdevopenwith.desktop
%{tde_datadir}/services/kdevpartexplorer.desktop
%{tde_datadir}/services/kdevpascalproject.desktop
%{tde_datadir}/services/kdevpascalsupport.desktop
%{tde_datadir}/services/kdevpcscustomimporter.desktop
%{tde_datadir}/services/kdevperlsupport.desktop
%{tde_datadir}/services/kdevpgf77options.desktop
%{tde_datadir}/services/kdevpghpfoptions.desktop
%{tde_datadir}/services/kdevphpsupport.desktop
%{tde_datadir}/services/kdevpythonsupport.desktop
%{tde_datadir}/services/kdevqtimporter.desktop
%{tde_datadir}/services/kdevquickopen.desktop
%{tde_datadir}/services/kdevrbdebugger.desktop
%{tde_datadir}/services/kdevregexptest.desktop
%{tde_datadir}/services/kdevreplace.desktop
%{tde_datadir}/services/kdevrubysupport.desktop
%{tde_datadir}/services/kdevscripting.desktop
%{tde_datadir}/services/kdevscriptproject.desktop
%{tde_datadir}/services/kdevsnippet.desktop
%{tde_datadir}/services/kdevsqlsupport.desktop
%{tde_datadir}/services/kdevtexttools.desktop
%{tde_datadir}/services/kdevtipofday.desktop
%{tde_datadir}/services/kdevtmakeproject.desktop
%{tde_datadir}/services/kdevtools.desktop
%{tde_datadir}/services/kdevtrollproject.desktop
%{tde_datadir}/services/kdevuichooser.desktop
%{tde_datadir}/services/kdevvalgrind.desktop
%{tde_datadir}/services/kdevvcsmanager.desktop
%{tde_datadir}/services/perldoc.protocol
%{tde_datadir}/services/pydoc.protocol
%{tde_datadir}/servicetypes/tdevelopappfrontend.desktop
%{tde_datadir}/servicetypes/tdevelopcodebrowserfrontend.desktop
%{tde_datadir}/servicetypes/tdevelopcompileroptions.desktop
%{tde_datadir}/servicetypes/tdevelopcreatefile.desktop
%{tde_datadir}/servicetypes/tdevelopdifffrontend.desktop
%{tde_datadir}/servicetypes/tdevelopdocumentationplugins.desktop
%{tde_datadir}/servicetypes/tdeveloplanguagesupport.desktop
%{tde_datadir}/servicetypes/tdevelopmakefrontend.desktop
%{tde_datadir}/servicetypes/tdeveloppcsimporter.desktop
%{tde_datadir}/servicetypes/tdevelopplugin.desktop
%{tde_datadir}/servicetypes/tdevelopproject.desktop
%{tde_datadir}/servicetypes/tdevelopquickopen.desktop
%{tde_datadir}/servicetypes/tdevelopsourceformatter.desktop
%{tde_datadir}/servicetypes/tdevelopvcsintegrator.desktop
%{tde_datadir}/servicetypes/tdevelopversioncontrol.desktop
%{tde_datadir}/apps/kdevcsharpsupport/
%{tde_datadir}/apps/kdevctags2/
%{tde_datadir}/apps/kdevcustomproject/
%{tde_datadir}/apps/kdevdebugger/
%{tde_datadir}/apps/kdevdesigner/
%{tde_datadir}/apps/kdevdesignerpart/
%{tde_datadir}/apps/kdevdiff/
%{tde_datadir}/apps/kdevdistpart/
%{tde_datadir}/apps/kdevdocumentation/
%{tde_datadir}/apps/kdevdoxygen/
%{tde_datadir}/apps/tdevelop/
%{tde_datadir}/apps/kdevfilecreate/
%{tde_datadir}/apps/kdevfilelist/
%{tde_datadir}/apps/kdevfilter/
%{tde_datadir}/apps/kdevfortransupport/
%{tde_datadir}/apps/kdevfullscreen/
%{tde_datadir}/apps/kdevgrepview/
%{tde_datadir}/apps/kdevjavasupport/
%{tde_datadir}/apps/kdevmakeview/
%{tde_datadir}/apps/kdevpartexplorer/
%{tde_datadir}/apps/kdevpascalproject/
%{tde_datadir}/apps/kdevpascalsupport/
%{tde_datadir}/apps/kdevperlsupport/
%{tde_datadir}/apps/kdevphpsupport/
%{tde_datadir}/apps/kdevpythonsupport/
%{tde_datadir}/apps/kdevquickopen/
%{tde_datadir}/apps/kdevrbdebugger/
%{tde_datadir}/apps/kdevregexptest/
%{tde_datadir}/apps/kdevreplace/
%{tde_datadir}/apps/kdevrubysupport/
%{tde_datadir}/apps/kdevscripting/
%{tde_datadir}/apps/kdevscriptproject/
%{tde_datadir}/apps/kdevsnippet/
%{tde_datadir}/apps/kdevsqlsupport
%{tde_datadir}/apps/kdevtipofday/
%{tde_datadir}/apps/kdevtools/
%{tde_datadir}/apps/kdevtrollproject/
%{tde_datadir}/apps/kdevvalgrind/
%{tde_datadir}/apps/tdeio_pydoc/
%{tde_datadir}/desktop-directories/tde-development-tdevelop.directory
%{tde_tdedocdir}/HTML/en/tdevelop/
%{tde_libdir}/libd.so.0
%{tde_libdir}/libd.so.0.0.0
%{tde_libdir}/libkinterfacedesigner.so.0
%{tde_libdir}/libkinterfacedesigner.so.0.0.0
%{tde_tdelibdir}/libkdevvisualboyadvance.la
%{tde_tdelibdir}/libkdevvisualboyadvance.so
%{tde_datadir}/apps/kdevvisualboyadvance/
%{tde_tdedocdir}/HTML/en/tde_app_devel/
%{tde_datadir}/mimelnk/text/x-fortran.desktop
%{tde_datadir}/services/kdevvisualboyadvance.desktop
%{tde_tdedocdir}/HTML/en/kdevdesigner/

##########

%package devel
Summary: Development files for %{name}
Group:		Development/Libraries/Other
Requires: %{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdevelop-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdevelop-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development files for tdevelop.

%files devel
%defattr(-,root,root,-)
%{tde_libdir}/lib*.so
%{tde_libdir}/lib*.la
%{tde_includedir}/*

##########

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-tdelibs >= %{tde_version}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdevelop-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdevelop-libs = %{?epoch:%{epoch}:}%{version}-%{release}

%description libs
This package contains the libraries needed for the tdevelop programs.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/libdesignerintegration.so.0
%{tde_libdir}/libdesignerintegration.so.0.0.0
%{tde_libdir}/libdocumentation_interfaces.so.0
%{tde_libdir}/libdocumentation_interfaces.so.0.0.0
%{tde_libdir}/libgdbmi_parser.so.0
%{tde_libdir}/libgdbmi_parser.so.0.0.0
%{tde_libdir}/libkdevbuildbase.so.0
%{tde_libdir}/libkdevbuildbase.so.0.0.0
%{tde_libdir}/libkdevbuildtoolswidgets.so.0
%{tde_libdir}/libkdevbuildtoolswidgets.so.0.0.0
%{tde_libdir}/libkdevcatalog.so.0
%{tde_libdir}/libkdevcatalog.so.0.0.0
%{tde_libdir}/libkdevcppparser.so.0
%{tde_libdir}/libkdevcppparser.so.0.0.0
%{tde_libdir}/libtdevelop.so.1
%{tde_libdir}/libtdevelop.so.1.0.0
%{tde_libdir}/libkdevextras.so.0
%{tde_libdir}/libkdevextras.so.0.0.0
%{tde_libdir}/libkdevpropertyeditor.so.0
%{tde_libdir}/libkdevpropertyeditor.so.0.0.0
%{tde_libdir}/libkdevqmakeparser.so.0
%{tde_libdir}/libkdevqmakeparser.so.0.0.0
%{tde_libdir}/libkdevshell.so.0
%{tde_libdir}/libkdevshell.so.0.0.0
%{tde_libdir}/libkdevwidgets.so.0
%{tde_libdir}/libkdevwidgets.so.0.0.0
%{tde_libdir}/liblang_debugger.so.0
%{tde_libdir}/liblang_debugger.so.0.0.0
%{tde_libdir}/liblang_interfaces.so.0
%{tde_libdir}/liblang_interfaces.so.0.0.0
%{tde_libdir}/libprofileengine.so.0
%{tde_libdir}/libprofileengine.so.0.0.0

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}



%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

# openldap 2.4 includes (CentOS 5)
if [ -d "/usr/include/openldap24" ]; then
  RPM_OPT_FLAGS="-I%{_includedir}/openldap24 -L%{_libdir}/openldap24 ${RPM_OPT_FLAGS}"
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
  -DWITH_BUILDTOOL_ALL=ON \
  -DWITH_LANGUAGE_ALL=ON \
  -DWITH_VCS_ALL=OFF \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"


%clean
%__rm -rf %{buildroot}


%changelog
