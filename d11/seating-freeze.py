#!/usr/bin/env python3

import sys

def main(input_file):
    lines = [list(i.strip()) for i in open(input_file).readlines() if i.strip()]
    seats = find_stable_map(lines)
    seats = '\n'.join((''.join(l) for l in seats))
    print(f"Occupied seats: {seats.count('#')}")

def find_stable_map(seats: str):
    convertion = ['L', '#']
    new_map = None
    while True:
        new_map = list(resolve_map(seats, *convertion))
        print("\n>> New map:")
        for line in new_map: print("".join(line))

        convertion = convertion[::-1]
        if new_map == seats:
            return new_map
        seats = new_map

def resolve_map(seats: list, from_c: str, to_c: str):
    for row, line in enumerate(seats):
        new_line = []
        for column, seat in enumerate(line):
            if seat == ".":
                new_line.append(".")
                continue
            nearby_occupied_seats = sum((
                int(seats[r][c] == "#")
                for r in range(row - 1, row + 2)
                for c in range(column - 1, column + 2)
                if 0 <= r < len(seats) and 0 <= c < len(line) and (r, c) != (row, column)
            ))
            if from_c == "L" and not nearby_occupied_seats:
                new_line.append("#")
            elif from_c == "#" and nearby_occupied_seats >= 4:
                new_line.append("L")
            else:
                new_line.append(seat)
        yield new_line

if __name__ == '__main__':
    main(sys.argv[1])
