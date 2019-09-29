# Python code to remove duplicate entries from sorted array
#

# Method1 - using set
def m1_remove_duplicates_from_sorted_array(myarray):
  print (list(set(myarray)))

# Method2 - without using set

def m2_remove_duplicates_from_sorted_array(myarray):
  print("my array initially: ")
  print (myarray)

  length=len(myarray)
  i = 0
  while i < length-1:
    if myarray[i] == myarray[i+1]:
      myarray.remove(myarray[i+1])
      length -= 1
      continue
    i +=1  
  print (myarray)
  return myarray
 
#################################
# Driver code
##################################
myarray = [1,1,1,2,2,2,2,3,3,4,4,5,5,6,7,8]
m2_remove_duplicates_from_sorted_array(myarray)

