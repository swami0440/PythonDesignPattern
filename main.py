"""
Design Pattern are reusable solution for problem that encounter in every day programming life.
It's generally targeted the solving the problem og object generation and integration
There 3 Main Types of Design Patterns


1) Creational Patterns : This type is deal with create objects and initialization.
                        This patter gives the flexibility in deciding which object need to create for given Case.
                        EXAMPLE:

                            1.1) Abstract Factory :
                            Lets you produce families of related objects without specifying their concrete classes.

                            1.2) Builder :
                            Lets you construct complex objects step by step. The pattern allows you to produce
                            different types and representations of an object using the same construction

                            1.3) Factory Method :
                            Provides an interface for creating objects in a superclass, but allows subclasses to
                            alter the type of objects that will be created.

                            1.4) Prototype :
                            Lets you copy existing objects without making your code dependent on their classes.

                            1.5) Singleton :
                            Lets you ensure that a class has only one instance, while providing a global access
                            point to this instance.


2) Structural Patterns : This type deal which class and object composition in simple word,This Pattern focus on
                        decoupling interface and implement of classes and it's object.
                        EXAMPLE :

                        2.1) Adapter :
                        Allows objects with incompatible interfaces to collaborate.

                        2.2) Bridge :
                        Lets you split a large class or a set of closely related classes into two separate
                        hierarchies—abstraction and implementation—which can be developed independently of
                        each other.

                        2.3) Composite :
                        Lets you compose objects into tree structures and then work with these structures as
                        if they were individual objects.

                        2.4) Decorator :
                        Lets you attach new behaviors to objects by placing these objects inside special wrapper
                        objects that contain the behaviors.

                        2.5) Facade :
                        Provides a simplified interface to a library, a framework, or any other complex set of
                        classes.

                        2.6) Flyweight :
                        Lets you fit more objects into the available amount of RAM by sharing common parts of
                        state between multiple objects instead of keeping all of the data in each object.

                        2.7) Proxy :
                        Lets you provide a substitute or placeholder for another object. A proxy controls access
                        to the original object, allowing you to perform something either before or after the
                        request gets through to the original object.

3) Behavioral Patterns : This type deal with communication between class and object.
                        EXAMPLE:

                        3.1) Chain of Responsibility :
                        Lets you pass requests along a chain of handlers. Upon receiving a request, each handler
                        decides either to process the request or to pass it to the next handler in the chain.

                        3.2) Iterator :
                        Lets you traverse elements of a collection without exposing its underlying representation
                        (list, stack, tree, etc.).

                        3.3) Memento :
                        Lets you save and restore the previous state of an object without revealing the details of
                        its implementation.

                        3.4) State:
                        Lets an object alter its behavior when its internal state changes. It appears as if the object
                        changed its class.

                        3.5) Template Method :
                        Defines the skeleton of an algorithm in the superclass but lets subclasses override specific
                        steps of the algorithm without changing its structure.

                        3.6) Command :
                        Turns a request into a stand-alone object that contains all information about the request.
                        This transformation lets you parameterize methods with different requests, delay or queue a
                         request's execution, and support undoable operations.

                        3.7) Mediator :
                        Lets you reduce chaotic dependencies between objects. The pattern restricts direct
                        communications between the objects and forces them to collaborate only via a mediator object.

                        3.8) Observer :
                        Lets you define a subscription mechanism to notify multiple objects about any events that
                         happen to the object they're observing.

                       3.9) Strategy :
                        Lets you define a family of algorithms, put each of them into a separate class, and make
                        their objects interchangeable.

                      3.10) Visitor :
                      Lets you separate algorithms from the objects on which they operate.



"""