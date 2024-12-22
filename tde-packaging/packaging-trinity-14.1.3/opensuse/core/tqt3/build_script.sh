
function fix_qconfig_h {
   mv include/qconfig.h include/qconfig.h.orig
   sed -e '1i\
#ifndef SuSE_QCONFIG_ALREADY_INCLUDED \
#define SuSE_QCONFIG_ALREADY_INCLUDED 1 \
#define PLUGIN_PATH_EXTENSION "'$PLUGIN_PATH'" \
 ' -e s@${RPM_BUILD_ROOT}@/@ -e '$a\
#endif' include/qconfig.h.orig \
   > include/qconfig.h
  
}

function call_configure {
  EXTRA_OPTIONS=$@
  OPENGL="-dlopen-opengl"
  case $EXTRA_OPTIONS in
     *-static*)
       OPENGL="-no-dlopen-opengl"
       ;;
       *)
       ;;
  esac

  [ "$WLIB" == "lib64" ] && PLATFORM=linux-g++-64 || PLATFORM=linux-g++
  LARGEFILE="-largefile"
  XCURSOR="-xcursor"
  XFT="-xft -xrender -I/usr/include/freetype2/ "
  [ -e /usr/$WLIB/libmng.so ] && LIBMNG="-system-libmng -plugin-imgfmt-mng" || LIBMNG="-qt-libmng "
  PGSQL="-plugin-sql-psql -I/usr/include -I/usr/include/pgsql/ -I/usr/include/pgsql/server"
  ODBC="-plugin-sql-odbc"

  if [ -f /.buildenv ] && grep -q BUILD_BASENAME=beta- /.buildenv ; then 
     export NO_BRP_STRIP_DEBUG=true
     export DEBUG="-debug"
  else
     export DEBUG="-release"
  fi

  PREFIX=/usr/lib/qt3/
  export LD_LIBRARY_PATH="/${PWD}/lib/"
  ORACLE="/opt/oracle/product/8.1.6/rdbms/demo/"
  [ -d $ORACLE ] && \
    ORACLE="-plugin-sql-oci -I$ORACLE" || \
    ORACLE=""

  for i in mkspecs/linux-*/qmake.conf ; do
    sed \
-e "s,QMAKE_CFLAGS_RELEASE[\t ]*=.*,QMAKE_CFLAGS_RELEASE    = $RPM_OPT_FLAGS," \
-e "s,QMAKE_CFLAGS[\t ]*=.*,QMAKE_CFLAGS            = -pipe $RPM_OPT_FLAGS," \
-e "s,QMAKE_INCDIR[\t ]*=.*,QMAKE_INCDIR            = /usr/include/," \
-e "s,QMAKE_LIBDIR[\t ]*=.*,QMAKE_LIBDIR            = /usr/$WLIB/," \
-e "s,QMAKE_LIBDIR_X11[\t ]*=.*,QMAKE_LIBDIR_X11        = /usr/X11R6/$WLIB/," \
-e "s,QMAKE_LIBDIR_QT[\t ]*=.*,QMAKE_LIBDIR_QT         = \$(QTDIR)/$WLIB/," \
-e "s,QMAKE_INCDIR_OPENGL[\t ]*=.*,QMAKE_INCDIR_OPENGL     = /usr/include/," \
-e "s,QMAKE_LIBDIR_OPENGL[\t ]*=.*,QMAKE_LIBDIR_OPENGL     = /usr/$WLIB/," \
        $i > ${i}.new &&\
    mv ${i}.new $i
  done
  sed -e "s/^CXXFLAGS=/CXXFLAGS= $RPM_OPT_FLAGS/" < qmake/Makefile.unix > qmake/Makefile.unix.tmp && mv qmake/Makefile.unix.tmp qmake/Makefile.unix
#  ld -Bsymbolic-functions -v >& /dev/null && perl -pi -e 's/^QMAKE_VARS=$/QMAKE_VARS="QMAKE_LFLAGS=-Wl,-Bdirect QMAKE_LFLAGS+=-Wl,-Bsymbolic-functions"/' configure

# png is direct linked, other picture formats are loaded at runtime
  OPTIONS="-platform $PLATFORM -qt-gif -stl $DEBUG \
	   -system-zlib -system-libjpeg -system-libpng \
           -plugin-imgfmt-jpeg -inputmethod \
           -nis -cups -ipv6 $OPENGL \
	   -xkb $LIBMNG -no-g++-exceptions $LARGEFILE $XCURSOR \
           $XFT $XINERAMA -sm -L/usr/$WLIB -L/usr/X11R6/$WLIB \
           -plugin-sql-mysql -I/usr/include/mysql/ \
           -tablet $ORACLE $PGSQL $ODBC -plugin-sql-sqlite $NEWABI \
    	   -prefix $PREFIX -libdir $PREFIX/$WLIB"

# use styles as plugins, beside platinum. leave windowsxp disabled
# nice idea, but too many dumb apps have a hardcoded style list :(
#  for i in plugins/src/styles/* ; do
#     if [ -d $i -a ${i##*/} != "platinum" -a ${i##*/} != "windowsxp" ]
#        then OPTIONS="$OPTIONS -plugin-style-${i##*/}"
#     fi
#  done

  [ -e /usr/$WLIB/mysql/ ] && OPTIONS="$OPTIONS -L/usr/$WLIB/mysql/"

# get sure we use the lib from the system
  rm -rf src/3rdparty/{libjpeg,libmng,libpng,sqlite,zlib}

  export PATH=$PWD/bin:$PATH
  echo yes|./configure $OPTIONS $EXTRA_OPTIONS

# make sure we don't have a crippled qt
  cp -v include/qconfig-dist.h include/qconfig.h
  #grep -q "full-config\"" include/qconfig.h || { echo "build key is wrong"; exit 42; }
}

function post_install {
  if echo $RPM_OPT_FLAGS | grep -q -- -g ; then 
     export NO_BRP_STRIP_DEBUG=true
  fi
}

