
#done without the benefit of an editor

street = [
    {‘grocer’: True},
{‘school’: True’, ‘museum’: True},
{},
{},
{‘bookstore’: True},
{‘museum’: True},
{‘grocer’: True}
]
requirements = {
‘bookstore’: True,
‘grocer’: True,
‘school’: True
}
Expected
answer
block
2


def solution(street, requirements):
    scores = [{}] * len(streets)
    # scores = [5, 0, 0, 0, 0, 0, 0]
    for i in range(len(street)):
        for key in requirements:
            my_req = {key: 0}

        for j in range(len(street)):
            for key in street[j]:
                if key in my_req:
                    my_req[key] = min(my_req[key], math.abs(j - i))
        scores[i] = my_req

    for key in


best_score = len(street) * 100
best_index = -1

best_average_dist = len(street) * 100
best_index = -1
for k in scores:
    max_distance = 0
    for key in scores[k]:
        max_distance = max(max_distance, scores[k][key])
        if max_distance < best_average_dist:
            best_average_dit = max_distance
            best_index = k

    for k in scores:
        my_score = 0
        for key in scores[k]:
            my_score += scores[k][key]

        if my_score < best_score:
            best_index = k
            best_score = scores[k]

    return best_score, best_index

if __name__ == “__main__”:
    tests = [
        [], {‘bookstore’: True}, (0, -1),
                                 street, requirements, (?, 2),
                                 [[{‘grocer’: True, museum: True},
    []], {‘campus’: True}, (200, -1)
    ]

    for street, requirements, expectation in tests:
        if
    expectations = solution(street, requirements):
    print(True)
    else:
    print(False)




