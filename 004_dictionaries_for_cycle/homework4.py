# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']
long_names = []
short_names = []
for name in names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)

print('Long names:', long_names)
print('Short names:', short_names)


# Given a list where each element is a year. Determine whether the given year is a leap year. 
# If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, 
# a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]
for year in years_list:
    # if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     print(year, 'YES')
    # else:
    #     print(year, 'NO')

    if year % 4 == 0 and year % 100 != 0:
        print(year, 'YES')
    elif year % 400 == 0:
        print(year, 'YES')
    else:
        print(year, 'NO')


# Write a program that prompts the user for a string and checks if the string contains only unique characters.
user_input = input('Enter something: ')

# if len(user_input) == len(set(user_input)):
#     print('All chars are unique')
# else:
#     print('Contains not unique chars')
count_nums = {}
for char in user_input:
    count_nums[char] = user_input.count(char)
if max(count_nums.values()) > 1:
    print('Non unique include')
else:
    print('All chars are unique')


# Write a program that checks gender for each person.
# If person is a male, print "This is NAME SURNAME. He is AGE years old"
# If person is a female, print "This is NAME SURNAME. She is AGE years old"
people = [
    ('Jane', 'Smith', 26, 'Female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'Male'),
]

for person in people:
    if person[-1].lower() == 'male':
        gender = 'He'
    else:
        gender = 'She'
    print(f'This is {person[0]} {person[1]}. {gender} is {person[2]} years old.')


# FIZZ BUZZ
# For range of numbers between 1 and 100.
# If number is divided by 3 without a remainder print number and FIZZ
# If number is divided by 5 without a remainder print number and BUZZ
# If number is divided by 5 and by 3 without a remainder print number and FIZZBUZZ

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print(num, 'FIZZBUZZ')
    elif num % 3 == 0:
        print(num, 'FIZZ')
    elif num % 5 == 0:
        print(num, 'BUZZ')
    