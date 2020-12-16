#!/usr/bin/env python3

import sys
from enum import Enum
from functools import reduce

class Direction(Enum):
    WEST = "W"
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"

class Move(Enum):
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"

def main(input_file):
    lines = (i.strip() for i in open(input_file).readlines())
    position = (0, 0)
    waypoint = (10, 1)
    position, waypoint = reduce(move_to, lines, (position, waypoint))
    print(f"Final position: {position} with distance={sum((abs(i) for i in position))}")

def move_to(inputs: tuple, navigation: str) -> tuple:
    (x, y), (wx, wy) = inputs
    action, value = navigation[0], int(navigation[1:])
    print(f"{x} / {y} + w= {wx} / {wy} . {navigation}")

    if action == Direction.WEST.value:
        wx -= value
    elif action == Direction.NORTH.value:
        wy += value
    elif action == Direction.EAST.value:
        wx += value
    elif action == Direction.SOUTH.value:
        wy -= value
    elif action == Move.LEFT.value:
        wx, wy = move_waypoint(wx, wy, value, Move.LEFT)
    elif action == Move.RIGHT.value:
        wx, wy = move_waypoint(wx, wy, value, Move.RIGHT)
    elif action == Move.FORWARD.value:
        x += wx * value
        y += wy * value
    return (x, y), (wx, wy)

def move_waypoint(wx, wy, degrees: int, move: Move, verbose="-v" in sys.argv):
    """
    >>> move_waypoint(9, 1, 90, Move.RIGHT)
    (1, -9)
    >>> move_waypoint(-60, 43, 90, Move.RIGHT)
    (43, 60)
    >>> move_waypoint(-62, -43, 90, Move.RIGHT)
    (-43, 62)
    >>> move_waypoint(15, -34, 90, Move.RIGHT)
    (-34, -15)
    >>> move_waypoint(9, 1, 90, Move.LEFT)
    (-1, 9)
    >>> move_waypoint(-60, 43, 90, Move.LEFT)
    (-43, -60)
    >>> move_waypoint(-62, -43, 90, Move.LEFT)
    (43, -62)
    >>> move_waypoint(60, -43, 90, Move.LEFT)
    (43, 60)
    >>> move_waypoint(-60, 43, 180, Move.RIGHT)
    (60, -43)
    """
    for _ in range(abs(int(degrees / 90))):
        if wx >= 0 and wy >= 0: # Top right
            if move == Move.RIGHT:
                wx, wy = wy, -wx
            else:
                wx, wy = -wy, wx
        elif wx < 0 and wy >= 0: # Top left
            if move == Move.RIGHT:
                wx, wy = wy, -wx
            else:
                wx, wy = -wy, wx
        elif wx >= 0 and wy < 0: # Bottom right
            if move == Move.RIGHT:
                wx, wy = wy, -wx
            else:
                wx, wy = -wy, wx
        else: # Bottom left
            if move == Move.RIGHT:
                wx, wy = wy, -wx
            else:
                wx, wy = -wy, wx
        if verbose: print(f"{wx}, {wy}")
    return wx, wy

if __name__ == '__main__':
    main(sys.argv[1])
