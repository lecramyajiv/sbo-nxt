#!/bin/sh

export TDE_DIR=/opt/trinity
export BIN_DIR=$TDE_DIR/bin
export INC_DIR=$TDE_DIR/include
export PR_INC_DIR=$TDE_DIR/include/private
export SYSCONFDIR=$prefix/etc
export MANDIR=$prefix/man
export sbindir=$prefix/sbin
export datadir=$prefix/share
export libexecdir=$prefix/libexec


if [ -d $TDE_DIR/lib@LIBDIRSUFFIX@/ ]; then
  LIBDIR=$TDE_DIR/lib@LIBDIRSUFFIX@
  LIBDIR1=$LIBDIR/plugins
  LIBDIR2=$LIBDIR/tqt
fi

export PATH=$TDE_DIR:$BIN_DIR:$INC_DIR:$PR_INC_DIR:$SYSCONFDIR:$LIBDIR:$LIBDIR1:$LIBDIR2:$MANDIR:$sbindir:$datadir:$libexecdir:$PATH
export LD_LIBRARY_PATH="$TDE_LID_DIR:${LD_LIBRARY_PATH}"
export PKG_CONFIG_PATH=$LIBDIR/pkgconfig:$PKG_CONFIG_PATH
