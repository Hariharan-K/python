# You are given a string s, and an array of pairs of indices in the 
#string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed)
# of the string.

#You can swap the characters at any pair of indices in the given pairs any number of times.

#Return the lexicographically smallest string that s can be changed to #after using the swaps.
#Input: s = "dcab", pairs = [[0,3],[1,2]]
#Output: "bacd"
#Explaination: 
#Swap s[0] and s[3], s = "bcad"
#Swap s[1] and s[2], s = "bacd"

def find_smallest_string_after_specified_swaps (my_string, two_d_array):
  my_list = list(my_string)
  print (my_list)
  swapped_strings = []
  for item in two_d_array:
    print (item[0], ' ', item[1])
    temp=my_list[item[0]]
    my_list[item[0]] = my_list[item[1]]
    my_list[item[1]] = temp
    print(my_list)
    swapped_strings.append(''.join(my_list))
    #print (swapped_strings)
  swapped_strings.sort()
  return (swapped_strings[0])

################################
# Driver code
################################
#print (find_min_distance("dcab",  [[0,3],[1,2]]))
print (find_min_distance("dcab",[[0,3],[1,2],[0,2]]))
