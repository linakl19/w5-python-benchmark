# Beneath each comment write the code and print out the result to check it works

'''LISTS'''
print("\n-------------LISTS--------------\n")

# Create a list and assign it to a variable
nums = [46,30,21,5,40]
print(f"{nums=}")

# Find the length of the list
print(f"Length of nums = {len(nums)}")

# Append an item to the list
nums.append(8)
print(f"Added 8 to nums = {nums=}")

# Find the value of an item in the list a specific index
index_4 = nums[4]
print(f"{index_4= }")

# Set the value of an item at a specific index
nums[5] = 31
print(f"Set a value to a specific index = {nums[5]=}")

# Check whether an item is in the list
if 30 in nums:
    print("30 is in nums")

# Sort the list
nums_sorted = sorted(nums)
print(f"Sort using sorted() = {nums_sorted}")

# Sort without bult-in method - Insertion sort
for i in range(1, len(nums)):
    num_to_sort = nums[i]
    j= i - 1

    while j >= 0 and nums[j]>num_to_sort:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = num_to_sort

print(f"Sort using insertion sort = {nums}")

# Iterate over the list using range, printing out each element and the index
print("Iterate using range=")
for i in range(len(nums)):
    print(f"{i}. {nums[i]}")

# Iterate over the list without using range, printing out each element
print("Iterate without using range=")
for num in nums:
    print(num)

'''TUPLES'''
print("\n-------------TUPLES--------------\n")

# Create a tuple and assign it to a variable
new_tuple = ("Hello", "World", "!")
print(f"{new_tuple=}")
print(type(new_tuple))

# Find the length of the tuple
tuple_length = len(new_tuple)
print(f"{tuple_length=}")

# Find the value of an item in the tuple a specific index
index_world = new_tuple[1]
print(f"{index_world=}")

# Check whether an item is in the tuple
if "Hello" in new_tuple:
    print(f"'Hello' is in new_tuple")

# Iterate over the tuple using range, printing out each element and the index
print("Iterate using range=")
for i in range(len(new_tuple)):
    print(f"{i}. {new_tuple[i]}")

# Iterate over the tuple without using range, printing out each element
print("Iterate without using range=")
for value in new_tuple:
    print(value)


'''STRINGS'''
print("\n-------------STRINGS--------------\n")

# Create a string and assign it to a variable
greeting = "Hello World!"
print(f"{greeting=}")

# Find the length of the string
length_greeting = len(greeting)
print(f"{length_greeting = }")

# Find the value of an character in the string a specific index
index_6 = greeting[6]
print(f"{index_6 = }")

# Check whether an item is in the string
if "!" in greeting:
    print("'!' is in greeting.")

# Concatenate (add) two strings together
greeting_2 = "Hola Mundo!"
new_greeting = greeting + " / " + greeting_2
print(f"{new_greeting = }")

# Create an f-string
print(f"f-string -> {greeting_2}")

# Split a string using .split
split_greeting = greeting.split()
print(split_greeting)

# Join a list of strings using .join
join_greeting = '*'.join(split_greeting)
print(f"{join_greeting = }")

# Iterate over the string using range, printing out each character and the index
for i in range(len(greeting)):
    print(f"{i}. {greeting[i]}")

# Iterate over the string without using range, printing out each character
for char in greeting:
    print(char)

'''DICTIONARIES'''
print("\n-------------DICTIONARIES--------------\n")


# Create a dictionary and assign it to a variable
new_dict = {'name':'Lina',
            'city': 'SeaTac'}
print(f"{new_dict = }")

# Find the length of the dictionary
print(f"Length dictionary: {len(new_dict)}")

# Add a new key/value pair
new_dict['Country'] = 'COL'
print(f"Add a new key/value pair: {new_dict}")

# Replace value for a given key
new_dict['Country'] = 'USA'
print(f"Replace value for a given key: {new_dict}")

# Check whether a key is in the dictionary
if new_dict["city"]:
    print('City in New Dict')

# Iterate over keys, printing each key
print(f"Print each key:")
for key in new_dict:
    print(f"{key}")

# Iterate over over key/value pairs using .items(), printing each key and value
for key, value in new_dict.items():
    print(f"{key}= {value}")

'''SETS'''
print("\n-------------SETS--------------\n")

# Create a set and assign it to a variable
new_set = {1,5,9}

# Find the length of the set
print(f"Set Length: {new_set}")

# Add a new element
new_set.add('David')
print(f"Adding new element: {new_set}")

# Remove an element
new_set.remove(9)
print(f"Removing element: {new_set}")

# Check whether a element is in the set
if 'David' in new_set:
    print('David es mi sobrino')

# Iterate over elements, printing each one out
print(f"Print each value in set:")
for value in new_set:
    print(value)

'''NUMBERS'''
print("\n-------------NUMBERS--------------\n")

# Add / subtract / multiply 2 numbers
print(f"{4 + 10 = }")
print(f"{10 - 4 = }")
print(f"{4 * 10 = }")

# Divide two numbers using normal (float) division
print(f"{5/2 = }")

# Divide two numbers using integer division
print(f"{5//2 =}")

# Find the modulo (remainder) of two numbers
print(f"{5%2 = }")

# Check whether a number is even/odd
if 5%2 == 1:
    print("I'm odd")
else:
    print("I'm even")

# Round a float down to an int
float_num=2.5
print(f"{round(float_num) = }")

'''FUNCTIONS'''
print("\n-------------FUNCTIONS--------------\n")

# Write a function that takes no arguments and call it
def write_no_arg_function():
    return("I don't take arguments")
print(write_no_arg_function())

# Write a function that takes one or more arguments and call it
def return_tuple_function(num1, num2):
    return num1, num2
print(f"{return_tuple_function(4,5) = }")

# Write a function that returns a value. Call the function and store the return value in a variable
def return_tuple_function(num1, num2):
    return num1, num2
num1, num2= return_tuple_function(10,20)
print(f"{num1 = }\n{num2 = }")

'''LOOPS'''
print("\n-------------LOOPS--------------\n")

# Write a while loop
print("While Loop:")
i = 1
while i <=5:
    print(i)
    i += 1

# Write a for loop that loops a set number of times (e.g. 10 times)
print("For loop: ")
for i in range(1, 11):
    print(i)

'''CONDITIONALS'''
print("\n-------------CONDITIONALS--------------\n")

# Write an if/elif/else statement
age = 25
if age >= 18:
    print("You're an adult in COL")
elif age < 18 and age >= 13:
    print("You're a teenager")
elif age >= 0:
    print("You're a kid")
else: 
    print("You're not a human")

# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=
print(f"{100 == 100 =}")
print(f"{100 != 100 =}")
print(f"{10 < 100 =}")
print(f"{100 > 50 =}")
print(f"{100 <= 100 =}")
print(f"{100 >= 80 =}")

'''NESTED DATA'''
print("\n-------------NESTED DATA--------------\n")

# Write a nested list (a list of lists) and assign it to a variable
nested_list = [[1,2,3],[4,5,6]]
print(f"{nested_list = }")

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second
nested_list_6 = nested_list[1][2]
print(f"{nested_list_6 = }")

# Iterate through the nested data structure using range
print("Iterate through the nested data structure using range")
for i in range(len(nested_list)):
    print(nested_list[i])
    for j in range(len(nested_list[i])):
        print(nested_list[i][j])

# Iterate through the nested data structure without using range 
print("Iterate through the nested data structure without using range")
for num_list in nested_list:
    print(f"{num_list = }")
    for num in num_list:
        print(num)

'''REMINDER'''

# You're doing great and you got this!
