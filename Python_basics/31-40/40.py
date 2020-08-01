"""
40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
"""

import math

def calculate_distance(p1, p2):
  distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
  return distance

point_1 = [4, 0]
point_2 = [6, 6]


print(calculate_distance(point_1, point_2) )