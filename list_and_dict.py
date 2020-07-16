# Lists
my_first_list = [1, 3.14, 'A', 'This is a string']

# Get element from list
# List returns value by index
print(my_first_list[0])

# Error
# print(my_first_list[10])

# Change item in list
my_first_list[2] = 'Python'
print(my_first_list[2])

# Add item to list
# Append - add item to the end of list
my_first_list.append('Java')
my_first_list.append('PHP')
my_first_list.append('Cobol')
print(my_first_list)

# Add item to list with index
my_first_list.insert(0, 'First Item')
print(my_first_list)

# Get item amount in list
print(len(my_first_list))

# Removing items from list
my_first_list.remove('Cobol')
print(my_first_list)
print(my_first_list.pop(0))

# Sort
unsorted_list = [10, 4, 6, 2, 3, 6, 7, 8, 0]
print(unsorted_list)

# ASC (Low to High)
unsorted_list.sort()
asc_sorted_list = unsorted_list
print(asc_sorted_list)

# DESC (High to Low)
unsorted_list.sort(reverse=True)
desc_sorted_list = unsorted_list
print(desc_sorted_list)

# Dictionary
my_first_dict = {'first_name': 'Andrew', 'last_name': 'Miko', 'birthdate': '1988-11-15'}

# Get item from Dict
print(my_first_dict['first_name'])
print(my_first_dict.get('last_name'))
# print(my_first_dict['birthdate'])  # Raise an Error
print(my_first_dict.get('birthdate'))  # Return None

# Change item in Dict
my_first_dict['first_name'] = 'Joe'
print(my_first_dict)

# Get keys and values
print(my_first_dict.keys())
print(my_first_dict.values())

# Remove key and value from Dict
del my_first_dict['birthdate']
print(my_first_dict)
my_first_dict.pop('first_name')
print(my_first_dict)

# Practice: Phone book
# Phone book: List
# Record in phone bool: Dict
# Dict Format: 'first_name', 'last_name', 'phone_number'

print('')
print('#' * 23)
print('### PHONE BOOK v0.1 ###')
print('#' * 23)
print('')

phone_book = []

# Prompt to enter new record data
first_name = input('First name? ')
last_name = input('Last name? ')
phone_number = input('Phone number? ')

# Store record data in solid structure
new_record = {
    'first_name': first_name,
    'last_name': last_name,
    'phone_number': phone_number
}

# Append new record to Phone book
phone_book.append(new_record)

# Print all records from Phone book
print(phone_book)