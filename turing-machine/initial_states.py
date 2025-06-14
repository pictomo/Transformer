# lecture "automaton and formal languages"
# 2023-9 example tm 1

# states
execution_count = 0
state = 0
tape = ["0", "1", "1"]
head = 0

# machine
delta = {0: {'0': (0, 'X', 1), '1': (1, 'X', 1)}, 1: {'1': (1, 'X', 1), 'B': (2, 'B', -1)}}
initial_state = 0
goal_states = [2]

# tape
alphabet = ['0', '1', 'X', 'B']
default_symbol = "B"
initial_tape = ['0', '1', '1']
initial_head = 0

