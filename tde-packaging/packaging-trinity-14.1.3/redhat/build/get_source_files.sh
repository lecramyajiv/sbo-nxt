#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"
DIST="$3"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
SPECFILE=$(get_specfile.sh ${PKGNAME} ${TDE_VERSION})
SPECDIR="${SPECFILE%/*}"
RPMPKGNAME="$(get_rpm_package_name.sh ${PKGNAME})"
[ ! -r "${SPECFILE}" ] && exit 2

while read var val; do
  case "${var}" in
    Version:*) VERSION="${val}";;
    Source*:|Source:|Patch[0-9]*:)
      if [ "${val:0:7}" = "http://" ] || [ "${val:0:8}" = "https://" ]; then
        FILE="${SPECDIR}/${val##*/}"
      else
        FILE="${SPECDIR}/${val}"
      fi
      if [ "${DIST}" = "any" ] && [ "${var//%\{?dist\}/}" = "${var}" ]; then
        FILES="${FILE//%\{?dist\}/.}"*
      else
        FILES="${FILE}"
      fi

      for FILE in $FILES; do
        for name in ${RPMPKGNAME} ${PKGNAME} trinity-${PKGNAME}; do
          file=$(rpm --define "tde_pkg ${PKGNAME}" \
                     --define "tde_version ${TDE_VERSION}" \
                     --define "name ${name}" \
                     --define "version ${VERSION}" \
                     --define "dist ${DIST:-$(rpmdist.sh --dist)}" \
                     -E "${FILE}")
          [ -r "${file}" ] && break
        done
        [ -r "${file}" ] && echo "${file}"
      done
    ;;
  esac
done < "${SPECFILE}" | sort -u
