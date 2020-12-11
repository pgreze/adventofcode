#!/usr/bin/env python3

import sys
from collections import Counter

def main(input_file):
    lines = open(input_file).readlines()
    numbers = list(set(int(l.strip()) for l in lines))
    diffs = count_diffs([0] + numbers + [numbers[-1] + 3])
    d1, d3 = diffs[1], diffs[3]
    print(f"{d1} * {d3} = {d1 * d3}")

def count_diffs(numbers: list):
    return Counter(
        numbers[idx + 1] - i
        for idx, i in enumerate(numbers[:-1])
    )

if __name__ == '__main__':
    main(sys.argv[1])
