#!/usr/bin/env python3

from os import path
import re

def main():
    passports = []
    passport = {}
    for line in get_input():
        if not line:
            passports.append(passport)
            passport = {}
            continue
        for field in line.split(' '):
            passport[field.split(':')[0]] = field.split(':')[1]
    passports.append(passport)

    valid_passports = 0
    for passport in passports:
        if is_valid(passport):
            valid_passports += 1
    print(f'Valid passports: {valid_passports}')

def is_valid(passport):
    ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if 'cid' in passport and len(passport) != 8:
        return False

    if 'cid' not in passport and len(passport) != 7:
        return False

    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False

    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False

    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    height = passport['hgt']
    if height.endswith('cm'):
        if int(height[:-2]) < 150 or int(height[:-2]) > 193:
            return False
    elif height.endswith('in'):
        if int(height[:-2]) < 59 or int(height[:-2]) > 76:
            return False
    else:
        return False

    if not re.match('#[0-9a-f]{6}', passport['hcl']):
        return False

    if passport['ecl'] not in ecl:
        return False

    if not re.match('^[0-9]{9}$', passport['pid']):
        return False

    return True

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
