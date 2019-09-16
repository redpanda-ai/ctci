def recursive_multiply(first, second, shifts=0):
    if second == 1:
        return first << shifts
    if second & 1 == 1:
        return (first << shifts) + recursive_multiply(first, second >> 1, shifts + 1)
    else:
        return 0 + recursive_multiply(first, second >> 1, shifts + 1)


def rec_mul(m1, m2):
    if m2 == 0:
        return 0
    if m2 & 1 == 1:
        return m1 + rec_mul(m1 << 1, m2 >> 1)
    else:
        return rec_mul(m1 << 1, m2 >> 1)

tests = [
    [1, 4],
    [1, 1],
    [5, 1],
    [16, 16],
    [12, 12]
]
for a, b in tests:
    c = recursive_multiply(a, b)
    d = rec_mul(a, b)

    print(f"{a} * {b} = {c}, {d}")