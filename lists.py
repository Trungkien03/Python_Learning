# generate all possible case about list in python and give comment about the print state of each print
# create a list
list1 = ['a', 'b', 'c']
print(list1)
# ['a', 'b', 'c']

# access list items
print(list1[0])
# a

# change list items
list1[0] = 'd'
print(list1)
# ['d', 'b', 'c']

# add items to the end of the list
list1.append('e')
print(list1)
# ['d', 'b', 'c', 'e']

# add items to the beginning of the list
list1.insert(0, 'f')
print(list1)
# ['f', 'd', 'b', 'c', 'e']

# remove items from the list
list1.remove('b')
print(list1)
# ['f', 'd', 'c', 'e']

# remove the last item from the list
list1.pop()
print(list1)
# ['f', 'd', 'c']

# remove the first item from the list
list1.pop(0)
print(list1)
# ['d', 'c']

# clear the list
list1.clear()
print(list1)
# []

# check if an item is in the list
print('d' in list1)
# False

# check if an item is not in the list
print('d' not in list1)
# True

# get the length of the list
print(len(list1))
# 0

# sort the list
list1 = ['d', 'b', 'c']
list1.sort()
print(list1)
# ['b', 'c', 'd']

# sort the list in descending order
list1.sort(reverse=True)
print(list1)
# ['d', 'c', 'b']

# reverse the list
list1.reverse()
print(list1)
# ['b', 'c', 'd']

# join two lists
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2
print(list3)
# ['a', 'b', 'c', 'd',


# Change list item
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList[1:2] = ["blackcurrant", "watermelon"]
print(thisList)

# Add list item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Copy list
thislist = ["apple", "banana", "cherry"]
newlist = thislist.copy()
print(newlist)

thislist = ["apple", "banana", "cherry"]
newlist = list(thislist)
print(newlist)

# Join list
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = list1.extend(list2)
print(list3)

# Nested list
list1 = ["apple", "banana", "cherry"]
list2 = ["google", "facebook", "microsoft"]
list3 = [list1, list2]
print(list3)

list1 = ["apple", "banana", "cherry"]
list2 = ["google", "facebook", "microsoft"]
list3 = list(zip(list1, list2))
print(list3)

# List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = [x for x in numbers if x % 2 == 0]
print(newlist)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = [x**2 for x in numbers]
print(newlist)