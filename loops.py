# FOR loop
text = "Vestibulum turpis sem aliquet eget"  # Lorem ipsum text generator
users = ['root', 'admin', 'andrew', 'kate']
user_details = {
    'fname': 'Andrew',
    'lname': 'Miko',
    'email': 'andrew@gmail.com',
    'is_active': False,
    'a': 0,
}

# for Element in Elements:
# ...

# print each user on new line from list of users
print('')
print('### FOR LOOP: LIST ###')
for user in users:
    print(user)

# print each user detail on new line from dict
print('')
print('### FOR LOOP: DICT ###')
for detail in user_details:
    # user_details[detail] -> value
    # user_details.get(detail) -> value
    print(detail)

print('')
print('### FOR LOOP: DICT V2 ###')

# return list of values
print(user_details.values())

# return list of keys
print(user_details.keys())

# return key and value pairs from dict
print(user_details.items())

for key, value in user_details.items():
    print(key, value)

# print each char from string
print('')
print('### FOR LOOP: STR ###')
for char in text:
    print(char)


# WHILE loop
stop = 0
while stop < 10:
    print(stop)
    stop += 1


# 1. show greeting message
# 2. show menu
# 3. do something with selected menu item (from menu)
# 4. exit from program using "exit" as menu item

# menu_item = ""
# while

brands = ['Google', 'Maxima', 'Rimi', 'Microsoft', 'Logitech', 'Samsung', 'Apple', 'Xiaomi']
for brand in brands:
    print('Original name:', brand)

    chars_to_change = ['o', 'e', 'a', 'i']
    new_name = ''
    for char in brand:
        if char in chars_to_change:
            # char = '#'
            continue

        new_name += char
        print(new_name)

    print('Changed name:', new_name)
    # break
