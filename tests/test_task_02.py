#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2."""


# Import Python libs
import unittest

# Import User libs
import task_02


class Task02TestCase(unittest.TestCase):
    """Test cases for Task 02"""

    def test_fibonacci(self):
        """Tests that fibo returns the correct values."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                    610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
                    46368, 75025, 121393, 196418, 317811, 514229]

        self.assertEqual(task_02.fibo(30), expected)


if __name__ == '__main__':
    unittest.main()
