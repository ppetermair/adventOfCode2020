#!/usr/bin/env python3

from os import path
import re
import ast

class SwapOperators(ast.NodeTransformer):
    def visit_Add(self, node):
        return ast.Mult()
    def visit_Mult(self, node):
        return ast.Add()

def main():
    sum = 0
    sum_with_precedence = 0
    for line in get_input():
        line = line.replace(' ', '')
        result = evaluate(line)
        result_with_precedence = evaluate_with_precedence(line)
        sum += result
        sum_with_precedence += result_with_precedence
    print(f'Sum: {sum}')
    print(f'Sum with + precedence: {sum_with_precedence}')

def evaluate(line):
    while not re.match(r'^\d+$', line):
        check_expression = re.search(r'\d+[+*]\d+', line)
        if check_expression:
            expression = check_expression.group()
            solved = solve_expression(expression)
            line = line.replace(expression, str(solved), 1)
        check_parentheses = re.search(r'\(\d+\)', line)
        if check_parentheses:
            expression = check_parentheses.group()
            line = line.replace(expression, expression[1:-1])
    return int(line)

def evaluate_with_precedence(line):
    line = line.replace('*', 'TMP').replace('+', '*').replace('TMP', '+')
    parsed = ast.parse(line, mode='eval')
    visited = SwapOperators().visit(parsed)
    return eval(compile(visited,'',mode='eval'))

def solve_expression(expression):
    if '+' in expression:
        return int(expression.split('+')[0]) + int(expression.split('+')[1])
    else: # '*'
        return int(expression.split('*')[0]) * int(expression.split('*')[1])

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
