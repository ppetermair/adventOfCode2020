#!/usr/bin/env python3

from os import path

def main():
    validPart1 = 0
    validPart2 = 0
    for line in get_input():
        min = int(line.split(" ")[0].split("-")[0])
        max = int(line.split(" ")[0].split("-")[1])
        letter = line.split(" ")[1].split(":")[0]
        password = line.split(" ")[2]
        count = password.count(letter)
        if (min <= count <= max):
            validPart1 += 1

        first_char_is_letter = password[min-1] == letter
        second_char_is_letter = password[max-1] == letter
        if (first_char_is_letter != second_char_is_letter):
            validPart2 += 1

        print("min: {} max: {} letter: {} password:{}".format(min, max, letter, password))
        print("Valid password Part I: {}".format(validPart1))
        print("Valid password Part II: {}".format(validPart2))

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
