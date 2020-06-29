"""
Write a Python program to print all even numbers from a given numbers list in the same order and 
stop the printing if any numbers that come after 237 in the sequence.
"""

def print_me(list):
    for i in list:
        if i > 237:
            break
        elif i % 2 == 0:
            print(i)

