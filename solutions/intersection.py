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


def intersection_new(list_a, list_b):
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
            print(f"Your lists intersect at {list_a.data}")
            return list_a
        list_a = list_a.next
        list_b = list_b.next

    print(f"Your lists do not intersect")
    return None


def intersection(list_1, list_2):
    print(f"\nList 1: {list_1}")
    print(f"List 2: {list_2}")

    r1, r2 = list_1, list_2

    while r1 and r2:
        r1 = r1.next
        r2 = r2.next

    longer, shorter, runner = list_1, list_2, r1
    if r2:
        longer, shorter, runner = list_2, list_1, r2

    while runner:
        longer = longer.next
        runner = runner.next

    while longer and shorter:
        if longer == shorter:
            print(f"Lists intersect at {longer.data}")
            return longer
        longer = longer.next
        shorter = shorter.next

    print(f"Lists do not intersect")
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

    funs = [intersection, intersection_new]
    for fun in funs:
        fun(a, r)
        fun(a, a)
        fun(r, a)
        fun(a, c)
        fun(a, v)