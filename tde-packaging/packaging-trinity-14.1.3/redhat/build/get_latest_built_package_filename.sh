#!/bin/bash

PKGNAME="$1"
[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

RPMDIR="$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})"
RPMDIR_ARCH="${RPMDIR}/$(rpm -E %_target_cpu)"
RPMDIR_NOARCH="${RPMDIR}/noarch"
RPMDIRS="${RPMDIR_ARCH} ${RPMDIR_NOARCH}"

RPM_PKGNAME="$(get_rpm_package_name.sh ${PKGNAME})"

RPM=$(find ${RPMDIRS} -name "trinity-${RPM_PKGNAME}-[0-9]*.rpm" | sort -n | tail -n 1)

if [ ! -r "${RPM}" ]; then
  RPM=$(find ${RPMDIRS} -name "${RPM_PKGNAME}-[0-9]*.rpm" | sort -n | tail -n 1)
  if [ ! -r "${RPM}" ]; then
    echo "Error, cannot find any package for '${PKGNAME}' !"
    exit 1
  fi
fi

echo $RPM
