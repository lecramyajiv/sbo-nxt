#!/bin/bash

WORKERS=$(getconf _NPROCESSORS_ONLN)
TDE_VERSION="${2:-${TDE_VERSION:-14.1.2}}"

LOCKFILE="/tmp/lock.${0##*/}"
while [ -e "${LOCKFILE}" ]; do
  echo "Waiting for lock file '${LOCKFILE}' to vanish."
  sleep 3
done

ARCH="$(rpm -E %{_target_cpu})"
RPMDIR=$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})
DIST="$(rpmdist.sh --dist)"

[ -d "${RPMDIR}/noarch" ] || mkdir -p "${RPMDIR}/noarch"
[ -d "${RPMDIR}/${ARCH}" ] || mkdir -p "${RPMDIR}/${ARCH}"

if [ -x "/usr/bin/createrepo_c" ]; then
  createrepo="/usr/bin/createrepo_c"
else
  createrepo="/usr/bin/createrepo"
fi

if [ -x /usr/sbin/urpmi ]; then
  REPOUPDATE='(cd ${RPMDIR}; genhdlist2 --clean --allow-empty noarch & genhdlist2 --clean --allow-empty ${ARCH} & wait; sudo urpmi.update rpmbuild.${ARCH} rpmbuild.noarch)'
elif [ -x /usr/bin/dnf ]; then
  REPOUPDATE='(cd ${RPMDIR}; ${createrepo} --workers=${WORKERS} ${ARCH} & ${createrepo} --workers=${WORKERS} noarch & wait; sudo dnf --repo="rpmbuild*" clean expire-cache)'
elif [ -x /usr/bin/zypper ]; then
  REPOUPDATE='(cd ${RPMDIR}; ${createrepo} --workers=${WORKERS} ${ARCH} & ${createrepo} --workers=${WORKERS} noarch & wait; sudo zypper refresh rpmbuild.${ARCH} rpmbuild.noarch)'
  #REPOUPDATE='(rsync -av ${RPMDIR}/ /tmp/rpm${DIST}/ && cd /tmp/rpm${DIST}; umask 0000; ${createrepo} --workers=${WORKERS} ${ARCH} & ${createrepo} --workers=${WORKERS} noarch & wait; rsync -av /tmp/rpm${DIST}/ ${RPMDIR}/; sudo zypper refresh rpmbuild.${ARCH} rpmbuild.noarch)'
elif [ -x /usr/bin/yum ]; then
  if [ "${DIST}" = ".el5" ]; then
    REPOUPDATE='(cd ${RPMDIR}; ${createrepo} ${ARCH} & ${createrepo} noarch & wait; sudo yum clean metadata --disablerepo="*" --enablerepo="rpmbuild*")'
  else
    REPOUPDATE='(cd ${RPMDIR}; ${createrepo} --workers=${WORKERS} ${ARCH} & ${createrepo} --workers=${WORKERS} noarch & wait; sudo yum clean metadata --disablerepo="*" --enablerepo="rpmbuild*")'
  fi
elif [ -x /usr/bin/apt-get ]; then
  REPOUPDATE='(cd ${RPMDIR}; genpkglist $PWD noarch & genpkglist $PWD ${ARCH} & wait; genbasedir --topdir=$PWD i586 x86_64 noarch; sudo apt-get update)'
fi

eval "${REPOUPDATE}; rm -f ${LOCKFILE}" || exit 1
