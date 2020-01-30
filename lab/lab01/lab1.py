#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:55:47 2020

@author: Trista
"""

'''lab exercise'''

'''lab 1'''
def square(x):
    return x * x
def opposite(x):
    return not x

def repeated(f, n, x):
    """Returns the result of composing f n times on x.
    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    count = n
    result = x
    while count != 0:
        result = f(result)
        count = count - 1
    return result

def sum_digits(n):
    """Sum all the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    result = 0
    while n > 0:
        result = result + n % 10
        n = n // 10
    return result
           
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    #[int(x) for x in str(num)]
    #method1 : return '88' in str(n)
    prev = False
    while n > 0:
        if n % 10 == 8:
            if prev == True:
                return True
            elif prev == False:
                prev = True
        else:
            prev = False
        n = n // 10
    return False

def falling(n, k):
    """Compute the falling factorial of n to depth k.
    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    result = 1
    while k > 0:
        result = result * n
        k = k - 1
        n = n - 1
    return result