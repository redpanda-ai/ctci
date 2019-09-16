def move_disc(n, rods, from_rod, to_rod):
    print(f"Move disk {n} from rod {from_rod} to {to_rod}")
    rods[to_rod].append(rods[from_rod].pop())
    print(rods)


def towers_of_hanoi(n, rods, from_rod, to_rod, aux_rod):
    if n == 1:
        move_disc(n, rods, from_rod, to_rod)
        return
    towers_of_hanoi(n - 1, rods, from_rod, aux_rod, to_rod)
    move_disc(n, rods, from_rod, to_rod)
    towers_of_hanoi(n - 1, rods, aux_rod, to_rod, from_rod)


if __name__ == "__main__":
    n = 5
    setup_rods = {
        "A": list(range(n, 0, -1)),
        "B": list(),
        "C": list()
    }
    print(setup_rods)
    towers_of_hanoi(n, setup_rods, "A", "B", "C")