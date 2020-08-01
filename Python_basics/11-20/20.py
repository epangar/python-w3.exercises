"""
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""

def string_number(str,n):
    if n > -1:
        answer = str*n
        print(answer)
        return answer
    else:
        print('ERROR, insert a positive value.')


