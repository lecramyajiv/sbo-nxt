#
# spec file for package tde-filesystem
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
 
 
Name:           tde-filesystem
Url:            http://www.trinitydesktop.org/
Version:        R13.99
Release:        1
License:        LGPLv2.1+
Group:          System/Fhs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Trinity Directory Layout
Source0:        macros.tde
Source1:        COPYING
BuildArch:	noarch
# Spare Dependency that we want tde-filesystem to pull in.
Requires:	cmake

%description
This package installs the Trinity directory structure.
 
 
 
Authors:
--------
    The Trinity Project <rxu@lincomlinux.org>
 
%prep
 
%build
 
%install
  install -D -m644 %{SOURCE0} $RPM_BUILD_ROOT/etc/rpm/macros.tde
  install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/doc/packages/tde-filesystem/COPYING

%clean
rm -rf "$RPM_BUILD_ROOT"
 
%files
%defattr(-,root,root)
%config /etc/rpm/macros.tde
%dir /usr/share/doc/packages/tde-filesystem
/usr/share/doc/packages/tde-filesystem/COPYING
 
%changelog
