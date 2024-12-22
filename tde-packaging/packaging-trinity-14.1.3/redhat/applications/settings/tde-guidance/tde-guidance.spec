#
# spec file for package tde-guidance (version R14)
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
%define tde_pkg tde-guidance
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

%define __arch_install_post %{nil}


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.8.0svn20080103
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	A collection of system administration tools for Trinity
Group:		Applications/Utilities
URL:		http://www.simonzone.com/software/guidance

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		trinity-%{tde_pkg}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	trinity-pytdeextensions
BuildRequires:	trinity-libpythonize0-devel
BuildRequires:	trinity-pytde
BuildRequires:	chrpath

BuildRequires:	libtool
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# SIP support
BuildRequires:	sip4-tqt-devel >= 4.10.5
Requires:		sip4-tqt >= 4.10.5

# PYTHON-QT support
BuildRequires:	pytqt-devel
BuildRequires:	trinity-pytde-devel
BuildRequires:	trinity-pytqt-tools

# XSCREENSAVER support
#  RHEL 4: disabled
#  RHEL 6: available in EPEL
#  RHEL 7: available in NUX
#  RHEL 8: available in EPEL
#  RHEL 9: available in EPEL
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version}
%define with_xscreensaver 1

%if 0%{?fedora} || 0%{?rhel} >= 5
BuildRequires:	libXScrnSaver-devel
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
BuildRequires:	xscreensaver-extras
%if 0%{?fedora}
BuildRequires:	xscreensaver-extras-base
%endif
BuildRequires:	xscreensaver-gl-base
BuildRequires:	xscreensaver-gl-extras
%endif

%if 0%{?suse_version}
BuildRequires:	libXScrnSaver-devel
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-data
BuildRequires:	xscreensaver-data-extra
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xscrnsaver-devel
%else
BuildRequires:	%{_lib}xscrnsaver%{?mgaversion:1}-devel
%endif
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
%if 0%{?pclinuxos} == 0
BuildRequires:	xscreensaver-extrusion
%endif
BuildRequires:	xscreensaver-gl
%endif
%endif

# PYTHON support
%if "%{python}" == ""
%global python python3
%endif
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

Requires:		pytqt
Requires:		trinity-pytde
Requires:		trinity-pytdeextensions
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
Requires:		hwdata
%endif

Requires:		%{name}-backends = %{?epoch:%{epoch}:}%{version}-%{release}

# POWERMANAGER support (requires HAL)
#define with_powermanager 1
Obsoletes:	trinity-tde-guidance-powermanager < %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-guidance < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-guidance = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Guidance currently consists of four programs designed to help you
look after your system:
 o  userconfig - User and Group administration
 o  serviceconfig - Service/daemon administration
 o  mountconfig - Disk and filesystem administration

