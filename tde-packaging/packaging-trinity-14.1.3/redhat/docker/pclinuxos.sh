#!/bin/bash -ex

NAME="pclinuxos"
VERSION="${1:-2024}" # E.g: '2020'
IMAGE="${NAME}:${VERSION}"
INSTALLROOT="/dev/shm/${IMAGE}"
[ -x /usr/bin/pigz ] && GZIP=pigz || GZIP=gzip

grep -qw "${INSTALLROOT}/dev" /proc/mounts && sudo umount "${INSTALLROOT}/dev"
sudo rm -rf "${INSTALLROOT}"
sudo mkdir -p "${INSTALLROOT}"

LANG=C

MIRROR="http://distrib-coffee.ipsl.jussieu.fr/pub/linux/pclinuxos/pclinuxos/apt/pclinuxos/64bit"

curl "${MIRROR}/RPMS.x86_64/" | sed -n "/a href/ s|.*href=\"\(.*\)\.rpm\".*|\1.rpm|p" >"/dev/shm/pkg.list"

mkdir -p "/dev/shm/packages"
while read pkg; do
  file="$(grep "^${pkg}-[0-9]" /dev/shm/pkg.list | sort | tail -n 1)"
  [ -z "${file}" ] && file="$(grep "^${pkg}[0-9]*-[0-9]" /dev/shm/pkg.list | sort | tail -n 1)"
  [ -z "${file}" ] && exit 1
  wget -nv -c "${MIRROR}/RPMS.x86_64/${file}" -O "/dev/shm/packages/${file}" || exit 2
done < "pclinuxos.pkg"

sudo mkdir -p "${INSTALLROOT}/dev"
sudo mount --bind "/dev" "${INSTALLROOT}/dev"

sudo mkdir -p "${INSTALLROOT}/var/lib/rpm"
sudo rpmdb --initdb --root="${INSTALLROOT}"

sudo rpm -Uvh --noscripts --nodeps --root="${INSTALLROOT}" "/dev/shm/packages/"*".rpm"

# Réinstall distro from inside chroot
sudo mount --bind "/dev/shm" "${INSTALLROOT}/dev/shm"
sudo rm -rf "${INSTALLROOT}/var/lib/rpm"
sudo chroot "${INSTALLROOT}" rpmdb --initdb
sudo chroot "${INSTALLROOT}" rpm -Uvh --nodeps "/dev/shm/packages/"*".rpm"

sudo cp "/etc/resolv.conf" "${INSTALLROOT}/etc/resolv.conf"
sudo chroot "${INSTALLROOT}" apt-get -y update
sudo chroot "${INSTALLROOT}" apt-get -y --fix-broken install
sudo chroot "${INSTALLROOT}" apt-get -y upgrade

sudo umount "${INSTALLROOT}/dev/shm"
sudo umount "${INSTALLROOT}/dev"

docker rmi -f "${IMAGE}" || :
sudo tar -C "${INSTALLROOT}" -c . | docker import - "${IMAGE}"
docker run -ti --rm "${IMAGE}" ls -l
sudo rm -rf "${INSTALLROOT}"

docker image save "${IMAGE}" | ${GZIP} -9 >"${HOME}/tde/docker/${IMAGE}.tar.gz"
