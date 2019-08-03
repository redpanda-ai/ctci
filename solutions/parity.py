def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # drops the lowest  set bit of x

    return result


def get_parity_cache(bits):
    cache = {}
    for i in range(2**bits):
        cache[i] = parity(i)

    return cache


def parity_2(x, bits, cache):
    result = 0

    while x > 0:
        nibble = x & (2**bits - 1)
        result ^= cache[nibble]
        x >>= bits

    return result




def one_count(x):
    result = 0
    while x:
        result += (x & 1)
        x >>= 1

    return result

def faster_one_count(x):
    result = 0
    while x:
        x = x & x - 1
        result += 1

    return result

tests = range(20,33)

for test in tests:
    bits = 4
    cache = get_parity_cache(bits)
    print(f"Number {test}, parity: {parity_2(test, bits, cache)}, ones: {one_count(test)}, faster_ones: {faster_one_count(test)}")
