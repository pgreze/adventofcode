#!/usr/bin/env python3

import sys
import re

def main(input_file, btype: str = "shiny gold"):
    lines = open(input_file).readlines()
    rules = dict(decode_rule(l) for l in lines)
    
    count = nbags_in(rules, btype)
    print(f"A {btype} bag contain {count} bags")

def decode_rule(s: str):
    container = s[:s.index(" bags contain ")]
    items = re.findall(r"(\d+) ([\w ]+) bag", s)
    return container, {btype: int(count) for count, btype in items}

def nbags_in(rules, btype, instances = 1, spaces="") -> int:
    print(f"Search {spaces}{btype} * {instances}")
    if btype not in rules:
        return 0
    count = 0
    for bt, ct in rules[btype].items():
        count += instances * ct
        count += nbags_in(rules, bt, instances * ct, spaces + " ")
    return count


if __name__ == '__main__':
    main(sys.argv[1])
