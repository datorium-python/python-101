# Decorators in Python


def add_numbers(a, b):
    return a + b


print(add_numbers(1, 2))


# func = add_numbers
# print(func(2, 3))


def say_hello(name):
    return f"Hello, {name}!"


def say_hola(name):
    return f"Hola, {name}!"


def say_yo(name):
    return f"Yo, {name}!"


def show_greeting(greeting_func, name):
    message = greeting_func(name)
    print(message)


# Say Hola!
show_greeting(say_hola, "Andrew")
show_greeting(say_yo, "Kate")


def parent(number):
    def less_than_10():
        return "number is less than 10"

    def equal_to_10():
        return "number is equal to 10"

    def more_than_10():
        return "number is more than 10"

    if number < 10:
        return less_than_10
    elif number == 10:
        return equal_to_10
    else:
        return more_than_10

# print(parent(10))
# print(parent(7))
# print(parent(99))


first_result = parent(10)
second_result = parent(7)

print(first_result())
print(second_result())


def my_decorator(func):
    def wrapper():
        print("Wrapper function called")
        print("Running func")
        func()
        print("Finish with func")
    return wrapper


@my_decorator
def say_salut():
    print("Salut!")


@my_decorator
def say_hello_friend():
    print("Hello, friend!")


say_salut()
say_hello_friend()


# OLD STYLE
# show_message_salut = my_decorator(say_salut)
# show_message_salut()
#
# show_message_hello_friend = my_decorator(say_hello_friend)
# show_message_hello_friend()


import functools


def decorator(func):
    # It's not necessary, but better to have it (c) Python Community
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)

        print("Wrapper started")
        print("Doing something")
        result = func(*args, **kwargs)
        print(result)
        print("Finished")
        return result
    return wrapper


@decorator
def say_hola_2():
    return "Hola, user!"


@decorator
def say_hola_3(name):
    return f"Hola, {name}!"


say_hola_2()
say_hola_3(name="Andrew")
