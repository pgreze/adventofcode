#!/usr/bin/env python3

import sys
from dataclasses import dataclass

@dataclass
class PasswordEntry:
    min_occ: int
    max_occ: int
    letter: str
    password: str

def main(input_file):
    entries = open(input_file).readlines()
    passwords = [parse_password_entry(entry) for entry in entries]
    valids = [p for p in passwords if check_password_entry(p)]
    print(f"Found {len(valids)} valid passwords inside {len(entries)} entries")

def parse_password_entry(entry: str) -> PasswordEntry:
    rules, middle, password = entry.split(" ")
    min_occ, max_occ = (int(i) for i in rules.split("-"))
    return PasswordEntry(min_occ, max_occ, middle.strip(":"), password)

def check_password_entry(entry: PasswordEntry) -> bool:
    return entry.min_occ <= entry.password.count(entry.letter) <= entry.max_occ

if __name__ == '__main__':
    main(sys.argv[1])
