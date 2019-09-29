# Python function to List all the unique permutations of elements of a 
# You are given a string s, and an array of pairs of indices in the #string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) 
# $of the string.



#Get Equal Substrings Within Budget

def get_equal_string_within_budget(s1,s2,cost):
  if len(s1) != len(s2):
    return 0
  strlen = len(s1)
  print ("cost = ", cost)
  dist = 0

  for i in range(strlen):
    dist += abs(ord(s1[i]) - ord(s2[i]))
    print("i = ", i, "distance = ", dist)
    if cost-dist == 0:
      return i+1
    elif cost-dist < 0:
      return i
    else:
      continue
         
  print ("value =", i+1)
  return i+1

# driver code

print (get_equal_string_within_budget("abcd", "bcdf",3))
print (get_equal_string_within_budget("abcd", "cdef", 3))
print (get_equal_string_within_budget("abcd", "acde", 0))
