#!/bin/sh

BUILDDIR=$PWD
export QTDIR=/usr/share/tqt3

# first copy over the libtqt-mt.so build configuration of .qmake.cache
cp /usr/share/tqt3/.qmake.cache ./.qmake.cache

# Now compile the examples. The themes example
# won't work since ntqconfig.h is not really correct with the
# ifdef's for the TQT_NO_xyz_STYLE, so we use make -k to continue
cd examples; qmake -o Makefile examples.pro; make -k

# Now compile the tutorial.
cd $BUILDDIR/tutorial; qmake -o Makefile tutorial.pro; make

# Then the designer examples. 
cd $BUILDDIR/tools/designer/examples
for a in `find . -type d -maxdepth 1 -mindepth 1`; do
        cd $a && qmake -o Makefile $a.pro; make; cd ..;
done

# There is a bigger sql example in book/ with more subdirectories:
cd book
for a in `find . -type d -maxdepth 1 -mindepth 1`; do
        cd $a && qmake -o Makefile $a.pro; make; cd ..;
done

# Finally, build the linguist tutorials:
cd $BUILDDIR/tools/linguist/tutorial
for a in `find . -type d -maxdepth 1 -mindepth 1`; do 
	cd $a && qmake -o Makefile $a.pro; make; cd ..; 
done

# Return to the build directory
cd $BUILDDIR 
