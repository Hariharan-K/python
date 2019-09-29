"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in 
the array is unique.
Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

def is_occurrence_unique (arr):
        db = {}
        for val in arr:
            if val not in db:
                db[val] = 0
            db[val] += 1
        print (db)
        return len(db.values()) == len(set(db.values()))

  
print (is_occurrence_unique([-3,0,1,-3,1,1,1,-3,10,0]))

 
