"""
32. Write a Python program to get the least common multiple (LCM) of two positive integers.
"""

def LCM(first, second):

  if first % second == 0:
        return first

  elif second % first == 0:
      return first  
  
  else:
    my_min = min([first, second])
    my_max = max([first, second])
    multiplier = 1
    counter = my_min

    while counter % my_max > 0:
      multiplier += 1
      counter = my_min * multiplier
      
    return counter

print(LCM(3,10))