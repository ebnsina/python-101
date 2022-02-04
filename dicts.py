# Empty dict

empty_dict = {}


# Access using square bracket notation
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
}

print(person['first_name'])


# get method
# ssn = person['ssn']
ssn = person.get('ssn')
ssn = person.get('ssn', '123-00-789')


# ADDING ITEM
person['gender'] = 'Male'

# MODIFY ITEM
person['last_name'] = 'Smith'

# REMOVE ITEM
del person['gender']

# LOOPING: keys(), values(), items()

# DICT COMPREHENSION
prices = {
    'apple': 12.88,
    'orange': 11.38,
    'mango': 15.66,
}


price_with_tax = {}

for item, price in prices.items():
    price_with_tax[item] = price * 1.15

print(price_with_tax)


price_with_tax = {item: price * 1.15 for (item, price) in prices.items()}

print(price_with_tax)
