def permutation(lst):
    """returns a list of lists"""
    if len(lst) == 0:
        return []  # empty list of lists

    if len(lst) == 1:
        return [lst]  # list of lists with a single list

    list_of_lists = []
    for i in range(len(lst)):
        m = lst[i]

        rem = lst[:i] + lst[i+1:]

        for p in permutation(rem):
            list_of_lists.append([m] + p)

    return list_of_lists


data = list('12345')

for p in permutation(data):
    print(p)