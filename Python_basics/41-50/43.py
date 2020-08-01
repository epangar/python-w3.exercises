"""
43. Write a Python program to get OS name, platform and release information.
"""

import platform
import os


def os_platform_and_release():
  print(os.name)
  print(platform.system())
  print(platform.release())