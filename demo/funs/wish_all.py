# Varying arguments - start argument
def wishall(*names, message = "Hello"):
    for n in names:
        print(message, n)


wishall('Garry', 'Martin', message = "Hi")
wishall('Joe', 'Jack', "Li", message = "Good Morning")
wishall('Kathy', "Belinda")
