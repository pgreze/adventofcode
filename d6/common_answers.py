#!/usr/bin/env python3

import sys
from functools import reduce

def main(input_file):
    data = open(input_file).read()
    count = sum((
        common_answers(idx, group)
        for idx, group in enumerate(data.split("\n\n"))
    ))
    print(f"Total = {count}")

def common_answers(idx, data):
    answer_per_person = [set(answers) for answers in data.split("\n") if answers]
    answers = reduce(set.intersection, answer_per_person)
    print(f"For the group {idx + 1}, common answers = {answers}")
    return len(answers)

if __name__ == '__main__':
    main(sys.argv[1])
