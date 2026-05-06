#!/usr/bin/env python3

import argparse

from Command import check_disk,check_cpu,check_user

parser = argparse.ArgumentParser()

parser.add_argument("--check",choices=["cpu","disk","user"],required=True)

args = parser.parse_args()

if args.check == "cpu":
    print(check_cpu())

elif args.check == "disk":
    print(check_disk())

elif args.check == "user":
    print(check_user())

