#!/usr/bin/env python3

import sys

def main(input_file):
    data = open(input_file).read()
    unique_answers = [
        set(group.replace("\n", "").strip())
        for group in data.split("\n\n")
    ]
    count = 0
    for idx, answers in enumerate(unique_answers):
        print(f"Group {idx + 1} replied positively to {len(answers)} questions")
        count += len(answers)
    print(f"Total = {count}")

if __name__ == '__main__':
    main(sys.argv[1])
