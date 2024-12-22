#
# spec file for package tdebindings (version R14)
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

# Required for PCLinuxOS: removes the ldflag '--no-undefined'
%if 0%{?pclinuxos}
%define _disable_ld_no_undefined 1
%endif

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg tdebindings
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

# Special note for RHEL4:
#  You must create symlink 'libgcj.so' manually because it does not exist by default.
# E.g:
#  ln -s /usr/lib/libgcj.so.5.0.0 /usr/lib/jvm/java/lib/libgcj.so
# or 64 bits:
#  ln -s /usr/lib64/libgcj.so.5.0.0 /usr/lib/jvm/java/lib/libgcj.so

Name:			trinity-%{tde_pkg}
Summary:		TDE bindings to non-C++ languages
Version:		%{tde_version}
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	autoconf automake libtool m4
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# ZLIB support
BuildRequires: zlib-devel

# PERL module support
BuildRequires: perl(ExtUtils::MakeMaker)

# GTK2 support
%if 0%{?rhel} == 4
BuildRequires:	evolution28-gtk2-devel
Requires:		evolution28-gtk2
BuildRequires:	evolution28-glib2-devel
Requires:		evolution28-glib2
BuildRequires:	evolution28-cairo-devel
Requires:		evolution28-cairo
BuildRequires:	evolution28-pango-devel
Requires:		evolution28-pango
BuildRequires:	evolution28-atk-devel
Requires:		evolution28-atk
%else
%if 0%{?mdkver} >= 5000000
BuildRequires:	%{_lib}gtk+2.0-devel
%else
BuildRequires:	gtk2-devel
%endif
%endif

# XULRUNNER support
%if 0%{?fedora} || 0%{?rhel} >= 5 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} >= 1220
#BuildRequires: xulrunner-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires: mozilla-xulrunner20-devel
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# GTK1 support
%if 0%{?fedora} || (0%{?rhel} >= 5 && 0%{?rhel} <= 7)
%define with_gtk1 1
BuildRequires: glib-devel
BuildRequires: gtk+-devel
%endif
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
%if 0%{?with_gtk1}
%define with_gtk1 1
BuildRequires: glib-devel
BuildRequires: gtk+-devel
%endif
%endif
%if 0%{?mdkversion} == 201100
%define with_gtk1 1
BuildRequires: %{_lib}glib1.2-devel
BuildRequires: %{_lib}gtk+-devel
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:	libgdk_pixbuf2.0-devel
%else
BuildRequires:	%{_lib}gdk_pixbuf2.0-devel
%endif
%endif
%if 0%{?fedora}
%if 0%{?fedora} >= 17
BuildRequires: gdk-pixbuf2-devel
%else
BuildRequires: gdk-pixbuf-devel
%endif
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

# PYTHON support
%define with_python 1
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

## ruby
BuildRequires:	ruby-devel >= 1.8
BuildRequires:	ruby >= 1.8
%if 0%{?fedora} >= 19
BuildRequires:	rubypick
%endif

# Check for Ruby library directory
%if "%{?ruby_libarchdir}" != "" && "%{?ruby_libarchdir}" != "%{_libdir}/%{name}"
%define ruby_arch %{?ruby_libarchdir}
%else
%if "%{?rb_archdir}" != ""
%define ruby_arch %{?rb_archdir}
%else
%if "%{?ruby_archdir}" != ""
%define ruby_arch %{?ruby_archdir}
%else
%{!?ruby_arch: %define ruby_arch %(ruby -rrbconfig -e 'puts Config::CONFIG["archdir"]' || ruby -rrbconfig -e 'puts RbConfig::CONFIG["archdir"]')}
%endif
%endif
%endif
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
%define ruby_arch %(ruby -rrbconfig -e 'puts Config::CONFIG["archdir"]')
%endif
%if 0%{?pclinuxos}
%define ruby_arch %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["archdir"]')
%endif

%if "%{?ruby_libdir}" != ""
%define ruby_rubylibdir %{?ruby_libdir}
%else
%if "%{?rb_libdir}" != ""
%define ruby_rubylibdir %{?rb_libdir}
%else
%{!?ruby_rubylibdir: %define ruby_rubylibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["rubylibdir"]' || ruby -rrbconfig -e 'puts RbConfig::CONFIG["rubylibdir"]')}
%endif
%endif

# Ruby 1.9 includes are located in strance directories ... (taken from ruby 1.9 spec file)
%global	_normalized_cpu	%(echo %{_target_cpu} | sed 's/^ppc/powerpc/;s/i.86/i386/;s/sparcv./sparc/;s/armv.*/arm/')

## java
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
BuildRequires:	java-1.4.2-gcj-compat-devel
BuildRequires:	libgcj-devel
BuildRequires:	gcc-java
%endif

%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}

