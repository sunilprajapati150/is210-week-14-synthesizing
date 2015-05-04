#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""


def oldfibo(count):
    """Fibo sequence generation function.
 
    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: A list of Fibonacci numbers.

    Examples:
        >>> oldfibo(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    iteration = 0
    lastnum, curnum = 0, 1
    numbers = [lastnum]
    while iteration < count:
        numbers.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum

    return numbers
