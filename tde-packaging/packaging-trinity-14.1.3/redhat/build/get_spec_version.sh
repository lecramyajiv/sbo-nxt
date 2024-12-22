#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

SPECFILE=$(get_specfile.sh  ${PKGNAME} ${TDE_VERSION})

[ ! -r "${SPECFILE}" ] && exit 2

VERSION=$(sed -n "/^Version:/ s/Version:[ 	]*//p" ${SPECFILE})
RELEASE=$(sed -n "/^Release:/ s/Release:[ 	]*//p" ${SPECFILE})
VERSION=$(rpm -E "${VERSION}")
VERSION=$(rpm --define "tde_version ${TDE_VERSION}" -E "${VERSION}")
RELEASE=$(rpm --define "tde_version ${TDE_VERSION}" -E "${RELEASE}")
RELEASE=${RELEASE%$(rpmdist.sh --dist)}

echo ${VERSION}-${RELEASE}
