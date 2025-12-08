# scope
# A variable is only available from inside the region it is created. This is called scope.
# Local Scope:
#      A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def display():
    x =100
    print(x)

display()

# Global Scope
"""
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local."""
x = 200
def display2():
    print(x)
display2()
print(x)

"""
Naming Variables
If you operate with the same variable name inside and outside of a function,
Python will treat them as two separate variables,
one available in the global scope (outside the function) and one available in the local scope (inside the function):
"""
y  =150
def display3():
    y = 160
    print(y)
display3()
print(y)

# Global Keyword:
"""
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global."""
def display4():
    global z 
    z = 250
    print(z)
display4()
print(z)

# Nonlocal Keyword:
"""
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function."""
def display5():
    w = 350
    def aabcd():
        nonlocal w
        w = 360
    aabcd()
    return w
print(display5())    

"""
The LEGB Rule:
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
"""
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

# -----------------------------------------------
# Python Decorators"
"""
Decorators let you add extra behavior to a function, without changing the function's code.
A decorator is a function that takes another function as input and returns a new function."""
# Basic Decorator:
# Define the decorator first, then apply it with @decorator_name above the function.
def my_func1(func):
    def myfunc():
        return func().lower()
    return myfunc
@ my_func1
def basicDecoratoe():
    return "HELLO WOrld......."
print(basicDecoratoe())
"""
By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
The function changecase is the decorator.
The function myfunction is the function that gets decorated.
"""
# Multiple Decorator Calls: A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
@ my_func1
def x():
    return "HHHHHOOOOOOO"
print(x())
@ my_func1
def a():
    return "ABCDEF......"
print(a())
# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function
def func2(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@func2
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

"""
Sometimes the decorator function has no control over the arguments passed from decorated function,
to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number,
and any type of arguments, and pass them to the decorated function.
"""
def func3(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@func3
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))
# Decorators can accept their own arguments by adding another wrapper level.
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())
"""
You can use multiple decorators on one function.
This is done by placing the decorator calls on top of each other.
Decorators are called in the reverse order, starting with the one closest to the function.
"""
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
