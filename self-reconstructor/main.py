#!/usr/bin/env python3

import sys

path = sys.argv[0]
# overwrite the file with its own content
with open(path, "r") as file:
    content = file.read()
with open(path, "w") as file:
    file.write(content)
