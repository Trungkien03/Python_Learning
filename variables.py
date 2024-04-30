
# create variable
x = 5
y = "John"
print(x)
print(len(y))
print(y)


# casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# get the type
x = 5
y = "John"
print(type(x))
print(type(y))


# Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a


# Assign multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)    # banana 
print(z)


# Global Variable
x = "awesome"

def myFunc():
  x = "fantastic"
  print("Python is " + x)

myFunc()
#Python is fantastic

print("Python is " + x)
#Python is awesome



# global keyword
def myFunc():
  global x
  x = "fantastic"

myFunc()

print("Python is " + x)
#Python is fantastic