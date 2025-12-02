# empty = {}
# empty = dict()

# print(type(empty))

# example = {
#     "name": "Jack",
#     "nickname": "Jack",
#     "courses": ['English', 'Math', 'Art'],
#     "number": 123,
#     "boolean": True,
#     "dictionary": {
#         "eye_color": "brown",
#         "height": 175
#     },
#     1: 'one',
#     0.5: 'half',
#     True: 'True value',
#     (1, 2, 3): 'set'
#     }

# print(example['courses'][1])
# print(example['dictionary']['eye_color'])
# print(example[(1, 2, 3)])

# print(example.get('name', []))
# example['name'] = 'Mary'
# example['phone'] = '555-555-5555'
# print(example)

# example.update({'name': 'Bob', 'surname': 'Smith'})
# print(example)

# surname = example.pop('name')
# print(surname)
# print(example)
# print(example.popitem())

# del example['name']
# print(len(example))


# print(dict([['one', 1], ['two', 2], ['three', 3]]))
# # print(list(example))
# print(example.keys())
# print(example.values())
# print(example.items())

# a = 7
# b = 10

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# print('123' == 123)
# print(ord('A'))
# print(chr(121))
# print('hello' > 'hellO')
# print([1, 2, 3] == [1, 2, 3])

# print(0 < a < 15)
# print(True and False)
# print(False or True)
# print(True and False or True)
# print(not False)

# print(4 not in [1, 2, 3])

# code = '3880316027'
# if len(code) == 11:
#     print(f'Your code is {code}')
# elif len(code) > 11:
#     print('Your code is too long')
# else:
#     print('Your code is too short')

# age = 26
# if age < 12 and age > 0:
#     print('Child')
# elif age <= 18:
#     print('Teenager')
# elif age <= 65:
#     print('Adult')
# elif age <= 120:
#     print('Senior')
# else:
#     print('Wrong input!')

# code = '38803160272'
# if len(code) == 11:
#     print(f'Your code is {code}')
# else:
#     if len(code) > 11:
#         print('Your code is too long')
#     else:
#         print('Your code is too short')

# name = input('Enter name: ')
# if name:
#     print(f'Hello {name}')
# else:
#     print('Hello stranger')


# print(list(range(1, 10)))
# print([*range(10)])
# print(*range(10, -10, -2))

# for num in range(10):
#     print(f'Number: {num}, Square: {num ** 2}')

# names = ['Jack', 'Mary', 'Bob', 'Jessica', 'Simon']
# for name in names:
#     if len(name) > 4:
#         print(f'Hello {name}. You have a long name')
#     else:
#         print(f'Hello {name}. You have a short name')

# people = [
#     {
#         'name': 'Jack',
#         'surname': 'Smith',
#         'salary': 2000
#     },
#     {
#         'name': 'Mary',
#         'surname': 'Gold',
#         'salary': 4000
#     },
#     {
#         'name': 'Bob',
#         'surname': 'Dylan',
#         'salary': 3000
#     }
# ]

# for person in people:
#     if person['name'] == 'Jack':
#         continue
#     elif person['name'] == 'Mary':
#         break
#     print(f'Hello {person['name']} {person['surname']}. Your salary is {person['salary']:.2f}$')

# print('Good bye!')

# for num1 in range(10):                  # 10
#     for num2 in range(10):              # 10 * 10 = 100
#         for num3 in range(10):          # 10 * 100 = 1000
#             for num4 in range(10):      # 10 * 1000 = 10000
#                 print(num1, num2, num3, num4)

# squares = []
# for x in range(1000000):
#     print(x ** 2)
#     # squares.append(x ** 2)


print(99 % 2 == 0)