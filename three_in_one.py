class ManyInOne:
    def __init__(self, stack_count):
        self.data = []
        self.tail_list = [None] * stack_count
        self.last_stack_id = None


    def push(self, stack_id, element, report=True):
        old_index = self.tail_list[stack_id]
        self.data.append((stack_id, element, old_index))
        self.tail_list[stack_id] = len(self.data) - 1
        self.last_stack_id = stack_id
        if report:
            print(f"Pushed {element} onto stack {stack_id}")

    def fix_tail(self, target_stack_id):
        """Swap the last_stack_id with the """
        if target_stack_id == self.last_stack_id:
            return
        self.data[self.tail_list[self.last_stack_id]], self.data[self.tail_list[target_stack_id]] = self.data[self.tail_list[target_stack_id]], self.data[self.tail_list[self.last_stack_id]]
        self.tail_list[self.last_stack_id], self.tail_list[target_stack_id] = self.tail_list[target_stack_id], self.tail_list[self.last_stack_id]
        self.last_stack_id = target_stack_id

    def pop(self, stack_id, report=True):
        if self.tail_list[stack_id] is None:
            print(f"Cannot pop from empty stack #{stack_id}")
            return None
            # raise Exception(f"Cannot pop from empty stack #{stack_id}")

        self.fix_tail(stack_id)
        _, result, old_index = self.data.pop()
        #self.last_stack_id = None or self.data[-1][0]
        if len(self.data) > 0:
            self.last_stack_id = self.data[-1][0]
        else:
            self.last_stack_id = None

        self.tail_list[stack_id] = old_index
        if report:
            print(f"Popped {result} from stack {stack_id}")
        return result

    def report(self):
        print(p)




    def __repr__(self):
        return f"\n\tdata: {self.data}\n\tindices {self.tail_list}]\n\tlast_stack_id: {self.last_stack_id}\n"


p = ManyInOne(4)
p.report()
p.push(0, "a")
p.push(0, "b")
p.push(0, "c")
p.push(1, "d")
p.push(2, "e")
p.push(3, "f")

p.report()
p.pop(0)
p.report()
p.pop(1)
p.pop(1)
p.pop(2)
p.report()
p.pop(0)
p.pop(0)
p.pop(0)
p.pop(3)
p.report()