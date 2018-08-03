'''
a few things to cover
1. memorization through decoration (this can be done though the decorator module, so do not take it from here and try to reinvent the wheel)
2. use magic methods to define the memory class 
3. curry (like the person)
4. notice this decorator does not keep the function signature and meta data (going back to 1). Metadata problem is fixed by functools.wraps. signature still being a problem.
'''

from functools import wraps 

class memo(object):
	def __init__(self):
		self.m = {} ## memorization part
		self.ct = {} ## count how many times which one used

    ## enable the **in** clause
	def __iter__(self):
		return self.m.__iter__()

    ## setitem and update the counter
	def __getitem__(self, key):
		self.ct[key] = self.ct.get(key, 0) + 1
		return self.m[key]

	def __setitem__(self, key, val):
		self.m[key] = val

def curried_deco(M):
	def deco(func):
		memo = M
		def f2(*args):
			if args not in memo:
				memo[args] = func(*args)
			return memo[args]
		return wraps(func)(f2)
	return deco 

if __name__ == '__main__':

    M = memo()
    @curried_deco(M)
    def myfunc(x, y):
    	'''The name is myfunc. This is the doc for myfunc.
    	'''
		## some time consuming junk
        return x + y**2

    for i in range(1000):
	    j = i % 3
	    k = i % 7
	    _ = myfunc(j, k)

    print M.m
    print M.ct 
    print myfunc.__doc__





