"""
58. Write a python program to find the sum of the first n positive integers.
"""

def sum_of_ints(end):
    
    answer = 0
    for i in range(1, end+1):
        answer += i
    
    return answer

