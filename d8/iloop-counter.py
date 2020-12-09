#!/usr/bin/env python3

import sys

def main(input_file):
    lines = open(input_file).readlines()
    instructions = [decode_inst(l) for l in lines]

    index, acc = iloop_search(instructions)
    print(f"Infinite loop found at {index} with acc = {acc}")

def decode_inst(line: str):
    operation, rem = line.split(" ")
    sign, arg = rem[0], int(rem[1:])
    return operation, sign, arg

def iloop_search(
    instructions: list,
    index = 0,
    acc = 0,
    history = set()
):
    print(f"Run instruction {index} {instructions[index]} with acc={acc}")
    if index in history:
        return index, acc

    operation, sign, arg = instructions[index]
    next_index = index + 1
    if operation == "acc":
        acc += resolve_arg(sign, arg)
    elif operation == "jmp":
        next_index = index + resolve_arg(sign, arg)
    # Iterate to the next instruction
    return iloop_search(instructions, next_index, acc, history.union({index}))

resolve_arg = lambda sign, arg: arg if sign == "+" else -arg

if __name__ == '__main__':
    main(sys.argv[1])
