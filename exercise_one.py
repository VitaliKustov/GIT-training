# Write a program to create a new string made of the middle three characters of an input string.
input = "JhonDipPeta"
middle = len(input) // 2
print(input[middle -1: middle +2])

#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Aunt"
s2 = "Sister"
count = int(len(s2)//2)
s3 = s2[0:count] + s1 + s2[count:]
print(s3)

#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characte
s1 = "America"
s2 = "Japan"
middle_s1 = int(len(s1)//2)
middle_s2 = int(len(s2)//2)
s3 = s1[0] + s2[0] + s1[middle_s1] + s2[middle_s2] + s1[-1] + s2[-1]
print(s3)

# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.
# Solution credits to Lauri Mei
s1 = "Yn"
s2 = "PYnative"
result = False
isFalse = 0
for char in s1:
    if s2.count(char) == 0:
        isFalse += 1
    else:
        isFalse += 0
if isFalse > 0:
    print("False")
else:
    print("True")

# Write a program to split a given string on hyphens and display first and last substring.
str1 = "Emma-is-a-data-scientist"
split_str1 = str1.split("-")
print(split_str1[0] + ", " + split_str1[-1])

# Reverse a given string
# Write a program to find the last position of a substring “Emma” in a given string.
str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Result = Last occurrence of Emma starts at index 43
result_str = str1.rfind("Emma")
print("Last occurrence of Emma starts at index " + str(result_str))