"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.
"""

def prt_str(str):

    if len(str) < 2:
        return ''
    elif len(str) == 2:
        return str + str
    else:
        str_len = len(str)
        last_char, second_to_last = str[str_len-1], str[str_len-2]
        return str[0]+str[1]+second_to_last+last_char

print(prt_str('12345678'))
print(prt_str('12'))
print(prt_str('1'))