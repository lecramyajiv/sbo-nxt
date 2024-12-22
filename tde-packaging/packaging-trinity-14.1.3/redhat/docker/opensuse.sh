#!/bin/bash

NAME="opensuse"
VERSION="$1" # E.g: '42.3'
IMAGE="${NAME}:${VERSION}"
INSTALLROOT="/dev/shm/${IMAGE}"

sudo rm -rf "${INSTALLROOT}"
sudo mkdir -p "${INSTALLROOT}"

sudo zypper --root "${INSTALLROOT}" \
  ar "http://download.opensuse.org/distribution/leap/${VERSION}/repo/oss/" "oss"
sudo zypper --root "${INSTALLROOT}" \
  ar "http://download.opensuse.org/distribution/leap/${VERSION}/repo/non-oss/" "non-oss"
sudo zypper --root "${INSTALLROOT}" \
  ar "http://download.opensuse.org/update/leap/${VERSION}/oss/" "update-oss"
sudo zypper --root "${INSTALLROOT}" \
  ar "http://download.opensuse.org/update/leap/${VERSION}/non-oss/" "update-non-oss"
sudo zypper --root "${INSTALLROOT}" \
  --gpg-auto-import-keys ref
sudo zypper --root "${INSTALLROOT}" \
  install -y bash vim zypper openSUSE-release

sudo tar -C "${INSTALLROOT}" -c . >"${IMAGE}.tar"
sudo rm -rf "${INSTALLROOT}"

docker rmi -f "${IMAGE}"
docker import "${IMAGE}.tar" "${IMAGE}"
