#!/bin/bash -ex

NAME="openmandriva"
VERSION="${1:-5.0}" # E.g: '26'
IMAGE="${NAME}:${VERSION}"
TAR="${NAME}-${VERSION}.tar"
INSTALLROOT="/dev/shm/${IMAGE}"

sudo rm -rf "${INSTALLROOT}"
sudo dnf install \
  --assumeyes \
  --disablerepo="*" \
  --enablerepo="omv*" \
  --installroot="${INSTALLROOT}" \
  --nodocs \
  --nogpgcheck \
  --refresh \
  --releasever="${VERSION}" \
  --repofrompath 'omv-release,http://mirror.openmandriva.org/$releasever/repository/x86_64/main/release/' \
  --repofrompath 'omv-updates,http://mirror.openmandriva.org/$releasever/repository/x86_64/main/updates/' \
   bash curl dnf vim

sudo tar -C "${INSTALLROOT}" -c . >"${TAR}"
sudo rm -rf "${INSTALLROOT}"

docker rmi -f "${IMAGE}"
docker import "${TAR}" "${IMAGE}"
