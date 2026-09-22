names = ['Joe', 'Jack', 'Larry', 'Jason', 'Peter']

uchars = set()

for name in names:
    uchars = uchars | set(name)


print(uchars)



