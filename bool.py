print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# and or not
a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are true")
else:
  print("At least one of the conditions is false")

if a > b or c > a:
  print("At least one of the conditions is true")
else:
  print("Both conditions are false")

if not(a > b):
  print("a is not greater than b")
else:
  print("a is greater than b")

# is and is not
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

print(id(a))


# values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myClass():
  def __len__(self):
    return 0

myObj = myClass()
print(bool(myObj))