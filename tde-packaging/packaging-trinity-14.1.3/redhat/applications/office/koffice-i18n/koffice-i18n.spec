#
# spec file for package koffice-i18n (version R14)
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
%define tde_pkg koffice-i18n
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


# Builds all supported languages (not unsupported ones)
%if "%{?TDE_LANGS}" == ""
%define TDE_LANGS bg ca cs da de el en_GB es et fi fr hu it ja km lv ms nb nds ne nl pl pt pt_BR ru sk sl sr sv tr uk zh_CN zh_TW
%endif


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.6.3
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Internationalization support for Koffice [Trinity]
Group:		User Interface/Desktops
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
BuildArch:	noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	findutils
BuildRequires:	gettext

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif


%description
%{summary}.

%package Bulgarian
Summary:		Bulgarian(bg) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-bg = %{?epoch:%{epoch}:}%{version}-%{release}
%description Bulgarian
%{summary}.

%package Bengali
Summary:		Bengali(bn) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-bn = %{?epoch:%{epoch}:}%{version}-%{release}
%description Bengali
%{summary}.

%package Tibetan
Summary:		Tibetan(bo) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-bo = %{?epoch:%{epoch}:}%{version}-%{release}
%description Tibetan
%{summary}.

%package Breton
Summary:		Breton(br) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-br = %{?epoch:%{epoch}:}%{version}-%{release}
%description Breton
%{summary}.

%package Bosnian
Summary:		Bosnian(bs) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-bs = %{?epoch:%{epoch}:}%{version}-%{release}
%description Bosnian
%{summary}.

%package Catalan
Summary:		Catalan(ca) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ca = %{?epoch:%{epoch}:}%{version}-%{release}
%description Catalan
%{summary}.

%package Czech
Summary:		Czech(cs) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-cs = %{?epoch:%{epoch}:}%{version}-%{release}
%description Czech
%{summary}.

%package Cymraeg
Summary:		Cymraeg language support for Koffice [Trinity]
Group:			User Interface/Desktops
%description Cymraeg
%{summary}.

%package Welsh
Summary:		Welsh(cy) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-cy = %{?epoch:%{epoch}:}%{version}-%{release}
%description Welsh
%{summary}.

%package Danish
Summary:		Danish(da) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-da = %{?epoch:%{epoch}:}%{version}-%{release}
%description Danish
%{summary}.

%package German
Summary:		German(de) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-de = %{?epoch:%{epoch}:}%{version}-%{release}
%description German
%{summary}.

%package Greek
Summary:		Greek(el) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-el = %{?epoch:%{epoch}:}%{version}-%{release}
%description Greek
%{summary}.

%package British
Summary:		British(en_GB) English support for TDE
Group:			User Interface/Desktops
Provides: %{name}-en_GB = %{?epoch:%{epoch}:}%{version}-%{release}
%description British
%{summary}.

%package Esperanto
Summary:		Esperanto(eo) support for TDE
Group:			User Interface/Desktops
Provides: %{name}-eo = %{?epoch:%{epoch}:}%{version}-%{release}
%description Esperanto
%{summary}.

%package Spanish
Summary:		Spanish(es) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-es = %{?epoch:%{epoch}:}%{version}-%{release}
%description Spanish
%{summary}.

%package Estonian
Summary:		Estonian(et) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-et = %{?epoch:%{epoch}:}%{version}-%{release}
%description Estonian
%{summary}.

%package Basque
Summary:		Basque(eu) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-eu = %{?epoch:%{epoch}:}%{version}-%{release}
%description Basque
%{summary}.

%package Finnish
Summary:		Finnish(fi) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-fi = %{?epoch:%{epoch}:}%{version}-%{release}
%description Finnish
%{summary}.

%package Faroese
Summary:		Faroese(fo) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-fo = %{?epoch:%{epoch}:}%{version}-%{release}
%description Faroese
%{summary}.

%package French
Summary:		French(fr) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-fr = %{?epoch:%{epoch}:}%{version}-%{release}
%description French
%{summary}.

