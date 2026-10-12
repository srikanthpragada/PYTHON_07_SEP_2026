class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.isempty():
            raise ValueError('Stack is empty!')
        return self.data.pop()

    def peek(self):
        if self.isempty():
            raise ValueError('Stack is empty!')
        return self.data[-1]

    @property
    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()

    def isempty(self):
        return len(self.data) == 0


s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # 20
print(s.pop())  # 20
print(s.length)  # property
s.clear()
print(s.isempty())  # True
