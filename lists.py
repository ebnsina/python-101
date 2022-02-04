from functools import reduce

# Empty list
empty_list = []

# Colors list
colors = ['Red', 'Green', 'Blue']


my_list = [1, 3, 4, 7]

# MODIFY ELEMENT TO LIST
my_list[0] = 10
print(my_list)

# ADDING ELEMENT TO LAST OF LIST
my_list.append(50)
print(my_list)

# REMOVING LAST ELEMENT FROM LIST
my_list.pop()
print(my_list)

# REMOVING SPECIFIC ELEMENT FROM LIST
del my_list[0]
print(my_list)

# REMOVING ELEMENT FROM LAST OF LIST
my_list.remove(4)
print(my_list)


# SORT LISTS
scores = [5, 7, 4, 6, 9, 8]
scores.sort(reverse=True)
print(scores)


# SORTED LISTS
sorted(scores)
print(scores)


# SLICE LISTS [start:end:step]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[1:4]
print(sub_colors)


# LIST UNPACK
colors = ['red', 'blue', 'green']
red = colors[0]
blue = colors[1]
green = colors[2]

red, blue, green = colors  # unpacking
cyan, magenta, *other = colors


# LOOP OVER LIST
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for item in enumerate(cities):
    print(item)


# GET INDEX OF SPECIFIC ELEMENT OF LISTS
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

result = cities.index('Mumbai')
print(result)


# MAP (function, iterable)
my_numbers = [10, 20, 30]
my_new_numbers = map(lambda x: x * 2, my_numbers)
print(list(my_new_numbers))

my_names = ['ebnsina', 'jane', 'sarah']
my_new_names = map(lambda name: name.capitalize(), my_names)
print(list(my_new_names))


# FILTER (function, list)
scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, scores)
print(list(filtered))

countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)
print(list(populated))


# REDUCE (function, list)
prices = [75, 65, 80, 95, 50]
total = reduce(lambda x, y: x + y, prices)
print(total)


# LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5]
sqaures = [number * 2 for number in numbers]

print(sqaures)
