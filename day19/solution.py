#!/usr/bin/env python3

from os import path
import re

rules = {}
messages = []
max_depth = 20

def main():

    for line in get_input():
        if ':' in line:
            rule_nr = line.split(': ')[0]
            rule = line.split(': ')[1]
            rules[int(rule_nr)] = rule
        elif 'a' in line or 'b' in line:
            messages.append(line)

    regex = get_regex(rules[0], 0)
    valid = 0
    for message in messages:
        if (re.fullmatch(regex, message)):
            valid += 1
    
    print(f'Valid messages Part I: {valid}')

    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"

    regex = get_regex(rules[0], 0)
    valid = 0
    for message in messages:
        if (re.fullmatch(regex, message)):
            valid += 1

    print(f'Valid messages Part II: {valid}')

def get_regex(rule, depth):
    if depth > max_depth:
        return ''

    if "|" in rule:
        subrule_or_part1 = [int(i) for i in rule[:rule.index("|") - 1].split(" ")]
        subrule_or_part2 = [int(i) for i in rule[rule.index("|") + 2:].split(" ")]
        regex1 = "(" + ")(".join([get_regex(rules[rule], depth + 1) for rule in subrule_or_part1]) + ")"
        regex2 = "(" + ")(".join([get_regex(rules[rule], depth + 1) for rule in subrule_or_part2]) + ")"
        return  f"({regex1})|({regex2})"
    elif 'a' in rule or 'b' in rule:
        return  rule[1:-1]
    else:
        sub_rules = [int(i) for i in rule.split(" ")]
        return "(" + ")(".join([get_regex(rules[rule], depth) for rule in sub_rules]) + ")"

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
