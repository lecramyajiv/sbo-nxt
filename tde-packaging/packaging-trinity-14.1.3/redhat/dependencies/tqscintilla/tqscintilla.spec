#
# spec file for package tqscintilla (version R14)
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
%define tde_pkg tqscintilla

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libtqscintilla %{_lib}tqscintilla
%else
%define libtqscintilla libtqscintilla
%endif


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.7.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TQt source code editing component based on Scintilla
Group:		Development/Libraries/C and C++
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		trinity-tqscintilla-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-filesystem >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	gettext

%description
Scintilla is a free source code editing component. It has features found
in standard editing components, as well as features especially useful
when editing and debugging source code.

TQScintilla is a port or Scintilla to the TQt GUI toolkit.

##########

%package -n %{libtqscintilla}7
Summary:	TQt source code editing component based on Scintilla
Group:		Development/Libraries/C and C++
Provides:	libtqscintilla = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libtqt3-mt >= 3.5.0

%description -n %{libtqscintilla}7
Scintilla is a free source code editing component. It has features found
in standard editing components, as well as features especially useful
when editing and debugging source code.

TQScintilla is a port or Scintilla to the TQt GUI toolkit.

%post -n %{libtqscintilla}7
/sbin/ldconfig

%postun -n %{libtqscintilla}7
/sbin/ldconfig

%files -n %{libtqscintilla}7
%defattr(-,root,root,-)
%doc ChangeLog LICENSE NEWS README
%{_libdir}/libtqscintilla.so.7
%{_libdir}/libtqscintilla.so.7.0.1
%{_libdir}/tqt3/plugins/designer/*.so
%dir %{_datadir}/tqt3/translations/
%{_datadir}/tqt3/translations/*.qm

##########

%package -n %{libtqscintilla}-devel
Summary:	TQScintilla Development Files
Group:		Development/Libraries/C and C++
Provides:	libtqscintilla-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{libtqscintilla}7 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libtqt3-mt-devel >= 3.5.0

%description -n %{libtqscintilla}-devel
This package contains the development files for tqscintilla.

%post -n %{libtqscintilla}-devel
/sbin/ldconfig

%postun -n %{libtqscintilla}-devel
/sbin/ldconfig

%files -n %{libtqscintilla}-devel
%defattr(-,root,root,-)
#%{_includedir}/tqscintilla/
%{_includedir}/tqt3/tqextscintilla.h
%{_includedir}/tqt3/tqextscintillaapis.h
%{_includedir}/tqt3/tqextscintillabase.h
%{_includedir}/tqt3/tqextscintillacommand.h
%{_includedir}/tqt3/tqextscintillacommandset.h
%{_includedir}/tqt3/tqextscintilladocument.h
%{_includedir}/tqt3/tqextscintillaglobal.h
%{_includedir}/tqt3/tqextscintillalexer.h
%{_includedir}/tqt3/tqextscintillalexerbash.h
%{_includedir}/tqt3/tqextscintillalexerbatch.h
%{_includedir}/tqt3/tqextscintillalexercpp.h
%{_includedir}/tqt3/tqextscintillalexercsharp.h
%{_includedir}/tqt3/tqextscintillalexercss.h
%{_includedir}/tqt3/tqextscintillalexerdiff.h
%{_includedir}/tqt3/tqextscintillalexerhtml.h
%{_includedir}/tqt3/tqextscintillalexeridl.h
%{_includedir}/tqt3/tqextscintillalexerjava.h
%{_includedir}/tqt3/tqextscintillalexerjavascript.h
%{_includedir}/tqt3/tqextscintillalexerlua.h
%{_includedir}/tqt3/tqextscintillalexermakefile.h
%{_includedir}/tqt3/tqextscintillalexerperl.h
%{_includedir}/tqt3/tqextscintillalexerpov.h
%{_includedir}/tqt3/tqextscintillalexerproperties.h
%{_includedir}/tqt3/tqextscintillalexerpython.h
%{_includedir}/tqt3/tqextscintillalexerruby.h
%{_includedir}/tqt3/tqextscintillalexersql.h
%{_includedir}/tqt3/tqextscintillalexertex.h
%{_includedir}/tqt3/tqextscintillamacro.h
%{_includedir}/tqt3/tqextscintillaprinter.h
%{_libdir}/libtqscintilla.so
%{_libdir}/pkgconfig/tqscintilla.pc
%exclude %{_libdir}/libtqscintilla.la
%exclude %{_libdir}/tqt3/plugins/designer/*.la

##########

%package -n %{libtqscintilla}-doc
Summary:	TQScintilla Documentation
Group:		Development/Libraries/C and C++
Provides:	libtqscintilla-doc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{libtqscintilla}7 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-filesystem >= %{tde_version}

%description -n %{libtqscintilla}-doc
This package contains the documentation for tqscintilla.

%files -n %{libtqscintilla}-doc
%defattr(-,root,root,-)
%{_docdir}/libtqscintilla/

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DLIB_INSTALL_DIR="%{_libdir}" \
  \
  -DBUILD_ALL="ON" \
  -DWITH_ALL_OPTIONS="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install -C build DESTDIR=%{?buildroot}

%if "%{?_docdir}" != "%{_datadir}/doc"
%__mkdir_p "%{?buildroot}%{_docdir}"
%__mv "%{?buildroot}%{_datadir}/doc/libtqscintilla/" "%{?buildroot}%{_docdir}/libtqscintilla/"
%endif


%clean
%__rm -rf $RPM_BUILD_ROOT


%changelog
