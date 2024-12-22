#!/bin/bash

TDE_VERSION="${1:-${TDE_VERSION:-14.1.2}}"
ARCH=$(rpm -E %_target_cpu)
RPMDIR=$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})

[ -d "${RPMDIR}/noarch" ] || mkdir -p "${RPMDIR}/noarch"
[ -d "${RPMDIR}/${ARCH}" ] || mkdir -p "${RPMDIR}/${ARCH}"

# RHEL / CentOS / Fedora
if [ -x "/usr/bin/dnf" ] || [ -x "/usr/bin/yum" ]; then
  cat <<EOF >/tmp/rpmbuild-tde.repo
[rpmbuild.${ARCH}]
name=rpmbuild.${ARCH}
baseurl=file://${RPMDIR}/${ARCH}
enabled=1
gpgcheck=0

[rpmbuild.noarch]
name=rpmbuild.noarch
baseurl=file://${RPMDIR}/noarch
enabled=1
gpgcheck=0
EOF
  sudo mv -f /tmp/rpmbuild-tde.repo /etc/yum.repos.d/
fi

# Mageia / Mandriva
if [ -x "/usr/sbin/urpmi" ]; then
  sudo urpmi.removemedia -y "rpmbuild"
  sudo urpmi.addmedia "rpmbuild.${ARCH}" "${RPMDIR}/${ARCH}"
  sudo urpmi.addmedia "rpmbuild.noarch" "${RPMDIR}/noarch"
fi

# openSUSE
if [ -x /usr/bin/zypper ]; then
  sudo rm -f "/etc/zypp/repos.d/rpmbuild"*
  sudo zypper ar -G "${RPMDIR}/${ARCH}" "rpmbuild.${ARCH}"
  sudo zypper ar -G "${RPMDIR}/noarch" "rpmbuild.noarch"
fi

# PCLOS
if [ -x "/usr/bin/apt-get" ]; then
  [ ! -L "${RPMDIR}/RPMS.${ARCH}" ] && ln -sf "${ARCH}" "${RPMDIR}/RPMS.${ARCH}"
  [ ! -L "${RPMDIR}/RPMS.noarch" ] && ln -sf "noarch" "${RPMDIR}/RPMS.noarch"
  echo "rpm file:${RPMDIR%/*} ${RPMDIR##*/} ${ARCH} noarch" | sudo tee "/etc/apt/sources.list.d/rpmbuild.list"
fi
