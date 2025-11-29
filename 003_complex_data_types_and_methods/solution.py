
# Extract the first and last elements.
# Create a new list containing only the middle three numbers using slicing.
nums = [10, 20, 30, 40, 50]

first_num, last_num = nums[0], nums[-1]
new_nums = nums[1:-1]

print(first_num, last_num, new_nums)

# Combine them into one list.
# Duplicate list a three times.
a = [1, 2, 3]
b = [4, 5]

combined = [a + b]

print(combined  * 3)

# Replace "green" with "yellow" using indexing only.
# Add "purple" to the end without using append.
colors = ["red", "green", "blue"]

colors[1] = 'yellow'
colors += ["purple"]

print(colors)

# Extract the first three items as a new tuple.
# Create a tuple containing only the last two items.
t = ("apple", "banana", "cherry", "date", "kiwi")

head_t = t[:3]
tail_t = t[-2:]

print(head_t, tail_t)

# Unpack values into variables x, y, z.
coords = (10, 20, 30)

x, y, z = coords

print(x, y, z)

# Find the intersection.
# Find elements in s1 but not in s2.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

intersection = s1.intersection(s2)
s1_only = s1 - s2

print(intersection, s1_only)

# remove duplicates from list "items"
items = [1, 2, 2, 3, 4, 4, 4, 5]

items = list(set(items))
print(items)

# Find elements in either set but not both
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

unic = s1.symmetric_difference(s2)

print(unic)


# Create a set of unique characters.
# Count how many unique characters the word has.
word = "mississippi"

unic_set = set(word)

print(unic_set, len(unic_set)) 

# Check if a is a subset of b.
# Check if b is a superset of a.
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b), b.issuperset(a))

# Remove "bird" from the set without using conditionals.
# Remove "turtle" and observe what happens (using .discard()).
animals = {"cat", "dog", "bird", "fish"}

animals.remove("bird")

print(animals, animals.discard("turtle"))

# Combine all sets into one set using a built-in (hint: set.union() can take multiple arguments).
list_of_sets = [{1, 2}, {2, 3, 4}, {4, 5}]

s1, s2, s3 = list_of_sets
union_of_sets = s1 | s2 | s3

print(union_of_sets)


