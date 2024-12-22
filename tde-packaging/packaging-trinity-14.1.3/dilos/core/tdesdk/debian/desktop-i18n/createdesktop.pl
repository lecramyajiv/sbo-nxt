#! /usr/bin/env perl

use strict;
use warnings;

use Getopt::Long;

sub printdate
{
    printf ( "%04i", ( $_[5] + 1900 ) );
    print "-";
    printf ( "%02i", $_[4] + 1);
    print "-";
    printf ( "%02i", $_[3] );
    print " ";
    printf ( "%02i", $_[2] );
    print ":";
    printf ( "%02i", $_[1] );
    print "+0000";
}

sub prepare
{
    #warn "Running on Perl V5.8.x" if $^V ge v5.8.0;

    binmode( STDOUT, ":utf8" ) if $^V ge v5.8.0;

    my @now = gmtime();
    print "#, fuzzy\n";
    print "msgid \"\"\n";
    print "msgstr \"\"\n";
    print "\"Project-Id-Version: desktop files\\n\"\n";
    print "\"Report-Msgid-Bugs-To: http://bugs.trinitydesktop.org\\n\"\n";
    print "\"POT-Creation-Date: "; printdate( @now ); print "\\n\"\n";
    print "\"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n\"\n";
    print "\"Last-Translator: FULL NAME <EMAIL\@ADDRESS>\\n\"\n";
    print "\"Language-Team: LANGUAGE <kde-i18n-doc\@kde.org>\\n\"\n";
    print "\"MIME-Version: 1.0\\n\"\n";
    print "\"Content-Type: text/plain; charset=UTF-8\\n\"\n";
    print "\"Content-Transfer-Encoding: 8bit\\n\"\n";
    print "\n\n";
}

sub processfiles
{
    my ( $files, $basedir) = ( @_ );
    for my $filename ( @$files )
    {
        chomp( $filename );
        open( FH, "<", $filename ) or warn "Cannot open file $filename";
        binmode( FH, ":utf8" ) if $^V ge v5.8.0;
    
        #warn("Using $filename");
        
        #my $regexp = qr{^(Name|Comment|Language|Keywords|About|Description|GenericName)=};
        my $regexp = qr{^(Name|Comment|Language|Keywords|About|Description|GenericName|Query|ExtraNames|X-TDE-Submenu)=};
    
        while( <FH> )
        {
            if ( m/$regexp/o )
            {
                my $msgid = $_;
                chomp( $msgid );
                $msgid =~ s/\\/\\\\/g;
                $msgid =~ s/\"/\\\"/g;
		if ($msgid =~ m/ +$/) {
                   $msgid =~ s/ +$//; # remove trailing spaces
		   print STDERR "ERROR: white space at the end of $msgid in $filename\n";
		}
                if ($msgid =~ m/\r+$/) {
                   $msgid =~ s/\r+$//; # remove trailing CR (Carriage Return)
		   print STDERR "ERROR: CR at the end of $msgid in $filename\n";
		}
		$filename =~ s,^$basedir/,,;
                print "#: $filename:$.\n";
                print "msgid \"$msgid\"\n";
                print "msgstr \"\"\n";
                print "\n";
            }
        }
    
        close( FH );
    }
}

my $onefilelist;
my $basedir;
GetOptions ( "file-list=s" => \$onefilelist,
	     "base-dir=s" => \$basedir
	   );

prepare;

open( FILELIST, $onefilelist ) or warn ( "Cannot open file list: $onefilelist" );
my @thislist = <FILELIST>;
processfiles( \@thislist, $basedir );
close( FILELIST );

