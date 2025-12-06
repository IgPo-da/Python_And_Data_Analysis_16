# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number

nums = [2, 4, 6, 1, 7, 3, 9]


def get_squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares


print(get_squares(nums))

# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_odd_even(numbers):
    odd, even = 0, 0
    for number in numbers:
        if number % 2:
            odd += 1
        else:
            even += 1
    return (odd, even)


result = get_odd_even(nums)
print(result)

# Write a function that accepts a list of numbers
# and returns largest number

nums = [2, 4, 6, 1, 7, 3, 9, 13, 6, 5]


def find_largest(numbers):
    return (max(numbers))


print(find_largest(nums))

# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)


def fizzbuzz(start=1, stop=30):
    for number in range(start, stop + 1):
        fizz_buzz_str = ''  # string for FIZZ, BUZZ or FIZZBUZZ
        if number % 3 == 0:
            fizz_buzz_str += "FIZZ"
        if number % 5 == 0:
            fizz_buzz_str += "BUZZ"
        if fizz_buzz_str:   # prints only number devided by 3 or 5
            print(number, fizz_buzz_str)


fizzbuzz()

WEIGHTS_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
WEIGHTS_2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)

id_code = 37008270150
id_code = 38702020053
id_code = 38001085718
id_code = 47101010033



def weighted_sum(weights, number):
    sum_of_weighted = 0
    for weight, digit in zip(weights, number):
        sum_of_weighted += weight * int(digit)
    return sum_of_weighted

def check_estonian_id(personal_id):
    number = str(personal_id)[:10]
    control_number = weighted_sum(WEIGHTS_1, number) % 11
    if control_number == 10:
        sum_2 = weighted_sum(WEIGHTS_2, number) % 11
        control_number = sum_2 if sum_2 < 10 else 0
    return control_number


print(f"id control number for ID {id_code} is {check_estonian_id(id_code)}")


