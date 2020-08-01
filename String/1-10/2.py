"""
2. Write a Python program to count the number of characters (character frequency) in a string.
"""


def count_char(str):

    dict = {}

    for i in range(0, len(str)):
        
        key = str[i]
        
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    
    return dict

