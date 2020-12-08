#!/usr/bin/env python3

from os import path
import re

def main():
    bag_dict = bag_dictionary()    
    outer_bag_result = []

    inner_bags = ['shiny gold']
    while len(inner_bags) > 0:
        outer_bags = []
        for inner_bag in inner_bags:
            for bag, content in bag_dict.items():
                if can_contain(content, inner_bag):
                    outer_bags.append(bag)
        inner_bags = outer_bags
        outer_bag_result.extend(outer_bags)
        
    outer_bag_result = list(set(outer_bag_result)) # remove duplicates
    inner_bag_result = count_inner_bags(bag_dict, 'shiny gold')

    print(f'{len(outer_bag_result)} bags can contain a shiny gold bag')
    print(f'A shiny gold bag must contains {inner_bag_result} bags')

def bag_dictionary():
    bag_dict = {}
    for line in get_input():
        outer_bag = line.split('contain')[0].split('bags')[0].strip()
        inner_bags = re.findall(r'\d+ [a-z]+ [a-z]+', line.split('contain')[1])
        bag_dict[outer_bag] = inner_bags
    return bag_dict

def count_inner_bags(bag_dict, bag):
    count = 0
    bag_content = bag_dict[bag]
    for bc in bag_content:
        bc_count = int(bc.split(' ', 1)[0])
        bc_bag = bc.split(' ', 1)[1]
        count += bc_count + bc_count * count_inner_bags(bag_dict, bc_bag)
    return count

def can_contain(content, bag):
    for c in content:
        if c.endswith(bag):
            return True
    return False

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
