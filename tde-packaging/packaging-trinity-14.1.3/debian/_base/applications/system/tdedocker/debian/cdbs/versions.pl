#!/usr/bin/env perl

use strict;
use warnings;

my $version = `dpkg-parsechangelog | awk '/^Version/ {print \$2}'`;
my ($version3, $version3_next);
my ($version2, $version2_next);

($version3 = $version)  =~ s/^(([^.]+\.){2}[^.+~-]+)[.+~-]?[^-]*-[^-]+$/$1/;
($version2 = $version3) =~ s/\.[^.]+$//;

($version3_next = $version3) =~ s/(?<=\.)(\d+)[a-z]?$/($1+1)/e;
($version2_next = $version2) =~ s/(?<=\.)(\d+)$/($1+1)/e;

print "KDE-Version3=$version3\n";
print "KDE-Version2=$version2\n";
print "KDE-Next-Version3=$version3_next\n";
print "KDE-Next-Version2=$version2_next\n";
