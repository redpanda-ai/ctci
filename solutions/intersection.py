class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        result = []
        r = self
        while r:
            result.append(r.data)
            r = r.next
        return "[" + ", ".join(result) + "]"


def intersection(list_a, list_b):
    runner_a, runner_b = list_a, list_b

    while runner_a and runner_b:
        runner_a = runner_a.next
        runner_b = runner_b.next

    while runner_a:
        runner_a = runner_a.next
        list_a = list_a.next

    while runner_b:
        runner_b = runner_b.next
        list_b = list_b.next

    while list_a and list_b:
        if list_a == list_b:
            # print(f"Your lists intersect at {list_a.data}")
            return list_a
        list_a = list_a.next
        list_b = list_b.next

    # print(f"Your lists do not intersect")
    return None


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    r = Node("r")
    s = Node("s")
    t = Node("t")
    u = Node("u")
    r.next = s
    s.next = t
    t.next = u
    u.next = d

    v = Node("v")
    w = Node("w")
    x = Node("x")
    v.next = w
    w.next = x

    list_tests = [
        (a, r, d),
        (a, a, a),
        (r, a, d),
        (a, c, c),
        (a, v, None)
    ]

    for list_1, list_2, expectation in list_tests:
        print(f"\nlist_1: {list_1}\nlist_2: {list_2}\nexpectation: {expectation}")
        if expectation is intersection(list_1, list_2):
            print("pass")
        else:
            print("fail")
