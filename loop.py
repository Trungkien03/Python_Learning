"""_summary_
    Python has two primitive loop commands:
        while loops
        for loops
"""

# while loop
i = 1
while i < 6:
  print(i)
  i += 1

# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
# Continue statement
for x in range(6):
  if x == 3:
    continue
  print(x)
  
# Break statement
for x in range(6):
  if x == 3:
    break
  print(x)
  
# else statement
for x in range(6):
  print(x)
else:
  print("Finally finished!")