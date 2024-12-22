#!/bin/bash

# Usage: gather_rpm_sources.sh <TDE_PACKAGE> <TDE_VERSION> <DESTINATION>
# Example: gather_rpm_sources.sh tdebase 14.1.2 /tmp/tdebase

PKGNAME="${1%/}"
PKGNAME="${PKGNAME##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"
TARGETDIR="${3:-/tmp/${PKGNAME}-${TDE_VERSION}}"
DIST="$(rpmdist.sh --dist)"

SPECFILE=$(get_specfile.sh ${PKGNAME} ${TDE_VERSION})
[ -z "${SPECFILE}" ] && exit 1

SOURCES=$(get_source_files.sh ${PKGNAME} ${TDE_VERSION} ${DIST})
TARBALL=$(get_latest_tarball_filename.sh ${PKGNAME} ${TDE_VERSION} || :)
VERSION=$(get_latest_tarball_version.sh ${PKGNAME} ${TDE_VERSION} || :)
case "${VERSION}" in *~pre*) PREVERSION="${VERSION#*~}";; esac

[ -z "${TMPPATH}" ] && TMPPATH="/dev/shm"
BUILDDIR="${TMPPATH}/BUILD${DIST}.$(uname -i)"
BUILDROOTDIR="${TMPPATH}/BUILDROOT${DIST}.$(uname -i)"
LOGFILE="${TMPPATH}/log.${COMP##*/}"

mkdir -p "${TARGETDIR}"
rm -f "${TARGETDIR}/"*

cp -f ${SPECFILE} ${SOURCES} ${TARBALL} "${TARGETDIR}"

### Check for patches

PATCHDIR="${HOME}/tde/patches/${TDE_VERSION}/$1"
if [ -d "${PATCHDIR}" ]; then
  cat "${PATCHDIR}/"*".patch" "${PATCHDIR}/"*".patch${DIST}" >>"${TARGETDIR}/one.patch" 2>/dev/null
  if [ "$(cat "${TARGETDIR}/one.patch" | wc -c)" = 0 ]; then
    rm -f "${TARGETDIR}/one.patch"
  else
    sed -i "${TARGETDIR}/"*".spec" \
        -e "/^Source0:/ s/$/\nPatch389: one.patch/" \
        -e "/%setup/ s/$/\n%patch389 -p1/"
  fi
fi

if [ "${DIST}" = ".fc41" ] || [ "${DIST}" = ".mga9" ] || [ "${DIST}" = ".omv5000" ] || [ "${DIST}" = ".osstw" ] || [ "${DIST:0:6}" = ".pclos" ]; then
  sed -i "${TARGETDIR}/"*".spec" \
      -e "s|%patch|%patch -P |g"
fi

exit 0
