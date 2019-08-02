from collections import Counter


def three_step(n: int, h: Counter):
    if n < 1:
        return
    if n == 1:
        h[n] += 1
    if n >= 1:
        three_step(n - 1, h)
    if n >= 2:
        three_step(n - 2, h)
    if n >= 3:
        three_step(n - 3, h)


c = Counter()

tests = [1, 2, 3, 4, 10]
for test in tests:
    three_step(test, c)
    print(f"There are {c[1]} ways to reach {test} steps")
    print(c)