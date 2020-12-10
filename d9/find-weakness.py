#!/usr/bin/env python3

import sys

def main(input_file, preamble_size):
    lines = open(input_file).readlines()
    numbers = [int(l.strip()) for l in lines]

    number = search_invalid_sum(numbers[:preamble_size], numbers[preamble_size:])
    print(f"Invalid sum = {number}")
    first, last = seach_consecutive_sum_for(numbers, number)
    print(f"{first} + {last} = {first + last}")

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

def seach_consecutive_sum_for(numbers: list, number: int):
    for idx, i in enumerate(numbers):
        count = i
        consecutive_numbers = {i}
        for j in numbers[idx + 1:]:
            count += j
            consecutive_numbers.add(j)
            if count == number:
                return min(consecutive_numbers), max(consecutive_numbers)
            elif count > number:
                break

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
