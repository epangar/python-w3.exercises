"""
42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""
import struct

def return_bits():
    return struct.calcsize("P") * 8

print(return_bits)