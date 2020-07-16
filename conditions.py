num_a = 10
num_b = -4
name = "Andrew"

# Other language
# if (condition) {
#   block
# }

# Python
# if condition:
#   block

if num_a > 1:
    print('num_a > 1')

# if False:
#     print('ALWAYS WORKS')

if num_b > 0:
    print('num_b > 0')
elif num_b < 0:
    print('num_b < 0')
elif num_b < -10:
    print('num_b < -10')
else:
    print('num_b: else block')

# Comparison operators
# >, <, >=, <=, ==, !=
if num_a == num_b:
    print('num_a and num_b are equal')
else:
    print('num_a and num_b not equal')

# AND / OR
if (num_a > 0) and (num_b > 0):
    print('num_a and num_b are > 0')

# NOT
if not num_a > 0:
    print('num_a > 0')

# IS
if num_a is num_b:
    print('something is wrong...')

# TODO: IN

print('EXIT')
