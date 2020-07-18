"""
46. Write a python program to get the path and name of the file that is currently executing.
"""

import os

def current_file_name():
  print("Current File Name : ",os.path.realpath(__file__))