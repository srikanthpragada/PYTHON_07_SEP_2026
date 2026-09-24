def has_upper(s):
    for c in s:
        if c.isupper():
            return True

    return False

r = has_upper('hello')
print(r)
r = has_upper('iPhone')
print(r)



