"""
41. Write a Python program to check whether a file exists.
"""

import os.path

def file_exists(file_name):
    return os.path.isfile(file_name)

print(file_exists('41.py'))
print(file_exists('fake_file.py'))