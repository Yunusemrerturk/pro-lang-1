import string
import random

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x%y)
        return (d, b, a-(x/y)*b)