# PCLinuxOS use SUN's Java
%if 0%{?pclinuxos}
BuildRequires:	java-devel
%else

# Others use OpenJDK
BuildRequires: java-openjdk
BuildRequires: java-devel >= 1.4.2
%if 0%{?suse_version} >= 1320
BuildRequires:	java-1_8_0-openjdk-devel
%endif
%if 0%{?fedora} >= 21 || 0%{?mgaversion} >= 5 || 0%{?rhel} >= 8
BuildRequires: java-1.8.0-openjdk-devel
%endif
%if 0%{?fedora} == 17 ||  0%{?fedora} == 18 ||  0%{?fedora} == 19 || 0%{?fedora} == 20 || 0%{?suse_version} == 1230 || 0%{?suse_version} == 1310 || 0%{?mgaversion} == 3 || 0%{?mgaversion} == 4 || 0%{?rhel} == 7
BuildRequires: java-1.7.0-openjdk-devel
%endif
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
BuildRequires: java-1.6.0-openjdk-devel
%endif

%endif
%endif

%if 0%{?suse_version}
%define java_home %{_usr}/%{_lib}/jvm/java
%else
%if 0%{?rhel} == 4
%define java_home %{_usr}/lib/jvm/java-1.4.2-gcj-1.4.2.0
%else
%define java_home %{_usr}/lib/jvm/java
%endif
%endif
%if 0%{?pclinuxos} == 0
%define with_java 1
%endif

## Perl
# There is no 'perl-devel' package on RHEL5
%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	perl-devel
%endif
%define perl_vendorarch %{expand:%%(eval `perl -V:installvendorarch`; echo $installvendorarch)}

## QScintilla
BuildRequires:	libtqscintilla-devel >= %{?tde_epoch:%{tde_epoch}:}1.7.1
%define with_qscintilla 1

Obsoletes:	trinity-kdebindings < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebindings = %{?epoch:%{epoch}:}%{version}-%{release}

# Metapackage requires
%if 0%{?with_java}
Requires: trinity-tdebindings-java = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-juic = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: trinity-libsmoketqt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libsmoketde = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: perl-dcop = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{with_python}
Requires: python-dcop = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: trinity-libkjsembed1 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kjscmd = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libkorundum0-ruby = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libqt0-ruby = %{?epoch:%{epoch}:}%{version}-%{release}


%description
TDE/DCOP bindings to non-C++ languages

%files
%defattr(-,root,root,-)

##########

%package java
Summary:	TDE Java bindings metapackage [Trinity]
Group:		System/Libraries
Requires:	trinity-libdcop3-java = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libdcop3-jni = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libqt3-java = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtqt3-jni = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtrinity-java = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtrinity-jni = %{?epoch:%{epoch}:}%{version}-%{release}

%description java
A metapackage depending on all TDE, Qt and DCOP bindings libraries
related to the Java language.

This package is part of the official TDE bindings module.

%files java
%defattr(-,root,root,-)

##########

%if 0%{?with_java}

%package -n trinity-libdcop3-java
Summary:	DCOP bindings for Java [Trinity]
Group:		System/Libraries

Requires:	trinity-libdcop3-jni = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libdcop3-java
This package contains the Java classes necessary to run Java programs
using the Java DCOP bindings. DCOP is the TDE Desktop COmmunications
Protocol, used for communicating with running TDE applications.

This package is part of the official TDE bindings module.

%files -n trinity-libdcop3-java
%defattr(-,root,root,-)
%{tde_libdir}/java/org/

%endif

##########

%if 0%{?with_java}

%package -n trinity-libdcop3-java-devel
Summary:	DCOP bindings for Java (dcopidl2java program) [Trinity]
Group:		Development/Languages/Java
Requires:	trinity-libdcop3-java = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libdcop3-java-devel
This package contains the dcopidl2java program which generates Java 
stubs from DCOP IDL files, necessary to do development with the DCOP Java
bindings. DCOP is the TDE Desktop COmmunications Protocol, used for
communicating with running TDE applications.

