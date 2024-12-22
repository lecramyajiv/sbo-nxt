#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

TARBALL=$(get_latest_tarball_filename.sh "${PKGNAME}" ${TDE_VERSION})

[ ! -r "${TARBALL}" ] && exit 2

VERSION=${TARBALL##*/}
VERSION=${VERSION#trinity-}
VERSION=${VERSION#${PKGNAME}-}
VERSION=${VERSION#${PKGNAME}_}
VERSION=${VERSION#*-}
VERSION=${VERSION%.tar.gz}
VERSION=${VERSION%.tar.bz2}
VERSION=${VERSION%.orig}
echo "$VERSION"
