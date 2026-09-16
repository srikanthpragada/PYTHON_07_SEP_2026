# Display all perfect numbers from 1 to 1000

for num in range(1, 10000):
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i

    if total == num:
        print(num, end = ' ')

