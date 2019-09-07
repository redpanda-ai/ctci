from bitstring import BitArray


def draw_horizontal_line(screen, width, x1, x2, y):
    """Draw a horizontal line on a screen of bits"""
    print(f"Drawing line from {x1, y} to {x2, y}")
    start = y * width * 8 + x1
    end = y * width * 8 + x2
    screen.set(1, list(range(start, end + 1)))


def print_screen(s, width):
    """Display a BitArray as a screen of bits"""
    height = len(s) // width // 8
    for e, i in enumerate(range(height)):
        line = ""
        for j in range(width):
            start_ind = i * width * 8 + (j * 8)
            line += f"{s[start_ind:start_ind+8].bin} "
        print(e, line)


if __name__ == "__main__":

    tests = [
        [5, 4, 4, 16, 3],
        [10, 6, 7, 17, 5]
    ]

    for height, width, x1, x2, y in tests:
        screen = BitArray(length=height * width * 8)
        print_screen(screen, width)
        draw_horizontal_line(screen, width, x1, x2, y)
        print_screen(screen, width)
        print()