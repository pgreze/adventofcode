#!/usr/bin/env python3

import sys
from dataclasses import dataclass

@dataclass
class PasswordEntry:
    idx1: int
    idx2: int
    letter: str
    password: str

def main(input_file):
    entries = open(input_file).readlines()
    passwords = [parse_password_entry(entry) for entry in entries]
    valids = [p for p in passwords if check_password_entry(p)]
    print(f"Found {len(valids)} valid passwords inside {len(entries)} entries")

def parse_password_entry(entry: str) -> PasswordEntry:
    rules, middle, password = entry.split(" ")
    idx1, idx2 = (int(i) for i in rules.split("-"))
    return PasswordEntry(idx1, idx2, middle.strip(":"), password)

def check_password_entry(entry: PasswordEntry) -> bool:
    idx1_check = entry.idx1 < len(entry.password) and entry.password[entry.idx1 - 1] == entry.letter
    idx2_check = entry.idx2 < len(entry.password) and entry.password[entry.idx2 - 1] == entry.letter
    return (idx1_check or idx2_check) and idx1_check != idx2_check

if __name__ == '__main__':
    main(sys.argv[1])
