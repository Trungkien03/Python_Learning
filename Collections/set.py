thisSet = {"apple", "banana", "cherry"}
print(thisSet)

# set with mixed data types
thisSet = {"apple", "banana", "cherry", "apple"}
print(thisSet)

# access set items
thisSet = {"apple", "banana", "cherry"}

# Set() Constructor
thisSet = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisSet)

# loop through set
for x in thisSet:
  print(x)

# set length
print(len(thisSet))

# set concatenation
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# set methods
thisSet = {"apple", "banana", "cherry"}
print(thisSet.add("orange"))
print(thisSet.remove("banana"))
print(thisSet.discard("banana"))
print(thisSet.pop())
print(thisSet.clear())

# set union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# set intersection
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.intersection(set2)
print(set3)

# set difference
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.difference(set2)
print(set3)

# set symmetric difference
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.symmetric_difference(set2)
print(set3)

# set isdisjoint
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1.isdisjoint(set2))

# set issubset
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1.issubset(set2))

# set issuperset
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print