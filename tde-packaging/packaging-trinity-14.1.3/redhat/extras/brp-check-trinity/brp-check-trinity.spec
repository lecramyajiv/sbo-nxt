#
# spec file for package brp-check-trinity (version R14)
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
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_prefix /opt/trinity

Name:		brp-check-trinity
Version:	1.0
Release:	1%{?dist}
Summary:	Build root policy check scripts for Trinity
Group:		System Environment/Daemons
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
BuildArch:	noarch

BuildRequires:	update-desktop-files
BuildRequires:	brp-check-suse
%if 0%{?suse_version} <= 1500
BuildRequires:	brp-extract-appdata
%endif
Requires:	update-desktop-files
Requires:	brp-check-suse
%if 0%{?suse_version} <= 1500
Requires:	brp-extract-appdata
%endif
Requires:	sed



%description
This package dynamically patches the openSUSE brp script to allow
building of Trinity Desktop Environment (TDE) instead of KDE3.
It should not be installed on runtime computer.


%files

%post
for i in \
	brp-desktop.data/applications.menu \
	brp-desktop.data/kde-settings.menu \
	brp-desktop.data/xdg_menu \
	brp-suse.d/brp-25-symlink \
	brp-suse.d/brp-72-extract-appdata \
	map-desktop-category.sh \
	suse_update_desktop_file.sh \
; do
	[ -r "/usr/lib/rpm/${i}" ] || continue
	[ -r "/usr/lib/rpm.orig/${i}" ] && continue
	echo "Patching file '/usr/lib/rpm/${i}' ..."
	install -D "/usr/lib/rpm/${i}" "/usr/lib/rpm.orig/${i}"
	sed -i "/usr/lib/rpm/${i}" \
		-e "s|opt/kde3|opt/trinity|g" \
		-e "s|kde-config|tde-config|g" \
		-e "s|kdesu|tdesu|g" \
		-e "s|kde-settings-|tde-settings-|g" \
		-e "s|doc/kde|doc/tde|g" \
		-e "s|kde_xdgdata|tde_xdgdata|g" \
		-e "s|applications/kde|applications/tde|g" \
		-e "s|KDE|TDE|g" \
		-e "s|kde-|tde-|g" \
%if 0%{?suse_version} >= 1550
		-e "s|/usr/share/applications|/opt/trinity/share/applications|g" \
		-e "/^for i in/ s|\\\| /\$RPM_BUILD_ROOT/opt/trinity/share/applnk \\\|" \
%endif
		-e "s|tde-settings.menu|kde-settings.menu|g"
	diff -Nua "/usr/lib/rpm.orig/${i}" "/usr/lib/rpm/${i}" || :
done


%postun
for i in \
	brp-desktop.data/applications.menu \
	brp-desktop.data/kde-settings.menu \
	brp-desktop.data/xdg_menu \
	brp-suse.d/brp-25-symlink \
	brp-suse.d/brp-72-extract-appdata \
	map-desktop-category.sh \
	suse_update_desktop_file.sh \
; do
	[ -r "/usr/lib/rpm.orig/${i}" ] || continue
	echo "Restoring file '/usr/lib/rpm/${i}' ..."
	install "/usr/lib/rpm.orig/${i}" "/usr/lib/rpm/${i}"
done
rm -rf "/usr/lib/rpm.orig"

##########

%prep

%build

%install

%clean
%__rm -rf %{?buildroot}


%changelog
