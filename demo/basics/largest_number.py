# take numbers until 0 is given and display largest positive number

largest = 0
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
        
    if num < 0:
        continue

    if num > largest:
        largest = num

if largest == 0:
    print('Sorry! No positive number given!')
else:
    print('Largest :', largest)