%package Frisian
Summary:		Frisian(fy) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-fy = %{?epoch:%{epoch}:}%{version}-%{release}
%description Frisian
%{summary}.

%package Irish
Summary:		Irish(ga) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Obsoletes: kde-i18n-Gaeilge < %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}-ga = %{?epoch:%{epoch}:}%{version}-%{release}
%description Irish
%{summary}.

%package Galician
Summary:		Galician(gl) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-gl = %{?epoch:%{epoch}:}%{version}-%{release}
%description Galician
%{summary}.

%package Hebrew
Summary:		Hebrew(he) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-he = %{?epoch:%{epoch}:}%{version}-%{release}
%description Hebrew
%{summary}.

%package Hindi
Summary:		Hindi(hi) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-hi = %{?epoch:%{epoch}:}%{version}-%{release}
%description Hindi
%{summary}.

%package Croatian
Summary:		Croatian(hr) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-hr = %{?epoch:%{epoch}:}%{version}-%{release}
%description Croatian
%{summary}.

%package Hungarian
Summary:		Hungarian(hu) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-hu = %{?epoch:%{epoch}:}%{version}-%{release}
%description Hungarian
%{summary}.

%package Indonesian
Summary:		Indonesian(id) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-id = %{?epoch:%{epoch}:}%{version}-%{release}
%description Indonesian
%{summary}.

%package Icelandic
Summary:		Icelandic(is) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-is = %{?epoch:%{epoch}:}%{version}-%{release}
%description Icelandic
%{summary}.

%package Italian
Summary:		Italian(it) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-it = %{?epoch:%{epoch}:}%{version}-%{release}
%description Italian
%{summary}.

%package Japanese
Summary:		Japanese(ja) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ja = %{?epoch:%{epoch}:}%{version}-%{release}
%description Japanese
%{summary}.

%package Khmer
Summary:		Khmer(km) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-km = %{?epoch:%{epoch}:}%{version}-%{release}
%description Khmer
%{summary}.

%package Korean
Summary:		Korean(ko) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ko = %{?epoch:%{epoch}:}%{version}-%{release}
%description Korean
%{summary}.

%package Kurdish
Summary:		Kurdish(ku) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ku = %{?epoch:%{epoch}:}%{version}-%{release}
%description Kurdish
%{summary}.

%package Lao
Summary:		Lao(lo) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-lo = %{?epoch:%{epoch}:}%{version}-%{release}
%description Lao
%{summary}.

%package Lithuanian
Summary:		Lithuanian(lt) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-lt = %{?epoch:%{epoch}:}%{version}-%{release}
%description Lithuanian
%{summary}.

%package Latvian
Summary:		Latvian(lv) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-lv = %{?epoch:%{epoch}:}%{version}-%{release}
%description Latvian
%{summary}.

%package Maori
Summary:		Maori(mi) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-mi = %{?epoch:%{epoch}:}%{version}-%{release}
%description Maori
%{summary}.

%package Macedonian
Summary:		Macedonian(mk) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-mk = %{?epoch:%{epoch}:}%{version}-%{release}
%description Macedonian
%{summary}.

%package Malay
Summary:		Malay(ms) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ms = %{?epoch:%{epoch}:}%{version}-%{release}
%description Malay
%{summary}.

%package Maltese
Summary:		Maltese(mt) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-mt = %{?epoch:%{epoch}:}%{version}-%{release}
%description Maltese
%{summary}.

%package LowSaxon
Summary:		Low Saxon (nds) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-nds = %{?epoch:%{epoch}:}%{version}-%{release}
%description LowSaxon
%{summary}.

%package Nepali
Summary:		Nepali(ne) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ne = %{?epoch:%{epoch}:}%{version}-%{release}
%description Nepali
%{summary}.

%package Dutch
Summary:		Dutch(nl) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-nl = %{?epoch:%{epoch}:}%{version}-%{release}
%description Dutch
%{summary}.

