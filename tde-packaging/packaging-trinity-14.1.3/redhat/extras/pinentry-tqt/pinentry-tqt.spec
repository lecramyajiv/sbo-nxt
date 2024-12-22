#
# spec file for package pinentry-tqt (version R14)
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


Name:		pinentry-tqt
Version:	1.3.1
Release:	1%{?dist}
Summary:	PIN or passphrase entry dialogs
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}.tar.gz

BuildRequires:	trinity-tqtinterface-devel

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gcc-c++
BuildRequires:	autoconf automake libtool m4
BuildRequires:	pkgconfig

BuildRequires:	libassuan-devel

# SECRET support
%if 0%{?mdkver} >= 5000000
BuildRequires:	%{_lib}secret-devel
%else
BuildRequires:	libsecret-devel
%endif

Requires:		pinentry


%description
This is a collection of PIN or passphrase entry dialogs which
utilize the Assuan protocol as specified in the Libassuan manual.

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q

%__sed -i "configure.ac" \
 -e "/^min_automake_version=/ s|=.*|=\"1.13\"|" \
 -e "/^NEED_GPG_ERROR_VERSION=/ s|=.*|=1.12|"


%build
unset QTDIR QTINC QTLIB

if [ -d "/usr/include/libassuan2" ]; then
  export CFLAGS="%{optflags} -I/usr/include/libassuan2"
fi

./autogen.sh

%if 0%{?mgaversion} == 6 || 0%{?mgaversion} == 7 || 0%{?pclinuxos}
%configure2_5x \
%else
%configure \
%endif
  --enable-pinentry-tqt \
  --enable-libsecret \
  --disable-doc \
  --disable-pinentry-curses \
  --disable-pinentry-fltk \
  --disable-pinentry-gnome3 \
  --disable-pinentry-gtk2 \
  --disable-pinentry-qt \
  --disable-pinentry-qt4 \
  --disable-pinentry-qt5 \
  --disable-pinentry-tty

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}
%__rm -f "%{buildroot}%{_bindir}/pinentry"


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/pinentry-tqt


%changelog
