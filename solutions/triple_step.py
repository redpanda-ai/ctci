from collections import Counter


def triple_step(steps):
    ways = [0, 1, 2, 4]
    for i in range(len(ways), steps + 1):
        # ways.append(ways[i - 1] + ways[i - 2] + ways[i - 3])
        ways.append(sum(ways[i-3:i]))

    return ways[steps]


if __name__ == "__main__":
    tests = list(range(0, 10))
    for test in tests:
        print(f"With {test} steps: {triple_step(test)} ways.")
