import re

# ? simple group example
pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')

match = re.search(pattern, '2025-12-15')

print(match)

# ? group(0) is always a full match
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))


# ? named groups
pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')

match = re.search(pattern, '2025-12-15')

print(match)
print(match.group('year'))
print(match.group('month'))
print(match.group('day'))

# ? Non capturing groups, using ?: will not create a group, but will use it
pattern = re.compile(r'(?:cat|dog)\s+(\d+)')
match = re.findall(pattern, 'cat 10 dog 20')

pattern = re.compile(r'(cat|dog)\s+(\d+)')
match = re.findall(pattern, 'cat 10 dog 20')

print('NON CAPTURING', match)


# ? Look after group
pattern = re.compile(r'(\d+)(?=kg)')
match = re.findall(pattern, '10kg 20g 30kg 4000t 394kg')

print('AFTER', match)

# ? Look before group
pattern = re.compile(r'(?<=€)\d+')
match = re.findall(pattern, '€100 $500 $200 €120')
print('BEFORE', match)

# ? Not followed by
pattern = re.compile(r'(\d+)(?!\+|\d)')
match = re.findall(pattern, '12-34+872*23+89')


print('NOT FOLLOWED', match)

# ? Not before
pattern = re.compile(r'(?<!\+|\d)(\d+)')
match = re.findall(pattern, '12-34+872*23+89')

print('NOT BEFORE', match)
