# Write a function to find the minimum distance between two words in a sentence. 
# Example sentence: "This is a good solution for the problem"
# Example word1 : solution
# Example word2: problem
# Distance in one direction is 3. Distance in the other direction is 5
# Hence the minimum is 3
# Assumption: words are not repeating
# If any of the my_string, sub1 or sub2 is empty string it returns -1
# if sub1 or sub2 not in the sentence, it returns -1
#
#
def find_min_distance_between_two_words_in_a_sentence(my_string, sub1,sub2):
  if my_string == "" or sub1 == "" or sub2 == "":
    return -1
  
  word_list = my_string.split(' ')
  str_len = len(word_list)
  
  if sub1 in word_list:
    sub1_index = word_list.index(sub1)
  else:
    return -1
  if sub2 in word_list:
    sub2_index = word_list.index(sub2)
  else:
    return -1

  distance1 = abs(sub1_index - sub2_index)
  distance2 = str_len - max(sub1_index,sub2_index) + min(sub1_index,sub2_index)

  return min(distance1,distance2)
##############################################
# Test case
# find_min_distance("This is a good solution for the problem", "for", "good")
# This should return 2
###############################################
print(find_min_distance("This is a good solution for the problem", "is", "solution"))
