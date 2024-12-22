#!/bin/sh

export TDE_DIR=/opt/trinity
export BIN_DIR=$TDE_DIR/bin
export INC_DIR=$TDE_DIR/include
export PR_INC_DIR=$TDE_DIR/include/private
export SYSCONFDIR=$TDE_DIR/etc
export MANDIR=$TDE_DIR/man
export datadir=$TDE_DIR/share
export docdir=$TDE_DIR/doc

if [ -d $TDE_DIR/lib@LIBDIRSUFFIX@/ ]; then
  LIBDIR=$TDE_DIR/lib@LIBDIRSUFFIX@
  LIBDIR1=$LIBDIR/plugins/styles
  LIBDIR2=$LIBDIR/tqt
  L3=$LIBIDR/plugins/inputmethods
  L4=$LIBDIR/plugins/designer
  L5=$LIBDIR/plugins/crypto
  L6=$LIBDIR/trinity
  L7=$L6/plugins/styles
  L8=$L6/plugins/designer
  L9=$LIBDIR/ksquirrel-libs
  La=$LIBDIR/trinity/integrations	
fi

export PATH=$PATH:$TDE_DIR:$BIN_DIR:$INC_DIR:$PR_INC_DIR:$SYSCONFDIR:$LIBDIR:$LIBDIR1:$LIBDIR2:$MANDIR:$datadir:$docdir:$L3:$L4:$L5:$L6:$L7:$L8:$L9:$La
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIDDIR:$LIBDIR1:$LIBDIR2:$L3:$L4:$L5:$L6:$L7:$L8:$L9:$La
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:$LIBDIR/pkgconfig
export XDG_DATA_DIRS=/usr/share:$datadir
export XDG_CONFIG_DIRS=/etc/xdg:$SYSCONFDIR/xdg
export TDEHOME=~/.tde
export TDEROOTHOME=/root/.tde
