#!/bin/bash

if [ ! "$(grep /opt/trinity/lib@LIBDIRSUFFIX@ /etc/ld.so.conf)" ]; then
  echo "/opt/trinity/lib@LIBDIRSUFFIX@" >> /etc/ld.so.conf
fi
