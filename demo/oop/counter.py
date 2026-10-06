class Counter:
    #constructor
    def __init__(self, value = 0):
        # Object Attributes
        self.value = value

    # Methods
    def inc(self, step = 1):
        self.value += step

    def dec(self, step = 1):
        self.value -= step

    def getvalue(self):
        return self.value

# Using class
c = Counter() #Create an object
c.inc() # increment by 1
c.inc(10)
print(c.getvalue())
#print(c.value)

c2 = Counter(100) #Create an object
c2.inc()
print(c2.getvalue())



