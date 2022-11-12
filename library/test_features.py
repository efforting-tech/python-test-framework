#Everything in this script will be accessible to the test module via modification of builtins

import sys
from . import state

#List of things to not include in the tests
NO_EXPORT = 'sys state NO_EXPORT'


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


#Here you can add your own custom features to make testing easier.