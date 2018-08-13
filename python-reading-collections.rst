##########
Collected useful posts about Python
##########

1. On Python magic methods (double unders, dunders)
    https://rszalski.github.io/magicmethods/

2. On Python descriptors and properties (which is an implementation of descriptors) 
    https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/ 

#. On Python metaclass 
    https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/#object-attribute-lookup
    https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/
        `Metaclasses are deeper magic that 99% of users should never worry about. If you wonder whether you need them, you don’t (the people who actually need them know with certainty that they need them, and don’t need an explanation about why).`
    http://www.vrplumber.com/programming/metaclasses.pdf

#. On inspect.getsourcelines to modify a function
    https://www.programcreek.com/python/example/2937/inspect.getsourcelines
    ``eval() and exec()`` can be used to dynamically change a function. But remember all these can be done using the **decorator** module. Do not try to reinvent the wheels.

#. On sklearn EstimatorBase base class the reason behind 
    ``"All estimators should specify all the parameters that can be set at the class level in their __init__ as explicit keyword arguments (no *args or **kwargs)."``
    http://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html
    https://stackoverflow.com/questions/23174964/how-to-gridsearch-over-transform-arguments-within-a-pipeline-in-scikit-learn

#. XGBOOST
    https://arxiv.org/pdf/1603.02754.pdf

#. python function signature
    https://emptysqua.re/blog/copying-a-python-functions-signature/

#. python command line arguments parsing libraries
    https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

#. priority queue
    http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php

#. python type, object, class, instance: difference
    https://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary
    http://www.cs.utexas.edu/~cannata/cs345/Class%20Notes/15%20Python%20Types%20and%20Objects.pdf
        ``1. <type 'object'> is an instance of <type 'type'>.
        2. <type 'object'> is a subclass of no object.
        3. <type 'type'> is an instance of itself.
        4. <type 'type'> is a subclass of <type 'object'>.``

        .. image:: ./media/python_metaclass.png
           :width: 150px

#. difference between `vars` vs. `dir`
    ``vars(cls) is like local() inside cls, returns cls.__dict__, while dir(cls) returns everything in the namespace, cls.__dict__ plus class methods/attributes plus its ancestor's dir()``  

#. on creating singleton in Python... in addition to a class instance counter (now it seems ugly), other methods like class decorator, class decorator returning a class, a base class that defines singleton property (override __new__), and a metaclass (override __call__).  
    https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    It is worth pointing out here, that are differences in these methods. What does a Singleton mean here? There is only one instance could be created, and/or the instance is **static**? With a method such as using a singleton class, which separates the creation `__new__` and initialization `__init__` of a class, there will be **one** and only **one** instance (with the same `id(object)` storage location for the object), but the same instance will be initialized again with different parameters. For example
    
    .. code-block: python

        class Singleton(object):
            _instance = None
            def __new__(cls, *args, **kwargs):
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
                return cls._instance

        class A(Singleton):
            def __init__(self, name):
                self.name = name

        a = A('tom')
        print(id(a), a.name)

        b = A('Jack')
        print(id(b), b.name)

        print(id(a), a.name)

    The output would be
    ``
    >>>140195539441984 tom
    
    >>>140195539441984 jack
    
    >>>140195539441984 jack

    ``

    While using a metaclass (override `__call__`), the method will cache the first ever created instance, and returns the same instance ever after. The new parameters will have no effect since it passes `__init__` completely.
    

.. code-block:: python

    class metaclass1(type):
        def __call__(self, *args, **kwargs):
            return super(metaclass, self).__call__(*args, **kwargs) 








