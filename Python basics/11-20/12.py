"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

import calendar

def print_date():
    year = int(input("Please include the year: "))
    month = int(input("Please include the month: "))
    print (calendar.month(year, month))

