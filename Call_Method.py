class Product:
    """
    This is the example of __call__ method,
    This method is call when we call the object
    and __init__ method will be call when we create the class object.
    """
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)

# Instance created
ans = Product()

# __call__ method will be called
ans(10, 20)