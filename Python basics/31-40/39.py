"""
39. Write a Python program to compute the future value of a specified principal amount, 
rate of interest, and a number of years.
"""

def interest(amount, rate, years):
  for i in range(1, years+1):
    amount = amount * ((100.00 + rate)/100)

  return amount