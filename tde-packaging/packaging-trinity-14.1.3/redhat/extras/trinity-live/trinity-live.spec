%define _prefix /usr

%define tde_bindir %{tde_prefix}/bin

Name:		trinity-live
Version:	3.5.13.2
Release:	1%{?dist}
License:	GPL
Summary:	Trinity Spins
Group:		Applications/System

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	fedora-kickstarts
Requires:	livecd-tools

Source0:	fedora-live-tde-base.ks
Source1:	fedora-livecd-tde.ks

%description
This package contains the Trinity configuration file to build a Fedora
LiveCD containing Fedora.

%package openbox
Summary:	bootstrap 'openbox' script that runs TDE's kwin
Requires:	trinity-twin
BuildArch:	noarch
Group:		Applications/System

%description openbox
There is a bug in 'firstboot' that prevents it to invoke 'openbox' correctly.
The provided script redirects 'openbox' to 'kwin'.
It is used on the Fedora TDE LiveCD.

%prep

%build
cat <<EOF >openbox
#!/bin/sh

# This script is used by 'firstboot' only.
# It allows to run TDE's kwin instead of openbox.

export PATH=%{tde_bindir}:\${PATH}
export HOME=/root
rm -rf \${HOME}/.DCOPserver*

rpm -e trinity-live-openbox

exec kwin \$@
EOF

%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_datadir}/spin-kickstarts
%__install -m 644 %{SOURCE0} %{?buildroot}%{_datadir}/spin-kickstarts
%__install -m 644 %{SOURCE1} %{?buildroot}%{_datadir}/spin-kickstarts

# Openbox
%__install -D -m 755 openbox "%{?buildroot}/usr/local/bin/openbox"


%files
%{_datadir}/spin-kickstarts/fedora-live-tde-base.ks
%{_datadir}/spin-kickstarts/fedora-livecd-tde.ks

%files openbox
/usr/local/bin/openbox


%changelog
