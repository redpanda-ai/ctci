from collections import deque

class Solution:
    def sorted_merge(self, a: deque, b: deque):
        c = []
        while a and b:
            print(a, b)
            if a[0] <= b[0]:
                c.append(a.popleft())
            else:
                c.append(b.popleft())

        remainder = a or b
        c.extend(remainder)
        a = c
        return a


a = deque([1, 2, 4])
b = deque([1, 2, 3])
s = Solution()
c = s.sorted_merge(a, b)

print(c)