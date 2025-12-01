# int
x = 10
s = -10
print(x)
print(type(x))

# str
x_1 = "abcde"
x_2 = 'abcde'
print(x_1, x_2, sep=" - ")
print(type(x_1), type(x_2),sep=" - ")

# float - duoble
x_3 = 1.10
s_1 = -1.10
s_2 = 10
s_3 = -10
print(x_3)
print(type(x_3))

# complex: Complex numbers are written with a "j" as the imaginary part
z = 1j 
s_4 = 4+5j
print(z)
print(type(z))  

# bool
x_4 = False
x_5 = True
print(x_4, x_5, sep=" - ")
print(type(x_4),type(x_5), sep=" - ")
#--------------------------------------------
# type casting
f = int(1)   # x will be 1
f = int(2.8) # y will be 2
f = int("3") # z will be 3

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#----------------------------------------------------
# Camel Case: myVariableName = "John"
# Pascal Case: MyVariableName = "John"
# Snake Case: my_variable_name = "John"
#-----------------------------------------------------
w, z, y = 1,2,3
print(w,z,y,sep=" - ")
w_1= z_1= y_1 = 4
print(w_1,z_1,y_1,sep=" , ")
q = ["w","z","y"]
w_2,z_2,y_2 = q
print(w_2,z_2,y_2,sep=" _ ")
#--------------------------------------------------
n = "python"
m = "is better"
p = 5
print(n,m)
print(n+m)
print(n,m,p)
# print(n+m+p)  => error
#-----------------------------------------
# Global variable
# (1):
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# (2):Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#                            To create a global variable inside a function, you can use the global keyword.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



