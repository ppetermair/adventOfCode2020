#!/usr/bin/env python3

from os import path

def main():
    # code here
    print(get_input())

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
