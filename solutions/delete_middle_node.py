class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        r = self
        result = ""
        while r:
            result += r.data + " -> "
            r = r.next

        return result

a = Node(data='a')
a.next = Node(data='b')
a.next.next = Node(data='c')
a.next.next.next = Node(data='d')
a.next.next.next.next = Node(data='e')


print(a)

class Solution:
    def solver(self, listy, target):
        print(f"Removing '{target}' from middle of {listy}")
        r = s = listy
        first = True
        while r:
            if first:
                r = r.next
                first = False
            elif r.next:
                if r.data == target:
                    s.next = r.next
                    return
                else:
                    r = r.next
                    s = s.next
            else:
                return


s = Solution()
print(a)
s.solver(a, 'c')
print(a)
s.solver(a, 'a')
print(a)
s.solver(a, 'e')
print(a)
s.solver(a, 'b')
print(a)