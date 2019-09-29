"""
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.
Note that the subarray needs to be non-empty after deleting one element.
Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
"""
import sys

def maximumSum(arr):
        del_sum = non_del_sum = 0
        res = -sys.maxsize
        for i,a in enumerate(arr):
            del_sum = max(del_sum + a,a)
            print ("delsum ", del_sum)
            if i > 0:
                del_sum = max(del_sum,non_del_sum)
                print ("delsum ", del_sum)

            non_del_sum = max(non_del_sum + a,a)
            res = max(res, del_sum)
        return res

#print(maximumSum([1,-2,0,3]))
print(maximumSum([1,-2,-2,3]))
#print(maximumSum([-1,-1,-1,-1]))
