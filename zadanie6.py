def uppercase_decorator(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"

@uppercase_decorator
def repeat_message(message):
    return message

# Przykłady użycia
print(say_hello())
print(repeat_message("Python is fun!"))
