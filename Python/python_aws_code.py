#!/usr/bin/env python3
# -*- mode: python; tab-width: 4; indent-tabs-mode: nil -*- for emacs

import argparse
import boto3
import datetime
import json

def parse_options():
    parser = argparse.ArgumentParser(
        description='A sample Python program with AWS specific option parsing, to be extended'
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
    parser.add_argument('-r', '--region',
                        help="Provide a non-default AWS region")
    parser.add_argument('-p', '--profile',
                        help="Provide a non-default AWS profile")
    opts = parser.parse_args()

    # Any post-processing, like checking mutually exclusive options, mandatory
    # options, happens here.

    return opts

def datetime_encoder(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def main():
    opts = parse_options()
    print(f"DEBUG   = {opts.debug}")
    print(f"DRYRUN  = {opts.dryrun}")
    print(f"VERBOSE = {opts.verbose}")
    print(f"PROFILE = {opts.profile}")
    print(f"REGION  = {opts.region}")
    if opts.profile:
        if opts.region:
            session = boto3.session.Session(profile_name=opts.profile,
                                            region_name=opts.region)
        else:
            session = boto3.session.Session(profile_name=opts.profile)
    else:
        if opts.region:
            session = boto3.session.Session(region_name=opts.region)
        else:
            session = boto3.session.Session()
    ec2 = session.client('ec2')
    results = ec2.describe_instances()
    print(json.dumps(results, sort_keys=True, indent=4, default=datetime_encoder))

main()
