def announce(f):
    def wrapper():
        print("About to run the dfunctions...")
        f()
        print("Done with the functions.")
        return wrapper

@announce
def hello():
    print("Hello, world!")

hello()