This package is part of the official TDE bindings module.

%files -n trinity-libdcop3-java-devel
%defattr(-,root,root,-)
%{tde_bindir}/dcopidl2java
%{tde_mandir}/man1/dcopidl2java.1*

%endif

##########

%if 0%{?with_java}

%package -n trinity-libdcop3-jni
Summary:	DCOP bindings for Java ( Native libraries ) [Trinity]
Group:		System/Libraries

%description -n trinity-libdcop3-jni
This package contains the shared libraries and scripts necessary to
run programs using the Java DCOP bindings. DCOP is the TDE Desktop
COmmunications Protocol, used for communicating with running TDE
applications.

This package is part of the official TDE bindings module.

%files -n trinity-libdcop3-jni
%defattr(-,root,root,-)
%{tde_libdir}/libjavadcop.la
%{tde_libdir}/libjavadcop.so

%endif

##########

%if 0%{?with_java}

%package -n trinity-libqt3-java
Summary:	Java bindings for Qt [Trinity]
Group:		System/Libraries
Requires:	trinity-libdcop3-jni = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtqt3-jni = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-juic = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libqt3-java
This package contains the Java classes necessary to run Java programs
using the Java Qt bindings. Qt is a very popular GUI toolkit, used by
the TDE desktop environment.

It also includes many example programs that make use of these bindings,
plus many of the Qt Tutorial examples translated into Java.

This package is part of the official TDE bindings module.

%files -n trinity-libqt3-java
%defattr(-,root,root,-)
%{tde_libdir}/java/qtjava*.jar
%{tde_tdedocdir}/HTML/en/javalib/

%endif

##########

%if 0%{?with_java}

%package -n trinity-libtqt3-jni
Summary:	Java bindings for TQt ( Native libraries ) [Trinity]
Group:		System/Libraries

Obsoletes:	trinity-libqt3-jni < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libqt3-jni = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtqt3-jni
This package contains the shared libraries necessary to run Java
programs using the Java Qt bindings. Qt is a very popular GUI
toolkit, used by the TDE desktop environment.

This package is part of the official TDE bindings module.

%files -n trinity-libtqt3-jni
%defattr(-,root,root,-)
%{tde_libdir}/lib*qtjavasupport.la
%{tde_libdir}/lib*qtjavasupport.so.*
%{tde_libdir}/jni/lib*qtjava.la
%{tde_libdir}/jni/lib*qtjava.so.*
%doc qtjava/ChangeLog

%endif

##########

%if 0%{?with_java}

%package -n trinity-libtqt3-jni-devel
Summary:	Development files fo Java bindings for TQt ( Native libraries ) [Trinity]
Group:		Development/Languages/Java
Requires:	trinity-libtqt3-jni = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-libqt3-jni-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libqt3-jni-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtqt3-jni-devel
This package contains the development files for trinity-libtqt3-jni.

This package is part of the official TDE bindings module.

%files -n trinity-libtqt3-jni-devel
%defattr(-,root,root,-)
%{tde_libdir}/lib*qtjavasupport.so
%{tde_libdir}/jni/lib*qtjava.so

%endif

##########

%if 0%{?with_java}

%package -n trinity-libtrinity-java
Summary:	Tdelibs bindings for Java [Trinity]
Group:		System/Libraries

Requires:	trinity-libtrinity-jni = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtrinity-java
This package contains the Java classes necessary to run Java programs
using the Java tdelibs bindings. TDE is the Trinity Desktop Environment, a
very popular UNIX Desktop Environment.

It also includes some example applications that use these Java
classes, and multiple usage samples of the most common TDE classes.

This package is part of the official TDE bindings module.

%files -n trinity-libtrinity-java
%defattr(-,root,root,-)
%{tde_libdir}/java/koala*.jar

%endif

##########

%if 0%{?with_java}

%package -n trinity-libtrinity-jni
Summary:	Tdelibs bindings for java ( Native libraries ) [Trinity]
Group:		System/Libraries

%description -n trinity-libtrinity-jni
This package contains the shared libraries necessary to run Java
programs using the Java tdelibs bindings. TDE is the Trinity Desktop
Environment, a very popular UNIX Desktop Environment.

This package is part of the official TDE bindings module.

%files -n trinity-libtrinity-jni
%defattr(-,root,root,-)
%{tde_libdir}/jni/libtdejava.la
%{tde_libdir}/jni/libtdejava.so.*
%doc tdejava/ChangeLog

