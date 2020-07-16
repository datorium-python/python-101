# Boolean
var_true = True  # int(1)
var_false = False  # int(0)

# Null / None Type
var_none = None

# Tuples
var_tuple = (1, 2, 3, 'abc')
print(var_tuple[0])

# Admins
admins = (
    (0, 'Andrew Miko', 'andrew@gmail.com'),
    (10, 'Joe Doe', 'joe@gmail.com'),
    (20, 'Kate Doe', 'kate@gmail.com'),
)

# Sets
var_seq_1 = {1, 2, 3, 1}
var_seq_2 = {3, 4, 5}
print(var_seq_1)

var_seq_union = var_seq_1.union(var_seq_2)
print(var_seq_union)
var_seq_diff_1 = var_seq_1.difference(var_seq_2)
var_seq_diff_2 = var_seq_2.difference(var_seq_1)
print(var_seq_diff_1)
print(var_seq_diff_2)

# First Example with Sets
admins = ['root', 'admin', 'kate']
users = ['admin', 'kate', 'andrew']
all_users = admins + users
print(type(all_users), all_users)
uniq_users = set(all_users)
print(uniq_users)

#
