class Box:
    def __init__(self, length, height, width):
        self.length = length
        self.width = width
        self.height = height

    def can_be_above(self, other):
        if other.length > self.length and other.height > self.height and other.width > self.width:
            return True
        return False

    def __repr__(self):
        return f"(l: {self.length}, w: {self.width}, h: {self.height})"


def create_stack(unsorted_boxes):
    # sort boxes by height
    boxes = sorted(unsorted_boxes, key=lambda x: x.height, reverse=True)
    for box in boxes:
        print(box)
    stack_map = [0] * len(boxes)
    return helper(boxes, None, 0, stack_map)


def helper(boxes, bottom, offset, stack_map):
    if offset >= len(boxes):
        return 0

    new_bottom = boxes[offset]
    height_with_bottom = 0
    if bottom is None or new_bottom.can_be_above(bottom):
        if stack_map[offset] == 0:
            stack_map[offset] = helper(boxes, new_bottom, offset + 1, stack_map)
            stack_map[offset] += new_bottom.height
        height_with_bottom = stack_map[offset]

    height_without_bottom = helper(boxes, bottom, offset + 1, stack_map)

    return max(height_with_bottom, height_without_bottom)




if __name__ == "__main__":
    boxes = [
        Box(3, 4, 2),
        Box(5, 9, 7),
        Box(1, 3, 6),
        Box(2, 8, 3),
        Box(1, 1, 1),
        Box(5, 6, 4),
        Box(6, 10, 15)
    ]
    print(create_stack(boxes))

