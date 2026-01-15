#!/usr/bin/python3
"""
Module for calculating minimum operations needed to reach n characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly
    n H characters in the file.

    The text editor can execute only two operations:
    - Copy All
    - Paste

    Args:
        n (int): The target number of H characters

    Returns:
        int: The minimum number of operations needed, or 0 if impossible

    Algorithm:
        The problem is solved using prime factorization.
        To reach n characters, we need to find the sum of all prime factors.
        
        Example: n = 12 = 2 × 2 × 3
        Operations: 2 + 2 + 3 = 7
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Find all prime factors and sum them
    while n > 1:
        # While n is divisible by current divisor
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        # Move to next potential divisor
        divisor += 1

    return operations
