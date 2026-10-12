while True:
    try:
        n = int(input("Enter a number :"))
        print(100 // n)
        break
    except ValueError:
        print('Sorry! Invalid input entered! Try again!')
    except ZeroDivisionError:
        print('Sorry! Zero is not valid! Try again!')

print("The End!")