%endif

##########

%if 0%{?with_java}

%package -n trinity-libtrinity-jni-devel
Summary:	Development files for tdelibs bindings for java ( Native libraries ) [Trinity]
Group:		Development/Languages/Java
Requires:	trinity-libtrinity-jni = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtrinity-jni-devel
This package contains the development files for trinity-libtrinity-jni.

This package is part of the official TDE bindings module.

%files -n trinity-libtrinity-jni-devel
%defattr(-,root,root,-)
%{tde_libdir}/jni/libtdejava.so

%endif

##########

%package -n trinity-libsmoketqt
Summary:	SMOKE Binding Library to Qt
Group:		System/Libraries

Obsoletes:	trinity-libsmokeqt1 < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libsmokeqt1 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libsmoketqt
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
Qt library.

This package is part of the official TDE bindings module.

%files -n trinity-libsmoketqt
%defattr(-,root,root,-)
%{tde_libdir}/libsmoketqt.so.*

##########

%package -n trinity-libsmoketqt-devel
Summary:	SMOKE Binding Library to TQt - Development Files
Group:		Development/Languages/Other
Requires:	trinity-libsmoketqt = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-libsmokeqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libsmokeqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libsmoketqt-devel
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
Qt library. This package contains the development files for the
library.

If you are a normal user, you probably don't need this
package.

This package is part of the official TDE bindings module.

%files -n trinity-libsmoketqt-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/smoke.h
%{tde_libdir}/libsmoketqt.so
%{tde_libdir}/libsmoketqt.la

##########

%package -n trinity-libsmoketde
Summary:	SMOKE Binding Library to TDE
Group:		System/Libraries

Obsoletes:	trinity-libsmokekde1 < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libsmokekde1 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libsmoketde
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
TDE libraries.

This package is part of the official TDE bindings module.

%files -n trinity-libsmoketde
%defattr(-,root,root,-)
%{tde_libdir}/libsmoketde.so.*

##########

%package -n trinity-libsmoketde-devel
Summary:	SMOKE Binding Library to TDE - Development Files
Group:		Development/Languages/Other
Requires:	trinity-libsmoketde = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-libsmokekde-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libsmokekde-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libsmoketde-devel
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
Qt and TDE libraries. This package contains the development files for
the library.

If you are a normal user, you probably don't need this
package.

This package is part of the official TDE bindings module.

%files -n trinity-libsmoketde-devel
%defattr(-,root,root,-)
%{tde_libdir}/libsmoketde.so
%{tde_libdir}/libsmoketde.la

##########

%package -n perl-dcop
Summary:	DCOP Bindings for Perl 
Group:		System/Libraries
%if 0%{?suse_version}
Requires:	perl-base
%else
Requires:	perl
%endif

Obsoletes:	trinity-kdebindings-dcopperl < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebindings-dcopperl = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-perl-dcop < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-perl-dcop = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n perl-dcop
Perl bindings to the DCOP interprocess communication protocol used by TDE

%files -n perl-dcop
%defattr(-,root,root,-)
%{perl_vendorarch}/auto/DCOP/
%{perl_vendorarch}/DCOP.pm
%{perl_vendorarch}/DCOP/
%doc dcopperl/AUTHORS dcopperl/Changes dcopperl/README dcopperl/TODO
%{tde_mandir}/man3/DCOP.3pm*

##########

%if 0%{with_python}

%package -n python-dcop
Summary:	DCOP bindings for Python
Group:		System/Libraries
Requires:	%{python}

Obsoletes:	trinity-python-dcop < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-python-dcop = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python-dcop
This package contains the shared libraries necessary to run and
develop Python programs using the Python DCOP bindings
libraries. DCOP is the TDE Desktop COmmunications Protocol, used for
communicating with running TDE applications.

This package is part of the official TDE bindings module.

%files -n python-dcop
%defattr(-,root,root,-)
%{python_sitearch}/pcop.la
%{python_sitearch}/pcop.so
%if 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?rhel} == 7 || 0%{?suse_version}
%{python_sitearch}/pydcop.py*
%if 0%{?rhel} == 7
%{python_sitearch}/__pycache__/pydcop.*.pyc
%endif
%else
%pycached %{python_sitearch}/pydcop.py
%endif

%endif

##########

%package -n trinity-libkjsembed1
Summary:	Embedded JavaScript library
Group:		System/Libraries

