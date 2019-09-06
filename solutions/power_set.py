def get_power_set(arr):
    n = 2 ** len(arr)
    ps = []

    for i in range(n):
        s = []
        k = 0
        while (i >> k) > 0:
            if (i >> k) & 1:
                s.append(arr[k])
            k += 1
        ps.append(s)

    return ps


if __name__ == "__main__":
    a = ["a", "b", "c", "d", "e", "f"]
    ps = get_power_set(a)
    for ind, s in enumerate(ps):
        print(ind, s)