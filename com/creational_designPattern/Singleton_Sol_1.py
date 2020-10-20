"""
Pattern name - SingleTon
Pattern type - Creational Design Pattern
"""

#%%
# Implementation way - 1
"""
Using __new__ ?

Whenever a class is instantiated __new__ and __init__ methods are called. 
__new__ method will be called when an object is created and __init__ method
 will be called to initialize the object. 
 
 __new__ Method retrun STRING
 __init__ Method return NONE
 
 class A(object): 
    # new method returning a string 
    def __new__(cls): 
        print("Creating instance") 
        return "GeeksforGeeks"
  
class B(object): 
    # init method returning a string 
    def __init__(self): 
        print("Initializing instance") 
        #Below line will throw the error
        return "GeeksforGeeks"
  
print(A()) 
print(B()) 

"""

class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


o1 = SingleTon()
print("Object - 1 ==>", o1)
o1.data = 10

o2 = SingleTon()
print("Object - 2 ==>", o2)
print("Object - 2 data ==>", o2.data)
o2.data = 5

print("Object - 1 data ==>", o1.data)


