"""
50. Write a Python program to print without newline or space. 
"""

def no_space(str, end):
  for i in range (0, end):
      i = int(i)
      print(str, end ='')
  print('\n')

no_space(":-)", 10)