"""
Python Function Annotation:
Annotation is provide the information about the function

for eg:
"func" function has  parameter
                    a --> int
                    b --> int
                    return --> str
Note:- This is just the way of provide the information about function.
        Function will work fine if pass the parameter as "str" or any
        it will return the value type as per our business logic


"""


def func(a: int, b: int) -> str:
    return a + b


print(func("abc", "pqr"))
print(type(func("abc", "pqr")))

# __annotation__ is the inbuilt function, Which is return the dictionary about the annotation information
# eg: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'str'>}
print(func.__annotations__)
