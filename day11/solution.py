#!/usr/bin/env python3

from os import path

def main():
    seat_plan = []
    for row_input in get_input():
        row = [seat for seat in row_input]
        seat_plan.append(row)

    new_seat_plan_partI = calculate_seat_plan(seat_plan, 1, 3)
    new_seat_plan_partII = calculate_seat_plan(seat_plan, len(seat_plan), 4)    

    print(f'Part I: {count_occupied_seats(new_seat_plan_partI)} seats occupied')
    print(f'Part II: {count_occupied_seats(new_seat_plan_partII)} seats occupied')


def calculate_seat_plan(seat_plan, depth, occupied_tolerance):
    old_seat_plan = []
    new_seat_plan = seat_plan.copy()
    iteration = 0    
    changed = True

    while changed:
        iteration += 1
        changed = False
        old_seat_plan = new_seat_plan
        new_seat_plan = []
        for row_idx, row in enumerate(old_seat_plan):
            new_row = []
            for seat_idx, seat in enumerate(row):
                new_seat = get_new_seat_status(row_idx, seat_idx, old_seat_plan, depth, occupied_tolerance)
                if seat != new_seat:
                    changed = True
                new_row.append(new_seat)
            new_seat_plan.append(new_row)
    print(f'Seat plan stabilized after {iteration} iterations')
    return new_seat_plan

def get_new_seat_status(row_idx, seat_idx, seat_plan, depth, occupied_tolerance):
    seat_value = seat_plan[row_idx][seat_idx]
    if seat_value == '.':
        return '.'
    occupied_seats = get_occupied_adjacent_seats(row_idx, seat_idx, seat_plan, depth)
    if occupied_seats > occupied_tolerance:
        return 'L'
    if occupied_seats == 0:
        return '#'
    return seat_value

def get_occupied_adjacent_seats(row_idx, seat_idx, seat_plan, depth):
    occupied = 0
    moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for move in moves:
        for d in range(1, depth + 1):
            row = row_idx + d * move[0]
            seat = seat_idx + d * move[1]
            if row <0 or row >= len(seat_plan):
                continue
            if seat <0 or seat >= len(seat_plan[0]):
                continue

            if seat_plan[row][seat] == '#':
                occupied += 1
                break
            if seat_plan[row][seat] == 'L':
                break
    return occupied

def count_occupied_seats(seat_plan):
    occupied = 0
    for row in seat_plan:
        for seat in row:
            if seat == '#':
                occupied += 1
    return occupied

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
