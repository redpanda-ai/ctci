from collections import Counter

class Solution:
    def solver(self, a, b):
        h = {}
        for letter in a:
            if letter not in h:
                h[letter] = 1
            else:
                h[letter] += 1

        for letter in b:
            if letter not in h:
                return False
            else:
                h[letter] -= 1
            if h[letter] == 0:
                del h[letter]

        if not h:
            return True
        return False


s = Solution()

tests = [
    ["taco", "cato"],
    ["", ""],
    ["aaaa", "aaa"],
    ["abcd", "abce"]
]

for a, b in tests:
    print(f"A: {a}, B: {b}, answer : {s.solver(a, b)}")
