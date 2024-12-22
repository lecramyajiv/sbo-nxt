#!/bin/sh

export TDE_DIR=/opt/trinity
export BIN_DIR=$TDE_DIR/bin
export INC_DIR=$TDE_DIR/include
export PR_INC_DIR=$TDE_DIR/include/private
export PLUGIN_DIR=$TDE_DIR/plugins

if [ -d $TDE_DIR/lib@LIBDIRSUFFIX@/ ]; then
  TDE_LID_DIR=$TDE_DIR/lib@LIBDIRSUFFIX@
fi

export PATH=$PATH:$TDE_DIR:$BIN_DIR:$INC_DIR:$PR_INC_DIR:$PLUGIN_DIR:$TDE_LID_DIR
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:$TDE_LID_DIR"
