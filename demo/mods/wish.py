import sys

if len(sys.argv) < 2:
    name = "Guest"
else:
    name = sys.argv[1]

print('Hello', name)
