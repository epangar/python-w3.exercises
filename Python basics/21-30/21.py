"""21. Write a Python program to find whether a given number (accept from the user) 
is even or odd, print out an appropriate message to the user."""

def even_or_odd():
  number = int(input('Insert a number: '))

  if number % 2 == 0:
    print("Even")
  else:
    print("Odd")

even_or_odd()