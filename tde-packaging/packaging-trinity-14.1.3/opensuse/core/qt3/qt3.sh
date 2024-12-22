case ":${PATH}:" in
  *:/usr/lib/qt3/bin:*) ;;
  *) PATH=$PATH:/usr/lib/qt3/bin
esac
QTDIR=/usr/lib/qt3
export QTDIR
