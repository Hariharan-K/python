# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:35:46 2019

@author: Hariharan_Krishnaswa
"""
###############################
# Given a pattern string and given string
# output the all occurrences of characters of the pattern string found in the given_string together

# Example-1: 
#pattern_str = "bxyzca" 
#given_str = "abcabcabc"
#output = "bbbcccaaa"

# Example-2: 

#pattern_str = "bca"
#given_str = "abc"
# output = "bca"
#
def string_output(pattern_str,given_str):
    print("pattern str = ",pattern_str)
    print("given str = ", given_str)
    pattern_list = list(pattern_str)
    given_dict = {}
    for char in given_str:
        if char not in given_dict:
            given_dict[char] = 0
        else:
            given_dict[char] += 1
    #given_list = list(given_str)
    #print ("given dict ", given_dict)
    output_list = []
    for char1 in pattern_list:
        if char1 in given_dict.keys():
            for count in range(given_dict[char1]+1):
                output_list.append(char1)
    return "".join(output_list)

#pattern_str = "bxyzca" 
#given_str = "abcabcabc"

pattern_str = "bca"
given_str = "abc"
print (string_output(pattern_str,given_str))
