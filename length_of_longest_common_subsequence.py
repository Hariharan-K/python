"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

  
def length_of_longest_common_subsequence(s1,s2):
  location_indexes = []
  for i in range(len(s2)):
    print ("index of chars in s2 in s1: ",s1.find(s2[i]))
    location_indexes.append(s1.find(s2[i]))
    print (location_indexes)

  if -1 in location_indexes:
    print ("not a subsequence")
    return 0

  inreasing = False
  prev_val = -1
  for val in location_indexes:
    if val > prev_val:
      prev_val = val
      increasing = True
      #print("not breaking")
      continue
    else:
      print (location_indexes.index(val))
      increasing = False
      break

  if increasing:
    return (location_indexes.index(val)+1)
  else:
    return 0

#driver code

s1 = "abdcde"
s2 ="adb"

print("length = ", length_of_longest_common_subsequence(s1,s2))
