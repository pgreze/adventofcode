#!/usr/bin/env python3

import sys

def main(input_file):
    lines = open(input_file).readlines()
    instructions = [decode_inst(l) for l in lines]

    index, acc = iloop_search(instructions)
    print(f"Infinite loop fixed after changing the instruction {index} with acc = {acc}")

def decode_inst(line: str):
    operation, rem = line.split(" ")
    sign, arg = rem[0], int(rem[1:])
    return operation, sign, arg

def iloop_search(
    instructions: list,
    index = 0,
    acc = 0,
    history = [],
    alternative_path = False
):
    if index >= len(instructions):
        # We finished the program 🙌
        return index, acc

    if index in [idx for idx, _ in history]:
        if alternative_path:
            # This is another infinite loop
            return -1, -1
        
        print(f"Infinite loop found at idx={index}")
        # let's try to change all visited nop of jmp until
        # we can find an optimistic path.
        for idx, idx_acc in history[::-1]:
            op, *args = instructions[idx]
            result = (-1, -1)
            if op == "jmp":
                # Replace with a nop operation
                result = iloop_search(
                    instructions, 
                    idx + 1, 
                    idx_acc, 
                    history + [(idx, idx_acc)],
                    alternative_path=True
                )
            elif op == "nop":
                # Try to replace with a jump
                result = iloop_search(
                    instructions, 
                    idx + resolve_arg(*args),
                    idx_acc, 
                    history + [(idx, idx_acc)],
                    alternative_path=True
                )

            if result != (-1, -1):
                # We just found a valid alternative path
                return index, result[1]
        print("No valid alternative path found")
        return (-1, -1)

    print(f"Run instruction {index} {instructions[index]} with acc={acc}")
    operation, *args = instructions[index]
    next_index = index + 1
    if operation == "acc":
        acc += resolve_arg(*args)
    elif operation == "jmp":
        next_index = index + resolve_arg(*args)
    # Iterate to the next instruction
    return iloop_search(instructions, next_index, acc, history + [(index, acc)])

resolve_arg = lambda sign, arg: arg if sign == "+" else -arg

if __name__ == '__main__':
    main(sys.argv[1])
