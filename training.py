# Print command
print("Welcome to class")
print(2+3)
print("Another day in class")
""" 
comment in triple quotes, for multiline
"""
name = "Vitali"
age = 15
Name = "Kustov"
print (name + " " + Name)
name = "Mirjam"
print (name + " " + Name)
print(type(name))

# int
age = 10
print(type(age))
#float
bal = -88576.79
print(type(bal))
e = 123E6
print(type(e))
#complex
comp = 3j+65
print(type(comp))
#type conversion/casting
#str(), int(), float(), complex()
bal = int(bal)
print(bal)
print(type(bal))

# Boolean data type
# expressed as True(1) or False (0)
# comparison >, <, >=, <=, !=, ==
# False and False = False
# False and True = False
# True and False = False
# True and True = True
print(2 >= 1)
print(False and False)
print(not (not True and not False))
"""
+, -, *, /
floor division //
modulus % (reminder)
exp **
"""
x = 9
y = 10
print(x // y)
print(y % x)
print(y ** x)
x += 1 # same as x = x + 1
y *= 2 # same as y = y * 2

hello = ("Welcome to python")
print(hello[8])
# for <<variable_name_for_each_char>> in <<string>>
#for chr in hello:
#    print(chr)
# lenght of string: len(<<string>>)
print(len(hello))

# check, if charactrer or phrase exist: in
txt = "it's a beautiful day"
print("beau" in txt)
print("day" not in txt)
""" 
    slicing of strings: <<string>>[<<start_index>>:<<end_index>>], starts from 0
    slice from a position to end: <<string>>[<<start_index>>:]
    slice from end: use negative index, starts from -1
"""
print(txt[3:7])
print(txt[7:])
print(txt[-4:-1])

"""
lower() or casefold() = return to lowercase
"""
print(txt.capitalize()) # capitalize first letter
print(txt.upper()) # cap all letters
print(txt.count("t"))
print(txt.endswith("x"))
print(txt.find('ful'))