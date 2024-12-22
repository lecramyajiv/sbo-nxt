#
# spec file for package libtqt-perl (version R14)
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
%define tde_pkg libtqt-perl
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeincludedir %{tde_includedir}/tde


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	3.008
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Perl bindings for the TQt library
Group:		Development/Libraries/Perl
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	automake autoconf libtool
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig

BuildRequires:	trinity-libsmoketqt-devel >= %{tde_version}

BuildRequires:	perl(ExtUtils::MakeMaker)

Requires:		perl-TQt = %{?epoch:%{epoch}:}%{version}-%{release}


%description
This module lets you use the TQt library from Perl.
It provides an object-oriented interface and is easy to use.

%files
%defattr(-,root,root,-)
%{tde_bindir}/puic
%{tde_mandir}/man1/puic.1*
%{_bindir}/pqtapi
%{_bindir}/pqtsh
%if 0%{?rhel} == 5
%{_datadir}/doc/libqt-perl/
%endif

##########

%package -n perl-TQt
Summary:	Perl bindings for the TQt library
Group:		Development/Libraries/Perl

Provides:		perl(TQtShell)
Provides:		perl(TQtShellControl)

%description -n perl-TQt
This module lets you use the TQt library from Perl.
It provides an object-oriented interface and is easy to use.

%files -n perl-TQt
%defattr(-,root,root,-)
%{perl_vendorarch}/TQt.pm
%{perl_vendorarch}/TQt.pod
%dir %{perl_vendorarch}/TQt
%{perl_vendorarch}/TQt/GlobalSpace.pm
%{perl_vendorarch}/TQt/attributes.pm
%{perl_vendorarch}/TQt/constants.pm
%{perl_vendorarch}/TQt/debug.pm
%{perl_vendorarch}/TQt/enumerations.pm
%{perl_vendorarch}/TQt/isa.pm
%{perl_vendorarch}/TQt/properties.pm
%{perl_vendorarch}/TQt/signals.pm
%{perl_vendorarch}/TQt/slots.pm
%{perl_vendorarch}/auto/TQt/
%{_mandir}/man3/TQt.3pm.*

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export TDEDIR=%{tde_prefix}
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --disable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --disable-smoke

# Fix invalid path in RHEL 5
%if 0%{?rhel} == 5
%__sed -i "PerlTQt/Makefile" -e "s|\$(PREFIX)/|\$(DESTDIR)\$(PREFIX)/|"
%endif

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Unwanted files
%__rm -f %{buildroot}%{perl_archlib}/perllocal.pod
%__rm -f %{buildroot}%{perl_vendorarch}/auto/TQt/.packlist


%clean
%__rm -rf %{buildroot}


%changelog