%description -n trinity-libkjsembed1
This package contains the shared libraries necessary to run programs
linked with the KJSEmbed library. This library provides JavaScript
embedded scripting facilities to TDE applications.

This package is part of the official TDE bindings module.

%files -n trinity-libkjsembed1
%defattr(-,root,root,-)
%{tde_libdir}/libkjsembed.so.*
%{tde_tdelibdir}/libimagefxplugin.la
%{tde_tdelibdir}/libimagefxplugin.so
%{tde_datadir}/services/imagefx_plugin.desktop
%{tde_tdelibdir}/libqprocessplugin.so
%{tde_tdelibdir}/libqprocessplugin.la
%{tde_datadir}/services/qprocess_plugin.desktop
%{tde_tdelibdir}/libfileitemplugin.la
%{tde_tdelibdir}/libfileitemplugin.so
%{tde_datadir}/services/tdefileitem_plugin.desktop
%{tde_datadir}/apps/kjsembed/
%{tde_datadir}/servicetypes/binding_type.desktop
%{tde_bindir}/embedjs
%{tde_datadir}/apps/embedjs/
%{tde_tdeappdir}/embedjs.desktop
%{tde_datadir}/icons/hicolor/16x16/apps/embedjs.png
%{tde_datadir}/icons/hicolor/32x32/apps/embedjs.png
%{tde_tdelibdir}/libjavascript.la
%{tde_tdelibdir}/libjavascript.so
%dir %{tde_datadir}/apps/kate
%dir %{tde_datadir}/apps/kate/scripts
%{tde_datadir}/apps/kate/scripts/swaptabs.js
%{tde_datadir}/apps/kate/scripts/swaptabs.ui
%{tde_datadir}/apps/kate/scripts/swaptabs.desktop
%{tde_datadir}/services/javascript.desktop
%doc kjsembed/docs/ChangeLog

##########

%package -n trinity-libkjsembed-devel
Summary:	Embedded JavaScript library (Development files)
Group:		Development/Libraries/Other
Requires:	trinity-libkjsembed1 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkjsembed-devel
This package contains the header files and symbolic links necessary
to develop and compile programs using the KJSEmbed library. This
library provides JavaScript embedded scripting facilities to TDE
applications.

It also includes lots of example programs that make use of these
bindings, plus comprehensive documentation of the bindings.

This package is part of the official TDE bindings module.

%files -n trinity-libkjsembed-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kjsembed/
%{tde_libdir}/libkjsembed.so
%{tde_libdir}/libkjsembed.la
%{tde_docdir}/trinity-libkjsembed-devel/

##########

%package -n trinity-kjscmd
Summary:	A script interpreter using the TDE JavaScript library
Group:		System/Libraries
Provides:	%{tde_bindir}/kjscmd

%description -n trinity-kjscmd
This package contains the kjscmd program, which is a standalone
JavaScript interpreter using the KJSEmbed library.

This package is part of the official TDE bindings module.

%files -n trinity-kjscmd
%defattr(-,root,root,-)
%{tde_bindir}/kjscmd
%{tde_tdeappdir}/kjscmd.desktop
%{tde_mandir}/man1/kjscmd.*
%{tde_tdelibdir}/libjsconsoleplugin.la
%{tde_tdelibdir}/libjsconsoleplugin.so

##########

%if 0%{?with_java}
%package -n trinity-juic
Summary:	The Qt Java UI Compiler
Group:		Development/Languages/Java
Requires:	trinity-libqt3-java = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-juic
This package contains the juic program, which is used to convert
a UI description file generated by the Qt Designer, and converts
it into a Qt Java class. It is necessary for compiling and 
developing programs using the Qt Java bindings together with Qt
Designer.

This package is part of the official TDE bindings module.

%files -n trinity-juic
%defattr(-,root,root,-)
%{tde_bindir}/juic
%{tde_datadir}/juic/
%{tde_mandir}/man1/juic.1*
%endif

##########

%package -n trinity-libkorundum0-ruby
Summary:	TDE bindings for Ruby [Trinity]
Group:		System/Libraries
Requires:	trinity-libqt0-ruby = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkorundum0-ruby
This package contains the files necessary for running and developing
Ruby code using the Korundum TDE Ruby bindings.

It also includes some example programs and templates that make use of
these bindings.

This package is part of the official TDE bindings module.

