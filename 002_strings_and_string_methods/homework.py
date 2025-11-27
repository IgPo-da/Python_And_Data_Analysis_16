# Useful links
"""
# W3 python reference
https://www.w3schools.com/python/python_reference.asp
# W3 string formatting table
https://www.w3schools.com/python/python_string_formatting.asp
"""

# Tasks
# Use provided variables to complete a task


# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(example_string1[:2] + example_string1[-2:])

# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2[0].upper() + example_string2[1:].lower())

# Write a code to return "Get rid of junk please"
example_string3 = "%-*Get rid of *junk* please*-%*"
print(example_string3[3:-4].replace("*",""))

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
print(example_string4[:6].title() + example_string4[6:-4] + example_string4[-4:].title())

# Find all occurrences of “Estonia” in a given string ignoring the case.
example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."

word = "Estonia"
position = example_string5.upper().find(word.upper(), 0)
while position != -1:
    print(f"The word {example_string5[position:position + len(word)]} is on the {position} place")
    position = example_string5.upper().find(word.upper(), position + len(word))


# Write a code to return f-string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"

print(f"{var2.title()}, {var3.lower()} {var1.title()}")


# # Write a code to return byte_string text value
byte_string = b"\316\273"

print(f"Text value form byte_string {byte_string} is {byte_string.decode("utf-8")}")
