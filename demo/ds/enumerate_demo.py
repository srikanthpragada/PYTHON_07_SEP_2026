l = [1, 4, 5, 29, 30]

# idx = 0
# for n in l:
#     print(idx, n)
#     idx += 1


# Unpack tuples given by enumerate()
for idx, v in enumerate(l, start=1):
    print(idx, v)
