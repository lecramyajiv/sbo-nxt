#!/bin/bash

PKGNAME="$1"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

RPM=$(get_latest_built_package_filename.sh "${PKGNAME}" ${TDE_VERSION})

[ ! -r "${RPM}" ] && echo "No package found for '${PKGNAME}' !" && exit 2

pkg_version="$(rpm -qp --qf "%{version}" "${RPM}")"
pkg_release="$(rpm -qp --qf "%{release}" "${RPM}")"

# Preversion
if [ "${pkg_release:0:2}" = "0_" ] || [[ "${pkg_release}" =~ _0_ ]]; then
  # Application packages: version does not match TDE version
  if [[ "${pkg_release}" =~ ${TDE_VERSION}_ ]] ; then
     # Likely application package
    eval VERSION="${pkg_release/0_/\~}"
  else
    # Likely core package
    eval VERSION="${pkg_version}${pkg_release/0_/\~}"
  fi
  VERSION="${VERSION/_~/\~}"
else
  # Stable version
  if [[ "${pkg_release}" =~ ${TDE_VERSION}_ ]] ; then
     # Likely application package
    eval VERSION="${pkg_release/_*/}"
  else
    # Likely core package
    eval VERSION="${pkg_version}"
  fi
fi

VERSION="${VERSION%.opt}" # Remove '.opt' suffix
VERSION="${VERSION%.[a-z]*}" # Remove distro suffix (e.g. '.el6')

echo "${VERSION}"
