from pprint import pp

# coords = [(2, 5), (3, 2), (1, 4), (4, 8)]
# #        [(1, 4), (2, 5), (3, 2), (4, 8)]

# coords.sort(key=lambda el: el[1])
# print(coords)

# people = [
#     {
#         'name': 'Jack',
#         'salary': 3000,
#     },
#     {
#         'name': 'Mary',
#         'salary': 4000,
#     },
#     {
#         'name': 'Bob',
#         'salary': 2000,
#     },
# ]

# people.sort(key=lambda person: person['salary'])
# print(people)

# # def sort_by_second(element):
# #     return element[1]

# # coords.sort(key=sort_by_second)

# # print(coords)

# # def sort_by_salary(element):
# #     return element['salary']

# # people.sort(key=sort_by_salary)
# # print(people)


# x = lambda: print("Hello world!")
# x()

# y = lambda a, b: a ** b
# print(y(2, 10))

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# zipped = zip(list1, list2, range(10), [11, 22, 33, 44, 55])

# print(list(zipped))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# new = filter(lambda num: num % 2 != 0, numbers)

# print(list(new))

# words = ['planet', 'electricity', 'bat', 'ball', 'world']

# long_words = list(filter(lambda word: len(word) > 6, words))
# short_words = list(filter(lambda word: len(word) <= 6, words))

# print(long_words)
# print(short_words)

# expanded_numbers = map(lambda num: {'number': num, 'square': num ** 2, 'cube': num ** 3}, numbers)
# pp(list(expanded_numbers))

# words_modified = map(lambda word: word.title(), words)
# pp(list(words_modified))

# first_letters = map(lambda word: word[0], words)
# pp(list(first_letters))

# numbers = [1, 2, 3, 4, 5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)

# squares = [num ** 2 for num in numbers]
# print(squares)

# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# labels = [f'{num} is Even' if num % 2 == 0 else f'{num} is Odd' for num in numbers]
# print(labels)

# pairs = [(x, y) for x in range(3) for y in range(3)]
# print(pairs)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# zipped = zip(list1, list2)

# summed = [x + y for x, y in zipped]
# print(summed)

# squared_dict = {num: num ** 2 for num in numbers}

# print(squared_dict)

# print({1, 2, 3} & {3, 4, 5})


