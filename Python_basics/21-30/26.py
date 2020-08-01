"""26. Write a Python program to create a histogram from a given list of integers."""

def histogram(char, list):
  answer = ""

  for i in list:
    answer += (char * i) + "\n"   

  print (answer)

histogram('@', [2,4,6,8,1])