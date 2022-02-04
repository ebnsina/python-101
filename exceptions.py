import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input.")
    sys.exit(1)


try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can not divided by zero.")
    sys.exit(1)

print(f"{x} / {y}: {result}")
