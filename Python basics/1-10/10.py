"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
"""

def triple_n(n):
    s = str(n)
    answer = 0

    for i in range(1,4):
        answer += int(s*i)
    
    print (answer)
    return answer


triple_n(5)
