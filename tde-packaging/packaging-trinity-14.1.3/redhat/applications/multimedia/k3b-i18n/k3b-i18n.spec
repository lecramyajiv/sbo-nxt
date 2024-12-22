#
# spec file for package k3b-i18n (version R14)
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
%define tde_pkg k3b-i18n
%define tde_prefix /opt/trinity
%define tde_appdir %{tde_datadir}/applications
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
Epoch:			%{tde_epoch}
Version:		1.0.5
Release:		%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Internationalization support for TDE [Trinity]
Group:			Applications/Archiving
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

Requires(post): coreutils
Requires(postun): coreutils

Requires:		trinity-k3b


%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.

##########

%package Danish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Danish (da) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-da < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-da = %{?epoch:%{epoch}:}%{version}-%{release}

%description Danish
This package contains the Danish translations for K3B.

%files Danish
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/da/k3b
%{tde_datadir}/locale/da/LC_MESSAGES/*.mo

##########

%package German
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		German (de) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-de < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-de = %{?epoch:%{epoch}:}%{version}-%{release}

%description German
This package contains the German translations for K3B.

%files German
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/de/k3b
%{tde_datadir}/locale/de/LC_MESSAGES/*.mo

##########

%package Greek
Group:			Applications/Archiving
Requires:		trinity-k3b >= %{version}
Summary:		Greek (el) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-el < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-el = %{?epoch:%{epoch}:}%{version}-%{release}

%description Greek
This package contains the greek translations for K3B.

%files Greek
%defattr(-,root,root,-)
#%{tde_tdedocdir}/HTML/el/k3b
%{tde_datadir}/locale/el/LC_MESSAGES/*.mo

##########

%package Spanish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Spanish (es) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-es < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-es = %{?epoch:%{epoch}:}%{version}-%{release}

%description Spanish
This package contains the Spanish translations for K3B.

%files Spanish
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/es/k3b
%{tde_datadir}/locale/es/LC_MESSAGES/*.mo

##########

%package Estonian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Estonian (et) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-et < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-et = %{?epoch:%{epoch}:}%{version}-%{release}

%description Estonian
This package contains the Estonian translations for K3B.

%files Estonian
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/et/k3b
%{tde_datadir}/locale/et/LC_MESSAGES/*.mo

##########

%package French
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		French (fr) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-fr < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-fr = %{?epoch:%{epoch}:}%{version}-%{release}

%description French
This package contains the French translations for K3B.

%files French
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/fr/k3b
%{tde_datadir}/locale/fr/LC_MESSAGES/*.mo

##########

%package Italian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Italian (it) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-it < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-it = %{?epoch:%{epoch}:}%{version}-%{release}

%description Italian
This package contains the Italian translations for K3B.

%files Italian
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/it/k3b
%{tde_datadir}/locale/it/LC_MESSAGES/*.mo

##########

%package Dutch
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Dutch (nl) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-nl < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-nl = %{?epoch:%{epoch}:}%{version}-%{release}

%description Dutch
This package contains the Dutch translations for K3B.

%files Dutch
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/nl/k3b
%{tde_datadir}/locale/nl/LC_MESSAGES/*.mo

##########

%package Polish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Polish (pl) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-pl < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-pl = %{?epoch:%{epoch}:}%{version}-%{release}

%description Polish
This package contains the Polish translations for K3B.

%files Polish
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/pl/k3b
%{tde_datadir}/locale/pl/LC_MESSAGES/*.mo

##########

%package Portuguese
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Portuguese (pt) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-pt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-pt = %{?epoch:%{epoch}:}%{version}-%{release}

%description Portuguese
This package contains the Portuguese translations for K3B.

%files Portuguese
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/pt/k3b
%{tde_datadir}/locale/pt/LC_MESSAGES/*.mo

##########

%package Brazil
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Brazilian Portuguese (pt_BR) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-pt_BR < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-pt_BR = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-k3b-i18n-ptbr < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-ptbr = %{?epoch:%{epoch}:}%{version}-%{release}

%description Brazil
This package contains the Brazilian Portuguese translations for K3B.

%files Brazil
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/pt_BR/k3b
%{tde_datadir}/locale/pt_BR/LC_MESSAGES/*.mo

##########

%package Russian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Russian (ru) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-ru < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-ru = %{?epoch:%{epoch}:}%{version}-%{release}

%description Russian
This package contains the Russian translations for K3B.

%files Russian
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/ru/k3b
%{tde_datadir}/locale/ru/LC_MESSAGES/*.mo

##########

%package Swedish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Swedish (sv) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-sv < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-sv = %{?epoch:%{epoch}:}%{version}-%{release}

%description Swedish
This package contains the Swedish translations for K3B.

%files Swedish
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/sv/k3b
%{tde_datadir}/locale/sv/LC_MESSAGES/*.mo

##########

%package Ukrainian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Ukrainian (uk) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-uk < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-uk = %{?epoch:%{epoch}:}%{version}-%{release}

%description Ukrainian
This package contains the Ukrainian translations for K3B.

%files Ukrainian
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/uk/k3b
%{tde_datadir}/locale/uk/LC_MESSAGES/*.mo

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
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DCMAKE_PROGRAM_PATH="%{tde_bindir}" \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%__rm -rf %{buildroot}%{tde_datadir}/locale/af
%__rm -rf %{buildroot}%{tde_datadir}/locale/ar
%__rm -rf %{buildroot}%{tde_datadir}/locale/bg
%__rm -rf %{buildroot}%{tde_datadir}/locale/br
%__rm -rf %{buildroot}%{tde_datadir}/locale/bs
%__rm -rf %{buildroot}%{tde_datadir}/locale/ca
%__rm -rf %{buildroot}%{tde_datadir}/locale/cs
%__rm -rf %{buildroot}%{tde_datadir}/locale/cy
%__rm -rf %{buildroot}%{tde_datadir}/locale/en_GB
%__rm -rf %{buildroot}%{tde_datadir}/locale/eu
%__rm -rf %{buildroot}%{tde_datadir}/locale/fa
%__rm -rf %{buildroot}%{tde_datadir}/locale/fi
%__rm -rf %{buildroot}%{tde_datadir}/locale/ga
%__rm -rf %{buildroot}%{tde_datadir}/locale/gl
%__rm -rf %{buildroot}%{tde_datadir}/locale/he
%__rm -rf %{buildroot}%{tde_datadir}/locale/hi
%__rm -rf %{buildroot}%{tde_datadir}/locale/hu
%__rm -rf %{buildroot}%{tde_datadir}/locale/is
%__rm -rf %{buildroot}%{tde_datadir}/locale/ja
%__rm -rf %{buildroot}%{tde_datadir}/locale/ka
%__rm -rf %{buildroot}%{tde_datadir}/locale/km
%__rm -rf %{buildroot}%{tde_datadir}/locale/lt
%__rm -rf %{buildroot}%{tde_datadir}/locale/mk
%__rm -rf %{buildroot}%{tde_datadir}/locale/ms
%__rm -rf %{buildroot}%{tde_datadir}/locale/nb
%__rm -rf %{buildroot}%{tde_datadir}/locale/nds
%__rm -rf %{buildroot}%{tde_datadir}/locale/ne
%__rm -rf %{buildroot}%{tde_datadir}/locale/nn
%__rm -rf %{buildroot}%{tde_datadir}/locale/pa
%__rm -rf %{buildroot}%{tde_datadir}/locale/rw
%__rm -rf %{buildroot}%{tde_datadir}/locale/se
%__rm -rf %{buildroot}%{tde_datadir}/locale/sk
%__rm -rf %{buildroot}%{tde_datadir}/locale/sr
%__rm -rf %{buildroot}%{tde_datadir}/locale/sr@Latn
%__rm -rf %{buildroot}%{tde_datadir}/locale/ta
%__rm -rf %{buildroot}%{tde_datadir}/locale/tr
%__rm -rf %{buildroot}%{tde_datadir}/locale/uz
%__rm -rf %{buildroot}%{tde_datadir}/locale/uz@cyrillic
%__rm -rf %{buildroot}%{tde_datadir}/locale/zh_CN
%__rm -rf %{buildroot}%{tde_datadir}/locale/zh_TW


%clean
%__rm -rf %{buildroot}


%changelog
