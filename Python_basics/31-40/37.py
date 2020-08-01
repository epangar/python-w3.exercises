"""
37. Write a Python program to display your details like name, age, address in three different lines.
"""

def my_program():
  name = str(input("Please enter your name: > "))
  age = str(input("Please enter your age: > "))
  adress = str(input("Please enter your adress : > "))

  arr = [name, age, adress]

  for element in arr:
    print("%s" % element)
