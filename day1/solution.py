#!/usr/bin/env python3

from os import path

def main():
    part1()
    part2()

def part1():
    values = get_input()
    for value in values:
        for other_value in values:
            if int(value) + int(other_value) == 2020:
                print('Part 1 solution: {}'.format(int(value) * int(other_value)))
                return

def part2():
    values = get_input()
    for value in values:
        for other_value in values:
            for third_value in values:
                if int(value) + int(other_value) + int(third_value) == 2020:
                    print('Part 2 solution: {}'.format(int(value) * int(other_value) * int(third_value)))
                    return

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
