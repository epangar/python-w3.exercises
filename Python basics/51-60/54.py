"""
54.Write a Python program to get the current username.
"""

from subprocess import call

def who():
  call(['whoami'])

who()
# OR

import getpass

def get_user():  
  print(getpass.getuser())

get_user()