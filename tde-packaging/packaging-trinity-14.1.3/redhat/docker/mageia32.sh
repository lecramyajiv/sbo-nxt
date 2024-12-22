#!/bin/bash

NAME="mageia32"
VERSION="$1" # E.g: '26'
IMAGE="${NAME}:${VERSION}"
TAR="${NAME}-${VERSION}.tar"
INSTALLROOT="/dev/shm/${IMAGE}"

sudo rm -rf "${INSTALLROOT}"
sudo mkdir -p "${INSTALLROOT}"
setarch i686 sudo urpmi \
  --root="${INSTALLROOT}" \
  --auto \
  bash vim urpmi mageia-release-common

sudo tar -C "${INSTALLROOT}" -c . >"${TAR}"
sudo rm -rf "${INSTALLROOT}"

docker rmi -f "${IMAGE}"
docker import "${TAR}" "${IMAGE}"
