"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date
first = date(2014, 7, 2)
last = date(2014, 7, 11)
answer = first - last 
print (answer.days)

