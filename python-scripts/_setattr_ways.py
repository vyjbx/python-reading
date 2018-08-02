'''
ways to set attribute in an object and the role of __setattr__
'''

class A(object):
	def __init__(self, val):
		self.val = val

	def __setattr__(self, name, val):
		print name, val
		super(A, self).__setattr__(name, val)

'''
__init__ actually calls __setattr__ when initiating properties. 


The setattr build-in method also calls an objects __setattr__. This is exactly the reason __setattr__(self, name, val) used super instead setattr
'''

def __setattr__(self, name, val):
	print name, val
	setattr(self, name, val)  ## this will not work and gives an Timeout Exception, as it falls into the loop

'''
here shows two ways of setting properties. Note self.__dict__ will not call __setattr__
'''

class B(object):
	def __init__(self, a, b):
		self.a = a
		self.___dict__['b'] = b

	def __setattr__(self, name, val):
		print name, val 
		super(B, self).__setattr__(name, val)


'''
__dict__ provides a detour around __setattr__ if latter needs to be over written for side effects.
(and can generate possible unwanted side effects)
'''





