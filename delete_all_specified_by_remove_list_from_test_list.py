# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:35:46 2019

@author: Hariharan_Krishnaswa
"""
#######################################################################
## Remove all occurrences of the elements of remove_list from test_list
#######################################################################
# initializing list  
test_list = [1, 3, 4, 6, 7,6,3,4,5,6,6] 
  
# initializing remove list  
remove_list = [3, 6,4,10] 
  
# printing original list  
print ("The original list is : " + str(test_list)) 
  
# printing remove list  
print ("The original list is : " + str(remove_list)) 
  
# using remove() to perform task 
# handled exceptions. 
for i in remove_list: 
    print ("i = ",i)
    
    try:
        print("count of ", i, test_list.count(i))
        for ct in range(test_list.count(i)):
            test_list.remove(i)
    except ValueError: 
        pass
  
# printing result 
print ("The list after performing remove operation is : " + str(test_list)) 
