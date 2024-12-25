#!/usr/bin/env python3

# Multi Type

import sys

path = sys.argv[0]

multi_content = """#!/usr/bin/env python3

# Multi Type

import sys

path = sys.argv[0]

multi_content = {0}{1}{0}
sky_content = {0}{2}{0}
power_content = {0}{3}{0}

with open(path, "w") as file:
    file.write(sky_content.format(chr(34) + chr(34) + chr(34), multi_content, sky_content, power_content))
"""
sky_content = """#!/usr/bin/env python3

# Sky Type

import sys

path = sys.argv[0]

multi_content = {0}{1}{0}
sky_content = {0}{2}{0}
power_content = {0}{3}{0}

with open(path, "w") as file:
    file.write(power_content.format(chr(34) + chr(34) + chr(34), multi_content, sky_content, power_content))
"""
power_content = """#!/usr/bin/env python3

# Power Type

import sys

path = sys.argv[0]

multi_content = {0}{1}{0}
sky_content = {0}{2}{0}
power_content = {0}{3}{0}

with open(path, "w") as file:
    file.write(multi_content.format(chr(34) + chr(34) + chr(34), multi_content, sky_content, power_content))
"""

with open(path, "w") as file:
    file.write(sky_content.format(chr(34) + chr(34) + chr(34), multi_content, sky_content, power_content))
