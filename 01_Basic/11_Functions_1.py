"""
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.
"""
# create:
def display():
    print("hello world")

display()
def fahrenheit_to_celsius(f):
    print((f-32)*5/9)
fahrenheit_to_celsius(100)
fahrenheit_to_celsius(50)
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back.
# If a function doesn't have a return statement, it returns None by default.
def display2():
    return "hello world"

a = display2()
print(a)
# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

print(display2())
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def average(nums):
    pass

# Default Parameter Values:
#   You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_func(name = "amin", age = 22):
    print("hello",name, age)

my_func()
my_func("ali")
my_func(20)  # ???!!!!!!
my_func("reza", 30)
# You can send arguments with the key = value syntax.
# This way, with keyword arguments, the order of the arguments does not matter.
my_func(name="arash", age= 40)
my_func(age= 50, name="mamad")
# Positional-Only Arguments
"""You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add , / after the arguments:"""
def my_func2(name, age,/):
   print(name, age)

my_func2("amin", 22)
# my_func2(name = "x", age= y)   can not ????

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_func3(*, name):
   print("hello", name)
my_func3(name= "xx")
# my_func3("xxxx")  can not ??????

# You can combine both argument types in the same function.
#   Arguments before / are positional-only, and arguments after * are keyword-only:
def my_func4(name, age,/,*,lasname):
   print(f"hello {name} {lasname} you have {age}")

my_func4("amir", 30, lasname="amiri")

# Passing Different Data Types
"""You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
The data type will be preserved inside the function:"""
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

# *args and **kwargs:
"""
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments."""
# Arbitrary Arguments - *args:
"""
If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly"""
"""
The *args parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments:
"""
def my_function4(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function4("Emil", "Tobias", "Linus")
# Using *args with Regular Arguments:
"""
You can combine regular parameters with *args.
Regular parameters must come before *args:"""
def my_function5(s,*args):
  for name in args:
     print(f"{s} {name}")

my_function5("Hello","Emil", "Tobias", "Linus")
## NOTE: *args is useful when you want to create flexible functions:
def my_function6(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function6(1, 2, 3))
print(my_function6(10, 20, 30, 40))
print(my_function6(5))
print(my_function6(0))
def my_function7(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function7(3, 7, 2, 9, 1))
# Arbitrary Keyword Arguments - **kwargs:
"""
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly."""
def my_function7(**kid):
  print("His last name is " + kid["lastname"])

my_function7(fname = "Tobias", lastname = "Refsnes")
"""
What is **kwargs?
The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments.
"""
def my_function8(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function8(name = "Tobias", age = 30, city = "Bergen")
"""
You can combine regular parameters with **kwargs.
Regular parameters must come before **kwargs:
"""
def my_function9(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function9("emil123", age = 25, city = "Oslo", hobby = "coding")

"""
Combining *args and **kwargs
You can use both *args and **kwargs in the same function.

The order must be:
regular parameters
*args
**kwargs
"""
def my_function10(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function10("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
# Unpacking Lists with *: If you have values stored in a list, you can use * to unpack them into individual arguments.
def my_function11(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function11(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function12(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function12(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
