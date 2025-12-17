import re

hex_pattern = re.compile(r'#[\dA-Fa-f]{6}')

not_followed = re.compile(r'(\d+)(?!\+|\d)')

print(not_followed.findall('987+23-45*22'))

time_pattern = re.compile(r'\b([01]\d|2[0-3]):([0-5][\d])\b')

print(list(time_pattern.finditer('234:231, 23:59, 25:40, 01:67, 01:43')))

names = re.compile(r'([A-Z][a-z]+ [A-Z][a-z])(?=\n)')
address = re.compile(r'\d{3} [A-Za-z0-9]+ St., ([A-Z][\'a-z- ]+)+ [A-Z]{2} \d{5}')

with open(r'009_re/people.txt', 'r') as file:
    data = file.read()

print(len(list(address.finditer(data))))

string_pattern = re.compile(r'[^a-zA-Z0-9]')

isikukood_pattern = re.compile(r'\b[1-8]\d{2}(0[1-9]|1[12])([0-2]\d|3[01])\d{4}\b')

