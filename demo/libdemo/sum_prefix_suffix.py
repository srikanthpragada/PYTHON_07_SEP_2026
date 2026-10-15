import re

st = "122xyz8923"

# look for first number
fn = re.search(r"^\d+", st)
if fn is None:
    print("Invalid Format!")
    exit()
ln = re.search(r"\d+$", st)
if ln is None:
    print("Invalid Format!")
    exit()

total =  int(fn.group()) + int(ln.group())
print(total)