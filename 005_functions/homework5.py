# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
def squares_list(numbers: list[int]) -> list[int]:
    squares = []
    for num in numbers:
        squares.append(int(num) ** 2)
    return squares

print(squares_list([1, 2, 3, 4, 5, 6, 7, 8]))

# user_list = input('Enter numbers separated with coma: ')
# print(squares_list(user_list.split(', ')))

# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens
def count_odd_and_evens(numbers: list[int]) -> tuple[int]:
    odds, evens = 0, 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return (odds, evens)

print(count_odd_and_evens([2, 5, 6, 8, 34, 23, 73]))


# Write a function that accepts a list of numbers
# and returns largest number
def largest_number(numbers: list[int]) -> int:
    return max(numbers)

print(largest_number([1, 2, 3, 4, 5, 6, -2]))

# x: str = 'Hello world'
# y: int = 'Hello world'

# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)
def fizz_buzz(start=1, end=101):
    for num in range(start, end + 1):
        if num % 5 == 0 and num % 3 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')

fizz_buzz(100, 200)