"""
32. Write a Python program to get the least common multiple (LCM) of two positive integers.
"""

def LCM(first, second):

  if first % second == 0:
        return first

  elif second % first == 0:
      return first  
  
  else:
    return 0