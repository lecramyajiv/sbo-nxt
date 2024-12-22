#!/bin/bash -ex

[ "$(whoami)" = "root" ] || exec sudo $0 $@
[ "$(rpm -E %_arch)" = "x86_64" ] && exec setarch i686 $0 $@

cd "$(dirname "$0")"

NAME="centos32"
VERSION="$1" # E.g: '5'
IMAGE="${NAME}:${VERSION}"
INSTALLROOT="/dev/shm/${IMAGE}"
DIR="el${VERSION}"

REPO="centos-${VERSION}"

# Installation minimale de la distribution
rm -rf "${INSTALLROOT}"
install -m 644 "${DIR}/${REPO}.repo" "/etc/yum.repos.d"
yum install --disablerepo="*" --enablerepo="${REPO}*" --nogpgcheck --releasever="${VERSION}" -y  --installroot "${INSTALLROOT}" libselinux yum yum-plugin-ovl
rm -f "/etc/yum.repos.d/${REPO}.repo"
touch "${INSTALLROOT}/etc/fstab" "${INSTALLROOT}/etc/mtab"

# Activation des dépôts YUM de l'atelier DEPL-IT (remplace les dépôts Internet)
rm -f "${INSTALLROOT}/etc/yum.repos.d/"*".repo"
install -m 644 "${DIR}/${REPO}.repo" "${INSTALLROOT}/etc/yum.repos.d"
install -m 644 "/etc/resolv.conf" "${INSTALLROOT}/etc/resolv.conf"
rm -f "${INSTALLROOT}/etc/group" "${INSTALLROOT}/etc/passwd" "${INSTALLROOT}/etc/pam.d/system-auth" "${INSTALLROOT}/usr/share/info/dir"

# Ré-installation de la distribution en utilisant le "yum" intégré
rm -rf "${INSTALLROOT}/var/lib/rpm/"*
install -m 644 "${DIR}/"{epel,repoforge}*".repo" "${INSTALLROOT}/etc/yum.repos.d"
cp -a "/dev/urandom" "${INSTALLROOT}/dev/urandom"
chroot "${INSTALLROOT}" yum install --nogpgcheck -y $(<${DIR}/packages.base)
find "${INSTALLROOT}" -name "*.rpmnew" -delete

# Création de l'image Tar
tar -C "${INSTALLROOT}" -c . >"${IMAGE}.tar"
rm -rf "${INSTALLROOT}"

# Création de l'image Docker
if [ "$(docker images -q "${IMAGE}")" != "" ]; then
  docker rmi -f "${IMAGE}"
fi
docker import "${IMAGE}.tar" "${IMAGE}"

# Test de l'image
docker run "${IMAGE}" yum repolist


exit 0
