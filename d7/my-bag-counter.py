#!/usr/bin/env python3

import sys
import re

def main(input_file, btype: str = "shiny gold"):
    lines = open(input_file).readlines()
    rules = dict(decode_rule(l) for l in lines)
    
    types = set(containers_for(btype, rules))
    print(types)
    print(f"{btype} bags can be holded in {len(types)} bags")

def decode_rule(s: str):
    container = s[:s.index(" bags contain ")]
    items = re.findall(r"(\d+) ([\w ]+) bag", s)
    return container, {btype: count for count, btype in items}

def containers_for(btype, rules):
    for container, items in rules.items():
        if btype not in items: continue
        yield container
        yield from containers_for(container, rules)

if __name__ == '__main__':
    main(sys.argv[1])
