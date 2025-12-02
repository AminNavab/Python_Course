# set_name = {................}
"""NOTE:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
# create:
## Sets cannot have two items with the same value.
## The values True and 1 are considered the same value in sets, and are treated as duplicates.
## The values False and 0 are considered the same value in sets, and are treated as duplicates.
## (1):
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
x = {1,2,3,True,0, False, "a","b"}
print(x)
print(type(x))
## (2):
x1 = set((1,2,8,6,"a",True,False))
print(x1)
print(type(x1))
#---------------------------------------
# len:
print(len(x))
#---------------------------------------
# access:
for i in x:
    print(i)
print(11 in x)
print(11 not in x)
#----------------------------------------
# change: Once a set is created, you cannot change its items, but you can add new items.
#----------------------------------------
# add:
m = {1,2,3,5,"a",False}
n = {8,6,7,10}
m.add(8)
print(m)
m.update(n)
print(m)
#----------------------------------------
# delete:
x = {1,2,8,6,"a","b",False,True}
print(x)
x.remove(1)  # If the item to remove does not exist, remove() will raise an error.
print(x)
x.discard(0) # If the item to remove does not exist, discard() will NOT raise an error.
print(x)
x.pop() # Remove a random item by using the pop() method.
print(x)
x.clear() # or del x
print(x)
#-----------------------------------------
# Loop:
w = {1,2,5,8,4,6,"a"}
for i in w:
    print(i)
#-----------------------------------------
# Join:
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates."""
z = {1,2,3,4,5,6}
w = {4,5,6,7,8,9}
q = {1,5,9}
print(z.union(w))   # print(z | w) , print(z.union(set1,set2,set3,...))
q.update(w)
print(q)
print(z.intersection(w))  # print(z & w) , 
print(z.intersection_update(w))  #The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
print(z.difference(w))   # print(z - w)
print(z.difference_update(w))  # The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
print(z.symmetric_difference(w)) # print(z ^ w) , The symmetric_difference() method will keep only the elements that are NOT present in both sets
print(z.symmetric_difference_update(w))  # The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
#----------------------------------------------
# frozenset:
"""
frozenset is an immutable version of a set.
Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset."""
x = frozenset({1,2,5,4,"a",9,6, False, 1.5})
print(x)
print(type(x))
# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.
"""
copy()	 	                Returns a shallow copy	
difference()	-	        Returns a new frozenset with the difference	
intersection()	&	        Returns a new frozenset with the intersection	
isdisjoint()	 	        Returns whether two frozensets have an intersection	
issubset()	<= / <	        Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	    Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	  |	                Returns a new frozenset containing the union
"""
#--------------------------------------------------
""" 
Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""




