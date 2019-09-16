def parens(input, base=""):
    open_p = base.count("(")
    closed_p = base.count(")")

    if open_p < input:
        parens(input, base=base+"(")
    if closed_p < open_p:
        parens(input, base=base+")")
    if open_p == closed_p == input:
        print(base)


if __name__ == "__main__":
    tests = [
        3, 4
    ]
    for test in tests:
        print(f"\nTest: {test}")
        parens(test)