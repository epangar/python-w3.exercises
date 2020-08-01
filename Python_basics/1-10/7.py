"""
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
"""

def extension(file):
    return file.split(".")[1]

f = str(input('Please add name of file: '))
print(extension(f))