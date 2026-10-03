def take_value(t):
    return t[1]  # return second element in the tuple (value)

d = {1 : 10, 4 : 2, 5: 100, 3:15, 2 : 200}

for t in sorted(d.items(), key = take_value):
    print(t)
