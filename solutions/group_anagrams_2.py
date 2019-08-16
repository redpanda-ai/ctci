from collections import defaultdict


def group_anagrams(anas):
    groups = defaultdict(list)
    for word in anas:
        x = "".join(sorted(word))
        groups[x].append(word)

    solution = []
    for key in groups.keys():
        solution.extend(groups[key])

    print(solution)


test = ["ABC", "BAC", "DEF", "FED", "FFE", "FOO"]
group_anagrams(test)