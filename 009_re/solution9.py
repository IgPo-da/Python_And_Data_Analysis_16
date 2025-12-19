# https://regexr.com/3cpbs
import requests
import re


print('1.  Find a HEX (HTML) color')
# 1. Write a regular expression to find a HEX (HTML) color written as #ABCDEF, i.e., it starts with # and is followed by 6 hexadecimal characters.
# HEX colors use values from 0 to 15, where 0–9 are digits from zero to nine, and 10–15 are letters from A to F.

URL = "https://raadiotallinn.err.ee"
URL = "https://rus.postimees.ee/"
try:
    with requests.get(URL) as response:
        response.raise_for_status()
        print(f"Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error accurred: {e}")

hyml_page = response.text
#print(response)
hex_color_pattern = re.compile(r"[#]([\da-fA-F]{6})")
matches = hex_color_pattern.finditer(hyml_page)

for match in matches:
    print(match, "HEX color code:", match.group(1))

print('2. Create a query to identify digits')
# 2. Create a query to identify digits in a text that are not followed by a plus sign (+).
# Examples of expressions: 2*9-6*5 or (3+5)-9*4.
example = "2*9-6*5(3+5)-9*4"

pattern = re.compile(r"[\d]{1}(?!\+)")
matches = pattern.findall(example)

print(matches)

print('3. Find time in a text')
# 3. Find time in a text. Time has the format hours:minutes. Both hours and minutes consist of two digits, for example: 09:00.
# Write a regular expression to find time in the string:
# 	"Breakfast at 09:00".
# 	Note that 37:98 is not a valid time.
# 	Valid range: [00:00 - 23:59]
# 	(123:312, 12:123, 123:23, 98:67 are not valid times).

time_test = ["22:00", "12:10", "13:40", "01:22", "8:40", "24:00", "22:60", "29:20",
                    "Breakfast at 09:00", "Note that 37:98 is not a valid time.",
                    "Valid range: [00:00 - 23:59]",
                    "(123:312, 12:123, 123:23, 98:67 are not valid times)."]

time_pattern = re.compile(r"\b((?:\d|[0]\d|1\d|2[0-3]):[0-5]\d)\b")
#matches = time_pattern.findall(time_string)
#print(matches)
for tt in time_test:
    matches = time_pattern.findall(tt)
    if matches:
#        print(matches.group(0))
        print(f'{tt} : {matches} - Positive match')
    else:
        print(f'{tt}    -   Not matched')


print('4. Write a program that selects data from the file people.txt:')
# 4. Write a program that selects data from the file people.txt:

# 	All first names and last names × 100
# 	All addresses × 100
file = "009_re/people.txt"

with open(file, 'r') as f:
    text = f.read()

#print(text)
Word = r"[A-Z][a-z]+"

person_name_pattern = re.compile(rf"^(({Word})\s+({Word}(?:-{Word})?))\s*$", re.MULTILINE)
#278 Main St., Gotham KY 89569
address_pattern = re.compile(rf"""^((\d{{3}}\s+\w+\s+St.,)\s+([\w']+(?:(-|\s)+\w+)?)\s+[A-Z]{{2}}\s+\d{{5}}\s*$)""", re.MULTILINE) 
matches_person = person_name_pattern.findall(text)
matches_address = address_pattern.findall(text)

for p, a in zip(matches_person, matches_address):
    print(f"{p[0]}      :       {a[0]}")

print(len(matches_person), len(matches_address))

print('5. Write a regular expression for characters a-z, A-Z, 0-9.')
# 5. Write a regular expression to validate a string and determine whether it consists only of the characters a-z, A-Z, 0-9.
def validate_string(string: str):
    pattern = re.compile(r"([^a-zA-Z0-9])")
    match = pattern.findall(string)
    if match:
        print("it consists NOT only of the characters a-z, A-Z, 0-9")
        print(match)
    else:
        print("it consists only of the characters a-z, A-Z, 0-9")  

validate_string("Write1a2regular3expression34to565validat&&@$")

print('6. Write a regular expression to validate an Estonian personal identification code (isikukood).')
# 6. Write a regular expression to validate an Estonian personal identification code (isikukood).

code ="38803160272"

def validate_id():
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    def validator(check_weight):
        result = 0
        for num in range(10):
            result += int(id_code[num]) * check_weight[num]
        return result % 11
    
    # 38803160272
    
    if validator(chk1) == 10:
        if validator(chk2) == int(id_code[-1]):
            print('Code is valid 2')
        else:
            print('Code is invalid')
    elif validator(chk1) == int(id_code[-1]):
        print('Code is valid 1')
    else:
        print('Code is invalid')

pattert = re.compile(r"\b(/d{2})\b")

id_code = pattern.findall(code)

if id_code:
    print(id_code)
    validate_id()


