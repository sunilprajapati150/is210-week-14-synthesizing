#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""wrapping the fibonacci series in a list"""

import task_01

def fibo(count):
    
    """A list comprehension generator for Fibonacci numbers.

    Args:
        count (int): The number of Fibonacci numbers to return.

    Returns:
        list: A list of Fibonacci numbers.

    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]

        >>> fibo(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    return [num for num in task_01.xfibo(count)]
