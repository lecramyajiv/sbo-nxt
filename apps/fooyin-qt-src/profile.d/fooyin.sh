 #!/bin/bash

if [ -d /usr/lib@LIBDIRSUFFIX@/fooyin ]; then
   export l=${l:-/usr/lib@LIBDIRSUFFIX@/fooyin}
   export l1=${l1:-$l/plugins}
   export l2=${l2:-/usr/lib@LIBDIRSUFFIX@/cmake/fooyin}
   export l3=${l3:-$l2/modules}
fi

export PATH=$PATH:$l:$l1:$l2:$l3
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$l:$l1:$l2:$l3
