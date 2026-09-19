
names = ['java', 'c', 'java', 'c', 'python', 'c#']

processed_names = []
for name in names:
    if name not in processed_names:
        print(f"{name:10}  {names.count(name)}")
        processed_names.append(name)
