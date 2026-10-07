class Stack:
    pass


s = Stack()
s.push(10)
s.push(20)
print(s.peek())   # 20
print(s.pop())    # 20
print(s.length()) # 1
print(s.isempty()) # False