These tools are available in Trinity Control Center, System Settings 
or can be run as standalone applications.

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README TODO
%{tde_bindir}/mountconfig
%{tde_bindir}/serviceconfig
%{tde_bindir}/userconfig
%attr(0644,root,root) %{tde_tdelibdir}/*.so
%attr(0644,root,root) %{tde_tdelibdir}/*.la
%{tde_datadir}/apps/guidance/
%{tde_tdeappdir}/*.desktop
%{tde_datadir}/icons/crystalsvg/*/*/*.png
%if 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?rhel} == 7 || 0%{?suse_version}
%{python_sitelib}/tde-guidance/SMBShareSelectDialog.py*
%{python_sitelib}/tde-guidance/SimpleCommandRunner.py*
%{python_sitelib}/tde-guidance/fuser.py*
%{python_sitelib}/tde-guidance/fuser_ui.py*
%{python_sitelib}/tde-guidance/mountconfig.py*
%{python_sitelib}/tde-guidance/serviceconfig.py*
%{python_sitelib}/tde-guidance/sizeview.py*
%{python_sitelib}/tde-guidance/unixauthdb.py*
%{python_sitelib}/tde-guidance/userconfig.py*
%if 0%{?rhel} == 7
%{python_sitelib}/tde-guidance/__pycache__/SMBShareSelectDialog.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/SimpleCommandRunner.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/fuser.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/fuser_ui.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/mountconfig.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/serviceconfig.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/sizeview.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/unixauthdb.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/userconfig.*.pyc
%endif
%else
%pycached %{python_sitelib}/tde-guidance/SMBShareSelectDialog.py
%pycached %{python_sitelib}/tde-guidance/SimpleCommandRunner.py
%pycached %{python_sitelib}/tde-guidance/fuser.py
%pycached %{python_sitelib}/tde-guidance/fuser_ui.py
%pycached %{python_sitelib}/tde-guidance/mountconfig.py
%pycached %{python_sitelib}/tde-guidance/serviceconfig.py
%pycached %{python_sitelib}/tde-guidance/sizeview.py
%pycached %{python_sitelib}/tde-guidance/unixauthdb.py
%pycached %{python_sitelib}/tde-guidance/userconfig.py
%endif

# Files from powermanager
%if 0%{?with_powermanager}
%exclude %{tde_datadir}/icons/hicolor/22x22/apps/power-manager.png
%exclude %{tde_datadir}/apps/guidance/pics/ac-adapter.png
%exclude %{tde_datadir}/apps/guidance/pics/battery*.png
%exclude %{tde_datadir}/apps/guidance/pics/processor.png
%endif

%{tde_tdedocdir}/HTML/en/tde-guidance/
%{tde_mandir}/man1/mountconfig-trinity.1*
%{tde_mandir}/man1/serviceconfig-trinity.1*
%{tde_mandir}/man1/userconfig-trinity.1*

##########

%package backends
Group:			Applications/Utilities
Summary:		collection of system administration tools for GNU/Linux [Trinity]
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
Requires:		hwdata
%endif
Requires:		%{python}

Obsoletes:		trinity-guidance-backends < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-guidance-backends = %{?epoch:%{epoch}:}%{version}-%{release}

%description backends
This package contains the platform neutral backends used in the
Guidance configuration tools.

%files backends
%defattr(-,root,root,-)
%dir %{python_sitelib}/tde-guidance
%if 0%{?mdkversion} || 0%{?pclinuxos} || 0%{?rhel} == 7 || 0%{?suse_version}
%{python_sitelib}/tde-guidance/MicroHAL.py*
%if 0%{?rhel} == 7
%{python_sitelib}/tde-guidance/__pycache__/MicroHAL.*.pyc
%endif
%else
%pycached %{python_sitelib}/tde-guidance/MicroHAL.py
%endif

##########

%if 0%{?with_powermanager}

%package powermanager
Group:			Applications/Utilities
Summary:		HAL based power manager applet [Trinity]
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		hal

Obsoletes:		trinity-guidance-powermanager < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-guidance-powermanager = %{?epoch:%{epoch}:}%{version}-%{release}

%if "%{tde_prefix}" == "/usr"
Conflicts:	guidance-power-manager
Conflicts:	kde-guidance-powermanager
%endif

%description powermanager
A power management applet to indicate battery levels and perform hibernate or
suspend using HAL.

%files powermanager
%defattr(-,root,root,-)
%{tde_bindir}/guidance-power-manager
%if 0%{?mdkver} ||0%{?pclinuxos} || 0%{?rhel} == 7 || 0%{?suse_version}
%{python_sitelib}/tde-guidance/MicroHAL.py*
%{python_sitelib}/tde-guidance/guidance-power-manager.py*
%{python_sitelib}/tde-guidance/powermanage.py*
%{python_sitelib}/tde-guidance/gpmhelper.py*
%{python_sitelib}/tde-guidance/powermanager_ui.py*
%{python_sitelib}/tde-guidance/guidance_power_manager_ui.py*
%{python_sitelib}/tde-guidance/notify.py*
%{python_sitelib}/tde-guidance/tooltip.py*
%{python_sitelib}/tde-guidance/__pycache__/MicroHAL.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/guidance-power-manager.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/powermanage.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/gpmhelper.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/powermanager_ui.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/guidance_power_manager_ui.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/notify.*.pyc
%{python_sitelib}/tde-guidance/__pycache__/tooltip.*.pyc
%else
%pycached %{python_sitelib}/tde-guidance/MicroHAL.py
%pycached %{python_sitelib}/tde-guidance/guidance-power-manager.py
%pycached %{python_sitelib}/tde-guidance/powermanage.py
%pycached %{python_sitelib}/tde-guidance/gpmhelper.py
%pycached %{python_sitelib}/tde-guidance/powermanager_ui.py
%pycached %{python_sitelib}/tde-guidance/guidance_power_manager_ui.py
%pycached %{python_sitelib}/tde-guidance/notify.py
%pycached %{python_sitelib}/tde-guidance/tooltip.py
%endif
%{tde_datadir}/icons/hicolor/22x22/apps/power-manager.png
%{tde_datadir}/apps/guidance/pics/ac-adapter.png
%{tde_datadir}/apps/guidance/pics/battery*.png
%{tde_datadir}/apps/guidance/pics/processor.png
%{tde_datadir}/autostart/guidance-power-manager.desktop

%endif

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%if 0%{?rhel} || 0%{?mgaversion} || 0%{?mdkversion}
%__sed -i "userconfig/unixauthdb.py" \
  -e "s|self.first_uid = .*|self.first_uid = 500|" \
  -e "s|self.first_gid = .*|self.first_gid = 500|"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I%{tde_tdeincludedir} -I%{tde_includedir}"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes FTBFS [Bug #1285]
%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
 -DBUILD_ALL="ON" \
 -DWITH_ALL_OPTIONS="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -fr $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT -C build


%clean
%__rm -rf %{buildroot}


%changelog
