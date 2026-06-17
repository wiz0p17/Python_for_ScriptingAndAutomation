import re

text = "ERROR Database Connection Failed"

match = re.search("ERROR",text)

print(match)


text = """
ERROR Disk Full
ERROR Database Failed
ERROR Connection Lost
"""

matches = re.findall("ERROR",text)

print(matches)

print(len(matches))

#Step 5: Wildcards
"""
Suppose:

ERROR Database Failed
ERROR Disk Full
ERROR Memory Leak"""

value = re.findall(r"ERROR.*",text)

print(value)


text = """
192.168.1.10
10.0.0.15
"""

ips = re.findall(r"\d+\.\d+\.\d+\.\d+",text)

print(ips)

text = """
admin@company.com
vivek@gmail.com
"""

value = re.findall(r"\S+@\S+",text)

print(value)

text = """
2026-06-25
2026-06-26
"""

value = re.findall(r"\d{4}-\d{2}-\d{2}",text)

print(value)

"""import re

with open(
    "server.log"
) as file:

    log = file.read()

errors = re.findall(
    r"ERROR.*",
    log
)

for error in errors:

    print(error)"""