# Functions in Python


def welcome(name, year=None):
    print('')
    print('#' * 10)
    print(f'Hello, {name}!')

    if year:
        print(f'Year: {year}!')

    print('#' * 10)


# 1 CASE
welcome('Andrew')

# 2 CASE
welcome('Kate', 1990)


def power_of_two(number):
    result = number ** 2
    return result


print(power_of_two)


result = power_of_two(10)
print(result)


def power_number(number, power):
    return number ** power


res_0 = power_number(2, 5)
res_1 = power_number(number=3, power=3)


func = power_number
print(func(5, 2))


