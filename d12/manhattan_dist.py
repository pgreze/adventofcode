#!/usr/bin/env python3

import sys
from enum import Enum
from functools import reduce

class Direction(Enum):
    WEST = "W"
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
directions = list(Direction)

class Move(Enum):
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"

def main(input_file):
    lines = (i.strip() for i in open(input_file).readlines())
    position = reduce(move_to, lines, (0, 0, Direction.EAST))
    print(f"Final position: {position} with distance={sum((abs(i) for i in position[0:2]))}")

def move_to(position: tuple, navigation: str) -> tuple:
    x, y, direction = position
    action, value = navigation[0], int(navigation[1:])
    print(f"{x}/{y}/{direction.value} . {navigation}")

    if action == Direction.WEST.value:
        x -= value
    elif action == Direction.NORTH.value:
        y += value
    elif action == Direction.EAST.value:
        x += value
    elif action == Direction.SOUTH.value:
        y -= value
    elif action == Move.LEFT.value:
        direction = resolve_move(direction, -value)
    elif action == Move.RIGHT.value:
        direction = resolve_move(direction, +value)
    elif action == Move.FORWARD.value:
        return move_to(position, f"{direction.value}{value}")
    return (x, y, direction)

resolve_move = lambda direction, degrees: \
    directions[(directions.index(direction) + int(degrees / 90)) % len(directions)]

if __name__ == '__main__':
    main(sys.argv[1])
