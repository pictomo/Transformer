#!/usr/bin/env python3

# Robot Mode

import sys

path = sys.argv[0]

content = """#!/usr/bin/env python3

# {2} Mode

import sys

path = sys.argv[0]

content = {0}{1}{0}

triple_quotes = chr(34) + chr(34) + chr(34)
with open(path, "w") as file:
    file.write(content.format(triple_quotes, content, {4}{3}{4}, {4}{2}{4}, chr(34)))
"""

triple_quotes = chr(34) + chr(34) + chr(34)
with open(path, "w") as file:
    file.write(content.format(triple_quotes, content, "Vehicle", "Robot", chr(34)))
