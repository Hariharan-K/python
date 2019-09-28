# Remove all occurrences of a  number x from a list of N elements
# Example: Remove 3 from a list of size 5 containing elements 1 3 2 3 3 
# Input: 3 5 1 3 2 3 3 
# Output: 1 2

# Input: 4 7 1 4 4 2 4 7 9
########################

import sys

def remove_all_occurrences(mylist,n):
# loop to traverse each element in list
# and, remove elements 
# which are equals to n
  i=0 #loop counter
  length = len(mylist)  #list length 
  while(i<length):
	  if(mylist[i]==n):
		  mylist.remove (mylist[i])
		# as an element is removed	
		# so decrease the length by 1	
		  length = length -1  
		# run loop again to check element							
		# at same index, when item removed 
		# next item will shift to the left 
		  continue
	  i = i+1

  # print list after removing given element
  print ("list after removing elements:")
  print (mylist)

####################
# Driver code ######
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 
val = x[0]
ar_size = x[1]
x = x[2:]
print ("val = ", val, "size = ", ar_size, x )
remove_all_occurrences(x, val)



