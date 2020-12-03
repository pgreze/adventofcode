#!/usr/bin/env python3

import sys

EXAMPLE = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip().split("\n")

tree_encounter_check = lambda pos: 1 if pos == "#" else 0

def main(forest_map):
    map_length = len(forest_map[0])
    # Resolve the initial position as the first encounter
    n_tree_encounter = tree_encounter_check(forest_map[0][0])
    column = 3 # Start from initial position + 3
    for row, line in enumerate(forest_map[1:]):
        # Consider this new tile
        column_rel = column % map_length
        print(f"For row={row+1}, column={column}, column_rel={column_rel}, status={line[column_rel]}")
        n_tree_encounter += tree_encounter_check(line[column_rel])
        # And continue to the next slope
        column += 3
    print(f"Forest could be traversed with {n_tree_encounter} encouters / {len(forest_map)} rows")

decode_map = lambda file: [i.strip() for i in open(file).readlines()]

if __name__ == '__main__':
    main(EXAMPLE if len(sys.argv) == 1 else decode_map(sys.argv[1]))
