'''
Meta program is to write code that generate or edit code. It has a wide range including parsers, compilers, etc.. We are going through a couple of examples such as wrappers and metaclass. 

wrappers are super functoin that takes a function or class as input, transforms the object, and output the transformed version of the object.

metaclass kicks in when generating the class with its __new__ method. The change is thus inherited through the chain and has effect for all the following classes

This example is copied from the one in the link.
https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/

'''

from functools import wraps 
import numpy as np 

def log_it(logging_file):
	def f(message):
		if logging_file:
			logging_file.info(message)
		else:
			print message 
	return f 

## the wrapper function will record the number of times it is called, and print or log into the file 
def wrap_func(logging_file = None):
	logger = log_it(logging_file)
    ## and something else accessible by all functions
	def wrapper(func):
		## function specific stuff
		memory = {
	        'counter': 0, ## number of times it is called
	    }
		@wraps(func)
		def f(*args, **kwargs):
			self = args[0]
			memory['counter'] += 1
			rst = func(*args, **kwargs)
			message = 'function: {0} called {1} times'.format(func.__name__, memory['counter']) + ' by class {0} object id {1}'.format(self.__class__, id(self)) + ' with input {0}, {1} and output {2}'.format(args, kwargs, rst)
			logger(message)
			return rst
		return f 
	return wrapper 

def cls_wrapper(cls):
    wrapper_func = wrap_func()
    for name, attribute in vars(cls).iteritems():
    	if callable(attribute):
    		setattr(cls, name, wrapper_func(attribute))
    return cls 

'''
Clearly decorator can change the method behaviors but what if we want to make this a class property? All the methods in sub-classes should inherite this property.
'''

class meta_wrap(type):
	def __new__(cls, name, bases, kwargs):
		new_cls = super(meta_wrap, cls).__new__(cls, name, bases, kwargs)
		return cls_wrapper(new_cls)


if __name__ == '__main__':

	@cls_wrapper
	class A1(object):
		def sqrt(self, x):
			return np.sqrt(x)

	class B1(A1):
		def add(self, x, y):
			return x + y 

	class C1(A1):
		def sqrt(self, x):
			# _ = super(C1, self).sqrt(x)
			return np.sqrt(x + 1)

	# a = A1()
	# a.sqrt(1)
	# a.sqrt(2)

	# b = B1()
	# b.sqrt(3)
	# b.sqrt(4)
	# b.add(1, 2)
	# b.add(3, 4)

	# c = C1()
	# c.sqrt(3)


	class A2(object):
		__metaclass__ = meta_wrap
		def sqrt(self, x):
			return np.sqrt(x)

	class B2(A2):
		def add(self, x, y):
			return x + y

	class C2(A2):
		def sqrt(self, x):
			return np.sqrt(x + 1)

	a = A2()
	a.sqrt(1)
	a.sqrt(2)

	b = B2()
	b.sqrt(3)
	b.sqrt(4)
	b.add(1, 2)
	b.add(3, 4)

	c = C2()
	c.sqrt(3)
















