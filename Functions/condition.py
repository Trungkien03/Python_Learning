# if else condition in python
a = 33
b = 33
if a > b:
  print("a is greater than b")
elif a < b:
  print("a is less than b")
else:
  print("a is equal to b")

# nested if else
a = 200
b = 33
c = 500

if a > b:
  if c > a:
    print("c is greater than a")
  else:
    print("a is greater than c")
else:
  if c > b:
    print("c is greater than b")
  else:
    print("b is greater than c")

# pass statement
a = 200
b = 33
c = 500

if a > b:
  pass
elif a < b:
  pass
else:
  pass

# break statement
a = 200
b = 33
c = 500

# usecase for not in or not
if a > b and c > a:
  print("Both conditions are true")
else:
  print("At least one of the conditions is false")

# usecase for not in or not
if a > b or c > a:
  print("At least one of the conditions is true")
else:
  print("Both conditions are false")

# usecase for not in or not
if not(a > b):
  print("a is not greater than b")
else:
  print("a is greater than b")

# usecase for not in or not
if not(a > b and c > a):
  print("Both conditions are not true")
else:
  print("At least one of the conditions is true")

# usecase for not in or not
if not(a > b or c > a):
  print("Both conditions are not true")
else:
  print("At least one of the conditions is true")

# usecase for not in or not
if not(not(a > b)):
  print("a is greater than b")
else:
  print("a is not greater than b")

# usecase for not in or not
if not(not(a > b and c > a)):
  print("Both conditions are true")
else:
  print("At least one of the conditions is false")

# usecase for not in or not
if not(not(a > b or c > a)):
  print("At least one of the conditions is true")
else:
  print("Both conditions are false")

# usecase for not in or not
if not(not(not(a > b))):
  print("a is not greater than b")
else:
  print("a is greater than b")

# usecase for not in or not
if not(not(not(a > b and c > a))):
  print("Both conditions are true")
else:
  print("At least one of the conditions is false")

# usecase for not in or not
if not(not(not(a > b or c > a))):
  print("At least one of the conditions is true")
else:
  print("Both conditions are false")

# usecase for not in or not