from bitstring import BitArray

def solve(arr):
    bf = BitArray(32000)
    for num in arr:
        if not bf[num]:
            bf.set(True, num)
        else:
            print(num)

tests = [
    [0, 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 10],
    [0, 1, 1, 2, 3, 2, 1, 5, 4]
]

for test in tests:
    solve(test)
