def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def ispalindrome(s):
    return s == s[::-1]


def haslower(s):
    for c in s:
        if c.islower():
            return True

    return False
