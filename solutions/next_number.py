def get_ones(num):
    ones = 0
    while num > 0:
        num = num & (num - 1)
        ones += 1

    return ones


def next_number(num):
    target_ones = get_ones(num)

    lower = None
    for l in range(num - 1, 0, -1):
        if get_ones(l) == target_ones:
            lower = l
            break

    higher = None
    for h in range(num + 1, (num << 1) + 1, 1):
        if get_ones(h) == target_ones:
            higher = h
            break

    return lower, higher


tests = list(range(10))
for test in tests:
    l, h = next_number(test)
    print(f"Input: {test}, lower: {l}, higher: {h}")
