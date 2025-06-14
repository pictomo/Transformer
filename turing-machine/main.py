#!/usr/bin/env python3

# states
execution_count = 378
state = 0
tape = ['.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '#', '.', '.', '#', '#', '.', '#']
head = 19

# machine
delta = {0: {' ': (1, '.', 1), '.': (0, '#', -1), '#': (0, '.', -1)}, 1: {' ': (0, '#', -1), '.': (1, '#', 1), '#': (0, ' ', 1)}}
initial_state = 0
goal_states = []

# tape
alphabet = [' ', '.', '#']
default_symbol = " "
initial_tape = [' ']
initial_head = 0

import sys

path = sys.argv[0]
content = """#!/usr/bin/env python3

# states
execution_count = {5}
state = {6}
tape = {7}
head = {8}

# machine
delta = {9}
initial_state = {10}
goal_states = {11}

# tape
alphabet = {12}
default_symbol = "{13}"
initial_tape = {14}
initial_head = {15}

import sys

path = sys.argv[0]
content = {1}{0}{1}

def tape_str(tape, head):
    s = "".join(tape)
    return s[:head] + "{2}033[1m" + s[head] + "{2}033[0m" + s[head+1:]

if execution_count == 0:
    print(str(execution_count).zfill(3), "Accepted" if state in goal_states else "Rejected", state, tape_str(tape, head))

next = delta.get(state, {3}{4}).get(tape[head], False)
if next:
    state = next[0]
    tape[head] = next[1]
    head += next[2]
    if head == len(tape):
        tape.append(default_symbol)
    elif head == -1:
        tape.insert(0, default_symbol)
        head = 0
    execution_count += 1
    print(str(execution_count).zfill(3), "Accepted" if state in goal_states else "Rejected", state, tape_str(tape, head))
else:
    print("No transition found.")
    sys.exit(1)

with open(path, "w") as file:
    file.write(
        content.format(content, chr(34) * 3, chr(92), chr(123), chr(125), execution_count, state, tape, head, delta, initial_state, goal_states, alphabet, default_symbol, initial_tape, initial_head)
    )
"""

def tape_str(tape, head):
    s = "".join(tape)
    return s[:head] + "\033[1m" + s[head] + "\033[0m" + s[head+1:]

if execution_count == 0:
    print(str(execution_count).zfill(3), "Accepted" if state in goal_states else "Rejected", state, tape_str(tape, head))

next = delta.get(state, {}).get(tape[head], False)
if next:
    state = next[0]
    tape[head] = next[1]
    head += next[2]
    if head == len(tape):
        tape.append(default_symbol)
    elif head == -1:
        tape.insert(0, default_symbol)
        head = 0
    execution_count += 1
    print(str(execution_count).zfill(3), "Accepted" if state in goal_states else "Rejected", state, tape_str(tape, head))
else:
    print("No transition found.")
    sys.exit(1)

with open(path, "w") as file:
    file.write(
        content.format(content, chr(34) * 3, chr(92), chr(123), chr(125), execution_count, state, tape, head, delta, initial_state, goal_states, alphabet, default_symbol, initial_tape, initial_head)
    )
