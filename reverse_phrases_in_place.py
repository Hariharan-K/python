#########################################################
# Write a function to reverse phrases in string (in place)
#########################################################

def reverse_phrases(my_string):
  return ' '.join(reversed(my_string.split(' ')))  

#########################################################
# Driver Code
#########################################################

print(reverse_phrases("I am going to dance!!"))
