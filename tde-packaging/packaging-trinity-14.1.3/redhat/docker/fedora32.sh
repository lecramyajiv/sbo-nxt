#!/bin/bash

NAME="fedora32"
VERSION="$1" # E.g: '26'
IMAGE="${NAME}:${VERSION}"
INSTALLROOT="/dev/shm/${IMAGE}"

sudo rm -rf "${INSTALLROOT}"
setarch i686 sudo dnf install \
  --refresh \
  --installroot="${INSTALLROOT}" \
  --releasever="${VERSION}" \
  --disablerepo="*" --enablerepo="fedora,updates" \
  --nodocs \
  --assumeyes \
  @core bash vim yum-plugin-ovl

sudo sed -i "${INSTALLROOT}/etc/yum.repos.d/"*".repo" \
         -e "s|\$basearch|i386|g" \
         -e "s|\$releasever|${VERSION}|g"

sudo tar -C "${INSTALLROOT}" -c . >"${IMAGE}.tar"
sudo rm -rf "${INSTALLROOT}"

docker rmi -f "${IMAGE}"
docker import "${IMAGE}.tar" "${IMAGE}"
