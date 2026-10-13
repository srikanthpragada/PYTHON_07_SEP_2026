import os

names = ['George', 'Jack', 'Larry', 'Scott', 'Jimmy']

# os.path.exists("names.txt")
with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")
