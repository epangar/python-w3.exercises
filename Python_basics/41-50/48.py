"""
48. Write a Python program to parse a string to Float or Integer. 
"""

def parse_me():
  parse_to_float = 'F' == str(input("Press 'I' to parse to an integer or 'F' to parse to a float: > ")).lower()
  my_string = str(input('Please add a string to parse: > '))

  if parse_to_float == True:
    return float(my_string)
  else:
    return int(my_string)
