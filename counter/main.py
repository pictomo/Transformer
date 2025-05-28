#!/usr/bin/env python3

execution_count = 0

import sys

path = sys.argv[0]
content = """#!/usr/bin/env python3

execution_count = {2}

import sys

path = sys.argv[0]
content = {0}{1}{0}

with open(path, "w") as file:
    file.write(
        content.format(chr(34) + chr(34) + chr(34), content, execution_count+1)
    )
"""

with open(path, "w") as file:
    file.write(
        content.format(chr(34) + chr(34) + chr(34), content, execution_count + 1)
    )
