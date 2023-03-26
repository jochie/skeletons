#!/usr/bin/env python3
# -*- mode: python; tab-width: 4; indent-tabs-mode: nil -*- for emacs

import argparse

def parse_options():
    parser = argparse.ArgumentParser(
        description='A sample Python program with option parsing, to be extended'
    )
    parser.add_argument('-d', '--debug',
                        help="Enable debug output",
                        default=False,
                        action='store_true')
    parser.add_argument('-v', '--verbose',
                        help="Enable verbose output",
                        default=False,
                        action='store_true')
    parser.add_argument('-n', '--dryrun',
                        help="Request dryrun (noop) mode",
                        default=False,
                        action='store_true')
    opts = parser.parse_args()

    # Any post-processing, like checking mutually exclusive options, mandatory
    # options, happens here.

    return opts

def main():
    opts = parse_options()
    print(f"DEBUG   = {opts.debug}")
    print(f"DRYRUN  = {opts.dryrun}")
    print(f"VERBOSE = {opts.verbose}")

if __name__ == "__main__":
    main()
