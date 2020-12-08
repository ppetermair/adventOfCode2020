#!/usr/bin/env python3

from os import path

def main():

    commands = get_input()
    broken_result = run_commands(commands, -1)
    fixed_result = ()

    for idx, command in enumerate(commands):
        if command.startswith('noop') or command.startswith('jmp'):
            result = run_commands(commands, idx)
            if result[0]:
                fixed_result = result
                break

    print(f'Broken commands accumlator value: {broken_result[1]}')
    print(f'Fixed commands accumlator value: {fixed_result[1]}')

def run_commands(commands, flip_index):
    accumulator = 0
    index = 0
    executed_indizes = []

    while True:
        command = commands[index]
        if index == flip_index:
            command = command.replace('noop', '+tmp+').replace('jmp', 'noop').replace('+tmp+', 'jmp')

        if command.startswith('acc'):
            accumulator += int(command.split(' ')[1])
            index += 1
        elif command.startswith('jmp'):
            index += int(command.split(' ')[1])
        else: # noop
            index += 1

        if index in executed_indizes or index > len(commands):
            return (False, accumulator)
        elif index == len(commands):
            return (True, accumulator)

        executed_indizes.append(index)


def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
