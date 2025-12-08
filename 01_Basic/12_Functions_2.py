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

