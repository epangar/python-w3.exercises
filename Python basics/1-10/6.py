
"""6. Write a Python program which accepts a sequence of comma-separated numbers from user and 
generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

import sys 

def elements(size):

    if size < 1:
        print("Bye!")
        sys.exit()
    else:
        my_list = []
        

        print('We need you to add %s elements:' % str(size))

        for i in range(0,size):
            element = input("Add an element: ")
            my_list.append(element)
            # new_tuple = (element)
            # my_tuple = my_tuple + new_tuple
        
        my_tuple = (*my_list, )
        

        print("My list is " + str(my_list))
        print("My tuple is " + str(my_tuple))
        sys.exit()


s = int(input('How long should the elements be? '))
elements(s)
