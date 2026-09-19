langs = ['Python', 'Java', 'JavaScript', 'c#']
vers = [3.14, 25, 2024]

# for idx in range(len(langs)):
#     print(langs[idx], vers[idx])

for l, v in zip(langs, vers):
    print(l, v)
