#!/bin/bash -ex

DISTRIB="$1"
TDE_VERSION="$2"
ARCH="$3"

[ -z "${TDE_VERSION}" ] && TDE_VERSION="14.1.2"
[ -z "${ARCH}" ] && ARCH="x86_64"

IMAGE="trinity.${DISTRIB}.${ARCH}:${TDE_VERSION}"

docker pull "docker:5000/${IMAGE}"
