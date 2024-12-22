#!/bin/bash

DISTRIB="$1"
TDE_VERSION="$2"
ARCH="$3"

[ -z "${TDE_VERSION}" ] && TDE_VERSION="14.1.2"
[ -z "${ARCH}" ] && ARCH="x86_64"
[ -x /usr/bin/podman ] && DOCKER=podman || DOCKER=docker

IMAGE="trinity.${DISTRIB}.${ARCH}:${TDE_VERSION}"
DIST="$(sed -n ${DISTRIB}/rpmmacros -e "/%dist/ s|.* ||p")"
if [ "${DIST}" = "%nil" ]; then DIST=".${DISTRIB}"; fi

mkdir -p "${HOME}/rpmbuild/RPMS/RPMS${DIST}.tde-${TDE_VERSION}"
mkdir -p "${HOME}/rpmbuild/SRPMS/SRPMS${DIST}.tde-${TDE_VERSION}"
mkdir -p "/dev/shm/${DOCKER}"
chmod 777 "${HOME}/rpmbuild/RPMS/RPMS${DIST}.tde-${TDE_VERSION}" "${HOME}/rpmbuild/SRPMS/SRPMS${DIST}.tde-${TDE_VERSION}"

case "${TDE_VERSION}" in
  "14.0."*) TDE_BRANCH="r14.0.x";;
  "14.1."*) TDE_BRANCH="r14.1.x";;
  *) TDE_BRANCH="master";;
esac

mkdir -p "${HOME}/rpmbuild/RPMS/RPMS${DIST}.tde-${TDE_VERSION}" "${HOME}/rpmbuild/SRPMS/SRPMS${DIST}.tde-${TDE_VERSION}"

${DOCKER} run -ti --rm \
  -h "${IMAGE}" \
  --name "${IMAGE//:/-}" \
  -v /dev/shm/${DOCKER}:/tmp:z \
  -u trinity \
  -e TMPPATH=/tmp \
  -e TDE_VERSION=${TDE_VERSION} \
  -e TDE_BRANCH=${TDE_BRANCH} \
  -w /home/trinity/tde/${TDE_BRANCH}/tde/packaging/redhat \
  -v ${HOME}/.gnupg:/home/trinity/.gnupg \
  -v ${HOME}/tde/3rdparty:/home/trinity/tde/3rdparty \
  -v ${HOME}/tde/master:/home/trinity/tde/master \
  -v ${HOME}/tde/r14.0.x:/home/trinity/tde/r14.0.x \
  -v ${HOME}/tde/r14.1.x:/home/trinity/tde/r14.1.x \
  -v ${HOME}/tde/patches:/home/trinity/tde/patches \
  -v ${HOME}/tde/tarballs:/home/trinity/tde/tarballs \
  -v ${HOME}/rpmbuild/RPMS/RPMS${DIST}.tde-${TDE_VERSION}:/home/trinity/rpmbuild/RPMS.tde-${TDE_VERSION} \
  -v ${HOME}/rpmbuild/SRPMS/SRPMS${DIST}.tde-${TDE_VERSION}:/home/trinity/rpmbuild/SRPMS.tde-${TDE_VERSION} \
  "${IMAGE}" setarch ${ARCH} bash
