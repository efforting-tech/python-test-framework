#Everything in this script will be accessible to the test module via modification of builtins

import sys
import fnmatch
from . import state

#List of things to not include in the tests
NO_EXPORT = 'fnmatch sys state NO_EXPORT'


def __build_class__(func, name, *bases, metaclass=type, **kwds):

	frame = sys._getframe(1)

	if Test in bases:
		from . import internals
		internals.run_test(func, name, frame, **kwds)

	else:
		return state.original_builtins['__build_class__'](func, name, *bases, metaclass=metaclass, **kwds)


def print(*items):
	if state.test_stack:
		printed_items = state.test_stack[-1]
		printed_items.append(items)
	else:
		#This is outside of a running test - perhaps when loading the test file, we will just print it as normal
		state.original_builtins['print'](*items)

class Test:
	pass

#See examples/demo1.py for an example of how this is used
def IterVars(name_list):
	calling_frame = sys._getframe(1)

	for name in name_list:
		yield name, calling_frame.f_locals[name]


def GlobVars(glob, sort=True):
	calling_frame = sys._getframe(1)
	vars = (k for k in tuple(calling_frame.f_locals.keys()) if fnmatch.fnmatch(k, glob))

	if sort:
		vars = sorted(vars)

	for k in vars:
		yield k, calling_frame.f_locals[k]

def DerivedTypes(base_type, information_source='locals'):
	#Note - when information_source is locals, (key, ref) tuples are yielded, but if information_source is gc, only ref is yielded
	if information_source == 'locals':
		calling_frame = sys._getframe(1)
		for k, v in tuple(calling_frame.f_locals.items()):
			if isinstance(v, type) and v is not base_type and issubclass(v, base_type):
				yield k, v
	elif information_source == 'gc':
		import gc

		meta_type = type(base_type)
		for item in gc.get_objects():
			if isinstance(item, meta_type) and issubclass(item, base_type) and item is not base_type:
				yield item

	else:
		raise Exception('No such information source: {information_source!r}')




#Here you can add your own custom features to make testing easier.