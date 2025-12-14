

"""
Task:
You have two lists: one containing names of students and another containing their corresponding scores.
Create a dictionary where the names are the keys and the scores are the values using zip().
"""

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 88]

student_scores = dict(zip(students, scores))
print(student_scores)
'''
Task:
You have a list of product prices in dollars. Convert them to euros using a given conversion rate (1 USD = 0.85 EUR).
Use map() to perform the conversion.
'''

usd_prices = [100, 150, 200, 250, 300]
conversion_rate = 0.85

eur_prices = list(map(lambda usd_price: usd_price * conversion_rate, usd_prices))
print(eur_prices)

'''
Task:
You have a list of ages. Use filter() to create a new list containing only the ages that are 18 or older.
'''

ages = [12, 17, 19, 24, 15, 30, 16, 18]

ages_filtered = list(filter(lambda age: age >= 18, ages))
print(ages_filtered)

'''
Task:
Given a dictionary of products and their prices, increase all prices by 10% using dictionary comprehension.
'''

products = {
    "Laptop": 1000,
    "Smartphone": 800,
    "Tablet": 500,
    "Headphones": 200
}

products = dict((key, round(value * 1.1, 2)) for key, value in products.items())
print(products)


'''
Task:
You have a list of numbers. 
- First, use a list comprehension to square all the numbers.
- Then, use filter() to extract only the squared numbers that are greater than 50.
'''

numbers = [3, 5, 7, 9, 11]

limit = 50
numbers_mod = [number ** 2 for number in numbers if number ** 2 > limit]

numbers_squared = [number ** 2 for number in numbers]
numbers_filtered = list(filter(lambda number: number > limit, numbers_squared))

print(numbers_mod, numbers_filtered)

