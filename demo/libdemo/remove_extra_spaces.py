st = """This is     to    test
how to   remove extra    spaces between     word
"""

import re

newst = re.sub(r" +", " ", st)

print(newst)
