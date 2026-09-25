
# Keyword-only arguments
def wish(*, message, user):
    print(message, user)


wish('Larry', 'Hi')
wish(message="Hello", user="Andy")
