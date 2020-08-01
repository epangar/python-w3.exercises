"""
47. Write a Python program to find out the number of CPUs using. 
"""

import multiprocessing

def number_of_CPUs():
  return multiprocessing.cpu_count()