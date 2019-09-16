class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enq(self, elem):
        self.in_stack.append(elem)

    def deq(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            raise Exception("Invalid to deq an empty MyQueue")

        return self.out_stack.pop()


if __name__ == "__main__":
    q = MyQueue()
    q.enq("A")
    q.enq("B")
    q.enq("C")
    print(q.deq())
    q.enq("D")
    print(q.deq())
    print(q.deq())
    print(q.deq())
    print(q.deq())