"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 
"""

def GCD(first, second):
    first_divisors = []
    second_divisors = []
    answer = 1
   
    if first % second == 0:
        return second

    elif second % first == 0:
        return first  

    else:
        for i in range(1, first):
            if first % i == 0:
                first_divisors.append(i)
        
        for j in range(1, second):
            if second % j == 0:
                second_divisors.append(j)


        answer = set(first_divisors).intersection(set(second_divisors))
        
        return max(answer) 

print(GCD(44, 99))