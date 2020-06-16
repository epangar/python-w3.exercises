"""
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged. 
"""

def is_string(str):
    if(str[0] == "I" and str[1] == "s"):
        return str
    else:
        return "Is" + str



