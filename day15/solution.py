#!/usr/bin/env python3

from os import path

def main():

    input = [int(x) for x in get_input()[0].split(',')]
    print(f'The 2020th number spoken is {last_number(input, 2021)}')
    print(f'The 30000000th number spoken is {last_number(input, 30000001)}')

def last_number(input, turns):
    last_spoken = input[-1]
    spoken = {}

    for idx, number in enumerate(input[:-1]):
        spoken[int(number)] = idx+1    

    for turn in range(len(input)+1, turns):
        if last_spoken in spoken:
            age = turn - 1 - spoken[last_spoken]
        else:
            age = 0
        spoken[last_spoken] = turn - 1
        last_spoken = age 
    return last_spoken  


def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
