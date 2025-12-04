"""
and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
# (1): use if,elif,else
x = 10
if x==11:
    print("x = 11")
elif x<9:
    print("x<9")
elif x==12:
    print("x = 12")
else: print("x>9")
## Short Hand If ... Else: Ternary operators
"""
When to Use Shorthand If???
Shorthand if statements and ternary operators should be used when:
1-The condition and actions are simple
2-It improves code readability
3-You want to make a quick assignment based on a condition"""
print("x == 10") if x==10 else print("x != 10")
a = 10
b = 10
print("a") if a>b else print("a = b") if a==b else print("b")
user = ""
print(f"hello {user if user else "amin"}")
## The pass Statement: if statements cannot be empty, but if you for some reason have an if statement with no content,
# #                          put in the pass statement to avoid getting an error.
"""
Why Use pass?
When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
"""
a = 11
b =10
if a>b:
    pass
#-------------------------------
# (2): Match => Instead of writing many if..else statements, you can use the match statement.
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
# NOTE: The value _ will always match, so it is important to place it as the last case to make it behave as a default case.
# Combine Values: Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
# You can add if statements in the case evaluation as an extra condition-check:
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
