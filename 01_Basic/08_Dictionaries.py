"""" NOTE:When choosing a collection type, it is useful to understand the properties of that type.
              Choosing the right type for a particular data set could mean retention of meaning, and,
              it could mean an increase in efficiency or security.""" 
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
# create:
# (1):
human = {
    "amin":20,
    "ali":21,
    "reza": "25",
}
print(human)
print(type(human))
# The values in dictionary items can be of any data type:
num = {
    "1": 1, # int
    "2": "2", # str
    "3": 3.3, # float
    "4":[1,2,3], # list
    "5": {1,2,3}, # tuple
    "6": (1,2,3), # set
    }
# (2):
x = dict(age=20, name = "amin")
print(x)
print(type(x))
#-----------------------------------
# access: 
# (1): dict_name[key]
print(human["amin"])
print(human["ali"])
# (2): .get(key)
print(human.get("reza"))
## Get Keys:
print(human.keys())   # return a list??
## Get Valuse:
print(human.values())  # return a list??
## Get Items:
print(human.items())   # return a tuple
#------------------------------------
# Check if Key Exists:
if "amin" in human:
    print("amin in human dict")
#------------------------------------
# len:
print(len(human))
#-------------------------------------
# Change:
# (1): dict_name[key] = new value
human["ali"] = 30
print(human)
# (2): .update({key:new value})
human.update({"reza":40})
print(human)
#-------------------------------------
# add:
# (1): dict_name[new key] = new value
human["arash"] = 26
print(human)
# (2): .update({new key:new value})
human.update({"amir":33})
print(human)
#----------------------------------
# delete:
# (1): .pop(key)
human.pop("ali")
print(human)
# (2): .popitem()      removes the last inserted item
human.popitem()
print(human)
# (3): del dict_name[key]
del human["reza"]
print(human)
# (4): .clear()
human.clear()
print(human)
#------------------------------------------------
# Loop:
for i in num:
    print(i)  # print all keys
print("===========")
for i in num:
    print(num[i])   # print all valus
print("===========")
for i in num.keys():
    print(i)  # print all keys
print("===========")
for i in num.values():
    print(i)  # print all valuse
print("===========")
for i,j in num.items():
    print(i,":", j)  # print all key_value
print("===========")
#---------------------------------------
# Copy:
x = {
    "1": 1,
    "2": 2
}
# (1):
y = x.copy()
print(y)
z = dict(x)
print(z)
#---------------------------------------------
# Nested Dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#  if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily2 = {
    "child1":child1,
    "child2": child2,
    "child3":child3
}
print(myfamily2)
# access: 
# (1): dict_name[key1][key2]
print(myfamily["child1"]["name"])
print("==================")
#(2): use loop
for i,j in myfamily2.items():
    print(i)
    for y in j:
        print(y,":",j[y])



"""
Method	        Description
clear() 	    Removes all the elements from the dictionary
copy()  	    Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items() 	    Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""
