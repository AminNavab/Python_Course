name = "Amin Navabzade"
print(name)

# Strings are Arrays:
print(name[0])
print(name[2])
print(name[10])
print(len(name))

# loop in str:
for i in name:
    print(i, sep=" , ")

# cheking str??:
if "min" in name:
    print("min is in name")
if "x" not in name:
    print("x is not in name")

# Slicing Strings:
print(name[5:12])  # from 5 to 12 (start = 5 , end = 12)
print(name[:8])  # from thr start
print(name[5:])  # to the end
# Negative Indexing: Use negative indexes to start the slice from the end of the string.
print(name[-8:-3])

# Modify Strings:
print(name.upper())
print(name.lower())
name2 = "   Amin Navabzade     "
print(name2.strip()) # Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print(name.replace("Amin", "Ali")) # "Amin" => "Ali"
a = "a,b,c,d,e"
print(a.split(",")) # The split() method returns a list where the text between the specified separator becomes the list items.

# F-Strings:
age = 22
print(f"I have {age}")
# Placeholders and Modifiers:
print("I have {age}")
# A placeholder can include a modifier to format the value: 
# #                  A modifier is included by adding a colon : followed by a legal formatting type,
# #                         like .2f which means fixed point number with 2 decimals:
price = 20
print(f"The price is {price:.2f} dollars")












