#############################
# Write a function to see from a string if the brackets matche or not
############################

def brackets_match(mystring):
  sq_b = 0
  curly_b = 0
  reg_b = 0

  str_list = list(mystring)
  if len(str_list) == 0:
    print ("Empty list")
  else:
    for char in str_list:
      if char == '{':
        curly_b += 1
      elif char == '}':
        curly_b -= 1
      elif char == ']':
        sq_b += 1
      elif char == '[':
        sq_b -= 1
      elif char == '(':
        reg_b +=1
      elif char == ')':
        reg_b -= 1
  if sq_b == 0 and curly_b == 0 and reg_b == 0:
    print ("brackers matched")
  else:
    print("brackerts don't match")

# driver code 
brackets_match("a(b+c) {} +d))")

