"""
18. Write a Python program to calculate the sum of three given numbers, if the values are equal 
then return three times of their sum.
"""

def sum_three(a, b, c):
    if a == b and a == c:
        return a * 9
    else:
        return a + b + c