%package Norwegian
Summary:		Norwegian(no) (Bokmaal) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-no = %{?epoch:%{epoch}:}%{version}-%{release}
%description Norwegian
%{summary}.

%package Norwegian-Nynorsk
Summary:		Norwegian(nn) (Nynorsk) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-nn = %{?epoch:%{epoch}:}%{version}-%{release}
%description Norwegian-Nynorsk
%{summary}.

%package Occitan
Summary:		Occitan(oc) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-oc = %{?epoch:%{epoch}:}%{version}-%{release}
%description Occitan
%{summary}.

%package Polish
Summary:		Polish(pl) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-pl = %{?epoch:%{epoch}:}%{version}-%{release}
%description Polish
%{summary}.

%package Portuguese
Summary:		Portuguese(pt) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-pt = %{?epoch:%{epoch}:}%{version}-%{release}
%description Portuguese
%{summary}.

%package Punjabi
Summary:		Punjabi(pa) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-pa = %{?epoch:%{epoch}:}%{version}-%{release}
%description Punjabi
%{summary}.

%package Brazil
Summary:		Brazil(pt_BR) Portuguese language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-pt_BR = %{?epoch:%{epoch}:}%{version}-%{release}
%description Brazil
%{summary}.

%package Romanian
Summary:		Romanian(ro) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ro = %{?epoch:%{epoch}:}%{version}-%{release}
%description Romanian
%{summary}.

%package Russian
Summary:		Russian(ru) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ru = %{?epoch:%{epoch}:}%{version}-%{release}
%description Russian
%{summary}.

%package Slovak
Summary:		Slovak(sk) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-sk = %{?epoch:%{epoch}:}%{version}-%{release}
%description Slovak
%{summary}.

%package Slovenian
Summary:		Slovenian(sl) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-sl = %{?epoch:%{epoch}:}%{version}-%{release}
%description Slovenian
%{summary}.

%package Serbian
Summary:		Serbian(sr) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-sr = %{?epoch:%{epoch}:}%{version}-%{release}
%description Serbian
%{summary}.

%package Swedish
Summary:		Swedish(sv) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-sv = %{?epoch:%{epoch}:}%{version}-%{release}
%description Swedish
%{summary}.

%package Tamil
Summary:		Tamil(ta) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ta = %{?epoch:%{epoch}:}%{version}-%{release}
%description Tamil
%{summary}.

%package Tajik
Summary:		Tajik(tg) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-tg = %{?epoch:%{epoch}:}%{version}-%{release}
%description Tajik
%{summary}.

%package Thai
Summary:		Thai(th) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-th = %{?epoch:%{epoch}:}%{version}-%{release}
%description Thai
%{summary}.

%package Turkish
Summary:		Turkish(tr) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-tr = %{?epoch:%{epoch}:}%{version}-%{release}
%description Turkish
%{summary}.

%package Ukrainian
Summary:		Ukrainian(uk) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-uk = %{?epoch:%{epoch}:}%{version}-%{release}
%description Ukrainian
%{summary}.

%package Venda
Summary:		Venda(ven) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-ven = %{?epoch:%{epoch}:}%{version}-%{release}
%description Venda
%{summary}.

%package Vietnamese
Summary:		Vietnamese(vi) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-vi = %{?epoch:%{epoch}:}%{version}-%{release}
%description Vietnamese
%{summary}.

%package Walloon
Summary:		Walloon(wa) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-wa = %{?epoch:%{epoch}:}%{version}-%{release}
%description Walloon
%{summary}.

%package Xhosa
Summary:		Xhosa(xh) (a Bantu language) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-xh = %{?epoch:%{epoch}:}%{version}-%{release}
%description Xhosa
%{summary}.

%package Chinese
Summary:		Chinese(zh_CN) (Simplified Chinese) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-zh_CN = %{?epoch:%{epoch}:}%{version}-%{release}
%description Chinese
%{summary}.

%package Chinese-Big5
Summary:		Chinese(zh_TW) (Big5) language support for Koffice [Trinity]
Group:			User Interface/Desktops
Provides: %{name}-tz_TW = %{?epoch:%{epoch}:}%{version}-%{release}
%description Chinese-Big5
%{summary}.



