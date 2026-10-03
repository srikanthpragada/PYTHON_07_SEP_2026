def first_3_chars(name):
    return  name[:3]

names = ['Andy', 'Anders', 'Jason', 'Scott', 'Mike', 'Marshall', 'Billy']

for name in sorted(names, key=lambda name: name[:3]):
    print(name)

