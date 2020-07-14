"""
49. Write a Python program to list all files in a directory in Python.
"""

from os import listdir
from os.path import isfile, join

def print_in_directory(directory):
  for file in listdir(directory):
    print (file)

print_in_directory('../41-50')
