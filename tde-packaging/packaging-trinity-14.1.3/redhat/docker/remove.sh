#!/bin/bash -ex

DISTRIB="$1"
TDE_VERSION="$2"
ARCH="$3"

[ -z "${TDE_VERSION}" ] && TDE_VERSION="14.1.2"
[ -z "${ARCH}" ] && ARCH="x86_64"
[ -x /usr/bin/podman ] && DOCKER=podman || DOCKER=docker

IMAGE="trinity.${DISTRIB}.${ARCH}:${TDE_VERSION}"
FILE="${HOME}/tde/docker/${IMAGE}.tar.gz"

${DOCKER} rmi -f "${IMAGE}"
rm -f "${FILE}"
