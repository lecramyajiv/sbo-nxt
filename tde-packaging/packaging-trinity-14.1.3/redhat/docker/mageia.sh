#!/bin/bash -e

NAME="mageia"
VERSION="${1:-9}" # E.g: '9'
IMAGE="${NAME}:${VERSION}"
INSTALLROOT="/dev/shm/${IMAGE}"
ARCH="x86_64"
[ -x /usr/bin/pigz ] && GZIP=pigz || GZIP=gzip

sudo rm -rf "${INSTALLROOT}"
sudo mkdir -p "${INSTALLROOT}"
sudo dnf -y \
  --disablerepo="*" \
  --enablerepo="mageia-${ARCH},updates-${ARCH}" \
  --installroot="${INSTALLROOT}" \
  --releasever="${VERSION}" \
  install \
  \
  bash \
  mageia-release-common \
  urpmi \
  vim

sudo chroot "${INSTALLROOT}" rpmdb --rebuilddb

FILE="${IMAGE//\//_}.tar"
sudo tar -C "${INSTALLROOT}" -c . >"${FILE}"
sudo rm -rf "${INSTALLROOT}"

docker rmi -f "${IMAGE}"
docker import "${FILE}" "${IMAGE}"

${GZIP} "${FILE}"
mkdir -p "${HOME}/tde/docker"
mv -fv "${FILE}.gz" "${HOME}/tde/docker"
