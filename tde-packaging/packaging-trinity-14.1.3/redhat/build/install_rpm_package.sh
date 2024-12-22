#!/bin/bash

LOCKFILE="/tmp/lock.${0##*/}"
while [ -e "${LOCKFILE}" ]; do
  echo "Waiting for lock file '${LOCKFILE}' to vanish."
  sleep 3
done

PKGNAME="${1}"

if [ -x /usr/sbin/urpmi ]; then
  PKGINST='sudo urpmi --auto --no-verify-rpm'
elif [ -x /usr/bin/dnf ]; then
  PKGINST="sudo dnf install -y --nogpgcheck"
elif [ -x /usr/bin/zypper ]; then
  PKGINST="sudo zypper install -y --allow-vendor-change"
elif [ -x /usr/bin/yum ]; then
  PKGINST='sudo yum install -y'
elif [ -x /usr/bin/apt-get ]; then
  PKGINST='sudo apt-get install -y'
fi

# Gets RPM package name and development package (if any)
RPM_PKGNAME="$(get_rpm_package_name.sh ${PKGNAME} devel)"

# Installing main package
eval ${PKGINST} ${RPM_PKGNAME} || exit 1
