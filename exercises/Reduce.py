#!/usr/bin/env python3

# ---------
# Reduce.py
# ---------

from functools import reduce
from operator  import add, mul, sub

def reduce_1 (bf, a, v) :
    i = 0
    s = len(a)
    while i != s :
        v = bf(v, a[i])
        i += 1
    return v

def reduce_2 (bf, a, v) :
    for i in range(len(a)) :
        v = bf(v, a[i])
    return v

def reduce_3 (bf, a, v) :
    p = iter(a)
    try :
        while True :
            v = bf(v, next(p))
    except StopIteration :
        pass
    return v

def reduce_4 (bf, a, v) :
    for w in a :
        v = bf(v, w)
    return v

def test (f) :
    assert f(add, [], 0) == 0

    a = [2, 3, 4]
    assert f(add, a, 0) ==  9
    assert f(sub, a, 0) == -9
    assert f(mul, a, 1) == 24

    a = ([2, 3, 4], [5, 6])
    assert f(add, a, []) == [2, 3, 4, 5, 6]

    a = [(2, 3, 4), (5, 6)]
    assert f(add, a, ()) == (2, 3, 4, 5, 6)

    a = ("abc", "de")
    assert f(add, a, "") == "abcde"

print("Reduce.py")

test(reduce_1)
test(reduce_2)
test(reduce_3)
test(reduce_4)
test(reduce)

print("Done.")