%files -n trinity-libkorundum0-ruby
%defattr(-,root,root,-)
%{tde_bindir}/rbtdesh
%{tde_bindir}/rbtdeapi
%{tde_bindir}/krubyinit
%{tde_bindir}/rbtdeconfig_compiler
%{ruby_rubylibdir}/Korundum.rb
%dir %{ruby_rubylibdir}/TDE
%{ruby_rubylibdir}/TDE/korundum.rb
%{ruby_arch}/korundum.la
%{ruby_arch}/korundum.so*
%doc korundum/ChangeLog
%{tde_mandir}/man1/krubyinit.1*
%{tde_mandir}/man1/rbtdeapi.1*
%{tde_mandir}/man1/rbtdesh.1*

##########

%package -n trinity-libqt0-ruby
Summary:	Qt bindings for Ruby [Trinity]
Group:		System/Libraries
Requires:	ruby

%description -n trinity-libqt0-ruby
This package contains the files necessary for running and developing
Ruby code using the Qt Ruby bindings.

It also includes some example programs that make use of these bindings,
plus many of the Qt Tutorial examples translated into Ruby.

This package is part of the official TDE bindings module.

%files -n trinity-libqt0-ruby
%defattr(-,root,root,-)
%{tde_bindir}/rbqtsh
%{tde_bindir}/rbqtapi
%{tde_bindir}/rbuic
%{tde_bindir}/qtrubyinit
%dir %{ruby_rubylibdir}/Qt
%{ruby_rubylibdir}/Qt/qtruby.rb
%{ruby_rubylibdir}/Qt.rb
%{ruby_arch}/qtruby.so*
%{ruby_arch}/qtruby.la
%{ruby_arch}/tqui.so*
%{ruby_arch}/tqui.la
%doc qtruby/ChangeLog
%{tde_mandir}/man1/qtrubyinit.1*
%{tde_mandir}/man1/rbqtapi.1*
%{tde_mandir}/man1/rbqtsh.1*
%{tde_mandir}/man1/rbuic.1*

##########

%if 0
%package -n trinity-kmozilla
Summary:	Kmozilla for TDE
Group:		System/Libraries

%description -n trinity-kmozilla
This package contains the kmozilla library fro TDE.

%files -n trinity-kmozilla
%defattr(-,root,root,-)
%{tde_bindir}/kmozilla
%{tde_libdir}/libkmozillapart.so.*
%{tde_libdir}/libkmozillapart.so
%{tde_libdir}/libkmozillapart.la
%{tde_datadir}/services/kmozilla.desktop
%endif

##########

%package -n trinity-xpart-notepad
Summary:	A small XPart editor
Group:		Productivity/Scientific/Math

%description -n trinity-xpart-notepad
xpart_notepad is a small XPart editor. Use it to understand how to use XPart.

%files -n trinity-xpart-notepad
%defattr(-,root,root,-)
%{tde_bindir}/shell_xparthost
%{tde_bindir}/xp_notepad
%{tde_libdir}/libxp_notepadpart.la
%{tde_libdir}/libxp_notepadpart.so
%{tde_libdir}/libxp_notepadpart.so.*
%{tde_datadir}/services/xp_notepad.desktop
%doc xparts/xpart_notepad/README

##########

%if 0%{?with_gtk1}
%package -n trinity-libgtkxparts1
Summary:	Xparts library for GTK
Group:		Development/Languages/Other

%description -n trinity-libgtkxparts1
This package contains the xparts library for GTK.

%files -n trinity-libgtkxparts1
%defattr(-,root,root,-)
%{tde_libdir}/libgtkxparts.so.*
%{tde_libdir}/libgtkxparts.la

%endif

##########

%package -n trinity-libtdexparts
Summary:	Xparts library for TDE
Group:		Development/Languages/Other

Obsoletes:	trinity-libkdexparts1 < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libkdexparts1 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtdexparts
This package contains the xparts library for TDE.

%files -n trinity-libtdexparts
%defattr(-,root,root,-)
%{tde_libdir}/libtdexparts.so.*
%{tde_libdir}/libtdexparts.la

##########

%package -n trinity-libxparts-devel
Summary:	Xparts development files
Group:		Development/Languages/Other
%if 0%{?with_gtk1}
Requires:	trinity-libgtkxparts1 = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:	trinity-libtdexparts = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libxparts-devel
This package contains the development files for Xparts library.

