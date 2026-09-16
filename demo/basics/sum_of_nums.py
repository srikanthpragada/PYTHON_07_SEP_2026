# take 10 numbers or until 0 is given and display total

total = 0
for i in range(10):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    total += num

print('Total :', total)



