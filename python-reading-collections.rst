####################################
Collected useful posts about Python
####################################

1. On Python magic methods (double unders, *dunders*)
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
           :width: 400px

#. difference between `vars` vs. `dir`
    ``vars(cls) is like local() inside cls, returns cls.__dict__, while dir(cls) returns everything in the namespace, cls.__dict__ plus class methods/attributes plus its ancestor's dir()``  

#. on creating singleton in Python... in addition to a class instance counter (now it seems ugly), other methods like class decorator, class decorator returning a class, a base class that defines singleton property (override ``__new__``), and a metaclass (override ``__call__``).  
    https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    
    It is worth pointing the difference in these methods. What a Singleton really means? Sure there is only one instance, but it has to be **static**? Methods such singleton class separate the creation ``__new__`` and initialization ``__init__`` of a class.  There will be **one** and only **one** instance (with the same ``id(object)`` storage location for the object), but the same instance will be initialized again with different parameters. For example
    

	.. sourcecode:: python

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

	    b = A('jack')
	    print(id(b), b.name)

	    print(id(a), a.name)

    The output would be
    
    ``>>>140195539441984 tom``

    ``>>>140195539441984 jack``
    
    ``>>>140195539441984 jack``


    While using a metaclass (override metaclass ``__call__``), the first ever created instance of a class is cached. It returns the exact same instance ever after. The new parameters have no effect as it by-passes ``__init__`` completely.

    .. sourcecode:: python

        class Single_meta(type):
            _instance = {} 
            def __call__(cls, *args, **kwargs):
                if cls not in cls._instance:
                    cls._instance[cls] = super(Single_meta, cls).__call__(*args, **kwargs)
                ## if in, instance creation is by-passed
                return cls._instance[cls]

        class A(object, metaclass=Single_meta):
            def __init__(self, name):
                self.name = name
            def __str__(self):
                return str(id(self)) + ':' + self.name

        a = A('tom')
        print(a)

        b = A('jack')
        print(b

        print(a)

    The output would be
    
    ``>>>140195539440864:tom``

    ``>>>140195539440864:tom``

    ``>>>140195539440864:tom``

    The second parameter `jack` had no effect at all.

#. Python **attributes**, how the object searchs for and accesses attributes. This is a good reading and explains a lot of things! **Python is all about attributes.**
    https://codesachin.wordpress.com/2016/06/09/the-magic-behind-attribute-access-in-python/

    .. image:: ./media/python_attribute_search.png
        :width: 400px

    
    Summary:
        1. There are cases when __class__ is absent;
        2. The stated order is only for **reading** attributes, not **writing** attributes.


    **1. What if, there is no ``__dict__`` in a class?** Such as a *dict* object. What is the search rule here? Here is an example, from ``sklearn.utils`` there is ``Bunch`` type. In such case, you need to override ``__setattr__`` and ``__get_attr__`` to modify the attribute access behavior explicitly.

    .. code-block:: python

        class Bunch(dict):
            def __init__(self, **kwargs):
                super(Bunch, self).__init__(kwargs)
            
            def __setattr__(self, key, val):
                self[key] = val

            def __getattr__(self, key):
                try:
                    return self[key]
                except KeyError:
                    raise AttributeError

    
    If we do 

    .. code-block:: python

        B = Bunch(**{'a'=4, 'b'=3})

    We can have a dict with attributes

    .. code-block:: python

        >>>B.a
        >>>4
        >>>B.a = 10
        >>>B.a
        >>>10
        
    Another handy, but could be **dangerous** way. This will lead to memory leak in early versions of python. 

    .. code-block:: python

        class Bunch2(dict):
            def __init__(self, **kwargs):
                super(Bunch2, self).__init__(kwargs)
                self.__dict__ = self

    
    
    Also, notice, since ``dict`` does not have ``__dict__`` attribute, if you do ``vars(dict_obj)``, you will be greeted by a ``TypeError``

    ``TypeError: vars() argument must have __dict__ attribute``

    An explanation to ``dictproxy``, which is the type of ``cls.__dict__`` 
    https://stackoverflow.com/questions/25440694/whats-the-purpose-of-dictproxy
    
    class ``__dict__`` is read-only to 1) ensure python interpreter optimization, and 2) for safety; object ``__dict__`` can have read, write, and delete access. Once deleted, it will be regenerated on the next assignment. 

    **2. when both descriptor and __setattr__ are implemented in an object**,  the ``descriptor().__set__`` is **never** called. See the following.

    https://stackoverflow.com/questions/9161302/using-both-setattr-and-descriptors-for-a-python-class

    There are a few workarounds. 
        1) Use a metaclass and a function decorator. Use the decorator to triage attribute write calls, if descriptor, then call the ``object.__setattr__(self, key, val)``, which will call the descriptor ``__set__``; if not, then call ``__setattr__``. Override metaclass ``__new__`` to wrap the ``__setattr__`` method, and put descriptor name in a hashmap (if ``hasattr(object, '__get__')``).
        2) Use ``if key in self.__class__.__dict__ and hasattr(self.__class__.__dict__, '__get__'):``. I would prefer 1) as it is something can be inherited, and can be changed easily on the metaclass level.

#. Good tutorial on opencv Python API cv2

    https://people.revoledu.com/kardi/tutorial/Python/Video+Analysis+using+OpenCV-Python.html

#. Best on python **relative** import

    https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

    ``"There are two ways to load a Python file: as the top-level script, or as a module. A file is loaded as the top-level script if you execute it directly, for instance by typing python myfile.py on the command line. It is loaded as a module if you do python -m myfile, or if it is loaded when an import statement is encountered inside some other file. There can only be one top-level script at a time; the top-level script is the Python file you ran to start things off."``

    ``"However, if your module's name is __main__, it is not considered to be in a package. Its name has no dots, and therefore you cannot use from .. import statements inside it. If you try to do so, you will get the "relative-import in non-package" error."`` 

    ``"Two solutions:``
        ``1. If you really do want to run moduleX directly, but you still want it to be considered part of a package, you can do python -m package.subpackage1.moduleX. The -m tells Python to load it as a module, not as the top-level script.``
        ``2. Or perhaps you don't actually want to run moduleX, you just want to run some other script, say myfile.py, that uses functions inside moduleX. If that is the case, put myfile.py somewhere else --- not inside the package directory -- and run it. If inside myfile.py you do things like from package.moduleA import spam, it will work fine."``

#. python c extensions

    https://dfm.io/posts/python-c-extensions/
    https://medium.com/@joshua.massover/python-c-extension-example-cef86ffab4ed


#. Python test modules (almost all of them)

    https://docs.python-guide.org/writing/tests/








