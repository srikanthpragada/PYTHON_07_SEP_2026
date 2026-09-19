names = ["Larry Page", "Larry Ellison", "Van Rossum", "Andrew NG", "Mark"]

total = 0
for name in names:
    total += len(name)

avg_len = total // len(names)

for name in names:
    if len(name) > avg_len:
        print(name)
