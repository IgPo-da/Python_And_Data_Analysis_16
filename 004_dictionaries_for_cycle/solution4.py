# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']
long_names = []
short_names = []
print()
for name in names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)

print(long_names)
print(short_names)
print()


# Given a list where each element is a year. Determine whether the given year is a leap year. If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]

for year in years_list:
    leap = "NO"
    if not year % 400:
        leap = "YES"
    elif not year % 4 and year % 100:
        leap = "YES"
    print(leap)


# Write a program that prompts the user for a string and checks if the string contains only unique characters.
user_input = input('\nEnter something: ')

unic = len(user_input) == len(set(user_input))
print(f"The string you provided contains {'duplicated' if not unic else 'only unique'} characters {set(user_input) if unic else ''}\n")


# Write a program that checks gender for each person.
# If person is a male, print "This is NAME SURNAME. He is AGE years old"
# If person is a female, print "This is NAME SURNAME. She is AGE years old"
people = [
    ('Jane', 'Smith', 26, 'female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'male'),
]

for name, surname, age, gender in people:
    gen = "She"
    if gender == "male":
        gen = "He"
    print(f"This is {name} {surname}. {gen} is {age} years old")
print()
# FIZZ BUZZ
# For range of numbers between 1 and 100.
# If number is divided by 3 without a remainder print number and FIZZ
# If number is divided by 5 without a remainder print number and BUZZ
# If number is divided by 5 and by 3 without a remainder print number and FIZZBUZZ

# I found a hint on Google, but wrote it myself :)
# I was surprised that I could use string concatenation for this particular case. 
# I was going to use another comparison on 3 and 5 at the same time or another 2 comparisons within the checks on 3 and 5
for i in range(1, 101):
    FB = ''
    if not i % 3:
        FB += "FIZZ"
    if not i % 5:
        FB += "BUZZ"
    if FB:
        print(i, FB)


