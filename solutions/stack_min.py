from collections import deque

class MyStack:
    def __init__(self):
        self.data = deque()
        self.min = None

    def push(self, element):
        self.data.append((element, self.min))
        if not self.min or element < self.min:
            self.min = element

    def pop(self):
        if self.data:
            d, self.min = self.data.pop()
            return d
        return None

    def get_min(self):
        return self.min

    def __repr__(self):
        return f"data: {self.data}, min: {self.min}"

m = MyStack()

print(m)
m.push(10)
print(m)
m.push(11)
print(m)
m.push(9)
print(m)
print(m.pop())
print(m)
print(m.pop())
print(m)
print(m.pop())
print(m)
print(m.pop())
print(m)
