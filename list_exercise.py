# Reverse a given list in python
info = ['karl', '100', 'Red', 'Mangoes']
info.reverse()
print(info)

"""
Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list,
then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
Hint: use list comprehension with zip function
"""

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# result = ['My', 'name', 'is', 'Kelly']
list_zip = [l1 + l2 for l1, l2 in zip(list1, list2)]
print(list_zip)

# Write a Python program to find the second largest number in the given list.
list1 = [10, 20, 4]
list2 = [70, 11, 20, 4, 100]
list1.sort()    # sort list
list2.sort()
print(list1[-2]) #print second last number
print(list2[-2])

# Concatenate two list
# Hint: use list comprehension
# <<new_list>> = [expression for item in list1 for y in list2]
# result = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newlist = [l1 + l2 for l1 in list1 for l2 in list2]
print(newlist)

# Write a program to find value 20 in the list,
# and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [5, 10, 15, 20, 25, 50, 20]
list_index = list1.index(20)
list1 = list1[:list_index]+[200]+list1[list_index:]
print(list1)

# Count number of occurrences of x in the given list
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
counter = 0
for var in lst:
    if var == x:
        counter += 1
print("#",x," appears", counter," times in given list")

# write a program to remove all occurrences of item 20
# Hint: list comprehension
list1 = [5, 20, 15, 20, 25, 50, 20]
remove = 20
list1 = [value for value in list1 if value != remove]
print(list1)

# Write a program to return the middle value of a list. If there are 2 middle values, return the second
names = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']
age = [10, 3, 45, 67, 89.0, 45]
middle_name = int (len(names)/2)
middle_age = int (len(age)/2)
print(names[middle_name])
print(age[middle_age])
