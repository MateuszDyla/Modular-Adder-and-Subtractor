import math


class ModularOperator:
    def __init__(self, modulus: int):
        self.n = None
        self.m = None
        self.subtract_mode = None
        self.set_modulus(modulus)

    def set_modulus(self, modulus: int):
        self.m = modulus
        self.n = math.log2(self.m)
        self.n = math.ceil(self.n)
        self.subtract_mode = 2 ** self.n - 1

    def add(self, x, y):
        return calculate(self.m, self.n, x, y, 0)

    def subtract(self, x, y):
        return calculate(self.m, self.n, x, y, 1)


'''
    ** - pow
    &  - bit-wise "and" 
    |  - bit-wise "or"
    ^  - bit-wise "xor"
    ~  - bit-wise "not"
'''


def calculate(m: int, n: int, x: int, y: int, s: int):
    # created to save up on computing
    repeating_part = x + (y ^ s*(2**n - 1))

    w = repeating_part + (2**n ^ s) + s
    v = repeating_part + (NOT(m) ^ s) + 1

    print(f'w={w}, v={v}, s={s}, 2**n={2**n}, !m={NOT(m)}, y^s={y^s}, 2**n^s={(2**n)^s}, !m^s={NOT(m)^s}')

    if (s == 0 and v < 2**n) or \
            (s == 1 and w >= 2**(n+1)):
        return w % 2**n

    return v % 2**n


# in python int is always signed, so we have to keep the leftmost bit as it was
# we can achieve it by using bit-mask which leftmost bit is always 0
# to do it, we have to subtract 1 from 1 left-shifted [num_of_bits] times
def NOT(number: int):
    bits = number.bit_length()
    bitmask = (1 << bits) - 1
    return ~number & bitmask
