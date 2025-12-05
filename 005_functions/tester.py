# def say_hello(name):
#     print(f"Hello {name}!")


# say_hello("Roman")


# def square(number):
#     return number**2


# print(square(5) * 60)

# print(1 + 2)

# def biggest_of_two(a, b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     else:
#         return a
    

# print(biggest_of_two(7, 5))

# def fizz_buzz(start, end):
#     for num in range(start, end + 1):
#         if num % 5 == 0 and num % 3 == 0:
#             print(num, 'FIZZBUZZ')
#         elif num % 3 == 0:
#             print(num, 'FIZZ')
#         elif num % 5 == 0:
#             print(num, 'BUZZ')

# fizz_buzz(100, 200)

# def area(a, b):
#     return a * b

# def perimeter(a, b):
#     return (a + b) * 2

# def count_materials(order):
#     total_area = 0
#     total_perimeter = 0
#     for carpet in order:
#         total_area += area(carpet['width'], carpet['height']) * carpet['amount']
#         total_perimeter += perimeter(carpet['width'], carpet['height']) * carpet['amount']
#     # return (total_area, total_perimeter)
#     print(f'Total carpet material: {total_area / 1000}m2\nTotal carpet edge material: {total_perimeter/100}m')

# order = [
#     {
#         'width': 80,
#         'height': 40,
#         'amount': 32
#     },
#     {
#         'width': 120,
#         'height': 80,
#         'amount': 23
#     },
#     {
#         'width': 120,
#         'height': 120,
#         'amount': 15
#     },
# ]

# count_materials(order)


# def example(b, c, a=0, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)


# example(1, 2, 3, 'as', 13, True, None, name='Jack')


# def test(a, b, c):
#     print(a, b, c)

# test(c=100, b=200, a=100)


# def new_print(*values, sep=' ', end='\n'):
#     str_list = []
#     for val in values:
#         str_list.append(str(val))
#     print(sep.join(str_list) + end)

# new_print(1, 2, 3, 4, 5, 6, 7)


# a, b, c = 1, 2, 3

# def visibility():
#     a = 10
#     b = 20
#     # c = 30
#     print(a, b, c)

# visibility()
# print(a, b, c)


# x = 10

# def test(id_code):
#     global x
#     x = 100
#     print(x)


# test()
# print(x)

# people = [
#     ('Mary', 'Smith', 25),
#     ('Bob', 'Gold', 30),
#     ('Jack', 'Green', 19),
#     ('Simon', 'Summers', 30),
# ]

# for name, surname, age, *rest in people:
#     print(name, surname, age)

# import utils as u

# print(u.double(12))
# print(u.triple(5))

# from utils import double as dbl, PI
# from utils import *

# print(double(123))
# print(PI)
while True:
    user_choice = input('1. Say hello\n' \
                        '2. Say good bye\n' \
                        '3. Sleep\n' \
                        '0. Exit\n'
                        '--> ')

    if user_choice == '1':
        print('Hello')
    elif user_choice == '2':
        print('Good bye')
    elif user_choice == '3':
        print('Sleep')
    elif user_choice == '0':
        print('quitting')
        exit()
    else:
        print('Choice is our of range')