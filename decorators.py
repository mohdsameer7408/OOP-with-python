# about decorator functions
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


# decorator_display = decorator_function(display)
# decorator_display()

display()

# about class decorators
# class DecoratorClass:
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print("call executed this before {}".format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
#
# @DecoratorClass
# def display():
#     print("Display function ran")
#
#
# display()
