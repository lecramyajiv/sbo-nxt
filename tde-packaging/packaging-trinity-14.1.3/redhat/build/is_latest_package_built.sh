#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

BUILT="$(get_latest_built_package_version.sh ${PKGNAME} ${TDE_VERSION})"
TARBALL="$(get_latest_tarball_version.sh ${PKGNAME} ${TDE_VERSION})"
RPM_PKGNAME="$(get_rpm_package_name.sh ${PKGNAME})"

[ -z "${TARBALL}" ] && exit 1

# If package version contains a "~": it's a pre-release
if [ "${BUILT/~/}" != "${BUILT}" ]; then
  if [ "${BUILT#*_pre}" = "${TARBALL#*~pre}" ]; then
    echo "Latest development package '${PKGNAME}' version '${BUILT}' is already built."
    exit 0
  fi
# Nominal case: no "~" caracter
else
  if [ "${TARBALL%-*}" = "${BUILT%-*}" ] || [[ "${BUILT}" =~ ${TARBALL}_[0-9]* ]]; then
    echo "Latest stable package '${PKGNAME}' version '${BUILT}' is already built."
    exit 0
  fi
fi

exit 1
