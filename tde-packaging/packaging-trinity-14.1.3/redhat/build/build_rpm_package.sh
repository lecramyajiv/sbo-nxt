#!/bin/bash -ex

# Usage: build_rpm_package.sh <TDE_PACKAGE> [TDE_VERSION]
# Example: build_rpm_package.sh tdebase 14.1.2


PKGNAME="${1%/}"
PKGNAME="${PKGNAME##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"
PATH="$(cd $(dirname $0); pwd):${PATH}"

SPECFILE=$(get_specfile.sh ${PKGNAME} ${TDE_VERSION})
VERSION=$(get_latest_tarball_version.sh ${PKGNAME} ${TDE_VERSION} || :)
case "${VERSION}" in *~pre*) PREVERSION="${VERSION#*~}";; esac

ARCH="$(uname -i)"
if [ "${ARCH}" = "unknown" ]; then
  ARCH="$(uname -m)"
fi
DIST="$(rpmdist.sh --dist)"
[ -z "${TMPPATH}" ] && TMPPATH="/dev/shm"
BUILDDIR="${TMPPATH}/BUILD${DIST}.${ARCH}"
BUILDROOTDIR="${TMPPATH}/BUILDROOT${DIST}.${ARCH}"
LOGFILE="${TMPPATH}/log.${PKGNAME##*/}"

export TEMPDIR="$(mktemp -d)"
gather_rpm_sources.sh "${PKGNAME}" "${TDE_VERSION}" "${TEMPDIR}"
specfile="${TEMPDIR}/${SPECFILE##*/}"

if [ "${DIST}" = ".omv2490" ]; then
  sed -i "${specfile}" -e "s|^%patch|%patch |"
fi

[ -d "${BUILDDIR}" ] || mkdir -p "${BUILDDIR}"

RPMDIR="$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})"
SRPMDIR="$(rpm -E %{_srcrpmdir}.tde-${TDE_VERSION})"

rpmbuild -ba \
  --define "_specdir ${TEMPDIR}" \
  --define "_sourcedir ${TEMPDIR}" \
  --define "_builddir ${BUILDDIR}" \
  --define "_buildrootdir ${BUILDROOTDIR}" \
  --define "_tmppath ${TMPPATH}" \
  --define "_rpmdir ${RPMDIR}" \
  --define "_srcrpmdir ${SRPMDIR}" \
  --define '_build_create_debug 1' \
  --define "vendor Trinity\ Desktop" \
  --define "packager Francois\ Andriot\ <francois.andriot@free.fr>" \
  --define "tde_version ${TDE_VERSION}" \
  --define "tde_prefix /opt/trinity" \
  --define "prevers${PREVERSION:+ion} ${PREVERSION:-0}" \
  --define "tde_patch 1" \
  --define "with_mpeg 1" \
  "${specfile}"
RET=$?

# Removes BUILDDIR if build succeeded
if [ ${RET} -eq 0 ]; then
  rm -rf "${BUILDDIR}/"*${PKGNAME}-${VERSION}*
fi

rm -rf "${TEMPDIR}"

exit $RET
