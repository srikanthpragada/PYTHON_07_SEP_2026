class Time:
    def __init__(self, h=0, m=0, s=0):
        # Initializes hours, mins and seconds
        self.h = h
        self.m = m
        self.s = s

    def total_seconds(self):
        # Returns total no. of seconds
        return self.h * 3600 + self.m * 60 + self.s

    def __eq__(self, other):
        return self.total_seconds() == other.total_seconds()

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __bool__(self):
        # Returns false if hours, mins and seconds are 0 otherwise true
        return self.h != 0 or self.m != 0 or self.s != 0

    def __gt__(self, other):
        return self.total_seconds() > other.total_seconds()

    def __add__(self, other):
        return Time(self.h + other.h, self.m + other.m, self.s + other.s)

t1 = Time(1, 20, 30)
t2 = Time(10, 20, 30)
print(t1) # calls t1.__str__()
print(t1 == t2) # calls t1.__eq__(t2)
t3 = Time() # h,m,s are set to zeros
if t3: # calls t3.__bool__()
    print("True")
else:
    print("False")
print (t1 < t2) # calls t1.__gt__(t2)
t4 = t1 + t2 # calls t1.__add__(t2)
print(t4)