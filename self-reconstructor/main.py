#!/usr/bin/env python3

import sys

path = sys.argv[0]

content = """#!/usr/bin/env python3

import sys

path = sys.argv[0]

content = {0}{1}{0}

with open(path, "w") as file:
    file.write(content.format(chr(34) + chr(34) + chr(34), content))
"""

with open(path, "w") as file:
    file.write(content.format(chr(34) + chr(34) + chr(34), content))
