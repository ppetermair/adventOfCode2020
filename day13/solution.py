#!/usr/bin/env python3

from os import path
from itertools import count

def main():
    earliest_time = int(get_input()[0])
    bus_ids = [(int(id), idx) for idx, id in enumerate(get_input()[1].split(',')) if id != 'x']
    
    for minute in count():
        time = earliest_time + minute
        buses_departing = get_buses_departing(time, bus_ids)
        if buses_departing:
            print(f'Found the earliest bus. Bus {buses_departing[0][0]} at time {time}')
            print(f'ID times waiting time is {(time - earliest_time) * buses_departing[0][0]}')
            break
    
    earliest_time = bus_ids[0][0]
    jump_time = bus_ids[0][0]    
    for bus in bus_ids[1:]:
        while (earliest_time + bus[1]) % bus[0] != 0:
            earliest_time += jump_time
        jump_time *= bus[0]

    print(f'Earliest time part II: {earliest_time}')

def get_buses_departing(time, bus_ids):
    result = []
    for bus in bus_ids:
            if time % bus[0] == 0:
                result.append(bus)
    return result

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
