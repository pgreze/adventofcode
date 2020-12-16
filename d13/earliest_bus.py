#!/usr/bin/env python3

import sys
from collections import Counter

def main(input_file):
    lines = open(input_file).readlines()
    departure = int(lines[0].strip())
    bus_ids = [int(i) for i in lines[1].strip().split(",") if i != "x"]
    bus_id, earliest_depart = min(
        ((id, (departure // id + 1) * id) for id in bus_ids),
        key=lambda x: x[1]
    )
    waiting_time = earliest_depart - departure
    print(f"Better take the bus {bus_id} at {earliest_depart}, result = {waiting_time * bus_id}")

if __name__ == '__main__':
    main(sys.argv[1])
