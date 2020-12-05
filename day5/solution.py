#!/usr/bin/env python3

from os import path

def main():

    seat_ids = []
    for boarding_pass in get_input():
        seat_ids.append(seat_id(boarding_pass))

    seat_ids.sort()
    print(f'Max Seat ID: {seat_ids[len(seat_ids)-1]}')

    for id in seat_ids:
        if id + 1 not in seat_ids and id + 2 in seat_ids:
            print(f'My Seat ID: {id+1}')
            break


def seat_id(boarding_pass):
    rows = boarding_pass[:7]
    row_numbers = [r for r in range(128)]
    columns = boarding_pass[7:]
    column_numbers = [c for c in range(9)]

    for char in rows:
        if char == 'F':
            row_numbers = row_numbers[:len(row_numbers)//2]
        else:
            row_numbers = row_numbers[len(row_numbers)//2:]
    for char in columns:
        if char == 'L':
            column_numbers = column_numbers[:len(column_numbers)//2]
        else:
            column_numbers = column_numbers[len(column_numbers)//2:]

    row = row_numbers[0]
    column = column_numbers[0]
    seat_id = row * 8 + column

    return seat_id

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
