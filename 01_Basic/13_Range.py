"""
The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
This set of numbers has its own data type called range.
Note: Immutable means that it cannot be modified after it is created.
"""
# range(start, end, step)
"""
Call range() With One Argument
If the range function is called with only one argument, the argument represents the stop value.
The start argument is optional, and if not provided, it defaults to 0.
range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).
"""
x = range(10)
"""
If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value.
range(3, 10) returns a sequence of each number from 3 to 9:
"""
y = range(3,10)
"""
Call range() With Three Arguments
If the range function is called with three arguments, the third argument represents the step value.
The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.
range(3, 10, 2) returns a sequence of each number from 3 to 9, with a step of 2:
"""
z = range(3,10,2)
# Using ranges:
for i in range(5):
    print(i)

"""
Using List to Display Ranges
The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.
Therefore, ranges are often converted to lists for display.
"""
print(list(range(5)))
print(list(range(5,8)))
print(list(range(5,15,2)))

# Slicing Ranges:
w = range(1,10)
print(w[3])
print(w[:4])

# Membership Testing:
q = range(1,20,2)
print("10 in q" if 10 in q else "10 not in q")
print("7 in q" if 7 in q else "7 not in q")

# Length:
r = range(10)
print(len(r))
