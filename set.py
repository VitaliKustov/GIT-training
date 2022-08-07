"""
Set:
    - a collection
    - unordered
    - unchangeable
    - unindexed
    - created/denoted with {}
    - set do not allow duplicates
"""

myset = {'mangoes', 'guaves', 'berries', 'honeydew', 'mangoes'}
print(myset)
print(len(myset))

for x in myset:
    print(x)

print('honeydew' in myset)

"""
Add items to a set:
- add  <<set>>>.add(<<item>>)
- update - adds items from a set into another set
    <<set1>>.update(<<set2>>)
- add any iterable/collection to a list
"""

myset.add('cantaloupe')
print(myset)
nuts = {'cashew', 'peanut', 'almonds', 'guavas', 'oranges'}
myset.update(nuts)
print(myset)
citrus = ['orange', 'tangerine', 'lemon', 'lime']
myset.update(citrus)
print(myset)

"""
Removing elements from a set:
    - remove <<set>>.remove(<<item>>) this generates error, if the item doesnt exist 
    - pop: removes last item in the set. But set is unordered, so dont know, wht will be removed.
    - discard: does not return error if item not found
    - clear
"""

myset.remove('guavas')
print(myset)
# myset.remove('passion')
print(myset)
myset.pop()
print(myset)

"""
Joining of set:
 - union: create new set with item 2 sets.
 Union also removes duplicates, if it occurs
"""
set1 = {'cashew', 'peanut', 'almonds', 'guavas'}
set2 = {'mangoes', 'guavas', 'berries', 'honeydew', 'mangoes'}

set3 = set1.union(set2)
print(set3)

"""
To get common values(duplicates) within a set:
 - intersection <<set1>>.intersection(<<set2>>)
 - intersection_update = what is common in both
"""
set1.intersection_update(set2)
print(set1)
print(set3)
print(set2)
set3.symmetric_difference_update(set2)
print(set3)

print(set3.isdisjoint(set2))