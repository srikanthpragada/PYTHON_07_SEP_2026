try:
    n = int(input("Enter a number :"))
    print(100 // n)
except ValueError:
    print('Invalid Number')
except Exception as ex:
    print(ex)
