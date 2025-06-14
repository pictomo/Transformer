#!/usr/bin/env python3

from time import sleep

# machine
delta = {0: {"0": (0, "X", 1), "1": (1, "X", 1)}, 1: {"1": (1, "X", 1), "B": (2, "B", -1)}}
initial_state = 0
goal_states = [2]

# tape
alphabet = ["0", "1", "X", "B"]
default_symbol = "B"
initial_tape = ["0", "1", "1"]
initial_head = 0

# state
accepted = False
tape = initial_tape
state = initial_state
head = initial_head

def tape_str(tape, head):
    s = "".join(tape)
    return s[:head] + "\033[1m" + s[head] + "\033[0m" + s[head+1:]

if state in goal_states:
	accepted = True
print("Accepted" if accepted else "Rejected", tape_str(tape, head))
sleep(1)

while True:
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
        if state in goal_states:
            accepted = True
        print("Accepted" if accepted else "Rejected", tape_str(tape, head))
        sleep(1)
    else:
        print("No transition found.")
        break