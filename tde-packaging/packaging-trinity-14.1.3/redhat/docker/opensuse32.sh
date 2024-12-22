#!/bin/bash -e

if [ "$(whoami)" != "root" ]; then
  sudo exec $0 $@
fi

VERSION="$1" # E.g: '42.3'

if [ "${VERSION}" = "tumbleweed" ]; then
  URL="https://download.opensuse.org/ports/i586/tumbleweed"
  NAME="opensuse32/tumbleweed"
else
  URL="http://download.opensuse.org/distribution/leap/${VERSION}"
  NAME="opensuse32/leap"
fi

IMAGE="${NAME}:latest"
INSTALLROOT="/dev/shm/${IMAGE}"

[ -x /usr/bin/pigz ] && GZIP=pigz || GZIP=gzip

for dir in dev proc sys; do
  if [ -d "${INSTALLROOT}/${dir}" ]; then
    umount "${INSTALLROOT}/${dir}"
  fi
done

rm -rf "${INSTALLROOT}"
mkdir -p "${INSTALLROOT}"

for dir in dev proc sys; do
  mkdir -p "${INSTALLROOT}/${dir}"
  mount --bind "/${dir}" "${INSTALLROOT}/${dir}"
done

zypper --root "${INSTALLROOT}" \
  ar "${URL}/repo/oss/" "oss"
zypper --root "${INSTALLROOT}" \
  ar "${URL}/repo/non-oss/" "non-oss"

if [ "${VERSION}" != "tumbleweed" ]; then
  zypper --root "${INSTALLROOT}" \
    ar "http://download.opensuse.org/update/leap/${VERSION}/oss/" "update-oss"
  zypper --root "${INSTALLROOT}" \
    ar "http://download.opensuse.org/update/leap/${VERSION}/non-oss/" "update-non-oss"
fi
zypper --root "${INSTALLROOT}" \
  --gpg-auto-import-keys ref
setarch i686 zypper --root "${INSTALLROOT}"  \
  install --download-only -y \
  bash \
  ca-certificates \
  curl \
  docbook-utils \
  filesystem \
  gawk \
  glibc \
  glibc-extra \
  grep \
  gzip \
  libpcre1 \
  libselinux1 \
  openSUSE-release \
  system-user-root \
  util-linux vim \
  xz \
  zlib \
  zypper
rpm -Uvh --root "${INSTALLROOT}" "${INSTALLROOT}/var/cache/zypp/packages/oss/"*"/"*".rpm"

chroot "${INSTALLROOT}" rpmdb --rebuilddb

for dir in dev proc sys; do
  umount "${INSTALLROOT}/${dir}"
done

rm -rfv "${INSTALLROOT}/var/cache/zypp/packages/"*

FILE="${IMAGE//\//_}.tar"
tar -C "${INSTALLROOT}" -c . >"${FILE}"
rm -rf "${INSTALLROOT}"

docker rmi -f "${IMAGE}"
docker import "${FILE}" "${IMAGE}"

${GZIP} "${FILE}"
mkdir -p "/home/${SUDO_USER}/tde/docker"
mv -fv "${FILE}.gz" "/home/${SUDO_USER}/tde/docker"
