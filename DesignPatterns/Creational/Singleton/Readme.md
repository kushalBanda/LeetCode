## Singleton

Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single point access to it for any other code. 

Singleton has almost the same pros and cons as global variables. Although they're super-handy, they break the modularity of your code.

You can't just use a class that depends on a Singletone in some other context, without carrying over the Singleton to the other context. Most of the time, thei limitation comes up during the creation of unit tests.


**Usage examples:** A lot of developers consider the Singleton pattern an antipattern. That’s why its usage is on the decline in Python code.

**Identification:** Singleton can be recognized by a static creation method, which returns the same cached object.
