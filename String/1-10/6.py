"""
6. Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3). If the given string already ends with 'ing' 
then add 'ly' instead. If the string length of the given string is less than 
3, leave it unchanged. 
"""

def style_str(str):
    str_len = len(str)

    if str_len >= 3:
        answer = ""

        if str[-3:] == 'ing':
            str += 'ly'
    else:
        str += 'ing'
    return str