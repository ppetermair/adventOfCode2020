#!/usr/bin/env python3

from os import path

def main():
    trees11 = trees_in_slope(1, 1)
    trees31 = trees_in_slope(3, 1)
    trees51 = trees_in_slope(5, 1)
    trees71 = trees_in_slope(7, 1)
    trees12 = trees_in_slope(1, 2)
    print(f'Trees multiplied: {trees11 * trees31 * trees51 * trees71 * trees12}')

def trees_in_slope(right, down):
    trees = 0
    horizontal_index = 0 - right
    for idx, row in enumerate(get_input()):
        if idx % down != 0:
            continue
        horizontal_index += right
        if horizontal_index > 30:
            horizontal_index -= 31
        if row[horizontal_index] == '#':
            trees += 1
    print(f'{trees} trees in {right} {down} slope')
    return trees

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
