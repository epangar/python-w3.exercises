"""
5. Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
"""

def style_str(str1, str2):
    
    answer1 = str2[0:2] + str1[2:]
    answer2 = str1[0:2] + str2[2:]
    answer = answer1 + " " + answer2
    return answer 

print(style_str('abc', 'xyz'))