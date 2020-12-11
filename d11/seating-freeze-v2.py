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
                int(fist_visible_seat(seats, (row + r, column + c), (r, c)) == "#")
                for r in range(-1, 2)
                for c in range(-1, 2)
                if (r, c) != (0, 0)
            ))
            if from_c == "L" and not nearby_occupied_seats:
                new_line.append("#")
            elif from_c == "#" and nearby_occupied_seats >= 5:
                new_line.append("L")
            else:
                new_line.append(seat)
        yield new_line

def fist_visible_seat(seats, pos: tuple, shift: tuple):
    """Return the first visible seat by continously applying the same shift.

    >>> fist_visible_seat(["...L.#.#.#.#."], (0, 0), (0, 1))
    'L'
    >>> fist_visible_seat([".....#.#.#.#."], (0, 4), (0, 1))
    '#'
    """
    row, column = pos
    rshift, cshift = shift
    while 0 <= row < len(seats) and 0 <= column < len(seats[0]):
        seat = seats[row][column]
        if seat != ".": return seat
        row += rshift
        column += cshift
    return None

if __name__ == '__main__':
    main(sys.argv[1])
