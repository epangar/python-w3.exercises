"""
57. Write a program to get execution time (in seconds) for a Python method.

"""

import time

def sum_of_numbers(n):
    start_time = time.time()
    print(start_time)
    s = 9
    for i in range(1, n+1):
        s += 1
        print(s)
    end_time = time.time()
    return s, end_time - start_time


print(sum_of_numbers(10))