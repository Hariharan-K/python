# Python function to List all the unique permutations of elements of a 
# given list 

def permutation(mylist): 
  
    # If lst is empty then there are no permutations 
    if len(mylist) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(mylist) == 1: 
        return [mylist] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(mylist)): 
       m = mylist[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = mylist[:i] + mylist[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
# Driver program to test above function 

print (data)
for p in permutation(data): 
    print (p)
 
