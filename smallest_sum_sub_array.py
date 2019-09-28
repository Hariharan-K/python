import sys

###################################################
## This function finds the smallest sum of subarray
###################################################
def smallestSumSubarr(arr, n): 
    # to store the minimum value that is ending 
    # up to the current index 
    min_value_ending_here = sys.maxsize 
      
    # to store the minimum value encountered so far 
    min_value_so_far = sys.maxsize 
    print (arr)
    # traverse the array elements 
    for i in range(n): 
        # if min_ending_here > 0, then it could not possibly 
        # contribute to the minimum sum further 
        print ("i = ",i, "arr", arr[i])
        if (min_value_ending_here > 0): 
            min_value_ending_here = arr[i] 
          
        # else add the value arr[i] to min_ending_here  
        else: 
            min_value_ending_here += arr[i] 
           
        # update min_so_far 
        print ("min value so far ", min_value_so_far)
        min_value_so_far = min(min_value_so_far, min_value_ending_here) 
        print ("min value ending here ", min_value_ending_here)
        print ("min value so far ", min_value_so_far)
        
      
    # required smallest sum contiguous subarray value 
    return min_value_so_far 

# Driver code# Driver code 
arr = [3, -4, 2, -3, -1, 7, -5] 
n = len(arr) 
print ("Smallest sum: ", smallestSumSubarr(arr, n))
