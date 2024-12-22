#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
[ -d "${TARBALLS_DIR}" ] || TARBALLS_DIR=~/tde/tarballs/${TDE_VERSION}/
[ -d "${TDE_PACKAGING_DIR}" ] || TDE_PACKAGING_DIR=~/tde/master/tde/packaging
[ -d "${DIST_PACKAGING_DIR}" ] || DIST_PACKAGING_DIR=${TDE_PACKAGING_DIR}/redhat/

EXTRA_DIR="$(cd ${TARBALLS_DIR}/../extras/; pwd)"

RET=""
for dir in "${TARBALLS_DIR}" "${EXTRA_DIR}" "${DIST_PACKAGING_DIR}"; do
  for v in \
    "${PKGNAME}-${TDE_VERSION}.tar.*" \
    "${PKGNAME}-${TDE_VERSION}*.tar.*" \
     "trinity-${PKGNAME}-${TDE_VERSION}.tar.*" \
     "trinity-${PKGNAME}-${TDE_VERSION}*.tar.*" \
     "${PKGNAME}[-_][0-9]*.tar.*" \
  ; do
    RET=$(find "${dir}" -follow -type f -name ${v} | sort | tail -n 1)
    [ -r "${RET}" ] && break
  done
  [ -r "${RET}" ] && echo "${RET}" && break
done

exit 0
