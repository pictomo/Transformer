#!/usr/bin/env python3

# Robot Mode

import sys

path = sys.argv[0]

vehicle_content = """#!/usr/bin/env python3

# Vehicle Mode

import sys

path = sys.argv[0]

vehicle_content = {0}{1}{0}
robot_content = {0}{2}{0}

triple_quotes = chr(34) + chr(34) + chr(34)
with open(path, "w") as file:
    file.write(robot_content.format(triple_quotes, vehicle_content, robot_content))
"""
robot_content = """#!/usr/bin/env python3

# Robot Mode

import sys

path = sys.argv[0]

vehicle_content = {0}{1}{0}
robot_content = {0}{2}{0}

triple_quotes = chr(34) + chr(34) + chr(34)
with open(path, "w") as file:
    file.write(vehicle_content.format(triple_quotes, vehicle_content, robot_content))
"""

triple_quotes = chr(34) + chr(34) + chr(34)
with open(path, "w") as file:
    file.write(vehicle_content.format(triple_quotes, vehicle_content, robot_content))
