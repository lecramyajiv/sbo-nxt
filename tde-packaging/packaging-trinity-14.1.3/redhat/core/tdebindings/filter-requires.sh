#!/bin/sh

if [ -x /usr/lib/rpm/redhat/find-requires ] ; then
FINDREQ=/usr/lib/rpm/redhat/find-requires
else
FINDREQ=/usr/lib/rpm/find-requires
fi

$FINDREQ $* | sed -e '/libcairo.so.2/d' -e '/libpangocairo-1.0.so.0/d'
