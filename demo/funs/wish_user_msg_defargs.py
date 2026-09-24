def wish(user = 'Guest', message = 'Hi'):
    print(message, user)

wish()
wish('Larry')     # Positional args
wish("Scott", "Hello")
wish(message="Hello", user="James")  # keyword args
wish(user="Martin")  # keyword args

# wish(10,20)
