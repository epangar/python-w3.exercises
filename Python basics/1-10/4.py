"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

from math import pi
user_radius = float(input('Please add the radius of the circle: '))

def area_circle(radius):
    print('For a given radius of ' + str(radius)+ ', the area of the circle is %s' % str(pi*(radius**2)))
    return (pi*(radius**2))

area_circle(user_radius)