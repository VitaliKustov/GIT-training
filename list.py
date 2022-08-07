"""
    lists are used to store multiple values in a variable
    list are denoted/created using []
    list are ordered collection of items
    allow duplicates
    changeable - add, remove, replace
"""

mylist = ['apples', 'mangoes', 2, 7.5, 'red']
print(type(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[2:4])

# use in to check if value exists in a list
print('guava' in mylist)

""" add items to a list
 - .append: add to end of list
 - .insert: add at a specific index
 <<list>>.insert(<<position>>, value
  - extend: appends elements from a list to another list
  - replace items using index []
  - remove items: <<list>>.remove(<<item>>), with duplicates, first one is removed
  - pop: removes the last item <<list>>.pop()
  <<list>>.pop(<<index>>): removes item at the position
  - clear: removes all items in a list
"""

mylist.append('guavas')
mylist.append('grapes')
mylist.insert(2, 'blueberries')
mylist.insert(0, 'mangoes')

exotic_fruits = ['cashew', 'wild blueberries', 'passion fruit']
mylist.extend(exotic_fruits)
print(mylist)

mylist[4] = 'corn' #replace
print(mylist)
mylist.remove('mangoes')
mylist.remove(7.5)
print(mylist)

mylist.pop(1)
print(mylist)
exotic_fruits.clear()
print(exotic_fruits)

age = [12, 14, 25, 39, 67, 45, 13]
print(min(age))
print(max(age))
print(sum(age))
print(sum(age) / len(age))

mylist.sort()
age.sort()
print(mylist)
print(age)
mylist.reverse()
print(mylist)

"""
Looping through a list
    - for loop
        for <<variable>> in <<list>> 
    - range(start, stop, step)
        default step is 1
"""
age = 10
name = "Vitali"
print(f"My name is {name}, I am {age} years old")
print("My name is " + name + ", I am " + str(age) + " years old")
print("My name is {}, I am {} years old".format(name, age))

#for var in mylist:
        #print(f"I love {var}") # f_string
        #print("I love "+ var)

# range(10) # 0 - 9
# range(5, 10) # 5 to 9
#for i in range(len(age)):
#       print(f"index {i}: {age[i]}")

"""
List Comprehension:
        - creates new list
        - short method of creating a list from an existing list
        - filter and perform operations
        [expression for item in <<list>> <<optional:condition>>]
"""
x = [print(f"My age is {x}") for x in str(age)]
#new_age = [x for x in age if x%2 == 0]
#print(new_age)

upp_list = [var.upper() for var in mylist]
print(upp_list)