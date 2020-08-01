"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

def sum_three(a,b,c):
  if a != b and a != c and c != b:
    return a + b + c
  else:
    return 0
