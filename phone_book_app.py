# Practice: Phone book
# Phone book: List
# Record in phone bool: Dict
# Dict Format: 'first_name', 'last_name', 'phone_number'

import datetime


def print_welcome():
    """Prints welcome message when program starts"""
    print('')
    print('#' * 23)
    print('### PHONE BOOK v0.2 ###')
    print('#' * 23)
    print('')


def parse_bday_value(value):
    if value.isnumeric():
        return int(value)
    else:
        return None


print_welcome()

phone_book = []

# Prompt to enter new record data
first_name = input('First name? ')
last_name = input('Last name? ')
phone_number = input('Phone number? ')
birth_date = input('Birth date? (YYYY-MM-DD) ')  # YYYY-MM-DD [1988-11-15]

# User gives birth date
# We parse (split) it by dashes (-)
# Example: '1988-11-15' => ['1988', '11', '15']
# str.split('-') => return list

if birth_date != '':
    birth_date_values = birth_date.split('-')  # Return List[]

    # WAS
    # if birth_date_values[0].isnumeric():
    #     birth_date_year = int(birth_date_values[0])
    # else:
    #     birth_date_year = None

    # if birth_date_values[1].isnumeric():
    #     birth_date_month = int(birth_date_values[1])
    # else:
    #     birth_date_month = None

    # if birth_date_values[2].isnumeric():
    #     birth_date_date = int(birth_date_values[2])
    # else:
    #     birth_date_date = None

    # CURRENT
    birth_date_value_year = birth_date_values[0]
    birth_date_year = parse_bday_value(birth_date_value_year)

    birth_date_value_month = birth_date_values[1]
    birth_date_month = parse_bday_value(birth_date_value_month)

    birth_date_value_date = birth_date_values[2]
    birth_date_date = parse_bday_value(birth_date_value_date)

    birth_date_tuple = (birth_date_year, birth_date_month, birth_date_date)
    current_year = datetime.datetime.now().year

    # age = 2020 - None -> Exception (Error)
    if birth_date_tuple[0] is None:
        age = None
    else:
        age = current_year - birth_date_tuple[0]

else:
    age = None
    birth_date_tuple = None

# Store record data in solid structure
new_record = {
    'first_name': first_name,
    'last_name': last_name,
    'phone_number': phone_number,
    'age': age,
    'birth_date': birth_date_tuple,
    'blocked': False,
}

# Append new record to Phone book
phone_book.append(new_record)

# Print all records from Phone book
print(phone_book)