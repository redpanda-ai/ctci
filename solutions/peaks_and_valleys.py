def peaks_and_valleys(arr):
    arr = sorted(arr)
    i, j = 0, len(arr) - 1
    peak = True
    while i < j:
        if peak:
            print(arr[j])
            j -= 1
        else:
            print(arr[i])
            i += 1
        peak = not peak

    print(arr[i])


test = [4, 2, 1, 3, 5, 7, 0]

print(test)
peaks_and_valleys(test)