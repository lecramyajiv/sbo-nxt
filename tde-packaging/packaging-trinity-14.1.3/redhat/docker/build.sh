#!/bin/bash -e

DISTRIB="$1"
TDE_VERSION="$2"
ARCH="$3"

[ -z "${TDE_VERSION}" ] && TDE_VERSION="14.1.2"
[ -z "${ARCH}" ] && ARCH="x86_64"
[ -x /usr/bin/podman ] && DOCKER=podman || DOCKER=docker
[ -x /usr/bin/pigz ] && GZIP=pigz || GZIP=gzip

IMAGE="trinity.${DISTRIB}.${ARCH}:${TDE_VERSION}"
FILE="${HOME}/tde/docker/${IMAGE}.tar.gz"

if [ $(${DOCKER} images -q "${IMAGE}") ]; then
  echo "Docker image '${IMAGE}' already exists."
elif [ -r "${FILE}" ]; then
  echo "Importing existing image '${FILE}'."
  zcat "${FILE}" | ${DOCKER} image load
else
  echo "Building new Docker image '${IMAGE}'."
  ${DOCKER} build -t "${IMAGE}" -f "${DISTRIB}/Dockerfile.${ARCH}" --build-arg TDE_VERSION="${TDE_VERSION}" --build-arg ARCH="${ARCH}" "${DISTRIB}"
  echo "Saving image to '${FILE}'"
  ${DOCKER} image save "${IMAGE}" | ${GZIP} >"${FILE}"
fi

# Strip 'localhost/' prefix from image tag
if ! ${DOCKER} images | while read name tag blah; do echo "${name}:${tag}"; done | grep -q "^${IMAGE}$"; then
  ${DOCKER} image tag "localhost/${IMAGE}" "${IMAGE}"
  #${DOCKER} image remove "localhost/${IMAGE}"
fi
