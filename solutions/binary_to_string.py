x = 1775
y = bin(x)
z = y[2:]
print(z)

tuples = []
last_letter = None
t = None
for letter in z:
    if last_letter == letter:
        t[1] += 1
    else:
        if t:
            tuples.append(t)
        last_letter = letter
        t = [letter, 1]
if t:
    tuples.append(t)

best_score = 0

print(tuples)
highest = 0
for i in range(len(tuples) - 2):
    a, b, c = tuples[i:i+3]
    if a[0] == c[0] == "1" and b[0] == "0" and b[1] == 1:
        print(a, b, c)
        highest = max(highest, a[1] + 1 + c[1])

print(highest)





