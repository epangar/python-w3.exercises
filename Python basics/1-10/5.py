"""5. Write a Python program which accepts the user's first and last name and print them 
in reverse order with a space between them."""

def full_name(first, last):
    answer = last + ' ' + first
    print(answer)
    return answer

f = str(input('Which is your first name? '))
l = str(input('Which is your last name? '))

full_name(f,l)