#
# spec file for package tdelibs-devel-doc
#
# Copyright (c) 2011 the Trinity Project (opensuse).
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
  
# Please submit bugfixes or comments via http://bugs.trinitydesktop.org/
#

# norootforbuild


Name:           tdelibs-devel-doc
BuildRequires:  OpenEXR-devel aspell-devel cups-devel db-devel doxygen graphviz tdelibs-devel krb5-devel libjasper libsndfile openldap2-devel qt3-devel-doc libtqt4-devel tde-filesystem utempter xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-scalable
BuildRequires:  avahi-compat-mDNSResponder-devel fdupes
URL:            http://www.trinitydesktop.org
License:        GPLv2+
Group:          Documentation/HTML
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Additional Package Documentation
Version:        R13.99
Release:        1
%define       tdelibs_patch_level b
BuildArch:      noarch
Requires:       tdelibs qt3-devel-doc
Source0:        tdelibs-%{version}.tar.bz2
Source1:        create-kdeapi
Source4:        api_docu_description

%description
This package contains a generated API documentation for all library
classes provided by tdelibs. The index page for all TDE API functions
is:

file:/usr/share/doc/TDE-API/index.html



Authors:
--------
    The KDE Team <kde@kde.org>

%prep
  echo %suse_version
%setup -q -n tdelibs-%{version}

%build
%if %is_plus
  # supplementary package
  DISTRI="openSUSE $BUILD_DISTRIBUTION_VERSION UNSUPPORTED"
%else
  # official build on released and maintained products
  DISTRI="openSUSE $BUILD_DISTRIBUTION_VERSION"
%endif
export QTDOCDIR=/usr/share/doc/packages/qt3/html
%cmake_tde -d build -- -DKDE_DISTRIBUTION="$DISTRI"
%make_tde -d build -- apidox 

%install
  list=`find . -name Makefile.am | xargs grep Doxy | sed -e "s,/Makefile.am.*,," | sort -u `
  for i in $list; do %makeinstall_tde -d build -- -C $i DESTDIR=$RPM_BUILD_ROOT install-apidox || true; done
  # The modern way, with kdevelop-incompatible api documentation :/
  mkdir -p $RPM_BUILD_ROOT/usr/share/doc/TDE-API/
  # *** everytime you edit the following line, you made a mistake. Update macros.tde
  # *** version instead
  KDEDOCDIR=%{_tde_htmldir}/en/kdelibs-apidocs
  # this is forgotten, but kdevelop needs it
  mkdir -p $RPM_BUILD_ROOT/$KDEDOCDIR
  if test -d apidocs/qt; then
    cp -a apidocs/qt $RPM_BUILD_ROOT/$KDEDOCDIR
  fi
  set +x
  exitc=0
  for i in `ls -1 $RPM_BUILD_ROOT/$KDEDOCDIR/*/html/index.html`; do 
      lib=`echo $i | sed -e 's,/html/index.html,,; s,.*/\([^/]*\)$,\1,'`
      if ! egrep "^$lib:" %SOURCE4 ; then
  	echo "ERROR: no description for library $lib"
        exitc=1
      fi
      sed -n -e 's@'"${lib}"':\(.*\)@\1@p' %SOURCE4 > ${RPM_BUILD_ROOT}/${KDEDOCDIR}/${lib}/description.SuSE
      echo "kdelibs"                          > ${RPM_BUILD_ROOT}/${KDEDOCDIR}/${lib}/package.SuSE
  done
  if test "$exitc" != 0; then
	exit $exitc
  fi
  ln -s $KDEDOCDIR/index.html $RPM_BUILD_ROOT/usr/share/doc/TDE-API/index.html
  rm -rf ${RPM_BUILD_ROOT}/%{_tde_datadir}
  mkdir -p $RPM_BUILD_ROOT/%{_tde_datadir}/tdelibs
  install -m 0755 %SOURCE1 $RPM_BUILD_ROOT/%{_tde_datadir}/tdelibs/
  %fdupes -s $RPM_BUILD_ROOT

%post
%{_tde_datadir}/tdelibs/create-kdeapi

%clean
  rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%dir %{_tde_sharedir}
%dir %{_tde_datadir}
%dir %{_tde_datadir}/tdelibs
%{_datadir}/doc/TDE-API
%{_tde_datadir}/tdelibs/create-kdeapi
%{_tde_docdir}

%changelog
