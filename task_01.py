#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci sequence generator"""

def xfibo(count):
    """takes one agrument and creates the sequence.

    Args:
        count(int): The number of Fibonacci numbers to return.

    Returns:
        Returns integer. Each number in a Fibonacci sequence starting with 0
        and stops at number specified.

    Example:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """
    iteration = 0
    beginnum, endnum = 0, 1
    while iteration < count:
        yield beginnum
        beginnum, endnum = endnum, beginnum + endnum
        iteration += 1
