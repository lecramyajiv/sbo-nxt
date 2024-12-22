#!/usr/bin/env perl

use strict;
use warnings;

my $version = `cmake --version | awk '/^cmake version/ {print \$3}' | tr -d '\n'`;
my ($version3, $version3_next);
my ($version2, $version2_next);

($version3 = $version)  =~ s/^(([^.]+\.){2}[^.+~-]+)[.+~-]?[^-]*-[^-]+$/$1/;
($version2 = $version3) =~ s/\.[^.]+$//;

($version3_next = $version3) =~ s/(?<=\.)(\d+)[a-z]?$/($1+1)/e;
($version2_next = $version2) =~ s/(?<=\.)(\d+)$/($1+1)/e;

print "CMake-Version3=$version3\n";
print "CMake-Version2=$version2\n";
print "CMake-Next-Version3=$version3_next\n";
print "CMake-Next-Version2=$version2_next\n";
