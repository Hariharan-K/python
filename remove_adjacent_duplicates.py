# Remove ad
# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the 
# left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made.
# It is guaranteed that the answer is unique.

"""
Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""

def remove_adjacent_duplicates(mystring,k):
    pool = []
    for idx, val in enumerate(mystring):
        print ("pool =", pool)
        
        if pool and pool[-1][0] == val:
            print ("pool [-1][0]", pool[-1][0])
            pool.append((val, pool[-1][1] + 1))
        else:
           pool.append((val, 1))
        print ("pool [-1][1]", pool[-1][1])
        if pool and pool[-1][1] == k:
            for i in range(k):
                pool.pop()
        print ("Popped pool", pool)
    return "".join([x[0] for x in pool])

# Driver code
# 
#print(remove_adjacent_duplicates("pbbcggttciiippooaais", 2))
#print(remove_adjacent_duplicates("abcd",2))
print(remove_adjacent_duplicates("deeedbbcccbdaa",3))


