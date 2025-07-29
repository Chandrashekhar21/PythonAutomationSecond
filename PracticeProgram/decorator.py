def precondition(func):
    def wrapper(*args,):
        print("hello")
        return func(*args, **kwargs)
    return wrapper