%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

(
for l in . %{TDE_LANGS}; do
  if [ $l != '.' ]; then
    pushd "%{tde_pkg}-${l}"
  else
    pushd ${l}
  fi

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
    -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
    -DDATA_INSTALL_DIR=%{tde_datadir}/apps \
    -DLIB_INSTALL_DIR=%{tde_libdir} \
    -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
    \
    -DBUILD_ALL=ON \
    \
    ..

  %__make %{?_smp_mflags}

  popd
done
) 2>&1 | tee /tmp/rpmbuild.$$

if grep -qw TDE_Error /tmp/rpmbuild.$$; then
  echo "Error while building. See '/tmp/rpmbuild.$$'"
  exit 1
fi

wait
rm -f /tmp/rpmbuild.$$

%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}

for l in %{TDE_LANGS}; do
  %__make DESTDIR=%{buildroot} -C build install-${l}
done


%clean
%__rm -rf %{buildroot}

%if "%( grep -w af <<< '%{TDE_LANGS}' )" != ""
%files Afrikaans
%defattr(-,root,root,-)
%{tde_datadir}/locale/af/*
%endif

%if "%( grep -w ar <<< '%{TDE_LANGS}' )" != ""
%files Arabic 
%defattr(-,root,root,-)
%{tde_datadir}/locale/ar/*
%endif

%if "%( grep -w az <<< '%{TDE_LANGS}' )" != ""
%files Azerbaijani
%defattr(-,root,root,-)
%{tde_datadir}/locale/az/*
%endif

%if "%( grep -w be <<< '%{TDE_LANGS}' )" != ""
%files Belarusian
%defattr(-,root,root,-)
%{tde_datadir}/locale/be/*
%endif

%if "%( grep -w bg <<< '%{TDE_LANGS}' )" != ""
%files Bulgarian
%defattr(-,root,root,-)
%{tde_datadir}/locale/bg/*
%endif

%if "%( grep -w bn <<< '%{TDE_LANGS}' )" != ""
%files Bengali
%defattr(-,root,root,-)
%{tde_datadir}/locale/bn/*
%endif

%if "%( grep -w bo <<< '%{TDE_LANGS}' )" != ""
%files Tibetan
%defattr(-,root,root,-)
%{tde_datadir}/locale/bo/*
%endif

%if "%( grep -w br <<< '%{TDE_LANGS}' )" != ""
%files Breton
%defattr(-,root,root,-)
%{tde_datadir}/locale/br/*
%endif

%if "%( grep -w bs <<< '%{TDE_LANGS}' )" != ""
%files Bosnian
%defattr(-,root,root,-)
%{tde_datadir}/locale/bs/*
%endif

%if "%( grep -w ca <<< '%{TDE_LANGS}' )" != ""
%files Catalan
%defattr(-,root,root,-)
%{tde_datadir}/locale/ca/*
%{tde_tdedocdir}/HTML/ca/
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/ca.xml
%endif

%if "%( grep -w cs <<< '%{TDE_LANGS}' )" != ""
%files Czech
%defattr(-,root,root,-)
%{tde_datadir}/locale/cs/*
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/cs.xml
%endif

%if "%( grep -w cy <<< '%{TDE_LANGS}' )" != ""
%files Welsh
%defattr(-,root,root,-)
%{tde_datadir}/locale/cy/*
%endif

%if "%( grep -w da <<< '%{TDE_LANGS}' )" != ""
%files Danish
%defattr(-,root,root,-)
%{tde_datadir}/locale/da/*
%{tde_tdedocdir}/HTML/da/
%endif

%if "%( grep -w de <<< '%{TDE_LANGS}' )" != ""
%files German
%defattr(-,root,root,-)
%{tde_datadir}/locale/de/*
%{tde_tdedocdir}/HTML/de/
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/de.xml
%endif

%if "%( grep -w el <<< '%{TDE_LANGS}' )" != ""
%files Greek
%defattr(-,root,root,-)
%{tde_datadir}/locale/el/*
%endif

%if "%( grep -w en_GB <<< '%{TDE_LANGS}' )" != ""
%files British
%defattr(-,root,root,-)
%{tde_datadir}/locale/en_GB/*
%{tde_tdedocdir}/HTML/en_GB/
%endif

%if "%( grep -w eo <<< '%{TDE_LANGS}' )" != ""
%files Esperanto
%defattr(-,root,root,-)
%{tde_datadir}/locale/eo/*
%endif

%if "%( grep -w es <<< '%{TDE_LANGS}' )" != ""
%files Spanish
%defattr(-,root,root,-)
%{tde_datadir}/locale/es/*
%{tde_tdedocdir}/HTML/es/
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/es.xml
%endif

%if "%( grep -w et <<< '%{TDE_LANGS}' )" != ""
%files Estonian
%defattr(-,root,root,-)
%{tde_datadir}/locale/et/*
%{tde_tdedocdir}/HTML/et/
%endif

%if "%( grep -w eu <<< '%{TDE_LANGS}' )" != ""
%files Basque
%defattr(-,root,root,-)
%{tde_datadir}/locale/eu/*
%endif

%if "%( grep -w fa <<< '%{TDE_LANGS}' )" != ""
%files Farsi
%defattr(-,root,root,-)
%{tde_datadir}/locale/fa/*
%endif

%if "%( grep -w fi <<< '%{TDE_LANGS}' )" != ""
%files Finnish
%defattr(-,root,root,-)
%{tde_datadir}/locale/fi/*
%endif

%if "%( grep -w fo <<< '%{TDE_LANGS}' )" != ""
%files Faroese
%defattr(-,root,root,-)
%{tde_datadir}/locale/fo/*
%endif

%if "%( grep -w fr <<< '%{TDE_LANGS}' )" != ""
%files French
%defattr(-,root,root,-)
%{tde_datadir}/locale/fr/*
%{tde_tdedocdir}/HTML/fr/
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/fr.xml
%endif

%if "%( grep -w fy <<< '%{TDE_LANGS}' )" != ""
%files Frisian
%defattr(-,root,root,-)
%{tde_datadir}/locale/fy/*
%endif

%if "%( grep -w ga <<< '%{TDE_LANGS}' )" != ""
%files Irish
%defattr(-,root,root,-)
%{tde_datadir}/locale/ga/*
%endif

%if "%( grep -w gl <<< '%{TDE_LANGS}' )" != ""
%files Galician
%defattr(-,root,root,-)
%{tde_datadir}/locale/gl/*
%endif

%if "%( grep -w he <<< '%{TDE_LANGS}' )" != ""
%files Hebrew
%defattr(-,root,root,-)
%{tde_datadir}/locale/he/*
%endif

%if "%( grep -w hi <<< '%{TDE_LANGS}' )" != ""
%files Hindi
%defattr(-,root,root,-)
%{tde_datadir}/locale/hi/*
%endif

%if "%( grep -w hr <<< '%{TDE_LANGS}' )" != ""
%files Croatian
%defattr(-,root,root,-)
%{tde_datadir}/locale/hr/*
%endif

%if "%( grep -w hu <<< '%{TDE_LANGS}' )" != ""
%files Hungarian
%defattr(-,root,root,-)
%{tde_datadir}/locale/hu/*
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/hu.xml
%endif

%if "%( grep -w id <<< '%{TDE_LANGS}' )" != ""
%files Indonesian
%defattr(-,root,root,-)
%{tde_datadir}/locale/id/*
%endif

%if "%( grep -w is <<< '%{TDE_LANGS}' )" != ""
%files Icelandic
%defattr(-,root,root,-)
%{tde_datadir}/locale/is/*
%endif

%if "%( grep -w it <<< '%{TDE_LANGS}' )" != ""
%files Italian
%defattr(-,root,root,-)
%{tde_datadir}/locale/it/*
%{tde_tdedocdir}/HTML/it/
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/it.xml
%endif

%if "%( grep -w ja <<< '%{TDE_LANGS}' )" != ""
%files Japanese
%defattr(-,root,root,-)
%{tde_datadir}/locale/ja/*
%endif

%if "%( grep -w km <<< '%{TDE_LANGS}' )" != ""
%files Khmer
%defattr(-,root,root,-)
%{tde_datadir}/locale/km/*
%endif

%if "%( grep -w ko <<< '%{TDE_LANGS}' )" != ""
%files Korean
%defattr(-,root,root,-)
%{tde_datadir}/locale/ko/*
%endif

%if "%( grep -w ku <<< '%{TDE_LANGS}' )" != ""
%files Kurdish
%defattr(-,root,root,-)
%{tde_datadir}/locale/ku/*
%endif

%if "%( grep -w lao <<< '%{TDE_LANGS}' )" != ""
%files Lao
%defattr(-,root,root,-)
%{tde_datadir}/locale/lo/*
%endif

%if "%( grep -w lt <<< '%{TDE_LANGS}' )" != ""
%files Lithuanian
%defattr(-,root,root,-)
%{tde_datadir}/locale/lt/*
%endif

%if "%( grep -w lv <<< '%{TDE_LANGS}' )" != ""
%files Latvian
%defattr(-,root,root,-)
%{tde_datadir}/locale/lv/*
%endif

%if "%( grep -w mi <<< '%{TDE_LANGS}' )" != ""
%files Maori
%defattr(-,root,root,-)
%{tde_datadir}/locale/mi/*
%endif

%if "%( grep -w mk <<< '%{TDE_LANGS}' )" != ""
%files Macedonian
%defattr(-,root,root,-)
%{tde_datadir}/locale/mk/*
%endif

%if "%( grep -w ms <<< '%{TDE_LANGS}' )" != ""
%files Malay
%defattr(-,root,root,-)
%{tde_datadir}/locale/ms/*
%endif

%if "%( grep -w mt <<< '%{TDE_LANGS}' )" != ""
%files Maltese
%defattr(-,root,root,-)
%{tde_datadir}/locale/mt/*
%endif

%if "%( grep -w nds <<< '%{TDE_LANGS}' )" != ""
%files LowSaxon
%defattr(-,root,root,-)
%{tde_datadir}/locale/nds/*
%endif

%if "%( grep -w ne <<< '%{TDE_LANGS}' )" != ""
%files Nepali
%defattr(-,root,root,-)
%{tde_datadir}/locale/ne/*
%endif

%if "%( grep -w nl <<< '%{TDE_LANGS}' )" != ""
%files Dutch
%defattr(-,root,root,-)
%{tde_datadir}/locale/nl/*
%{tde_tdedocdir}/HTML/nl/
%endif

%if "%( grep -w nb <<< '%{TDE_LANGS}' )" != ""
%files Norwegian
%defattr(-,root,root,-)
%{tde_datadir}/locale/nb/*
%endif

%if "%( grep -w nn <<< '%{TDE_LANGS}' )" != ""
%files Norwegian-Nynorsk
%defattr(-,root,root,-)
%{tde_datadir}/locale/nn/*
%endif

%if "%( grep -w oc <<< '%{TDE_LANGS}' )" != ""
%files Occitan
%defattr(-,root,root,-)
%{tde_datadir}/locale/oc/*
%endif

%if "%( grep -w pa <<< '%{TDE_LANGS}' )" != ""
%files Punjabi
%defattr(-,root,root,-)
%{tde_datadir}/locale/pa/*
%endif

%if "%( grep -w pl <<< '%{TDE_LANGS}' )" != ""
%files Polish
%defattr(-,root,root,-)
%{tde_datadir}/locale/pl/*
%endif

%if "%( grep -w pt <<< '%{TDE_LANGS}' )" != ""
%files Portuguese
%defattr(-,root,root,-)
%{tde_datadir}/locale/pt/*
%{tde_tdedocdir}/HTML/pt/
%endif

%if "%( grep -w pt_BR <<< '%{TDE_LANGS}' )" != ""
%files Brazil
%defattr(-,root,root,-)
%{tde_datadir}/locale/pt_BR/*
%{tde_tdedocdir}/HTML/pt_BR/
%endif

%if "%( grep -w ro <<< '%{TDE_LANGS}' )" != ""
%files Romanian
%defattr(-,root,root,-)
%{tde_datadir}/locale/ro/*
%endif

%if "%( grep -w ru <<< '%{TDE_LANGS}' )" != ""
%files Russian
%defattr(-,root,root,-)
%{tde_datadir}/locale/ru/*
%{tde_tdedocdir}/HTML/ru/
%endif

%if "%( grep -w sk <<< '%{TDE_LANGS}' )" != ""
%files Slovak
%defattr(-,root,root,-)
%{tde_datadir}/locale/sk/*
%{tde_tdedocdir}/HTML/sk/
%dir %{tde_datadir}/apps/koffice
%dir %{tde_datadir}/apps/koffice/autocorrect
%{tde_datadir}/apps/koffice/autocorrect/sk.xml
%endif

%if "%( grep -w sl <<< '%{TDE_LANGS}' )" != ""
%files Slovenian
%defattr(-,root,root,-)
%{tde_datadir}/locale/sl/*
%{tde_tdedocdir}/HTML/sl/
%endif

%if "%( grep -w sr <<< '%{TDE_LANGS}' )" != ""
%files Serbian
%defattr(-,root,root,-)
%{tde_datadir}/locale/sr/*
%endif

%if "%( grep -w sv <<< '%{TDE_LANGS}' )" != ""
%files Swedish
%defattr(-,root,root,-)
%{tde_datadir}/locale/sv/*
%{tde_tdedocdir}/HTML/sv/
%endif

%if "%( grep -w ta <<< '%{TDE_LANGS}' )" != ""
%files Tamil
%defattr(-,root,root,-)
%{tde_datadir}/locale/ta/*
%endif

%if "%( grep -w tg <<< '%{TDE_LANGS}' )" != ""
%files Tajik
%defattr(-,root,root,-)
%{tde_datadir}/locale/tg/*
%endif

%if "%( grep -w th <<< '%{TDE_LANGS}' )" != ""
%files Thai
%defattr(-,root,root,-)
%{tde_datadir}/locale/th/*
%endif

%if "%( grep -w tr <<< '%{TDE_LANGS}' )" != ""
%files Turkish
%defattr(-,root,root,-)
%{tde_datadir}/locale/tr/*
%endif

%if "%( grep -w uk <<< '%{TDE_LANGS}' )" != ""
%files Ukrainian
%defattr(-,root,root,-)
%{tde_datadir}/locale/uk/*
%endif

%if "%( grep -w ven <<< '%{TDE_LANGS}' )" != ""
%files Venda
%defattr(-,root,root,-)
%{tde_datadir}/locale/ven/*
%endif

%if "%( grep -w vi <<< '%{TDE_LANGS}' )" != ""
%files Vietnamese
%defattr(-,root,root,-)
%{tde_datadir}/locale/vi/*
%endif

%if "%( grep -w wa <<< '%{TDE_LANGS}' )" != ""
%files Walloon
%defattr(-,root,root,-)
%{tde_datadir}/locale/wa/*
%endif

%if "%( grep -w xh <<< '%{TDE_LANGS}' )" != ""
%files Xhosa
%defattr(-,root,root,-)
%{tde_datadir}/locale/xh/*
%endif

%if "%( grep -w zh_CN <<< '%{TDE_LANGS}' )" != ""
%files Chinese
%defattr(-,root,root,-)
%{tde_datadir}/locale/zh_CN/*
%endif

%if "%( grep -w zh_TW <<< '%{TDE_LANGS}' )" != ""
%files Chinese-Big5
%defattr(-,root,root,-)
%{tde_datadir}/locale/zh_TW/*
%endif


%changelog
