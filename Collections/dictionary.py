thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
print(thisDict)

# access dictionary item
print(thisDict["brand"])

# loop through dictionary
for x, y in thisDict.items():
  print(x, y)

# dictionary length
print(len(thisDict))

# add item to dictionary
thisDict["color"] = "red"
print(thisDict)

# update item in dictionary
thisDict.update({"year": 2020})
print(thisDict)

# remove item from dictionary
del thisDict["model"]
print(thisDict)

# clear dictionary
thisDict.clear()
print(thisDict)

# copy dictionary
newDict = thisDict.copy()
print(newDict)

# nested dictionary
thisDict = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "cars": [
    {"model": "Ford", "year": 2018},
    {"model": "Toyota", "year": 2017}
  ]
}
print(thisDict["cars"][0]["model"])

# dictionary comprehension
thisDict = {x: x**2 for x in range(6)}
print(thisDict)