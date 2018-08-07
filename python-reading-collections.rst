##########
Collected useful posts about Python
##########

1. On Python magic methods (double unders, dunders)
    https://rszalski.github.io/magicmethods/

2. On Python descriptors and properties (which is an implementation of descriptors) 
    https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/ 

3. On Python metaclass 
    https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/#object-attribute-lookup

4. On inspect.getsourcelines to modify a function
    https://www.programcreek.com/python/example/2937/inspect.getsourcelines
    ``eval() and exec()`` can be used to dynamically change a function. But remember all these can be done using the **decorator** module. Do not try to reinvent the wheels.

5. On sklearn EstimatorBase base class the reason behind 
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


