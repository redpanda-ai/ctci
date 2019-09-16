class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data}"


a = Node()
a.next = Node(data=1)
a.next.next = Node(data=2)
a.next.next.next = Node(data=3)


def kth_to_last_2(node, k):
    runner = node
    answer = None

    for i in range(k):
        if runner.next:
            runner = runner.next
        else:
            return None

    answer = node

    while runner.next:
        runner = runner.next
        answer = answer.next

    return answer


def kth_to_last(node, k):
    if k <= 0:
        return None
    answer = node
    runner = node
    counter = k
    while runner:
        if counter == 0:
            answer = answer.next
        else:
            counter -= 1
        runner = runner.next

    if counter == 0:
        return answer
    return None



class Solution:
    def solver(self, k, linked_list):
        if k <= 0:
            return Node(data=f"k must be greater than 0, {k} is invalid")

        runner = linked_list.next
        counter = 0
        while runner:
            counter += 1
            runner = runner.next

        runner = linked_list.next
        target = counter - k

        if target < 0:
            return Node(data=f"Undefined, there are not {k} elements in the linked list")

        counter = 0

        while runner:
            if target == counter:
                return runner
            counter += 1
            runner = runner.next


s = Solution()

tests = [0, 1, 2, 3, 4, 5]
for k in tests:
    # print(f"The {k}th-to-last Node is {s.solver(k, a)}, {kth_to_last(a, k)}")
    print(f"The {k}th-to-last Node is {kth_to_last(a, k)}")
    print(f"The {k}th-to-last Node is {kth_to_last_2(a, k)}")

