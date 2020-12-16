#!/usr/bin/env python3

from os import path

def main():

    input = get_input()
    my_ticket = [int(ticket) for ticket in input.split('\n\n')[1].split('\n')[1].split(',')]

    notes = {}
    for note in input.split('\n\n')[0].split('\n'):
        description = note.split(': ')[0].strip()
        ranges = note.split(': ')[1].strip()
        values = get_values(ranges)
        notes[description] = values
    
    nearby_tickets = []
    invalid_values = []
    for line in input.split('\n\n')[2].strip().split('\n')[1:]:
        ticket = []
        valid = True
        for value in line.split(','):
            ticket.append(int(value))
            if not is_valid(int(value), notes):
                invalid_values.append(int(value))
                valid = False
        if valid:
            nearby_tickets.append(ticket)

    print(f'Invalid values sum: {sum(invalid_values)}')
    
    notes_order = {}
    while len(notes_order) < 20:

        for idx in range(20):
            ticket_values = []
            for ticket in nearby_tickets:
                ticket_values.append(ticket[idx])
            possible_note_descriptions = find_correct_note(notes, ticket_values, notes_order.values())
            if len(possible_note_descriptions) == 1:
                notes_order[idx] = possible_note_descriptions[0]
    
    departure_values = []
    for idx, note_description in notes_order.items():
        if note_description.startswith('departure'):
            departure_values.append(my_ticket[idx])
    
    result = 1
    for value in departure_values:
        result = result * value
    
    print(f'My ticket departe values multiplied: {result}')

def find_correct_note(notes, ticket_values, exclude):
    possible_note_descriptions = []
    for note_description, note_values in notes.items():
        found = True
        for ticket_value in ticket_values:
            if ticket_value not in note_values:
                found = False
                break
        if found and note_description not in exclude:
            possible_note_descriptions.append(note_description)

    return possible_note_descriptions

def is_valid(value, notes):
    for note_tickets in notes.values():
        if value in note_tickets:
            return True
    return False        

def get_values(ranges_string):
    numbers = []
    for a_range in ranges_string.split(' or '):
        for value in range(int(a_range.split('-')[0]), int(a_range.split('-')[1])+1):
            numbers.append(value)
    return numbers

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return f.read()

if __name__ == '__main__':
    main()
