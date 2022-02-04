def announce(fn):
    def wrapper():
        print("Start running function...")
        fn()
        print("Done with the function.")
    return wrapper


@announce
def say_hello():
    print("Hello World!")


say_hello()
