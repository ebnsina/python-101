# For loop


for i in [0, 1, 2, 3, 4]:
    print(i)


for i in range(0, 50):
    print(i)


name = 'ebnsina'

for char in name:
    print(char)


# While loop
cart = [
    {'name': 'apple', 'qty': 10},
    {'name': 'orange', 'qty': 20},
    {'name': 'mango', 'qty': 40},
]


fruit = input('Enter a fruit: ')

i = 0
item_found = False

while i < len(cart):
    item = cart[i]

    if item['name'] == fruit:
        item_found = True
        print(f"{item['qty']} {item['name']}")

    i += 1


# DO while
i = 0

while True:
    i += 1
    text = input("Enter: ")

    if text == 'quit':
        break
