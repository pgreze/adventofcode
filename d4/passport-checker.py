#!/usr/bin/env python3

import sys
import re

REQUIRED_FIELDS = {
    "byr": "Birth Year",
    "iyr": "Issue Year",
    "eyr": "Expiration Year",
    "hgt": "Height",
    "hcl": "Hair Color",
    "ecl": "Eye Color",
    "pid": "Passport ID",
    "cid": "Country ID",
}.keys()

def main(input_file):
    data = open(input_file).read()
    passports = decode_passports(data)
    valids = sum((is_valid(p, REQUIRED_FIELDS) for p in passports))
    north_pole_creds = sum((is_valid(p, REQUIRED_FIELDS - {"cid"}) for p in passports)) - valids
    print(f"Found {valids} valids + {north_pole_creds} North Pole credentials = {valids + north_pole_creds} among {len(passports)} passports")

def decode_passports(data: str):
    passports = data.split("\n\n")
    return [decode_passport(passport) for passport in passports]

def decode_passport(passport):
    map = re.split("[\n ]", passport.strip())
    return dict((decode_passport_entry(entry) for entry in map))

def decode_passport_entry(entry, sep=":"):
    parts = entry.split(sep)
    return (parts[0], sep.join(parts[1:]))

def is_valid(map, fields):
    return 1 if len(fields - map.keys()) == 0 else 0

if __name__ == '__main__':
    main(sys.argv[1])