%files -n trinity-libxparts-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/xtdeparts/
%if 0%{?with_gtk1}
%{tde_libdir}/libgtkxparts.so
%endif
%{tde_libdir}/libtdexparts.so

##########

%package xparts-extras
Summary:	Extra xparts for TDE [Trinity]
Group:		Development/Languages/Other

# Metapckage requires
Requires:	trinity-xpart-notepad = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?with_gtk1}
Requires:	trinity-libgtkxparts1 = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:	trinity-libtdexparts = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libdcop-c = %{?epoch:%{epoch}:}%{version}-%{release}

%description xparts-extras
This package contains extra xparts-based modules for Trinity
This includes the mozilla-konqueror plugin

This package is part of the official TDE bindings module.

%files xparts-extras
%defattr(-,root,root,-)

###########

%package -n trinity-libdcop-c
Summary:	DCOP bindings for C [Trinity]
Group:		System/Libraries

%description -n trinity-libdcop-c
This package contains the DCOP bindings for C.

%files -n trinity-libdcop-c
%defattr(-,root,root,-)
%{tde_libdir}/libdcopc.so.*

###########

%package -n trinity-libdcop-c-devel
Summary:	DCOP bindings for C, development files [Trinity]
Group:		Development/Languages/C and C++
Requires:	trinity-libdcop-c = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libdcop-c-devel
This package contains the development files for DCOP bindings for C.

%files -n trinity-libdcop-c-devel
%defattr(-,root,root,-)
%{tde_libdir}/libdcopc.so
%{tde_libdir}/libdcopc.la
%{tde_tdeincludedir}/dcopc/

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Languages/Other

Requires:	trinity-tdelibs-devel >= %{tde_version}
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdebindings-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebindings-devel = %{?epoch:%{epoch}:}%{version}-%{release}

# Metapackage
Requires:	trinity-libsmoketqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?with_java}
Requires:	trinity-libdcop3-java-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:	trinity-libsmoketde-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkjsembed-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libxparts-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libdcop-c-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?with_java}
Requires:	trinity-libtqt3-jni-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtrinity-jni-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description devel
This package contains the development files for the TDE bindings.

%files devel
%defattr(-,root,root,-)

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

%if "%{?perl_vendorarch}" == ""
exit 1
%endif

%if "%{?ruby_rubylibdir}" == ""
exit 2
%endif

%if "%{?ruby_arch}" == ""
exit 3
%endif

%if 0%{?mdkver} >= 5000000
touch config.h.in
%endif

# [tdebindings] Function 'rb_frame_this_func' does not exist in RHEL4/5
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
%__sed -i "qtruby/rubylib/qtruby/Qt.cpp" \
       -i "korundum/rubylib/korundum/Korundum.cpp" \
       -e "s|rb_frame_this_func|rb_frame_last_func|g"
%endif

# Another strange FTBFS in RHEL 5
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
%__sed -i "xparts/xpart_notepad/shell_xparthost.cpp" \
       -i "xparts/xpart_notepad/xp_notepad.cpp" \
       -e "/TDEApplication/ s| );|, true, true, true);|"
%endif

# Disable kmozilla, it does not build with recent xulrunner (missing 'libmozjs.so')
%__sed -i "xparts/Makefile.am" \
       -e "s|SUBDIRS = .*|SUBDIRS = src xpart_notepad|"

# Fix Fedora >= 28 automatic invalid dependency to '/usr/bin/kjscmd'
%if 0%{?fedora} >= 28 || 0%{?mgaversion} >= 7 || 0%{?rhel} >= 8
%__sed -i "kjsembed/tdescript/swaptabs.js" \
       -i "kjsembed/stdlib/cmdline.js" \
       -e "s|/usr/bin/env kjscmd|%{tde_bindir}/kjscmd|"
%endif

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export TDEDIR=%{tde_prefix}

unset JAVA_HOME ||:
%{?java_home:JAVA_HOME=%{java_home}; export JAVA_HOME}

# sip/PyQt/PyKDE built separately, not here
export DO_NOT_COMPILE="$DO_NOT_COMPILE python"

# Ruby headers, strange location ...
if [ -d "/usr/include/%{_normalized_cpu}-linux" ]; then
  export EXTRA_INCLUDES="/usr/include/%{_normalized_cpu}-linux"
fi

