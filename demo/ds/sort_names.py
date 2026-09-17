# Take names until end is given and print them in sorted order

names = []

while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    if name not in names:
        names.append(name)

names.sort()

for name in names:
    print(name)
