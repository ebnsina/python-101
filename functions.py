

def square(x):
    return x * x


# args

def result_args(*args):
    print(args)
    return sum(args)


print(result_args(10, 20, 30, 40))

# kwargs


def result_kwargs(**kwargs):
    print(kwargs)
    print(
        f"Product name {kwargs['name']}, price is {kwargs['price']} and quantity is {kwargs['quantity']}.")


print(result_kwargs(name='Apple', price=100, quantity=5))
