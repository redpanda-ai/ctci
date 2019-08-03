def bit_flip_zero(x, y):
    z = x ^ y
    flips = 0
    while z:
        z = z & (z - 1)
        flips += 1

    return flips


print(bit_flip_zero(16, 15))
