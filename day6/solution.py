#!/usr/bin/env python3

from os import path

def main():
    groups = []
    group_questions = []
    groups.append(group_questions)

    for line in get_input():
        if not line:
            group_questions = []
            groups.append(group_questions)
            continue
        group_questions.append(line)
    
    sum_of_group_questions = 0
    sum_of_same_group_questions = 0
    for gr in groups:
        sum_of_questions = unique_questions(gr)
        sum_of_same_questions = same_questions(gr)
        
        sum_of_group_questions += sum_of_questions
        sum_of_same_group_questions += sum_of_same_questions

    print(f'Sum of all group questions: {sum_of_group_questions}')
    print(f'Sum of all same group questions: {sum_of_same_group_questions}')

def unique_questions(group_questions):
    return len(unique_questions_as_set(group_questions))

def same_questions(group_questions):
    unique = unique_questions_as_set(group_questions)

    same = 0
    for u in unique:
        found = 0
        for questions in group_questions:
            if u in questions:
                found += 1
        if found == len(group_questions):
            same += 1
    return same

def unique_questions_as_set(group_questions):
    return set(''.join([i for i in group_questions]))

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
