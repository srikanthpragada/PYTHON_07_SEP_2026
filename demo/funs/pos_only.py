# Positional-only arguments
def wish(name, message, /):
    print(message, name)


wish('Larry', 'Hi')
# wish(message="Hello", user="Andy")
