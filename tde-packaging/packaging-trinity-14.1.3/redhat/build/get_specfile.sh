#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

[ -d "${TDE_PACKAGING_DIR}" ] || TDE_PACKAGING_DIR="${HOME}/tde/${TDE_BRANCH:-master}/tde/packaging"
[ -d "${DIST_PACKAGING_DIR}" ] || DIST_PACKAGING_DIR="${TDE_PACKAGING_DIR}/redhat"

# Special case for QT3
if [ "${PKGNAME}" = "qt3" ]; then
  case "$(rpmdist.sh --dist)" in
    .oss*) DIST_PACKAGING_DIR="${TDE_PACKAGING_DIR}/opensuse" ;;
    .mga*|.mdk*|.pclos*) DIST_PACKAGING_DIR="${TDE_PACKAGING_DIR}/mageia" ;;
  esac
fi

for filename in \
  "${PKGNAME}-${TDE_VERSION}.spec" \
  "${PKGNAME}-14.0.0.spec" \
  "${PKGNAME}.spec" \
  "trinity-${PKGNAME}-${TDE_VERSION}.spec" \
  "trinity-${PKGNAME}-14.0.0.spec" \
  "trinity-${PKGNAME}.spec" \
; do
  SPECFILE="$(find "${DIST_PACKAGING_DIR}" -follow -name "${filename}")"
  [ -r "${SPECFILE}" ] && break || continue
done

if [ -r "${SPECFILE}" ]; then
  echo "${SPECFILE}"
  exit 0
else
  exit 1
fi
