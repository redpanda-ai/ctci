def edit_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # s2 is longer than s1

    distances = range(len(s1) + 1)

    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))

        distances = distances_
    return distances[-1]

tests = [
    ("cat", "wolf"),
    ("can", "can"),
    ("abc", "aba"),
    ("ababa", "ababa"),
    ("abcab", "bbcbb")
]


def ed_3(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    #print(tbl)
    return tbl[i,j]


def ed_4(s1, s2):
    m, n = len(s1) + 1, len(s2) + 1
    tbl = {}

    for i in range(m):
        tbl[i, 0] = i
    for j in range(n):
        tbl[0, j] = j

    for i in range(1, m):
        for j in range(1, n):
            cost = 0
            if s1[i - 1] is not s2[j - 1]:
                cost = 1
            tbl[i, j] = min(
                tbl[i - 1, j - 1] + cost,
                tbl[i - 1, j] + 1,
                tbl[i, j - 1] + 1)

    return tbl[m - 1, n - 1]


def ed_5(s1, s2):
    m, n = len(s1) + 1, len(s2) + 1
    dp = {}
    for i in range(m):
        dp[i, 0] = i
    for j in range(n):
        dp[0, j] = j

    for i in range(1, m):
        for j in range(1, n):
            cost = 1
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            dp[i, j] = min(
                dp[i - 1, j - 1] + cost,
                dp[i - 1, j] + 1,
                dp[i, j - 1] + 1
            )

    return dp[m - 1, n - 1]





def edit_distance_2(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for line in dp:
        print(line)

    for i in range(m + 1):
        for j in range(n + 1):
            if i is 0:
                dp[i][j] = j
            elif j is 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-i][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    for line in dp:
        print(line)

    return dp[m][n]


for s1, s2 in tests:
    ed = edit_distance(s1, s2)
    print(f"S1: {s1}, S2:{s2}, edit_distance: {ed}")
    #print(edit_distance_2(s1, s2))
    #print(ed_3(s1, s2))
    print(ed_5(s1, s2))


print("done")