#!/usr/bin/env python3

import sys
import os.path

VERBOSE = "-v" in sys.argv

def main(input_file):
    data = [i.strip() for i in open(input_file).readlines()]
    seats = [p for d in data for p in (decode_pass(d),) if p]
    if not seats:
        print("No valid boarding pass found")
        return
    
    for p_seat in seats:
        seat = next_seat(p_seat)
        n_seat = next_seat(seat)
        if seat in seats or n_seat not in seats:
            continue
        is_valid = seat[0] not in (0, 127)
        print(f"{seat} (ID={resolve_seat_id(seat)}) (valid={is_valid})")

def decode_pass(boarding_pass: str):
    if len(boarding_pass) != 10:
        return None
    row, column = (0, 127), (0, 7)
    for idx, letter in enumerate(boarding_pass):
        ret = process_direction(letter, row, column, reduce=idx in (6, 9))
        if ret is None:
            print(f"Invalid letter {letter} in {boarding_pass}")
            return None
        if VERBOSE: print(f"{(row, column)} . {letter} -> {ret}")
        row, column = ret
    pos = (row, column)
    end="\n\n" if VERBOSE else "\n"
    print(f"{boarding_pass} = {pos} (ID={resolve_seat_id(pos)})", end=end)
    return pos

def process_direction(letter, row, column, reduce):
    if letter == "F":
        if reduce: return (row[0], column)
        top, bottom = row
        bottom -= process_shift(row)
        return ((top, int(bottom)), column)
    elif letter == "B":
        if reduce: return (row[1], column)
        top, bottom = row
        top += process_shift(row)
        return ((int(top) + 1, bottom), column)
    elif letter == "L":
        if reduce: return (row, column[0])
        left, right = column
        right -= process_shift(column)
        return (row, (left, int(right)))
    elif letter == "R":
        if reduce: return (row, column[1])
        left, right = column
        left += process_shift(column)
        return (row, (int(left) + 1, right))
    return None

process_shift = lambda r: (r[1] - r[0]) / 2
resolve_seat_id = lambda p: p[0] * 8 + p[1]

def next_seat(seat):
    row, column = seat
    if column == 7:
        return (row + 1, 0)
    return (row, column + 1)

if __name__ == '__main__':
    main(sys.argv[1])
