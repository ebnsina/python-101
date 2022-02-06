# Functions are first class citizen:

from functools import reduce


def say_hello():
    return 'Hello!'


hello = say_hello()

my_list = ['ebnsina', 100, say_hello]

# print(my_list)


# Functions can be pass to another function as argument: Function composition
def inner():
    print('I am inner function.')


def outer(fn):
    fn()


# outer(inner)


# Callback function
fruits = ['apple', 'orange', 'mango']


print(sorted(fruits, key=len, reverse=True))


# Anonnymous function with lambda

# OLD WAY
def sort_reverse(s):
    return s[::-1]


# LAMBDA WAY
sort_reverse2 = lambda s: s[::-1]

print(sort_reverse('hello'))
print(sort_reverse2('hello'))


# LAMBDA WAY 2
print((lambda s: s[::-1])('Hello World'))


# DATA
results = [100, 200, 300, 400]

animals = ['lion', 'tiger', 'wolf']

products = [
    {'name': 'Smart Phone', 'price': 400},
    {'name': 'Smart TV', 'price': 290},
    {'name': 'Laptop', 'price': 800},
    {'name': 'Book', 'price': 15},
    {'name': 'Pen', 'price': 35},
    {'name': 'Kindle', 'price': 99},
]


# MAP: map(fn, iter)
def reversy(str):
    return str[::-1]


# it return map obj, so we need to turn it into list
print(list(map(reversy, animals)))


# FILTER: filter(fn, iter)
print(list(filter(lambda x: x > 100, results)))

# REDUCE: reduce(fn, iter)
print(reduce(lambda a, b: a + b, results))

print(reduce(lambda a, b: a if a > b else b, results))


# List comprehension
# OLD WAY
values = []
for i in range(1, 5):
    values.append(i * 2)

print(values)

# NEW WAY
multiply_by_2 = [i * 2 for i in range(1, 5)]
print(multiply_by_2)

# Dict comprehension
# OLD WAY

calculated_price = []
for product in products:
    tax = round(product['price'] * 1.15, 2)
    calculated_price.append(tax)

print(sorted(calculated_price))

# NEW WAY
price_with_tax = {round(product['price'] * 1.15, 2) for product in products}
print(sorted(price_with_tax))
