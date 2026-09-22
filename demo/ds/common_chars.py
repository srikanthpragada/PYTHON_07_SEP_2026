names = ['Jack', 'James', 'Jason', 'Jackson']

uchars = set(names[0])

for name in names[1:]:
    uchars = uchars & set(name)


print(uchars)
print("".join(uchars))



