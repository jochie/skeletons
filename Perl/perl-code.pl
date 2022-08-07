#!/usr/bin/env perl
# -*- mode: perl; perl-indent-level: 4; indent-tabs-mode: nil -*- for emacs

use strict;
use warnings;

use Getopt::Long;
use Pod::Usage;

my %options = (
    debug   => 0,
    dryrun  => 0,
    verbose => 0,
    help    => 0,
    manual  => 0
);

sub parse_options()
{
    if (!@ARGV) {
        pod2usage(-verbose => 1,
                  -exitval => 0);
    }
    GetOptions("help|h"    => \$options{help},
               "manual|m"  => \$options{manual},
               "verbose|v" => \$options{verbose},
               "dryrun|n"  => \$options{dryrun},
               "debug|d"   => \$options{debug}) ||
        pod2usage(-verbose => 0,
                  -message => " ", # Force a line-break
                  -exitval => 1);
    if ($options{help}) {
        pod2usage(-verbose => 1,
                  -exitval => 0);
    } elsif ($options{manual}) {
        pod2usage(-verbose => 2,
                  -exitval => 0);
    }
    if (@ARGV > 0) {
        pod2usage(-verbose => 1,
                  -message => "Too many parameters given.\n");
    }
}

sub main()
{
    parse_options();
    print("Hello world.\n");
}

main();


__END__

=pod

=head1 NAME

perl-code - A sample self-documenting Perl program with option parsing

=head1 SYNOPSIS

perl-code [-d|-debug|-n|--dryrun|-m|--manual|-v|--verbose]

=head1 DESCRIPTION

This sample Perl program demonstrates option parsing as well as built-in
documentation. The options are for enabling debugging output, verbose
output, and requesting that the program operates in dryrun mode.

=head1 OPTIONS

=over 5

=item B<--debug>, B<-d>

Enable debugging output.

=item B<--dryrun>, B<-n>

Request that the program operates in dryrun (noop) mode.

=item B<--manual>, B<-m>

Provide built-in (unix) manual style documentation.

=item B<--verbose>, B<-v>

Enable verbose output.

=back

=cut
