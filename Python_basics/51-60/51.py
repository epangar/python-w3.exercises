"""
51. Write a Python program to determine profiling of Python programs.
"""

import cProfile

def factorial(n):
  if n == 1:
    return 1
  else:
    return factorial(n-1)*n


cProfile.run(factorial(5))
