import sys
from operator import add
from itertools import product

def get_heights(schematic):
    heights = [-1] * len(schematic[0])
    for r, row in enumerate(schematic):
        for c, col in enumerate(row):
            if col == '#':
                heights[c] += 1
    return heights

def main():
    schematics = [sch.split('\n') for sch in sys.stdin.read().split('\n\n')]
    locks = [get_heights(sch) for sch in schematics if '#' in sch[0]]
    keys = [get_heights(sch[::-1]) for sch in schematics if '.' in sch[0]]
    print(sum([1 if all(v <= 5 for v in list(map(add, lock, key))) else 0 for lock, key in product(locks, keys)]))

if __name__ == "__main__":
    main()