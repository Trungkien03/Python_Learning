thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

# access tuple item
print(thisTuple[1])

# loop through tuple
for x in thisTuple:
  print(x)

# tuple length
print(len(thisTuple))

# tuple concatenation
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple slicing
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[2:5])

# tuple methods
thisTuple = ("apple", "banana", "cherry")
print(thisTuple.count("apple"))
print(thisTuple.index("cherry"))

# nested tuple
thisTuple = (("apple", "banana"), ("cherry", "orange"))
print(thisTuple[0][1])

# tuple unpacking
thisTuple = ("apple", "banana", "cherry")
(x, y, z) = thisTuple
print(x)
print(y)
print(z)

# Using Asterisk*
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(*x, y, z) = thisTuple
print(y)
print(z)

# tuple comprehension
thisTuple = (x for x in range(10))
print(thisTuple)