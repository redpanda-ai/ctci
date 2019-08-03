def solve(in_string):
    l, r = 0, len(in_string) - 1

    while l <= r:
        if in_string[l] != in_string[r]:
            return False
        l += 1
        r -= 1

    return True


tests = [
    "",
    "a",
    "abccba",
    "bcdcb",
    "abcabc"
]
if __name__ == "__main__":
    for test in tests:
        print(f"test: {test}, palindrome: {solve(test)})")
