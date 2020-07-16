"""
45. Write a python program to call an external command in Python.

"""

from subprocess import call

def run_console_script(script):
  call(script)

run_console_script(['ls', '-l'])
run_console_script(['npm', 'list', '-g'])