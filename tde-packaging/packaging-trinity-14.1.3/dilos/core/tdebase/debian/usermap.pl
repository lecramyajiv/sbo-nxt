#!/usr/bin/perl

# Copyright (C) 2005 Mandriva
# Olivier Blin
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

my %flags = (
    idVendor => 0x0001,
    idProduct => 0x0002,
);

sub parse_usermap_line {
    local $_ = shift;
    /^#/ and next;
    my %match;
    @match{module, match_flags, idVendor, idProduct} = 
	/^(\S+)\s+0x(\w{2,})\s+0x(\w{2,})\s+0x(\w{2,})\s+0x(\w{2,})\s+0x(\w{2,})\s+0x(\w{2})\s+0x(\w{2})\s+0x(\w{2})\s+0x(\w{2})\s+0x(\w{2})\s+0x(\w{2})(?:\s+0x(\w{2,}))?/
	or die qq(unable to parse line "$_");
    $match{match_flags} = hex($match{match_flags});
    $match{driver_info} ||= 0;

    my @rule;
    while (my ($key, $flag) = each(%flags)) {
	hex($match{match_flags}) & $flag and push @rule, qq(ATTRS{$key}=="$match{$key}",);
    }
    push @rule,
    (
     qq(MODE="660",),
     );
    push @rule,
    (
     qq(GROUP="plugdev"),
     );
    print join(' ', @rule) . "\n";
}

print "DRIVERS!=\"usb\", GOTO=\"kcontrol_rules_end\"\n";
print "ACTION!=\"add\"\, GOTO=\"kcontrol_rules_end\"\n";
print "SUBSYSTEMS!=\"usb\"\, GOTO=\"kcontrol_rules_end\"\n\n";

foreach my $usermap (@ARGV) {
    open(my $IN, $usermap . (-x $usermap && "|")) or die "unable to open usermap $usermap";
    parse_usermap_line($_) foreach <$IN>;
}

print "\nLABEL=\"kcontrol_rules_end\"\n";
