#!/usr/bin/env python3

import sys

def main(input_file):
    numbers = open(input_file).readlines()
    pairs = ((int(i), int(j)) for i in numbers for j in numbers[1:])
    valid_sums = ((i, j) for i, j in pairs if i + j == 2020)
    i, j = next(valid_sums)
    print(f"{i} * {j} = {i * j}")

if __name__ == '__main__':
    main(sys.argv[1])
