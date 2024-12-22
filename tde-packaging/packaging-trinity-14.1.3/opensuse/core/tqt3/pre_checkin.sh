#!/bin/bash
# This script is called automatically during autobuild checkin.

cp -fl qt3.changes qt3-extensions.changes
cp -fl qt3.changes qt3-devel-doc.changes

for spec in qt3-extensions.spec qt3-devel-doc.spec; do 
{ sed -n -e '1,/COMMON-BEGIN/p' $spec.in
  sed -n -e '/COMMON-BEGIN/,/COMMON-END/p' qt3.spec
  sed -n -e '/COMMON-END/,$p' $spec.in; } > $spec.tmp && perl update_spec.pl $spec.tmp attributes > $spec && rm $spec.tmp
done


osc service localrun format_spec_file
