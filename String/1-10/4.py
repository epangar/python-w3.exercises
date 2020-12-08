"""
4. Write a Python program to get a string from a given string where all 
occurrences of its first char have been changed to '$', except the first 
char itself.
"""

def style_str(str):
    first = str[0]
    str_len = len(str)

    answer = ""

    for i in range(0, str_len):
        char = str[i]

        if i == 0:
            answer += char
        elif i > 0 and char == first:
            answer += '$'
        else:
            answer += char
    return answer