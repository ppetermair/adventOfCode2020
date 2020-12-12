#!/usr/bin/env python3

from os import path

def main():
    distance = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    distance_part2 = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    facing = 'E'

    for instruction in get_input():
        action = instruction[:1]
        value = int(instruction[1:])
        if action == 'F':
            distance[facing] += value
            for wp_direction, wp_value in waypoint.items():
                distance_part2[wp_direction] += wp_value * value
        elif action == 'R' or action == 'L':
            facing = get_new_facing(facing, action, value)
            waypoint = get_new_waypoint(waypoint, action, value)
        else:
            distance[action] += value
            waypoint[action] += value

    print(f'Manhattan distance part I: {get_manhattan_distance(distance)}')
    print(f'Manhattan distance part II: {get_manhattan_distance(distance_part2)}')

def get_manhattan_distance(distance):
    east_west_distance = abs(distance['E'] - distance['W'])
    north_south_distance = abs(distance['N'] - distance['S'])
    return east_west_distance + north_south_distance

def get_new_waypoint(current_waypoint, action, value):
    new_waypoint = {}
    for wp_direction, wp_value in current_waypoint.items():
        new_facing = get_new_facing(wp_direction, action, value)
        new_waypoint[new_facing] = wp_value
    return new_waypoint

def get_new_facing(current_facing, action, value):
    directions = ['N', 'E', 'S', 'W']
    value = value // 90
    if action == 'L':
        value = value * -1
    new_index = directions.index(current_facing) + value
    if new_index > 3:
        new_index = new_index - 4
    if new_index < 0:
        new_index = new_index + 4
    return directions[new_index]

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
