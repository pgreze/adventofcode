#!/usr/bin/env python3

import sys

def main(input_file, preamble_size):
    lines = open(input_file).readlines()
    numbers = [int(l.strip()) for l in lines]

    number = search_invalid_sum(numbers[:preamble_size], numbers[preamble_size:])
    print(f"Invalid sum = {number}")

def search_invalid_sum(preamble: list, numbers: list) -> int:
    number = numbers[0]
    print(f"Search if {number} is a sum of a pair in {preamble}")
    found = any((
        i + j == number
        for idx, i in enumerate(preamble[:-1])
        for j in preamble[idx:]
    ))
    if not found:
        return number
    return search_invalid_sum(preamble[1:] + [number], numbers[1:])

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
