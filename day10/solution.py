#!/usr/bin/env python3

from os import path

def main():
    
    adapters = [int(line) for line in get_input()]
    adapters = sorted(adapters)

    jolt_differences = {1: 0, 2: 0, 3: 1}
    for idx, adapter in enumerate(adapters):
        previous_adapter = 0
        if idx > 0:
            previous_adapter = adapters[idx-1]
        difference = adapter - previous_adapter
        jolt_differences[difference] += 1

    result = jolt_differences[1] * jolt_differences[3]
    print(f'Amount of 1-jolt differences times amount of 3-jolt differences is {result}')

    ways_to_reach = {}
    for adapter in adapters:
        ways = 0
        for distance in range (1, 4):
            if adapter-distance in ways_to_reach:
                ways = ways + ways_to_reach[adapter-distance]
        if adapter <= 3:
            ways += 1
        ways_to_reach[adapter] = ways
    
    print(f'Unique ways to reach last adapter is {ways_to_reach[max(adapters)]}')

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
