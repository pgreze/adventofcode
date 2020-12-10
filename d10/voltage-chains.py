#!/usr/bin/env python3

import sys
from collections import Counter

def main(input_file):
    lines = open(input_file).readlines()
    numbers = list(set(int(l.strip()) for l in lines))
    count = pow(2, adapter_chain_count(numbers))
    print(f"Available chains = {count}")

def adapter_chain_count(numbers: list, index = 0):
    if index >= len(numbers):
        return 0
    count, number = 0, numbers[index]
    chain = [number]
    while (index + count + 1) < len(numbers) and \
        numbers[index + count + 1] == (numbers[index + count] + 1):
        print(f"{number} + {numbers[index + count + 1]}")
        chain += [numbers[index + count + 1]]
        count += 1
    if count: print(f"{count - 1} with {chain}")
    return max(0, count - 1) + adapter_chain_count(numbers, index + count + 1)

if __name__ == '__main__':
    main(sys.argv[1])
