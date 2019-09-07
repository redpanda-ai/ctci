from collections import Counter


def triple_step(steps):
    ways = [1, 1, 2]
    for i in range(3, steps + 1):
        ways.append(ways[i - 1] + ways[i - 2] + ways[i - 3])

    return ways[steps]


if __name__ == "__main__":
    tests = [
        0,
        1,
        2,
        3,
        4,
        5
    ]
    for test in tests:
        print(f"With {test} steps: {triple_step(test)} ways.")
