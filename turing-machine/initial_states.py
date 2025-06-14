# lecture "automaton and formal languages"
## 2023-9 example tm 1

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


# Wolfram's 2-state 3-symbol turing machine

# states
execution_count = 0
state = 0
tape = ["0"]
head = 0

# machine
delta = {
	0: {'0': (1, '1', 1), '1': (0, '2', -1), '2': (0, '1', -1)},
	1: {'0': (0, '2', -1), '1': (1, '2', 1), '2': (0, '0', 1)}
}
initial_state = 0
goal_states = []

# tape
alphabet = ['0', '1', '2']
default_symbol = "0"
initial_tape = ['0']
initial_head = 0

## display optimized

# states
execution_count = 0
state = 0
tape = ["0"]
head = 0

# machine
delta = {
	0: {' ': (1, '.', 1), '.': (0, '#', -1), '#': (0, '.', -1)},
	1: {' ': (0, '#', -1), '.': (1, '#', 1), '#': (0, ' ', 1)}
}
initial_state = 0
goal_states = []

# tape
alphabet = [' ', '.', '#']
default_symbol = "0"
initial_tape = ['0']
initial_head = 0