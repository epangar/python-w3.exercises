"""22. Write a Python program to count the number 4 in a given list."""

def count_int(num, list):
  answer = 0
  
  for i in list:
    if i == num:
      answer += 1
  
  print(answer)

