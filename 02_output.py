# object(s):Any object, and as many as you like. Will be converted to string before printed
#sep='separator':Optional. Specify how to separate the objects, if there is more than one. Default is ' '
#end='end':Optional. Specify what to print at the end. Default is '\n' (line feed)
#file:Optional. An object with a write method. Default is sys.stdout
#flush:Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
print("hello world")

x = ("1","2","3")
print(x)

print("hello", end=" ")
print("world times 2")

print("a","b","c",sep="---")

print(10)
print(10+50)
print("ali have",20,"years old")