#!/usr/bin/env python3

# ----------
# IsPrime.py
# ----------

from math     import sqrt
from unittest import main, TestCase

def is_prime (n) :
    assert n > 0
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :
        if (n % i) == 0 :
            return False
    return True

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertFalse(is_prime( 1))
        self.assertFalse(is_prime( 2))
        self.assertTrue (is_prime( 3))
        self.assertFalse(is_prime( 4))
        self.assertTrue (is_prime( 5))
        self.assertFalse(is_prime( 6))
        self.assertTrue (is_prime( 7))
        self.assertFalse(is_prime( 8))
        self.assertTrue (is_prime( 9))
        self.assertFalse(is_prime(10))
        self.assertTrue (is_prime(11))

main()

"""
% coverage3 run --branch IsPrime.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

% coverage3 report
Name      Stmts   Miss Branch BrMiss  Cover
-------------------------------------------
is_prime     23      0      6      0   100%
"""
