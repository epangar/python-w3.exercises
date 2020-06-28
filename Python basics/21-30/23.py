"""
23. Write a Python program to get the n (non-negative integer) copies of the first 2 
characters of a given string. Return the n copies of the whole string if the length is less than 2. 
"""

def get_copies(str, num):

  if num > 0:
    if len(str) >= 2:
      chars = str[:2]

      print(chars * num)
    else:
      print(str * num)

get_copies('abcdef', 5)
get_copies('ab', 5)