# Specific path for RHEL4
if [ -d "/usr/X11R6" ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi
if [ -d "/usr/evolution28" ]; then
  export PATH="/usr/evolution28/bin:${PATH}"
  export PKG_CONFIG_PATH="/usr/evolution28/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"
fi

# Warning: openSUSE 13.1: /usr/include/ruby-2.0.0/ruby.h
%if 0%{?suse_version} == 1310 || 0%{?suse_version} == 1320
EXTRA_INCLUDES="/usr/include/ruby-%{rb20_ver}:/usr/include/ruby-%{rb20_ver}/%{_target}"
%endif
%if 0%{?suse_version} >= 1330
EXTRA_INCLUDES="/usr/include/ruby-%{rb_ver}:/usr/include/ruby-%{rb_ver}/%{_target}-gnu"
%endif

# Force python version
export PYTHON=%{__python}

# Warning: GCC visibility causes FTBFS [Bug #1285]
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --docdir=%{tde_docdir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --with-extra-includes=%{_includedir}/tqt:${EXTRA_INCLUDES} \
  --with-extra-libs=%{tde_libdir} \
%if 0%{with_python}
  --with-pythondir=%{_usr} \
%endif
  \
  %{?with_java:--with-java=%{java_home}} %{!?with_java:--without-java} \
  %{?with_qscintilla:--enable-qscintilla} %{!?with_qscintilla:--disable-qscintilla}

# Ensure python was detected properly
if grep "LIBPYTHON=''" "config.log"; then
  exit 1
fi

# Build dcopperl with specific options
pushd dcopperl
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor INSTALLVENDORMAN3DIR=%{tde_mandir}/man3
%__make OPTIMIZE="$RPM_OPT_FLAGS" ||:
popd

# smoke (not smp-safe)
%__make -C smoke

# The rest is smp-safe
%__make %{?_smp_mflags} PYTHON=%{__python}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT

%__make install DESTDIR=%{?buildroot} \
  PYTHON=%{__python}

# Removes some perl files
find $RPM_BUILD_ROOT -type f -a \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'

%if 0%{?with_java}
# Installs juic
%__install -D -m 755 qtjava/designer/juic/bin/juic	%{?buildroot}%{tde_bindir}/juic
%__install -d -m 755 %{?buildroot}%{tde_datadir}/juic/common
%__install -m 644 qtjava/designer/juic/common/*.xml %{?buildroot}%{tde_datadir}/juic/common
%__install -m 644 qtjava/designer/juic/common/*.xsl %{?buildroot}%{tde_datadir}/juic/common
%__install -d -m 755 %{?buildroot}%{tde_datadir}/juic/java
%__install -m 644 qtjava/designer/juic/java/*.xml %{?buildroot}%{tde_datadir}/juic/java
%__install -m 644 qtjava/designer/juic/java/*.xsl %{?buildroot}%{tde_datadir}/juic/java
%__install -m 644 qtjava/designer/juic/juic.xsl  %{?buildroot}%{tde_datadir}/juic
%endif

# kjsembed sample files
%__install -d -m 755 %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install -m 644 kjsembed/plugins/customobject_plugin.cpp %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install -m 644 kjsembed/plugins/customobject_plugin.h %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install -m 644 kjsembed/plugins/customobject_plugin.desktop %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install -m 644 kjsembed/plugins/customqobject_plugin.cpp %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install -m 644 kjsembed/plugins/customqobject_plugin.h %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install -m 644 kjsembed/plugins/customqobject_plugin.desktop %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/

# Move 'embedjs.desktop' to correct location
%__mv -f "%{?buildroot}%{tde_datadir}/applnk/Utilities/embedjs.desktop" "%{?buildroot}%{tde_tdeappdir}/embedjs.desktop"
%__rm -rf "%{?buildroot}%{tde_datadir}/applnk"

# Move dcoppython to %python_sitearch
if [ ! -d "%{?buildroot}%{python_sitearch}" ] && [ -d "%{?buildroot}%{python_sitelib}" ]; then
  %__mkdir_p "%{?buildroot}%{python_sitearch}"
  %__mv -f "%{?buildroot}%{python_sitelib}/"{pcop.la,pcop.so,pydcop.py} "%{?buildroot}%{python_sitearch}"
  rmdir "%{?buildroot}%{python_sitelib}"
fi

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -u kjscmd  Development 
%suse_update_desktop_file -u embedjs Development 
%endif


%clean
%__rm -rf $RPM_BUILD_ROOT


%changelog
