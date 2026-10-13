try:
    with open("names.txt", "rt") as f:
        for line in f.readlines():
            print(line, end='')
except Exception as ex:
    print('Error :', ex)
