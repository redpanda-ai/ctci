def get_power_set(arr):
    n = len(arr)
    ps = []
    for i in range(2 ** n):
        l = []
        j = i + 0
        k = 0
        while j > 0:
            if j & 1 == 1:
                l.append(arr[k])
            j >>= 1
            k += 1
        ps.append(l)

    return ps


if __name__ == "__main__":
    a = ["a", "b", "c", "d", "e"]
    for s in get_power_set(a):
        print(s)