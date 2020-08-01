"""
Write a Python program to print out a set containing all the colors from 
color_list_1 which are not present in color_list_2.
"""

def print_those(list1, list2):
    first = set(list1)
    second = set(list2)
    print(first.difference(second))
