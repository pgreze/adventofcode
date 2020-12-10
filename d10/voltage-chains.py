#!/usr/bin/env python3

import sys
from collections import Counter

def main(input_file):
    lines = open(input_file).readlines()
    numbers = list(set(int(l.strip()) for l in lines))
    chains = list(create_adapter_chains(numbers, 0))
    print(f"Available chains = {len(chains)}")

def create_adapter_chains(numbers: list, number: int, chain = []):
    chain = chain + [number]
    if number == numbers[-1]:
        yield chain

    for step in range(1, 4):
        if number + step in numbers:
            yield from create_adapter_chains(numbers, number + step, chain)

if __name__ == '__main__':
    main(sys.argv[1])
