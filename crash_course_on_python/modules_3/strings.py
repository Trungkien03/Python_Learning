def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for character in string: 
        # Complete the if-statement using a string method. 
        if character.isalpha():
            count_alpha += 1  
    return count_alpha

 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21



def format_address(address_string):

    house_number = ""
    street_name = ""

    # Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isdigit():
           house_number = address_part
       else:
           street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()
 
    # Use a string method to return the required formatted string.
    return f"House number {house_number} on a street named {street_name}"


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print: "House number 55 on a street named North Center Drive"


def alphabetize_lists(list1, list2):
  new_list = [] # Initialize a new list.
  new_list = list1 + list2 # Combine the lists.
  new_list.sort() # Sort the combined lists.
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']


def even_numbers(first, last):
    return [num for num in range(first, last) if num % 2 == 0]

print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]




def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for continents, country_list in countries_dict.items():
        # Use a string method to format the required string.
        result += f"{country_list}\n"
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']


def combine_guests(guests1, guests2):
  guests2.update(guests1)
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))

car_make = "Lamborghini"

print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])