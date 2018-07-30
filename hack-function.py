"""
This is a dangerous and hacky way to edit a function dynamically, or not. It is used by decorator module and other applications to mimic a functions signature.

It has the power, but try not to use it unless it is the absolute last option available.

Note in addition to it is a bad way to define decorator, even though add_print decorator pattern, this will not work

@add_print 
def func(*args, **kwargs)

as @add_print is part of function source code. It needs to be removed in the return function. There are other and better ways to copy the signature and meta data.

environment version is python 2.7
"""

import re, inspect 

fname = re.compile(r'\b[_a-zA-Z][_\da-zA-Z]*\(') ## check filename
return_pattern = re.compile(r'\breturn\b')

def newfunc(scripts, new_name):
	'''asign a new name to the function'''
	split_fname = fname.split(scripts[0])
	line1 = ('{} ' + new_name + '({}').format(*split_fname)
	return [line1] + scripts[1:]

def return2print(line):
	'''
	generate return line, or a different oneline effect 
	'''
	return re.sub(return_pattern, 'print', line)

def insert_func(scripts):
	'''
	insert a print statement (or a different side effect) before return statement to print out the returned value. 
	other effects are also possible, such as change the return value, data type, etc..
	'''
	new_script = []
	while scripts:
		line = scripts.pop()
		new_script.append(line)
		if return_pattern.findall(line):
			new_script.append(return2print(line))
	return '\n'.join(new_script[::-1])

def add_print(func):
	'''
	combine steps. eval is to expose the function change out of the add_print function scope. 
	This change can also be returned through a class/instance property or another mutable data structure such as list or dict
	'''
	new_fname = 'print_' + func.__name__
	scripts = inspect.getsource(func).split('\n')
	new_scripts = newfunc(scripts, new_fname)
	exec(insert_func(new_scripts))
	return eval(new_fname)

def testfunc(a, b, c):
	'''
	--return-- in __doc__ string could mess the above code up
	ignore now
	'''
	if a > 0:
		return a ** b
	elif a == 0:
		return None
	else:
		return 'negative value'

if __name__ == '__main__':
	for i in [1, 0, -1]:
		new_func = add_print(testfunc)
		_ = new_func(i, 2, 0)

