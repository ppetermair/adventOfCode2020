#!/usr/bin/env python3

from os import path

def main():

    input = [int(line) for line in get_input()]
    preamble = []
    invalid_number = -1

    for idx, number in enumerate(input):
        preamble.append(number)
        if (idx < 24):
            continue
        if not is_valid_sum(preamble, number):
            invalid_number = number
            print(f'Value {number} at index {idx} is not a valid number.')
            break
    
    start_index, stop_index = find_contiguous_set_for_sum(input, invalid_number)
    min_number = min(input[start_index:stop_index+1])
    max_number = max(input[start_index:stop_index+1])
    print(f'Contiguous set found from index {start_index} to {stop_index} with a result sum of {min_number + max_number}')

def find_contiguous_set_for_sum(input, number):
    for idx, value in enumerate(input):
        sum = value
        subset_index = idx + 1
        while subset_index < len(input) and sum < number:            
            sum += input[subset_index]            
            if sum == number:
                return (idx, subset_index)
            subset_index += 1


def is_valid_sum(preamble, number):
    for p1 in preamble:
        for p2 in preamble:
            if p1 + p2 == number:
                return True
    return False


def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
