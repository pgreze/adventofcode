#!/usr/bin/env python3

import sys
from functools import reduce

tree_encounter_check = lambda pos: 1 if pos == "#" else 0

def main(forest):
    slope_mode = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    mode_to_result = [(mode, resolve_encounters(forest, *mode)) for mode in slope_mode]
    for mode, result in mode_to_result:
        print(f"For {mode}, encounters={result}")
    results = [r for _, r in mode_to_result]
    result = reduce(lambda x, y: x * y, results)
    print(f"product({','.join(str(r) for r in results)}) = {result}")

def resolve_encounters(forest, shift_right, shift_bottom, verbose = "-v" in sys.argv) -> int:
    map_length = len(forest[0])
    # Resolve the initial position as the first encounter
    n_tree_encounter = tree_encounter_check(forest[0][0])
    column = shift_right # Start from initial position + shift_right
    if verbose:
        print(f">> For Right {shift_right}, Down {shift_bottom}")
        print(("X" if forest[0][0] == "#" else "O") + forest[0][1:])
    for row, line in enumerate(forest[1:]):
        if (row + 1) % shift_bottom != 0:
            if verbose: print(line)
            continue
        # Consider this new tile
        column_rel = column % map_length
        n_tree_encounter += tree_encounter_check(line[column_rel])
        if verbose:
            marked_line = line[0:column_rel] + ("X" if line[column_rel] == "#" else "O") + line[column_rel+1:]
            print(marked_line)
        # And continue to the next slope
        column += shift_right
    return n_tree_encounter

if __name__ == '__main__':
    main([i.strip() for i in open(sys.argv[1]).readlines()])
