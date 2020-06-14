"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

def test_number(n):
    return n in range(900, 1101) or n in range(1900, 2101)

