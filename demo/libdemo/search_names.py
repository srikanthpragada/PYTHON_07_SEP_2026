name = input("Enter name : ")

f = open("names.txt", "rt")

while True:
    line = f.readline().strip()
    if line == "":   # EOF
        print("Sorry! Name not found!")
        break

    if line == name:
        print('Found!')
        break

f.close()


f.close()
