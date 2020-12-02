#!/usr/bin/env python3

import sys

def main(input_file):
    numbers = open(input_file).readlines()
    triples = ((int(i), int(j), int(k)) for i in numbers for j in numbers[1:] for k in numbers[2:])
    valid_sums = ((i, j, k) for i, j, k in triples if i + j + k == 2020)
    i, j, k = next(valid_sums)
    print(f"{i} * {j} * {k} = {i * j * k}")

if __name__ == '__main__':
    main(sys.argv[1])
