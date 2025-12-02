
# Extract the first and last elements.
# Create a new list containing only the middle three numbers using slicing.
nums = [10, 20, 30, 40, 50]
first, *rest, last = nums
print(first)
print(rest)
print(last)


# Combine them into one list.
# Duplicate list a three times.
a = [1, 2, 3]
b = [4, 5]
new = a + b
# a.extend(b)
print(new * 3)


# Replace "green" with "yellow" using indexing only.
# Add "purple" to the end without using append.
colors = ["red", "green", "blue"]
colors[1] = "yellow"
# colors += ["purple"]
colors.extend(["purple"])

print(colors)


# Extract the first three items as a new tuple.
# Create a tuple containing only the last two items.
t = ("apple", "banana", "cherry", "date", "kiwi")
first = t[:3]
last = t[-2:]
print(first)
print(last)


# Unpack values into variables x, y, z.
coords = (10, 20, 30)
x, y, z = coords
print(x)
print(y)
print(z)

# Find the intersection.
# Find elements in s1 but not in s2.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
intersect = s1.intersection(s2)
print(intersect)
unique = s1.difference(s2)
print(unique)


# remove duplicates from list "items"
items = [1, 2, 2, 3, 4, 4, 4, 5]
items = list(set(items))
print(items)


# Find elements in either set but not both
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print(x.symmetric_difference(y))


# Create a set of unique characters.
# Count how many unique characters the word has.
word = "mississippi"
unique = set(word)
print(len(unique), unique)

# Check if a is a subset of b.
# Check if b is a superset of a.
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))
print(b.issuperset(a))


# Remove "bird" from the set without using conditionals.
# Remove "turtle" and observe what happens (using .discard()).
animals = {"cat", "dog", "bird", "fish"}
animals.discard('bird')
animals.discard('turtle')
print(animals)


# Combine all sets into one set using a built-in (hint: set.union() can take multiple arguments).
list_of_sets = [{1, 2}, {2, 3, 4}, {4, 5}]
# print(list_of_sets[0].union(list_of_sets[1], list_of_sets[2]))
new = list_of_sets[0].union(list_of_sets[1], list_of_sets[2])
new_all = list(list_of_sets[0]) + list(list_of_sets[1]) + list(list_of_sets[2])
print(new)
print(new_all)