# take 10 numbers or until 0 is given and display avg

count = total = 0

for i in range(10):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    total += num
    count += 1

print('Average :', total // count)



