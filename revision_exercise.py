# Reverse the order of words in a given sentence.
from typing import List

str_val = "Hello World"
#output = "World Hello"
a = str_val.split()
a.reverse()
print(" ".join(a))

# Write a program  that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# hint: use set() =>
# output = [10, 23, 5, 67]
list1 = [10, 23, 23, 5, 67, 10]
myList = set(list1)
print(list(myList))

# Write a password strength verifier in Python that checks if user password is strong.
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# password = 'food'
password = '1EggPerD@y'
l, u, p, d = 0, 0, 0, 0
for i in password:
    if (i.islower()):
        l+=1
    if (i.isupper()):
        u+=1
    if (i.isdigit()):
        d+=1
    if (i=="#" or i=="$" or i=="&" or i=="^" or i=="#" or i=="@"or i=="!"):
        p+=1
if l>=1 and u>=1 and p>=1 and d>=1:
    print("True")
else:
    print("False")

# Write a program to reverse row sort in list of lists
# result = [[6,4,1], [9,7], [9,8,4,2]]
list_id = [[4,1,6], [7,9], [8,9,2,4]]
for ele in list_id:
    ele.sort(reverse=True)
print(list_id)

# Write a program to pair elements with rear element in matrix row
# result = [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]
list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
res = []
for key in list1:
    res.append([[ele, key[-1]] for ele in key[:-1]])
print(res)

# Replace each special symbol with # in the following string
# Hint: import string, and use string.punctuation
# result = "#There #are three# students# and# 1 trainer#"
# solution from GeeksForGeeks
str1 = "%There &are three( students$ and& 1 trainer!"
import string
import re
chars = re.escape(string.punctuation)
print(re.sub(r'['+chars+']', '',str1))

# Remove all characters for string except integers
# hint: list comprehension and isdigit()
# result = 102
str1 = "My mum has a 10 year old dog and 2 fishes"
numeric_filter = filter(str.isdigit, str1)
numeric_string = "".join(numeric_filter)
print(numeric_string)

# Remove all empty strings from a list of strings
# hint: use filter() => https://docs.python.org/3/library/functions.html#filter
name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']

# using filter() to perform removal
test_list = list(filter(None, name_list))

# Printing modified list
print(test_list)