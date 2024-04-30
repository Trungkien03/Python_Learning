# quote inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# multiline string 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String are arrays
a = "Hello, World!"
print(a[1])

#looping through strings
for x in "banana":
  print(x)

#string length
a = "Hello, World!"
print(len(a))

#check string
txt = "The best things in life are free!"
print("free" in txt)

#find the position
txt = "The best things in life are free!"
x = txt.find("free")
print(x)

#replace string
txt = "The best things in life are free!"
x = txt.replace("free", "good")
print(x)

#upper and lower case
txt = "Hello, World!"
print(txt.upper())
print(txt.lower())

#title case
txt = "Hello, World!"
print(txt.title())

#strip
txt = "     Hello, World!     "
print(txt.strip())

#split
txt = "Hello, World!"
x = txt.split(",")
print(x)

#join
my_list = ["Hello", "World!"]
x = " ".join(my_list)
print(x)

#format
age = 36
name = "John"
txt = "My name is {} and I am {} years old.".format(name, age)
print(txt)

#format with numbers
txt = "The price is {:.2f} dollars.".format(29.95)
print(txt)

#format with dates
import datetime
x = datetime.datetime.now()
print(x.strftime("%B %d, %Y"))

price = 59
txt = f"The price is {price} dollars"
print(txt)