# print('Task 01')

# #! Write a function that accepts a list of numbers as an argument
# #! And returns list with squares for each number

# numbers = input('Enter your numbers separated by spaces: ')
# numbers = [int(num) for num in numbers.split()] # Convert string input into a list of integers

# def square_list(numbers):
#     return [num ** 2 for num in numbers]

# print(square_list(numbers)) # Call the function and print the result

#?______________________________
# print('Task 02')

#! Write a function that accepts a list of numbers
#! And returns a tuple with two numbers, amount of odd and even numbers
#! Example: input -> [1, 2, 3, 4, 5] output (3, 2)
#! Where 3 is amount of Odds and 2 is amount of evens

# numbers = input('Enter your numbers separated by spaces: ')
# numbers = [int(num) for num in numbers.split()] # Convert string input into a list of integers

# def count_odds_evens(numbers):
#     odd_count = 0
#     even_count = 0

#     for num in numbers:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1

#     return ('Number of odd numbers:', odd_count, 'Number of even numbers:', even_count)
# print(count_odds_evens(numbers))

#?___________________
# print('Task 03')
# #! Write a function that accepts a list of numbers
# #! and returns largest number 

# numbers = input('Enter your numbers separated by spaces: ')
# numbers = [int(num) for num in numbers.split()] # Convert string input into a list of integers

# def maximum_number(numbers):
#     return ('Maximum number is:', max(numbers))
# print(maximum_number(numbers))

#?_________________________

#! ID CARD

#if not input.isdigit() or len(input) != 4:
#    print("Ivalid input ❌ (Must be exactly 4 digits and numbers only)")

id_number = input('Enter your ID number: ')

if len(id_number) != 8:
    print('Ivalid input ❌ (Must be exactly 8 digits)')
else:
    print('Valid input ✔. Your ID code is:', id_number)

    if (int(id_number[0]) % 2 == 1):
        print ('Genger: Male')
    else:
        print('Gender: Female')

    if int(id_number[0]) == 1 or int(id_number[0]) == 2:
        birth_century = range(1800,1899)
    elif int(id_number[0]) == 3 or int(id_number[0]) == 4:
        birth_century = range(1900,1999)
    elif int(id_number[0]) == 5 or int(id_number[0]) == 6:
        birth_century = range(2000,2099)
    elif int(id_number[0]) == 7 or int(id_number[0]) == 8:
        birth_century = range(2100,2199)
    print('Birth century:', birth_century)

    # birth_year = int(id_number[1] + id_number[2])
    # print(birth_year)

    birth_year = birth_century[0] + int(id_number[1] + id_number[2])
    print('Birth Year:', birth_year)

    birth_month = int(id_number[3] + id_number[4])
    if birth_month == int('01'):
            # birth_month = 'January'
        print(birth_month)

#49203100053