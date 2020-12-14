#!/usr/bin/env python3

from os import path

def main():

    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    memory_part1 = {}
    memory_part2 = {}

    for line in get_input():

        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
            continue

        mem_adr = int(line.split(' = ')[0][4:-1])
        mem_value = int(line.split(' = ')[1])

        memory_part1[mem_adr] = apply_mask_to_value(mem_value, mask)

        masked_address = apply_mask_to_address(mem_adr, mask)
        for comb in get_address_combinations(masked_address):
            memory_part2[comb] = mem_value

    print(f'Sum of part 1 memory values: {sum(memory_part1.values())}')
    print(f'Sum of part 2 memory values: {sum(memory_part2.values())}')

def apply_mask_to_value(value, mask):
    binary_value = format(value, '036b')
    for idx, mask_char in enumerate(mask):
        if mask_char != 'X':
            binary_value = binary_value[:idx] + mask_char + binary_value[idx+1:]
    return int(binary_value, 2)

def apply_mask_to_address(address, mask):
    binary_value = format(address, '036b')
    for idx, mask_char in enumerate(mask):
        if mask_char == 'X' or mask_char == '1':
            binary_value = binary_value[:idx] + mask_char + binary_value[idx+1:]
    return binary_value

def get_address_combinations(address):
    result = [address]
    for idx, addr_char in enumerate(address):
        if addr_char == 'X':
            tmp = []
            for r in result:
                tmp.append(r[:idx] + '1' + r[idx+1:])
                tmp.append(r[:idx] + '0' + r[idx+1:])
            result = tmp
    return [int(r, 2) for r in result]

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
