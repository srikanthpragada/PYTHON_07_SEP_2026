st = "How do you do"

d = {}
for c in st:
    if c not in d:
        d[c] = st.count(c)

# Another way to do it
d2 = {}
for c in st:
    d2[c] = d2.get(c, 0) + 1

#print(d2)

for c, cnt in sorted(d.items()):
    print(c, cnt)
