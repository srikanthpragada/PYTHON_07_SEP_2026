# Take a number and display whether it is prime

num = int(input("Enter a number :"))

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(f'Not a prime as it has {i} as factor')
        break
else:
    print('Prime Number!')


