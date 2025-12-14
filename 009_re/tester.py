import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
example*com
example&com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
800-*555-*1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Mary Robinson
Mr. T
abc
ball mall hall wall tall _all 4all
'''

sentence = 'Start a sentence and then bring it to an end'


# pattern = re.compile(r'M(r|s|rs)\.? [A-Z][a-z]*( [A-Z][a-z]*)?')


# matches = re.finditer(pattern, text_to_search)
# matches = pattern.finditer(text_to_search)

# for m in matches:
#     print(m)
#     print(m.start())
#     print(m.end())
#     print(m.span())
#     print(m.group())

# for m in matches:
#     # print(text_to_search[m.start():m.end()])
#     # print(m.group())
#     print(m)

# with open(r"009_re/people.txt", 'r') as file:
#     data = file.read()

# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# matches = list(pattern.finditer(data))

# for m in matches:
#     print(m)

# print(len(matches))


# emails = '''
# SampleMaiL@example.com
# john.sample@my-work.net
# jack-125-production@colledge.edu
# bob.Samples@example.co.uk
# example@example.org
# '''

# urls = '''
# https://www.google.com
# http://www.wordpress.org
# https://www.nasa.gov.net
# https://example.net
# www.example.net
# example.net
# '''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# matches = pattern.findall(emails)

# print(matches)

# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# print(pattern.findall(text_to_search))
# print(pattern.fullmatch('333-333-3333'))
# print(pattern.search(text_to_search))
# print(pattern.match('333-333-3333 444-444-4444'))
# print(pattern.split(text_to_search))
# print(pattern.sub('***', text_to_search))


# pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')

# match = pattern.search('2025-12-15')
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))
# print(match.group(3))


# pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')

# match = pattern.search('2025-12-15')
# print(match.group(0))
# print(match.group('year'))
# print(match.group('month'))
# print(match.group('day'))

# pattern = re.compile(r'(?:\d{4})-(\d{2})-(\d{2})')

# match = pattern.search('2025-12-15')
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))


# pattern = re.compile(r'(\d+)(?=kg)')
# pattern = re.compile(r'(?<=\$)\d+')

# match = pattern.findall('$400 @300 &400 $23')
# print(match)

# pattern = re.compile(r'(?<!\$|\d)\d+')

# match = pattern.findall('$400 @300 &400 $23')
# print(match)

pattern = re.compile(r'(\d+)(?!kg|\d)')

match = pattern.findall('10kg 200g 400t 876kg')
print(match)

