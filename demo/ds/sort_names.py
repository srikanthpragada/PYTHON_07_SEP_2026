# Take names until end is given and print them in sorted order

names = []

while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    # check whether name is already present in names
    for n in names:
        if n.lower() == name.lower():
            break
    else: # name is not found
        names.append(name)

names.sort()

for name in names:
    print(name)
