#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Do a Zero Downtime Deployment by taking an old and a new AMIs.')
parser.version = '1.0'

parser.add_argument('-v', '-vv', '-vvv', '--verbose', action='count')
parser.add_argument('--version', action='version')

parser.add_argument('OLD_AMI_ID', type=str, help='Run deploy with old and new AMI_ID')
parser.add_argument('NEW_AMI_ID', type=str, help='List AMI id')

parser.print_help()

args = parser.parse_args()
