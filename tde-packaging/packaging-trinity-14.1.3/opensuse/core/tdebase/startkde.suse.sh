
#
# do we run in a prelinked system ?
#
if test -f /etc/sysconfig/prelink; then
. /etc/sysconfig/prelink
  if test "$USE_PRELINK" = "yes" ; then
     KDE_IS_PRELINKED=1
     export KDE_IS_PRELINKED
  else
     unset KDE_IS_PRELINKED
  fi
fi

#
# Do we have a special Gtk theming for our Qt widget theme ?
#
if [ ! -e $HOME/.no-qtrc-to-gtkrc-mapping ]; then

  SUSE_VERSION="`cat /etc/SuSE-release | sed -n 's/VERSION = //p'`"

    # Defaults for SuSE 9.0
    GTK2_SYSCONFDIR=/etc/opt/gnome
    GTK2_DATADIR=/opt/gnome/share/themes/

  # use general gtk-qt-engine
  if [ -e "$GTK2_DATADIR/Qt/gtk-2.0/gtkrc" ] ; then
    GTK2_THEME_RC="$GTK2_DATADIR/Qt/gtk-2.0/gtkrc"
  fi

  # GTK2
  # NOTE: ~/.gtkrc-2.0-kde is added later (in latest KDE only)
  if [ "$GTK2_RC_FILES" ]; then
    export GTK2_RC_FILES="$GTK2_RC_FILES:$GTK2_THEME_RC:$HOME/.gtkrc-2.0-qtengine:$HOME/.gtkrc-2.0"
  else
    export GTK2_RC_FILES="$GTK2_SYSCONFDIR/gtk-2.0/gtkrc:$GTK2_THEME_RC:$HOME/.gtkrc-2.0-qtengine:$HOME/.gtkrc-2.0"
  fi

fi

#
# use optimized libs, if your CPU has the needed support
# (kdemultimedia package has some SSE optimized libs)
[ -z "$LD_HWCAP_MASK" ]    && export LD_HWCAP_MASK=0x20000000

if [ -r /etc/sysconfig/windowmanager ]; then
  # Do the user want the SuSE theme ?
  source /etc/sysconfig/windowmanager

  # Should we really enable FAM support for KDE ?
  export USE_FAM="$KDE_USE_FAM"

  # Disable IPv6 ?
  if [ "$KDE_USE_IPV6" = "no" ]; then
     export KDE_NO_IPV6=1
  fi
  # Disable IDN ?
  if [ "$KDE_USE_IDN" = "no" ]; then
     export KDE_NO_IDN=1
  fi

else
  if [ -r /etc/rc.config ]; then
    # Do the user want the SuSE theme ?
    INSTALL_DESKTOP_EXTENSIONS=`bash -c "source /etc/rc.config && echo \\$INSTALL_DESKTOP_EXTENSIONS"`

    # Should we really enable FAM support for KDE ?
    USE_FAM=`bash -c "source /etc/rc.config && echo \\$KDE_USE_FAM"`
    export USE_FAM
  fi
fi

#
# create SuSE defaults
#
if [ "$INSTALL_DESKTOP_EXTENSIONS" == "yes" ]; then
  if [ -x /opt/kde3/bin/kde-open ]; then
     export DESKTOP_LAUNCH=kde-open
  fi
  if [ "$USER" == "root" ]; then
     if [ ! -e "$HOME/.skel/kdebase3" -a ! -e "$KDEHOME/share/config/kdeglobals" ]; then
        if [ -e "/opt/kde3/bin/startkde.theme.unitedlinux" ]; then
           . /opt/kde3/bin/startkde.theme.unitedlinux
           copy_default_root_ul "$KDEHOME"
           create_default_desktop_ul "$HOME/Desktop/"
        fi

        if [ -e "/opt/kde3/bin/startkde.theme" ]; then
           . /opt/kde3/bin/startkde.theme
        fi
        copy_default_root "$KDEHOME"
        create_default_desktop "$HOME/Desktop/"
        mkdir -p $HOME/.skel/
        touch $HOME/.skel/kdebase3 $HOME/.skel/kdebase3.91
     fi
  else
     if [ ! -e "$HOME/.skel/kdebase3" -a ! -e "$KDEHOME/share/config/kdeglobals" ]; then
        if [ -e "/opt/kde3/bin/startkde.theme.unitedlinux" ]; then
           . /opt/kde3/bin/startkde.theme.unitedlinux
           copy_default_user_ul "$KDEHOME"
           create_default_desktop_ul "$HOME/Desktop/"
        fi

        if [ -e "/opt/kde3/bin/startkde.theme" ]; then
          . /opt/kde3/bin/startkde.theme
        fi
        copy_default_user "$KDEHOME"
        create_default_desktop "$HOME/Desktop/"
        mkdir -p $HOME/.skel/
        touch $HOME/.skel/kdebase3 $HOME/.skel/kdebase3.91
     fi
  fi
  if [ -e /opt/kde3/bin/startkde.update93 -a ! -e "$HOME/.skel/kdebase3.93" ]; then
     . /opt/kde3/bin/startkde.update93
     mkdir -p $HOME/.skel/
     touch $HOME/.skel/kdebase3.93
  fi
  for i in /opt/kde3/share/UnitedLinux/addon-scripts/*; do
    [ -r "$i" ] && \
     . "$i"
  done
fi

# check if any rpms have been (un)installed since ksycoca
# had been built, if yes, trigger ksycoca rebuild immediatelly
# instead of delayed

kdehome=$HOME/.kde
test -n "$KDEHOME" && kdehome=`echo "$KDEHOME"|sed "s,^~/,$HOME/,"`
host=$HOSTNAME
test -n "$XAUTHLOCALHOSTNAME" && host=$XAUTHLOCALHOSTNAME
ksycoca="$kdehome/cache-$host/ksycoca"

if test -f "$ksycoca"; then
    if test -f /var/lib/rpm/Packages; then
	if test /var/lib/rpm/Packages -nt "$ksycoca"; then
	    rm -f "$ksycoca"
	fi
    fi
fi
